import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Open a URL in a headless browser and optionally save a screenshot."
    )
    parser.add_argument("url", help="The URL to open")
    parser.add_argument(
        "--screenshot",
        type=Path,
        default=None,
        help="Optional output path for a screenshot (for example screenshots/page.png)",
    )
    parser.add_argument(
        "--wait-seconds",
        type=float,
        default=5.0,
        help="How long to wait after the page loads before capturing output",
    )
    parser.add_argument(
        "--timeout-ms",
        type=int,
        default=30000,
        help="Navigation timeout in milliseconds",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = args.screenshot

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(args.url, wait_until="domcontentloaded", timeout=args.timeout_ms)
        page.wait_for_timeout(int(args.wait_seconds * 1000))

        title = page.title()
        print(f"Title: {title}")
        print(f"URL: {page.url}")

        if output_path is not None:
            page.screenshot(path=str(output_path), full_page=True)
            print(f"Screenshot saved to: {output_path}")

        browser.close()


if __name__ == "__main__": 
    main()
