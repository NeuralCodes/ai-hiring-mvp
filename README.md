# AI Hiring MVP

Minimal viable product for AI-assisted candidate evaluation and hiring workflow automation on GCP.

## Components

- **Ingestion**: Pull candidate data from GetOnBoard job platform
- **Evaluation**: Score and rank candidates using LLM-based analysis
- **Prompts via Sheets**: Manage evaluation criteria and prompts through Google Sheets
- **Push to ATS**: Sync evaluated candidates to TeamTailor

## Architecture

The system operates as a pipeline of independently deployable Cloud Functions. Candidate data flows from external job boards through an ingestion function, gets stored and enriched via Google Sheets, then evaluated by an LLM-powered scoring function. Qualified candidates are pushed to the applicant tracking system. Shared logic for Sheets access, LLM interaction, and configuration lives in a common package imported by each function.
