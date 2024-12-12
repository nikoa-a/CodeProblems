class ProductOfArrayExceptSelf (object):

    def productExceptSelf(self, nums):

        # Initial cumulative product values for left and right arrays
        leftMult = 1
        rightMult = 1

        # Initialize the left and right arrays with zeros
        left = [0] * len(nums)
        right = [0] * len(nums)

        # Populate the left and right arrays
        # 'i' moves forward for the left array, 'j' moves backward for the right array
        for i in range(len(nums)):
            j = -i - 1 # Equivalent to iterating backwards

            # Fill the left array with cumulative products from the left
            left[i] = leftMult
            leftMult *= nums[i]

            # Fill the right array with cumulative products from the right
            right[j] = rightMult
            rightMult *= nums[j]

        # Combine left and right arrays explicitly
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result