import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.ClimbingStairs.ClimbingStairs import ClimbingStairs

def test_climbing_stairs():
    climbing_stairs_instance = ClimbingStairs()

    # Test case 1
    n = 2
    expected = 2
    assert climbing_stairs_instance.climbStairs(n) == expected

    # Test case 2
    n = 3
    expected = 3
    assert climbing_stairs_instance.climbStairs(n) == expected
    