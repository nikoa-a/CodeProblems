class SearchInsertPosition:

    def searchInsert(self, nums, target):

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        # If target is not found, left naturally becomes the correct insert position when the loop exits.
        return left