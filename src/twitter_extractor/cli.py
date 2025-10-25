#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: cli.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Command-line interface to search recent tweets and export results to CSV.

Usage:
python -m twitter_extractor.cli "python lang:en -is:retweet" --pages 2 --out outputs/tweets.csv

Notes:
- Uses argparse; integrates with entry point `twitter-extractor`.
===========================================================================
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .api import TwitterClient
from .io_utils import to_dataframe, save_csv
from .utils import flatten_tweets


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Search recent tweets and save to CSV (Tweepy v2)",
    )
    p.add_argument("query", help="Search query, e.g. 'python (lang:en)' ")
    p.add_argument("--out", type=Path, default=Path("outputs/tweets.csv"), help="CSV path")
    p.add_argument("--max-results", type=int, default=100, help="Max results per page (10..100)")
    p.add_argument("--pages", type=int, default=2, help="How many pages to fetch (x*max-results)")
    p.add_argument("--start-time", type=str, default=None, help="ISO8601 start time")
    p.add_argument("--end-time", type=str, default=None, help="ISO8601 end time")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    client = TwitterClient()

    all_rows = []
    for page in client.search(
        query=args.query,
        max_results=args.max_results,
        start_time=args.start_time,
        end_time=args.end_time,
        limit_pages=args.pages,
    ):
        tweets = page.data or []
        rows = flatten_tweets(tweets, includes=page.includes)
        all_rows.extend(rows)

    df = to_dataframe(all_rows)
    save_csv(df, args.out)

    print(f"Saved {len(df)} rows to {args.out}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())