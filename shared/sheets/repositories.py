"""
Repository abstractions for Sheets data access.

Provides domain-specific data access patterns on top of the raw Sheets client.
"""

from typing import Optional

from shared.schemas import Candidate, Evaluation
from shared.sheets.client import SheetsClient


class CandidateRepository:
    """
    Repository for candidate data stored in Sheets.

    TODO: Implement candidate CRUD operations
    TODO: Add filtering and pagination
    """

    def __init__(self, client: SheetsClient) -> None:
        self.client = client

    def get_all(self) -> list[Candidate]:
        """Retrieve all candidates from the sheet."""
        raise NotImplementedError

    def get_by_id(self, candidate_id: str) -> Optional[Candidate]:
        """Retrieve a candidate by ID."""
        raise NotImplementedError

    def save(self, candidate: Candidate) -> None:
        """Save or update a candidate."""
        raise NotImplementedError


class PromptRepository:
    """
    Repository for evaluation prompts stored in Sheets.

    TODO: Implement prompt retrieval by job type
    TODO: Add prompt versioning support
    """

    def __init__(self, client: SheetsClient) -> None:
        self.client = client

    def get_evaluation_prompt(self, job_type: str) -> str:
        """Get the evaluation prompt for a specific job type."""
        raise NotImplementedError

    def get_all_prompts(self) -> dict[str, str]:
        """Get all configured prompts."""
        raise NotImplementedError
