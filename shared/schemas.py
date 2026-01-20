"""
Data schemas for the AI Hiring MVP.

Pydantic models for candidates, evaluations, job posts, and prompts.
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --------------------------------
# Enums
# --------------------------------


class Source(str, Enum):
    """Candidate source platform."""

    GETONBOARD = "getonboard"


class FitLabel(str, Enum):
    """LLM evaluation fit classification."""

    STRONG_YES = "strong_yes"
    YES = "yes"
    MAYBE = "maybe"
    NO = "no"


class Decision(str, Enum):
    """Recruiter decision on candidate."""

    PUSH = "push"
    HOLD = "hold"
    REJECT = "reject"


class TeamtailorStatus(str, Enum):
    """Status of candidate push to TeamTailor."""

    NOT_SENT = "not_sent"
    SENT = "sent"
    FAILED = "failed"


# --------------------------------
# TABLE 1: candidates_raw
# --------------------------------


class CandidateRaw(BaseModel):
    """
    Raw candidate identity and source data.
    One row = one person. Never contains AI evaluations.
    """

    # Primary key
    candidate_id: str

    # Source info
    source: Source
    source_candidate_id: str
    created_at: datetime

    # Candidate fields
    full_name: str
    email: str
    phone: Optional[str] = None
    linkedin_url: Optional[str] = None
    cv_url: Optional[str] = None
    raw_profile_url: str


# --------------------------------
# TABLE 2: candidates_evaluations
# --------------------------------


class CandidateEvaluation(BaseModel):
    """
    AI evaluation of a candidate for a specific job.
    One row = one evaluation. Immutable except for recruiter decision.
    """

    # Keys
    evaluation_id: str
    candidate_id: str  # FK to candidates_raw
    job_post_id: str
    prompt_version: str

    # Metadata
    evaluated_at: datetime

    # LLM outputs
    fit_label: FitLabel
    fit_score: int = Field(ge=1, le=5)
    reasons: str
    red_flags: Optional[str] = None

    # Workflow (decision is recruiter-editable)
    decision: Decision = Decision.HOLD
    teamtailor_status: TeamtailorStatus = TeamtailorStatus.NOT_SENT


# --------------------------------
# TABLE 3: job_posts
# --------------------------------


class JobPost(BaseModel):
    """
    Minimal job metadata from GetOnBoard.
    Connects candidates, evaluations, and prompts.
    """

    job_post_id: str
    job_post_name: str
    active: bool = True
    getonboard_url: str
    default_prompt_version: str


# --------------------------------
# TABLE 4: prompts
# --------------------------------


class Prompt(BaseModel):
    """
    Recruiter-editable evaluation prompt.
    Versioned and job-specific.
    """

    prompt_version: str
    job_post_id: str
    prompt_content: str
