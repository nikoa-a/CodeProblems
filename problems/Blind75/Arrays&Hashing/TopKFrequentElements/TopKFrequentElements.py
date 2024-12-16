import heapq

class TopKFrequentElements (object):

    # With heap we can achieve O(n log k) time complexity
    # Where n is the length of the array and k is the number of top frequent elements.
    def topKFrequent(self, nums, k):

        # Initialize a dictionary to store the frequency of each number
        numFreq = {}

        # Iterate through the list of numbers
        for num in nums:
            # Increment the frequency of the number in the dictionary by 1
            numFreq[num] = numFreq.get(num, 0) + 1

        # Initialize a min-heap
        heap = []

        # Iterate through the dictionary of numbers and their frequencies and push them into the heap
        for num, freq in numFreq.items():
            heapq.heappush(heap, (freq, num))
            # If the size of the heap is greater than k, pop the smallest element
            if len(heap) > k:
                heapq.heappop(heap)

        # Initialize a list to store the top k frequent elements
        topK = [pair[1] for pair in heap]

        # Return the top k frequent elements
        return topK


# Time complexity: O(n log k)
# Space complexity: O(n + k)