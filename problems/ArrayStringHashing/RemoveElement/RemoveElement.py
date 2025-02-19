class RemoveElement():

    def removeElement(self, nums, val):

        last = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1): # Iterate backwards
            if nums[i] == val:
                nums[i] = nums[last]
                nums[last] = "_"
                last -= 1

        return last + 1