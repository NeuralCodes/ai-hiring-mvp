# Architecture

## Overview

TODO: Detailed architecture documentation to be added.

## Components

### Cloud Functions

- **ingest_getonboard**: Pulls candidates from GetOnBoard
- **evaluate_candidate**: Scores candidates using Gemini
- **push_teamtailor**: Syncs to TeamTailor ATS

### Shared Package

- **sheets/**: Google Sheets integration
- **llm/**: Gemini API client and prompt building

### Data Flow

See `flow.mmd` for the visual representation.

## Infrastructure

Managed via Terraform in `infra/terraform/`.
