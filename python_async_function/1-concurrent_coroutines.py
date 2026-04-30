#!/usr/bin/env python3
"""Async coroutine that executes multiple wait_random coroutines."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return sorted delays."""
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return sorted(delays)
