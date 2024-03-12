import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.FizzBuzz.FizzBuzz import FizzBuzz

def test_fizz_buzz():
    fizzbuzz_instance = FizzBuzz()

    # Test case 1
    n = 3
    expected = ["1", "2", "Fizz"]
    assert fizzbuzz_instance.fizzBuzz(n) == expected

    # Test case 2
    n = 15
    expected = [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert fizzbuzz_instance.fizzBuzz(n) == expected


    # Test case 3
    n = 0
    expected = []
    assert fizzbuzz_instance.fizzBuzz(n) == expected
