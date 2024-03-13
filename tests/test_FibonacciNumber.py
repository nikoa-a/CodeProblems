import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.FibonacciNumber.FibonacciNumber import FibonacciNumber

def test_fibonacci_number():
    fibonacci_instance = FibonacciNumber()

    # Test case 1
    n = 2
    expected = 1
    assert fibonacci_instance.fibonacciNumber(n) == expected

    # Test case 2
    n = 3
    expected = 2
    assert fibonacci_instance.fibonacciNumber(n) == expected


    # Test case 3
    n = 4
    expected = 3
    assert fibonacci_instance.fibonacciNumber(n) == expected
    