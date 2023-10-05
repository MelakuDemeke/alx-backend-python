#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable:
    def mul(n: float) -> float:
        return n * multiplier