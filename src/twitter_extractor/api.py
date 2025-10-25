#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: api.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Thin wrapper around Tweepy v2 Client to perform recent search and optional posting.

Usage:
from twitter_extractor.api import TwitterClient
client = TwitterClient()
for page in client.search("python lang:en -is:retweet", pages=1):
    ...

Notes:
- Set wait_on_rate_limit=True to handle API rate limits gracefully.
===========================================================================
"""
from __future__ import annotations

from typing import Optional, Sequence

import tweepy

from .config import load_credentials


DEFAULT_TWEET_FIELDS: Sequence[str] = (
    "id",
    "text",
    "author_id",
    "created_at",
    "lang",
    "conversation_id",
    "public_metrics",
)


class TwitterClient:
    """Thin wrapper over Tweepy v2 Client for search and (optional) posting."""

    def __init__(self, *, bearer_only: bool = True):
        creds = load_credentials()
        if bearer_only:
            self.client = tweepy.Client(bearer_token=creds.bearer_token, wait_on_rate_limit=True)
            self._can_write = False
        else:
            # For write endpoints, you must provide full credentials.
            self.client = tweepy.Client(
                bearer_token=creds.bearer_token,
                consumer_key=creds.api_key,
                consumer_secret=creds.api_key_secret,
                access_token=creds.access_token,
                access_token_secret=creds.access_token_secret,
                wait_on_rate_limit=True,
            )
            self._can_write = True

    # --- READ ---
    def search(
        self,
        query: str,
        *,
        max_results: int = 100,
        start_time: Optional[str] = None,  # ISO 8601
        end_time: Optional[str] = None,    # ISO 8601
        tweet_fields: Sequence[str] = DEFAULT_TWEET_FIELDS,
        expansions: Sequence[str] | None = ("author_id",),
        user_fields: Sequence[str] | None = ("id", "name", "username"),
        limit_pages: int | None = 10,
    ):
        """Generator over Tweepy Paginator pages for recent search."""
        paginator = tweepy.Paginator(
            self.client.search_recent_tweets,
            query=query,
            max_results=min(max(10, max_results), 100),
            tweet_fields=list(tweet_fields),
            expansions=list(expansions) if expansions else None,
            user_fields=list(user_fields) if user_fields else None,
            start_time=start_time,
            end_time=end_time,
        )
        for i, page in enumerate(paginator):
            yield page
            if limit_pages and i + 1 >= limit_pages:
                break

    # --- WRITE (optional) ---
    def post_tweet(self, text: str) -> str:
        if not self._can_write:
            raise RuntimeError("Client not initialized with write permissions.")
        resp = self.client.create_tweet(text=text)
        return str(resp.data.get("id"))