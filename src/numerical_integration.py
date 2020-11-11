from typing import Callable, List, Tuple
import random

def left_right_sum(f: Callable[[float], float],
                   interval: Tuple[float, float],
                   n_subintervals: int) -> (float, float):
    a, b = interval
    x_delta = (b - a) / n_subintervals

    ys = [f(a + x_delta * i) for i in range(n_subintervals + 1)]
    left_sum = x_delta * sum(ys[:len(ys) - 1])
    right_sum = x_delta * sum(ys[1:])

    return (left_sum, right_sum)

def trapezoid_sum(f: Callable[[float], float],
                  interval: Tuple[int, int],
                  n_subintervals: int) -> float:
    a, b = interval
    h = (b - a) / n_subintervals

    ys = [f(a + h * i) for i in range(n_subintervals + 1)]
    trapezoids = 1 / 2 * h * (f(a) + f(b) + 2 * sum([f(a + h * i) for i in range(1, n_subintervals)]))

    return trapezoids

def simpson_18rule(f: Callable[[float], float],
                   interval: Tuple[int, int],
                   n_subintervals: int) -> float:
    a, b = interval
    h = (b - a) / n_subintervals

    spline = 2 * sum(f(a + 2 * k * h) for k in range(1, int((n_subintervals - 2) / 2) + 1)) \
           + 4 * sum(f(a + (2 * k - 1) * h) for k in range(1, int(n_subintervals / 2) + 1))
    simpsons = h / 3 * (f(a) + f(b) + spline)
    
    return simpsons

def simpson_38rule(f: Callable[[float], float],
                   interval: Tuple[int, int],
                   n_subintervals: int) -> float:

    pass

def trapezoid_sum_error(f_derived: Callable[[float], float],
                        interval: Tuple[int, int],
                        n_subintervals: int) -> float:
    a, b = interval
    xi, _ = find_max(f_derived, interval)
    error =  -1 * (b - a) ** 3 / (12 * n_subintervals ** 2) * f_derived(xi)

    return error

def simpson18_error(f_derived: Callable[[float], float],
                    interval: Tuple[int, int],
                    n_subintervals: int) -> float:
    a, b = interval
    xi, _ = find_max(f_derived, interval)
    h = (b - a) / n_subintervals
    error =  1 / 180 * (b - a) * h ** 4 * f_derived(xi)

    return error


def find_max(f: Callable[[float], float],
             interval: Tuple[int, int],
             steps: float = 0.0001) -> float:
             
    a, b = interval
    fs = [(a + i * steps, f(a + i * steps)) for i in range(int((b - a) / steps) + 1)]

    return max(fs, key=lambda t: t[1])
