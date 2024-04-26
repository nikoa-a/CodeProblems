class CombinationSum (object):

    def combinationSum(self, candidates, target):

        # Initialize the result list
        result = []

        # Define the recursive depth first search function to find the combinations
        def dfs(i, current, total):
            # If the total is equal to the target, add the current combination to the result list
            if total == target:
                result.append(current.copy())
                return
            
            # If the total is greater than the target or the index is greater than the length of the candidates list, return
            if i >= len(candidates) or total > target:
                return

            # Include the current candidate in the current combination
            current.append(candidates[i])
            # Recursively call the function with the current index, the current combination, and the total sum
            dfs(i, current, total + candidates[i])
            # Backtrack: Remove the current candidate from the current combination before trying the next one
            current.pop()
            # Move to the next candidate and continue the recursion
            dfs(i + 1, current, total)

        # Call the depth first search function with the initial index, an empty list, and a total of 0
        dfs(0, [], 0)
        # Return the result list
        return result
