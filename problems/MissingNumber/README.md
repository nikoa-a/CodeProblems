## Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

---

#### Example 1:
> **Input:** nums = [3,0,1]<br>
> **Output:** 2<br>
> **Explanation:**<br>
> n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

#### Example 2:

> **Input:** nums = [0,1]<br>
> **Output:** 2<br>
> **Explanation:**<br>
> n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

#### Follow up: 
> Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Solved with XOR, exclusive OR, for best efficiency

Easiest way of solving this is:

```python
def missingNumber(self, nums):

        for n in range(len(nums) + 1):
            if n not in nums:
                return n

        return 0
```
