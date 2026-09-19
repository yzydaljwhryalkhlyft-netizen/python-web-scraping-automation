# High Performance Python Web Scraper and Data Extractor

An enterprise grade Python script designed to safely extract clean, structured datasets from complex websites while bypassing modern anti bot challenges.

## Key Engineering Capabilities
- **Playwright Automation** Replaces traditional requests to handle heavy, dynamic JavaScript loaded content.
- **Anti Bot Resilience** Built in custom headers and human like interactions to prevent 403 Forbidden or 429 Too Many Requests errors.
- **Automated Data Cleaning** Seamless integration with the Pandas library to drop duplicates, format prices, and structure datasets immediately.
- **Clean Deliverables** Generates organized, sorting ready Excel (XLSX) or CSV files for direct business analysis.

## Project Structure
- `scraper.py` Core automation script managing headless sessions and element parsing.
- `extracted_data.xlsx` Sample generated output confirming data schema and alignment accuracy.

## Security Compliance
This architecture isolates credentials and strictly adheres to dynamic site delays to preserve server health and avoid system bans.
