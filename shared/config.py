"""
Configuration management for the AI Hiring MVP.

Responsible for loading environment variables, secrets, and runtime configuration.
Will support different environments (dev, staging, prod) and GCP Secret Manager integration.
"""

import os

# Main Google Spreadsheet ID
# https://docs.google.com/spreadsheets/d/1GJB2Oa84ipQj-blw-moSt0JxaANZxzsaIROCMAtDqhI
MAIN_SPREADSHEET_ID = "1GJB2Oa84ipQj-blw-moSt0JxaANZxzsaIROCMAtDqhI"


def get_config() -> dict:
    """
    Load and return application configuration.

    Returns:
        dict: Configuration dictionary with:
            - spreadsheet_id: Main Google Spreadsheet ID
            - project_id: GCP project ID (from env or default)
            - region: GCP region (from env or default)
    """
    return {
        "spreadsheet_id": os.getenv("SPREADSHEET_ID", MAIN_SPREADSHEET_ID),
        "project_id": os.getenv("GCP_PROJECT_ID", ""),
        "region": os.getenv("GCP_REGION", "us-central1"),
    }
