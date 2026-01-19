"""
Prompt construction utilities.

Builds evaluation prompts by combining templates with candidate data.
"""

from shared.schemas import Candidate


class PromptBuilder:
    """
    Builder for constructing LLM evaluation prompts.

    TODO: Implement template variable substitution
    TODO: Add support for multi-part prompts
    TODO: Add prompt validation
    """

    def __init__(self, template: str) -> None:
        """
        Initialize with a prompt template.

        Args:
            template: The prompt template with placeholders.
        """
        self.template = template

    def build(self, candidate: Candidate, **kwargs) -> str:
        """
        Build a complete prompt for a candidate.

        Args:
            candidate: The candidate to evaluate.
            **kwargs: Additional template variables.

        Returns:
            The fully constructed prompt.
        """
        raise NotImplementedError

    @staticmethod
    def format_candidate_data(candidate: Candidate) -> str:
        """
        Format candidate data for inclusion in a prompt.

        Args:
            candidate: The candidate to format.

        Returns:
            Formatted string representation.
        """
        raise NotImplementedError
