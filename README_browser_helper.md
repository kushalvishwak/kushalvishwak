# Browser helper

This repository now includes a small Windows-friendly browser automation helper.

## Usage

Run:

```powershell
python browser_helper.py https://example.com --screenshot screenshots/example.png --wait-seconds 3
```

This will:
- open the URL in a headless Chromium browser
- print the page title and final URL
- save a screenshot if requested

## Requirements

Install the dependency once:

```powershell
python -m pip install playwright
python -m playwright install chromium
```
