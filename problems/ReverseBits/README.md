## Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

**Example 1:**

**Input:** n = 00000010100101000001111010011100

**Output:** 964176192 (00111001011110000010100101000000)

**Explanation:** The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Easiest solution to this problem. This approach may not be as efficient as bitwise operation:
```python
def reverseBits(self, n):
    # Convert n to binary string, reverse it, and convert it back to integer
    res = int(format(n, '032b')[::-1], 2)
    return res
```
