# AI Hiring MVP

Minimal viable product for AI-assisted candidate evaluation and hiring workflow automation on GCP.

## Components

- **Ingestion**: Pull candidate data from GetOnBoard job platform
- **Evaluation**: Score and rank candidates using LLM-based analysis
- **Prompts via Sheets**: Manage evaluation criteria and prompts through Google Sheets
- **Push to ATS**: Sync evaluated candidates to TeamTailor

## Architecture

The system operates as a pipeline of independently deployable Cloud Functions. Candidate data flows from external job boards through an ingestion function, gets stored and enriched via Google Sheets, then evaluated by an LLM-powered scoring function. Qualified candidates are pushed to the applicant tracking system. Shared logic for Sheets access, LLM interaction, and configuration lives in a common package imported by each function.

## Google Spreadsheet

The main data storage is a Google Spreadsheet that contains four sheets (tabs):

### Main Spreadsheet
- **URL**: https://docs.google.com/spreadsheets/d/1GJB2Oa84ipQj-blw-moSt0JxaANZxzsaIROCMAtDqhI
- **ID**: `1GJB2Oa84ipQj-blw-moSt0JxaANZxzsaIROCMAtDqhI`

### Sheets Structure

1. **candidates_raw**: Raw candidate identity and source data
   - One row = one person
   - Never contains AI evaluations
   - Columns: candidate_id, source, source_candidate_id, created_at, full_name, email, phone, linkedin_url, cv_url, raw_profile_url

2. **candidates_evaluations**: AI evaluations of candidates
   - One row = one evaluation
   - Immutable except for recruiter decision field
   - Columns: evaluation_id, candidate_id, job_post_id, prompt_version, evaluated_at, fit_label, fit_score, reasons, red_flags, decision, teamtailor_status

3. **job_posts**: Minimal job metadata from GetOnBoard
   - Columns: job_post_id, job_post_name, active, getonboard_url, default_prompt_version

4. **prompts**: Recruiter-editable evaluation prompts
   - Versioned and job-specific
   - Columns: prompt_version, job_post_id, prompt_content

### Setting Up the Spreadsheet

To initialize the spreadsheet structure from the Pydantic schemas:

```bash
# Install script dependencies
pip install -r scripts/requirements.txt

# Set up Google service account credentials
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json

# Run the setup script
python scripts/setup_spreadsheet.py
```

This script will:
- Create the required sheets if they don't exist
- Set up headers from schema field names
- Freeze header rows
- Add data validation for enum fields (dropdowns)
- Format columns appropriately

**Note**: The script is idempotent - it won't overwrite existing sheets, only creates missing ones.

### Configuration

The spreadsheet ID is configured in `shared/config.py` as `MAIN_SPREADSHEET_ID`. It can be overridden via the `SPREADSHEET_ID` environment variable.
