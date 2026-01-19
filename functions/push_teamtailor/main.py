"""
Cloud Function entrypoint for push_teamtailor.

TODO: This function is responsible for:
- Reading evaluated candidates from Sheets
- Filtering candidates that meet criteria
- Pushing qualified candidates to TeamTailor ATS
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
