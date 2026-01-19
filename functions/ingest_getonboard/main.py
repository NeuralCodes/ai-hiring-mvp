"""
Cloud Function entrypoint for ingest_getonboard.

TODO: This function is responsible for:
- Receiving webhook events or scheduled triggers
- Fetching new candidates from the GetOnBoard API
- Storing candidate data in Google Sheets for processing
"""

import functions_framework
from flask import Request

from handler import handle


@functions_framework.http
def main(request: Request) -> tuple[str, int]:
    """
    HTTP Cloud Function entrypoint.

    Args:
        request: The incoming HTTP request.

    Returns:
        Response tuple of (body, status_code).
    """
    return handle(request)
