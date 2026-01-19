"""
Handler for push_teamtailor function.

Syncs evaluated candidates to TeamTailor applicant tracking system.
"""

from flask import Request


def handle(request: Request) -> tuple[str, int]:
    """
    Handle the push request.

    This function should:
    1. Load evaluated candidates from Sheets
    2. Filter candidates meeting score threshold
    3. Transform data to TeamTailor format
    4. Create/update candidates in TeamTailor via API
    5. Mark synced candidates in Sheets
    6. Return sync summary

    Args:
        request: The incoming HTTP request.

    Returns:
        Response tuple of (body, status_code).
    """
    raise NotImplementedError
