# Twitter Extractor (Tweepy v2) — CLI & Tkinter GUI

> Built with ❤️ by [mobinyousefi-cs](https://github.com/mobinyousefi-cs)

This project searches recent tweets via the official Twitter/X API (v2) using Tweepy, and saves the results into CSV files using pandas. It provides both a command‑line interface and a simple Tkinter GUI.

> ⚠️ You must have Twitter/X API credentials. At minimum, **BEARER_TOKEN** for read/search. For write endpoints (e.g., posting tweets), you need full keys/tokens.

## Features
- Recent search via Tweepy v2 `Client` with rate-limit handling
- Clean flattening to CSV (id, text, created_at, metrics, etc.)
- CLI (`twitter-extractor`) and GUI (`twitter-extractor-gui`)
- `src/` layout, pytest, Ruff, Black, GitHub Actions CI

## Quickstart

### 1) Clone & create venv
```bash
git clone https://github.com/mobinyousefi-cs/twitter-extractor.git
cd twitter-extractor
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
````

### 2) Install

```bash
pip install -U pip
pip install -e .
```

### 3) Configure credentials

Create a `.env` file in project root **or** export env vars in your shell:

```env
# Required for read/search
TW_BEARER_TOKEN=YOUR_BEARER_TOKEN

# Optional if you want write access
TW_API_KEY=...
TW_API_SECRET=...
TW_ACCESS_TOKEN=...
TW_ACCESS_SECRET=...
```

> Where do I get these? Apply for a developer account at Twitter/X and create a Project & App to generate tokens.

### 4) Run CLI

```bash
twitter-extractor "python lang:en -is:retweet" --pages 2 --max-results 50 --out outputs/tweets.csv
```

### 5) Run GUI

```bash
twitter-extractor-gui
```

Enter a query (e.g., `python lang:en -is:retweet`), choose page count and output path, then **Fetch**.

## Testing & Linting

```bash
pytest
ruff check .
black --check .
```

## Packaging

```bash
pip install build
python -m build
```

## Notes

* This tool uses **recent search** (last ~7 days). For full archive search, you need appropriate elevated access.
* Respect Twitter/X Developer Policy and local laws when collecting and storing data.

## License

MIT