class JumpGame (object):

    # Greedy solution O(n)
    def canJump(self, nums):

        # Initialize target to the last index
        target = len(nums) - 1

        # Iterate backwards from the last index
        for i in range(len(nums) - 1, -1, -1):
            # If the current index plus the value at the current index is greater than or equal to the target
            if i + nums[i] >= target:
                # Update the target to the current index (move it one to the left)
                target = i

        # If the target is 0, then we can reach the end
        return True if target == 0 else False
