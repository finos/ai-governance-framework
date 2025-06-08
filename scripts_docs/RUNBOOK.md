# Scripts Runbook

## Generated Artifacts

### `docs/_data/nist-sp-800-53r5.yml`
```bash
python scripts/dl_nist-pdfs.py --document sp-800-53r5 --leafs
```

**Note:** The PDF navigation pane for NIST SP 800-53r5 is incomplete, so the automated script will miss some entries.
Manual additions were made and may need to be reapplied for:
- `CA-2`, `CA-7`, `IR-5`, `PM-25`, `PM-31`, and `PT-1`

### `docs/_data/nist-ai-600-1.yml`
```bash
python scripts/dl_nist-pdfs.py --document ai-600-1 --leafs
```

### `docs/_data/eu-ai-act.yml`
```bash
python scripts/dl_eu-ai-act.py
```

### `docs/_data/ffiec-itbooklets.yml`
```bash
python scripts/dl_ffiec-itbooklets.py --yml
```
