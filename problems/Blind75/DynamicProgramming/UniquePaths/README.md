## Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

---

#### Example 1:

<img src="UniquePaths.jpg" alt="Unique Paths">

> **Input:** m = 3, n = 7<br>
> **Output:** 28

#### Example 2:

> **Input:** m = 3, n = 2<br>
> **Output:** 3<br>
> **Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:<br>
> 1. Right -> Down -> Down<br>
> 2. Down -> Down -> Right<br>
> 3. Down -> Right -> Down<br>

---

**Solution explained in picture**

<img src="UniquePathsDrawing.jpg" alt="Unique Paths Solution">
