"""
Data schemas for the AI Hiring MVP.

Defines dataclasses and validation schemas for candidates, evaluations,
and other domain objects passed between functions.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Candidate:
    """
    Represents a candidate from the job platform.

    TODO: Add all required fields from GetOnBoard API
    TODO: Add validation logic
    """

    id: str
    name: str
    email: Optional[str] = None


@dataclass
class Evaluation:
    """
    Represents an LLM evaluation of a candidate.

    TODO: Define scoring fields
    TODO: Add evaluation metadata
    """

    candidate_id: str
    score: Optional[float] = None
    reasoning: Optional[str] = None
