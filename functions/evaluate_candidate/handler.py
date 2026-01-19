"""
Handler for evaluate_candidate function.

Evaluates candidates using LLM-based analysis with prompts
managed through Google Sheets.
"""

from flask import Request


def handle(request: Request) -> tuple[str, int]:
    """
    Handle the evaluation request.

    This function should:
    1. Parse candidate ID(s) from request
    2. Load candidate data from Sheets
    3. Load evaluation prompt for the job type
    4. Build the complete prompt with candidate data
    5. Call Gemini for evaluation
    6. Parse and store the evaluation result
    7. Return evaluation summary

    Args:
        request: The incoming HTTP request.

    Returns:
        Response tuple of (body, status_code).
    """
    raise NotImplementedError
