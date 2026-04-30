#!/usr/bin/env python3
"""Measure runtime of async comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run 4 async comprehensions in parallel"""
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    return time.time() - start
