#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: tests/test_io_utils.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Unit tests for DataFrame conversion and CSV saving utilities.

Usage:
pytest -q

Notes:
- Writes to tmp_path; asserts output exists.
===========================================================================
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from twitter_extractor.io_utils import to_dataframe, save_csv
from twitter_extractor.models import TweetRow


def test_to_dataframe_and_save(tmp_path: Path):
    rows = [
        TweetRow(id="1", created_at=None, text="hi", author_id="2", like_count=1, retweet_count=0, reply_count=0, quote_count=0, lang="en", conversation_id="1"),
        TweetRow(id="2", created_at=None, text="hey", author_id="3", like_count=2, retweet_count=1, reply_count=0, quote_count=0, lang="en", conversation_id="2"),
    ]
    df = to_dataframe(rows)
    assert isinstance(df, pd.DataFrame)
    out = save_csv(df, tmp_path / "out.csv")
    assert out.exists()