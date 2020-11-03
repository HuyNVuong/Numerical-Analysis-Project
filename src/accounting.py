from typing import Callable
import math

def build_netincome_function(A: Callable[[float], float], r: float) -> Callable[[float], float]:
    return lambda t: A(t) * math.exp(-r * t)