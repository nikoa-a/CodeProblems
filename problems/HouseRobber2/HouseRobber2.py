class HouseRobber2 (object):

    def rob(self, nums):

        # nums[0] is needed to handle the edge case where there is only one house
        # robHelper(nums[1:]) robs all houses except the first house
        # robHelper(nums[:-1]) robs all houses except the last house
        # Return the max amount of money that can be robbed from the three cases
        return max(nums[0], self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
    


    # Helper function to calculate the max amount of money that can be robbed
    # Code from first HouseRobber problem
    def robHelper(self, nums):
        rob1 = 0
        rob2 = 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
