# Copilot Custom Instructions for Proactive Commute Shield

## Repository Context
This is a **public open-core showcase** repository for the Proactive Commute Shield project, developed at the 5th Agentic AI Hackathon with Google Cloud (Mini Hackathon Shibuya, September 5, 2026).

## Air-Gap Tier 2 Security Boundary
This repository operates under strict Air-Gap Tier 2 isolation. Copilot MUST adhere to the following constraints:

### Absolute Prohibitions
- **DO NOT** reference, generate, or suggest any internal or private filesystem paths (e.g., `C:\internal\...`, `/private/...`)
- **DO NOT** use internal agent identifiers, organizational IDs, or proprietary naming conventions
- **DO NOT** embed API keys, secrets, tokens, or credentials in any form — always use environment variables or `.env.example` placeholders
- **DO NOT** reference internal governance standards, protocols, or framework nomenclature
- **DO NOT** generate code that calls real external APIs without proper environment variable gating

### Technology Stack
- **Language**: Python 3.11+
- **UI Framework**: Streamlit
- **AI Backend**: Google Vertex AI (Gemini 2.0 Flash)
- **Transit API**: Ekispert API (Val Laboratory)
- **Security**: Trend Micro Vision One (TrendAI)
- **Beauty/AR**: YouCam (Perfect Corp)

### Testing Standards
- All tests use `DEMO_KEY` fast-mock mode for 100% offline operation
- No real API calls are permitted in test suites
- Test file location: `tests/test_fast_mock_e2e.py`

### Documentation Standards
- `README.md`: Primary documentation in Japanese (for domestic audience)
- `AGENTS.md`: English technical specification (for international users and AI agents)
- Both files must maintain bidirectional semantic links

### License
MIT License — all contributions must be compatible with MIT licensing terms.
