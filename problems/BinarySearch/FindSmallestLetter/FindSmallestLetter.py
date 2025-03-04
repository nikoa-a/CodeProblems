class FindSmallestLetter:

    def nextGreatersLetter(self, letters, target):

        left, right = 0, len(letters) - 1

        # Edge case
        if target < letters[left] or target >= letters[right]:
            return letters[left]

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid - 1
            elif letters[mid] <= target:
                left = mid + 1
            
        # If left is greater than right
        return letters[left]