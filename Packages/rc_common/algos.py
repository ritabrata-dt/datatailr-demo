from typing import List
import numpy as np


def get_zeros(n: int) -> List[int]:
    return [0] * n


def get_ones(n: int) -> List[int]:
    return [1] * n


def get_sin(x: List[float]) -> List[float]:
    return np.sin(x)


def get_range(start: float, end: float, step: float) -> List[float]:
    return np.arange(start, end, step)
