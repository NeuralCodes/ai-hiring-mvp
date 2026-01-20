"""
Script to set up Google Spreadsheet structure from Pydantic schemas.

This script creates the required sheets (tabs) in the main spreadsheet with:
- Proper headers from schema field names
- Frozen header rows
- Data validation for enum fields
- Column formatting

Usage:
    python scripts/setup_spreadsheet.py

Requires:
    - GOOGLE_APPLICATION_CREDENTIALS env var pointing to service account JSON
    - Service account with Sheets API enabled and access to the spreadsheet
"""

import os
import sys
from typing import Any

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Add parent directory to path to import shared modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.config import MAIN_SPREADSHEET_ID
from shared.schemas import (
    CandidateRaw,
    CandidateEvaluation,
    JobPost,
    Prompt,
    Source,
    FitLabel,
    Decision,
    TeamtailorStatus,
)


class SpreadsheetSetup:
    """Sets up Google Spreadsheet structure from Pydantic schemas."""

    def __init__(self, spreadsheet_id: str, credentials_path: str | None = None):
        """
        Initialize with service account credentials.

        Args:
            spreadsheet_id: The Google Spreadsheet ID to set up
            credentials_path: Path to service account JSON. If None, uses
                GOOGLE_APPLICATION_CREDENTIALS env var.
        """
        self.spreadsheet_id = spreadsheet_id

        if credentials_path:
            creds = service_account.Credentials.from_service_account_file(
                credentials_path,
                scopes=[
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive",
                ],
            )
        else:
            creds = service_account.Credentials.from_service_account_file(
                os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
                scopes=[
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive",
                ],
            )

        self.sheets_service = build("sheets", "v4", credentials=creds)

    def setup_all_sheets(self) -> None:
        """Set up all required sheets in the spreadsheet."""
        print(f"Setting up spreadsheet: {self.spreadsheet_id}")
        print(f"URL: https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}\n")

        # Get existing sheets
        existing_sheets = self._get_existing_sheets()

        # Set up each sheet (create if doesn't exist, update if exists)
        if "candidates_raw" not in existing_sheets:
            self._setup_sheet_candidates_raw()
        else:
            print("  ⚠ Sheet 'candidates_raw' already exists, skipping...")

        if "candidates_evaluations" not in existing_sheets:
            self._setup_sheet_candidates_evaluations()
        else:
            print("  ⚠ Sheet 'candidates_evaluations' already exists, skipping...")

        if "job_posts" not in existing_sheets:
            self._setup_sheet_job_posts()
        else:
            print("  ⚠ Sheet 'job_posts' already exists, skipping...")

        if "prompts" not in existing_sheets:
            self._setup_sheet_prompts()
        else:
            print("  ⚠ Sheet 'prompts' already exists, skipping...")

        print("\n✓ Spreadsheet setup complete!")

    def _get_existing_sheets(self) -> list[str]:
        """Get list of existing sheet names."""
        try:
            sheet_metadata = (
                self.sheets_service.spreadsheets()
                .get(spreadsheetId=self.spreadsheet_id)
                .execute()
            )
            return [s["properties"]["title"] for s in sheet_metadata["sheets"]]
        except HttpError as e:
            print(f"Error accessing spreadsheet: {e}")
            raise

    def _setup_sheet_candidates_raw(self) -> None:
        """Set up candidates_raw sheet with headers and validation."""
        sheet_name = "candidates_raw"
        fields = list(CandidateRaw.model_fields.keys())

        # Create sheet
        requests = [
            {
                "addSheet": {
                    "properties": {
                        "title": sheet_name,
                        "gridProperties": {"frozenRowCount": 1},
                    }
                }
            }
        ]

        self.sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={"requests": requests},
        ).execute()

        # Get sheet ID
        sheet_id = self._get_sheet_id(sheet_name)

        # Write headers
        self.sheets_service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range=f"{sheet_name}!A1",
            valueInputOption="RAW",
            body={"values": [fields]},
        ).execute()

        # Add data validation for source enum
        source_col = fields.index("source")
        validation_requests = [
            {
                "setDataValidation": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": 10000,
                        "startColumnIndex": source_col,
                        "endColumnIndex": source_col + 1,
                    },
                    "rule": {
                        "condition": {
                            "type": "ONE_OF_LIST",
                            "values": [{"userEnteredValue": v.value} for v in Source],
                        },
                        "showCustomUi": True,
                        "strict": True,
                    },
                }
            }
        ]

        self.sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={"requests": validation_requests},
        ).execute()

        print(f"  ✓ Created sheet: {sheet_name}")

    def _setup_sheet_candidates_evaluations(self) -> None:
        """Set up candidates_evaluations sheet with headers and validation."""
        sheet_name = "candidates_evaluations"
        fields = list(CandidateEvaluation.model_fields.keys())

        requests = [
            {
                "addSheet": {
                    "properties": {
                        "title": sheet_name,
                        "gridProperties": {"frozenRowCount": 1},
                    }
                }
            }
        ]

        self.sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={"requests": requests},
        ).execute()

        sheet_id = self._get_sheet_id(sheet_name)

        # Write headers
        self.sheets_service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range=f"{sheet_name}!A1",
            valueInputOption="RAW",
            body={"values": [fields]},
        ).execute()

        # Add validations for enum fields
        fit_label_col = fields.index("fit_label")
        decision_col = fields.index("decision")
        status_col = fields.index("teamtailor_status")

        validation_requests = [
            {
                "setDataValidation": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": 10000,
                        "startColumnIndex": fit_label_col,
                        "endColumnIndex": fit_label_col + 1,
                    },
                    "rule": {
                        "condition": {
                            "type": "ONE_OF_LIST",
                            "values": [{"userEnteredValue": v.value} for v in FitLabel],
                        },
                        "showCustomUi": True,
                        "strict": True,
                    },
                }
            },
            {
                "setDataValidation": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": 10000,
                        "startColumnIndex": decision_col,
                        "endColumnIndex": decision_col + 1,
                    },
                    "rule": {
                        "condition": {
                            "type": "ONE_OF_LIST",
                            "values": [{"userEnteredValue": v.value} for v in Decision],
                        },
                        "showCustomUi": True,
                        "strict": True,
                    },
                }
            },
            {
                "setDataValidation": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": 10000,
                        "startColumnIndex": status_col,
                        "endColumnIndex": status_col + 1,
                    },
                    "rule": {
                        "condition": {
                            "type": "ONE_OF_LIST",
                            "values": [
                                {"userEnteredValue": v.value} for v in TeamtailorStatus
                            ],
                        },
                        "showCustomUi": True,
                        "strict": True,
                    },
                }
            },
        ]

        self.sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={"requests": validation_requests},
        ).execute()

        print(f"  ✓ Created sheet: {sheet_name}")

    def _setup_sheet_job_posts(self) -> None:
        """Set up job_posts sheet with headers."""
        sheet_name = "job_posts"
        fields = list(JobPost.model_fields.keys())

        requests = [
            {
                "addSheet": {
                    "properties": {
                        "title": sheet_name,
                        "gridProperties": {"frozenRowCount": 1},
                    }
                }
            }
        ]

        self.sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={"requests": requests},
        ).execute()

        # Write headers
        self.sheets_service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range=f"{sheet_name}!A1",
            valueInputOption="RAW",
            body={"values": [fields]},
        ).execute()

        print(f"  ✓ Created sheet: {sheet_name}")

    def _setup_sheet_prompts(self) -> None:
        """Set up prompts sheet with headers."""
        sheet_name = "prompts"
        fields = list(Prompt.model_fields.keys())

        requests = [
            {
                "addSheet": {
                    "properties": {
                        "title": sheet_name,
                        "gridProperties": {"frozenRowCount": 1},
                    }
                }
            }
        ]

        self.sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={"requests": requests},
        ).execute()

        # Write headers
        self.sheets_service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range=f"{sheet_name}!A1",
            valueInputOption="RAW",
            body={"values": [fields]},
        ).execute()

        print(f"  ✓ Created sheet: {sheet_name}")

    def _get_sheet_id(self, sheet_name: str) -> int:
        """Get the sheet ID for a given sheet name."""
        sheet_metadata = (
            self.sheets_service.spreadsheets()
            .get(spreadsheetId=self.spreadsheet_id)
            .execute()
        )
        return next(
            s["properties"]["sheetId"]
            for s in sheet_metadata["sheets"]
            if s["properties"]["title"] == sheet_name
        )


def main():
    """Main entry point."""
    if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
        print("Error: GOOGLE_APPLICATION_CREDENTIALS environment variable not set")
        print("Please set it to the path of your service account JSON file")
        sys.exit(1)

    setup = SpreadsheetSetup(MAIN_SPREADSHEET_ID)
    setup.setup_all_sheets()


if __name__ == "__main__":
    main()
