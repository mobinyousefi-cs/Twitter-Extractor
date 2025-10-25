#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Twitter Extractor (Tweepy v2 — CLI & GUI)
File: gui/app.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-25
Updated: 2025-10-25
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Tkinter GUI to input search parameters and save tweets to CSV.

Usage:
from twitter_extractor.gui.app import run
run()

Notes:
- Simple, blocking Tk mainloop; suitable for quick desktop usage.
===========================================================================
"""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

from ..api import TwitterClient
from ..io_utils import to_dataframe, save_csv
from ..utils import flatten_tweets


class TwitterGUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Twitter Extractor")
        self.geometry("640x360")
        self.resizable(False, False)
        self._build()

    def _build(self):
        pad = {"padx": 10, "pady": 6}

        frm = ttk.Frame(self)
        frm.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frm, text="Query").grid(row=0, column=0, sticky="w", **pad)
        self.q_var = tk.StringVar(value="python lang:en -is:retweet")
        ttk.Entry(frm, textvariable=self.q_var, width=60).grid(row=0, column=1, columnspan=3, sticky="ew", **pad)

        ttk.Label(frm, text="Max/Page").grid(row=1, column=0, sticky="w", **pad)
        self.max_var = tk.IntVar(value=50)
        ttk.Spinbox(frm, from_=10, to=100, textvariable=self.max_var, width=8).grid(row=1, column=1, sticky="w", **pad)

        ttk.Label(frm, text="Pages").grid(row=1, column=2, sticky="w", **pad)
        self.pages_var = tk.IntVar(value=2)
        ttk.Spinbox(frm, from_=1, to=50, textvariable=self.pages_var, width=8).grid(row=1, column=3, sticky="w", **pad)

        ttk.Label(frm, text="Start (ISO8601)").grid(row=2, column=0, sticky="w", **pad)
        self.start_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.start_var, width=30).grid(row=2, column=1, sticky="w", **pad)

        ttk.Label(frm, text="End (ISO8601)").grid(row=2, column=2, sticky="w", **pad)
        self.end_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.end_var, width=30).grid(row=2, column=3, sticky="w", **pad)

        ttk.Separator(frm).grid(row=3, column=0, columnspan=4, sticky="ew", pady=6)

        ttk.Label(frm, text="Output CSV").grid(row=4, column=0, sticky="w", **pad)
        self.out_var = tk.StringVar(value=str(Path("outputs/tweets.csv")))
        ttk.Entry(frm, textvariable=self.out_var, width=50).grid(row=4, column=1, columnspan=2, sticky="ew", **pad)
        ttk.Button(frm, text="Browse", command=self._browse).grid(row=4, column=3, sticky="w", **pad)

        btns = ttk.Frame(frm)
        btns.grid(row=5, column=0, columnspan=4, pady=12)
        ttk.Button(btns, text="Fetch", command=self._fetch).pack(side=tk.LEFT, padx=6)
        ttk.Button(btns, text="Quit", command=self.destroy).pack(side=tk.LEFT, padx=6)

    def _browse(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if path:
            self.out_var.set(path)

    def _fetch(self):
        try:
            client = TwitterClient()
            all_rows = []
            for page in client.search(
                query=self.q_var.get().strip(),
                max_results=int(self.max_var.get()),
                start_time=(self.start_var.get().strip() or None),
                end_time=(self.end_var.get().strip() or None),
                limit_pages=int(self.pages_var.get()),
            ):
                tweets = page.data or []
                all_rows.extend(flatten_tweets(tweets, includes=page.includes))

            df = to_dataframe(all_rows)
            save_csv(df, Path(self.out_var.get()))
            messagebox.showinfo("Done", f"Saved {len(df)} rows.")
        except Exception as e:  # pragma: no cover - GUI surface
            messagebox.showerror("Error", str(e))


def run():  # pragma: no cover
    app = TwitterGUI()
    app.mainloop()


if __name__ == "__main__":  # pragma: no cover
    run()