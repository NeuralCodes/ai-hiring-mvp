"""
Google Sheets integration subpackage.

Provides client and repository abstractions for reading/writing
candidate data and prompts from Google Sheets.
"""

from shared.sheets.client import SheetsClient
from shared.sheets.repositories import CandidateRepository, PromptRepository

__all__ = ["SheetsClient", "CandidateRepository", "PromptRepository"]
