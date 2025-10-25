#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: models.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Lightweight dataclasses used to represent flattened tweet rows for CSV/DF export.

Usage:
from twitter_extractor.models import TweetRow

Notes:
- Keep models minimal and serializable.
===========================================================================
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TweetRow:
    """Flattened tweet row for CSV/DF."""

    id: str
    created_at: Optional[datetime]
    text: str
    author_id: Optional[str]
    like_count: Optional[int]
    retweet_count: Optional[int]
    reply_count: Optional[int]
    quote_count: Optional[int]
    lang: Optional[str]
    conversation_id: Optional[str]
