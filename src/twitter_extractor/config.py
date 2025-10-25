#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: config.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Environment-backed configuration utilities for loading Twitter/X API credentials.

Usage:
from twitter_extractor.config import load_credentials
creds = load_credentials()

Notes:
- Supports .env via python-dotenv.
- For read-only search, BEARER_TOKEN is sufficient.
===========================================================================
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

# Load .env if present (useful for local dev)
load_dotenv()


@dataclass(frozen=True)
class TwitterCredentials:
    """Holds Twitter/X API credentials.

    Only BEARER_TOKEN is required for *read/search* with Tweepy v2 Client.
    For *write* (post tweet, etc.) you need API_KEY/API_SECRET and
    ACCESS_TOKEN/ACCESS_TOKEN_SECRET as well.
    """

    bearer_token: str
    api_key: Optional[str] = None
    api_key_secret: Optional[str] = None
    access_token: Optional[str] = None
    access_token_secret: Optional[str] = None


def load_credentials() -> TwitterCredentials:
    bt = os.getenv("TW_BEARER_TOKEN") or os.getenv("BEARER_TOKEN")
    if not bt:
        raise RuntimeError(
            "Missing BEARER token. Set TW_BEARER_TOKEN or BEARER_TOKEN in env/.env."
        )

    return TwitterCredentials(
        bearer_token=bt.strip(),
        api_key=(os.getenv("TW_API_KEY") or os.getenv("API_KEY") or None),
        api_key_secret=(os.getenv("TW_API_SECRET") or os.getenv("API_SECRET") or None),
        access_token=(os.getenv("TW_ACCESS_TOKEN") or os.getenv("ACCESS_TOKEN") or None),
        access_token_secret=(
            os.getenv("TW_ACCESS_SECRET") or os.getenv("ACCESS_TOKEN_SECRET") or None
        ),
    )