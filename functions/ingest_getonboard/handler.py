"""
Handler for ingest_getonboard function.

Fetches candidate data from GetOnBoard job platform and stores it
in Google Sheets for downstream processing by the evaluation function.
"""

from flask import Request


def handle(request: Request) -> tuple[str, int]:
    """
    Handle the ingestion request.

    This function should:
    1. Authenticate with GetOnBoard API
    2. Fetch new/updated candidates since last sync
    3. Transform data to internal schema
    4. Write candidates to the Sheets repository
    5. Return summary of ingested records

    Args:
        request: The incoming HTTP request.

    Returns:
        Response tuple of (body, status_code).
    """
    raise NotImplementedError
