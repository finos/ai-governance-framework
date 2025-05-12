# Download Scripts

These scripts bring in Markdown versions of LLM-related risks from OWASP and NIST to make it easier to enlist a coding assistant (GitHub Copilot, etc.) to help with cross-referencing tasks.

Unless otherwise noted, they are implemented using `bash(1)` and `curl(1)` to (hopefully) make them useful across multiple platforms without needing to worry about language versions and packages.

## dl-owasp-llm-md
  - Downloads Markdown files from the OWASP repository into the `_refs-markdown/owasp-llm_<year>` directory.
  - Defaults to 2025 by default. Pass `2024` if you want a copy of that instead.
  - Usage: `./dl-owasp-llm-md [year]`

## dl_nist-ai-600-1-md`
   - Downloads the (presumably-latest) `NIST.AI.600-1.md` file from the (unofficial) Cloud Security Alliance GitHub repository.
   - Saves the file to the `_refs-markdown/nist-ai-600_<year>` directory.
   - Usage: `./dl_nist-ai-600-1-md`


