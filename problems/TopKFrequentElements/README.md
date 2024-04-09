## Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

**Follow up:** Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

---

#### Example 1:
> **Input:** nums = [1,1,1,2,2,3], k = 2<br>
> **Output:** [1,2]

#### Example 2:
> **Input:** nums = [1], k = 1<br>
> **Output:** [1]

---

O(n log n) solution with sorting could look like:
```python
def topKFrequent(self, nums, k):

        # Initialize a dictionary to store the frequency of each number
        numFreq = {}

        # Iterate through the list of numbers
        for num in nums:
            # Increment the frequency of the number in the dictionary by 1
            numFreq[num] = numFreq.get(num, 0) + 1

        # Sort the dictionary by frequency in descending order
        sortedFreq = sorted(numFreq.items(), key=lambda x: x[1], reverse=True)
        
        # Get the top k frequent numbers
        topK = [pair[0] for pair in sortedFreq[:k]]

        # Return the top k frequent numbers
        return topK
```