"""
Cloud Function entrypoint for evaluate_candidate.

TODO: This function is responsible for:
- Receiving candidate IDs to evaluate
- Loading prompts from Sheets
- Calling Gemini for evaluation
- Storing evaluation results back to Sheets
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
