"""
Configuration management for the AI Hiring MVP.

Responsible for loading environment variables, secrets, and runtime configuration.
Will support different environments (dev, staging, prod) and GCP Secret Manager integration.
"""


def get_config() -> dict:
    """
    Load and return application configuration.

    TODO: Implement environment variable loading
    TODO: Add GCP Secret Manager integration
    TODO: Support environment-specific overrides
    """
    raise NotImplementedError
