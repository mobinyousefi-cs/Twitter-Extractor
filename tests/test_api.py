#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: tests/test_api.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Unit tests for the TwitterClient wrapper using mocks.

Usage:
pytest -q

Notes:
- Uses unittest.mock patching for Tweepy and credentials loader.
===========================================================================
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

from twitter_extractor.api import TwitterClient


@patch("twitter_extractor.api.load_credentials")
@patch("tweepy.Client")
def test_client_init_readonly(mock_client, mock_load):
    mock_load.return_value = type("C", (), {"bearer_token": "BT"})()
    c = TwitterClient()
    assert hasattr(c, "client")
    mock_client.assert_called_once()


@patch("twitter_extractor.api.load_credentials")
@patch("tweepy.Client")
def test_search_generates_pages(mock_client, mock_load):
    mock_load.return_value = type("C", (), {"bearer_token": "BT"})()

    # Fake Tweepy paginator pages
    fake_page = type("P", (), {"data": [MagicMock()], "includes": {}})()
    mock_client.return_value.search_recent_tweets.return_value = [fake_page]

    c = TwitterClient()
    gen = c.search("python", limit_pages=1)
    first = next(gen)
    assert hasattr(first, "data")