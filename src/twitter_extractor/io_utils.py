#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: io_utils.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
DataFrame helpers and CSV persistence utilities for tweet rows.

Usage:
from twitter_extractor.io_utils import to_dataframe, save_csv

Notes:
- Ensures datetime columns are parsed to pandas datetime.
===========================================================================
"""
from __future__ import annotations

import pandas as pd
from pathlib import Path
from typing import Iterable

from .models import TweetRow


def to_dataframe(rows: Iterable[TweetRow]) -> pd.DataFrame:
    df = pd.DataFrame([r.__dict__ for r in rows])
    # Ensure datetime columns are serializable
    if "created_at" in df.columns:
        df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    return df


def save_csv(df: pd.DataFrame, path: Path, index: bool = False) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)
    return path