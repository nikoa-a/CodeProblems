## Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

---

#### Example 1:
> **Input:** a = 1, b = 2<br>
> **Output:** 3

#### Example 2:
> **Input:** a = 2, b = 3<br>
> **Output:** 5

---

This has more simple solution with Java that can not be achieved in Python:
```java
public int getSum(int a, int b) {

    // Loop until the carry value ends up being 0
    while (b != 0) {
        // Calculate the carry bit and shift it to the left
        int carry = (a & b) << 1;
        // Sum without considering the carry
        a = a ^ b;
        // Update 'b' to hold the carry for the next iteration
        b = carry;
    }
    // Return the final sum
    return a;
}
```
