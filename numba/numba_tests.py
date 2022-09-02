"""
Testing utilities for Numba
"""
import timeit
from numba import jit
import numpy as np

"""
Numba is a just-in-time compiler for Python that works best on code that uses NumPy arrays and functions, and loops. 
The most common way to use Numba is through its collection of decorators that can be applied to your functions to 
instruct Numba to compile them. When a call is made to a Numba-decorated function it is compiled to machine code 
“just-in-time” for execution and all or part of your code can subsequently run at native machine code speed!
"""

