from typing import Callable
import math

def build_future_income_function(A: Callable[[float], float], T: float, r: float) -> Callable[[float], float]:
    return lambda t: A(t) * math.exp(r * (T - t))

def build_present_value_function(A: Callable[[float], float], r: float) -> Callable[[float], float]:
    return lambda t: A(t) * math.exp(-r * t)    