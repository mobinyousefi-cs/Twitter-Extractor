#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: __init__.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Package initialization and version helper for the twitter_extractor package.

Usage:
from twitter_extractor import __version__

Notes:
- Falls back to \"0.0.0\" when distribution metadata is unavailable.
===========================================================================
"""
"""twitter_extractor package.

High-level utilities for extracting tweets with Tweepy v2 Client, via
both CLI and Tkinter GUI interfaces.

Author: Mobin Yousefi (github.com/mobinyousefi-cs)
License: MIT
"""
from importlib.metadata import version, PackageNotFoundError

__all__ = [
    "__version__",
]

try:
    __version__ = version("twitter-extractor")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"