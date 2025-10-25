#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: utils.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Utility functions to flatten Tweepy Tweet objects into CSV-friendly records.

Usage:
from twitter_extractor.utils import flatten_tweets

Notes:
- Public metrics are optional; defaults are handled safely.
===========================================================================
"""
from __future__ import annotations

from typing import Iterable, List

from .models import TweetRow


def flatten_tweets(tweets: Iterable, includes: dict | None = None) -> List[TweetRow]:
    """Convert Tweepy Tweet objects to flat rows.

    Parameters
    ----------
    tweets: Iterable of tweepy.Tweet
    includes: Optional includes dict returned by Tweepy (users, etc.)
    """
    rows: List[TweetRow] = []
    for t in tweets:
        public_metrics = getattr(t, "public_metrics", None) or {}
        rows.append(
            TweetRow(
                id=str(getattr(t, "id", "")),
                created_at=getattr(t, "created_at", None),
                text=getattr(t, "text", ""),
                author_id=str(getattr(t, "author_id", "")) or None,
                like_count=public_metrics.get("like_count"),
                retweet_count=public_metrics.get("retweet_count"),
                reply_count=public_metrics.get("reply_count"),
                quote_count=public_metrics.get("quote_count"),
                lang=getattr(t, "lang", None),
                conversation_id=str(getattr(t, "conversation_id", "")) or None,
            )
        )
    return rows