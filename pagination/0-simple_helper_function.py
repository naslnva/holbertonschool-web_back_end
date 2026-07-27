#!/usr/bin/env python3
"""This module provides helper functions for pagination."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end indexes for pagination.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
