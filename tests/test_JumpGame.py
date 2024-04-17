import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.JumpGame.JumpGame import JumpGame

def test_longest_common_prefix():
    jump_game_instance = JumpGame()

    # Test case 1
    nums = [2,3,1,1,4]
    expected = True
    assert jump_game_instance.canJump(nums) == expected

    # Test case 1
    nums = [3,2,1,0,4]
    expected = False
    assert jump_game_instance.canJump(nums) == expected
