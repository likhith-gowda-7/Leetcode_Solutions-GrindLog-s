> 📌 **Cross-listed:** Primary location is [Array/1260-Shift-2D-Grid](../../Array/1260-Shift-2D-Grid). This problem also appears under: **Array**, **Matrix**, **Simulation**

# 1260. Shift 2D Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/shift-2d-grid/)


## 📝 Problem Description

Given a 2D `grid` of size `m x n` and an integer `k`. You need to shift the `grid` `k` times.

In one shift operation:

	- Element at `grid[i][j]` moves to `grid[i][j + 1]`.

	- Element at `grid[i][n - 1]` moves to `grid[i + 1][0]`.

	- Element at `grid[m - 1][n - 1]` moves to `grid[0][0]`.

Return the *2D grid* after applying shift operation `k` times.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/11/05/e1.png)
```

**Input:** `grid` = [[1,2,3],[4,5,6],[7,8,9]], k = 1
**Output:** [[9,1,2],[3,4,5],[6,7,8]]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2019/11/05/e2.png)
```

**Input:** `grid` = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
**Output:** [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

```

Example 3:**

```

**Input:** `grid` = [[1,2,3],[4,5,6],[7,8,9]], k = 9
**Output:** [[1,2,3],[4,5,6],[7,8,9]]

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m <= 50`

	- `1 <= n <= 50`

	- `-1000 <= grid[i][j] <= 1000`

	- `0 <= k <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution involves treating the 2D grid as a 1D array and shifting its elements according to the given rules. This approach allows us to simplify the problem and apply a standard array rotation technique.

**Approach**

1. Calculate the total number of elements in the grid (`m*n`) and store it in `last`.
2. If `k` is 0, return the original grid as no shifts are needed.
3. Create a dummy array `dummy` of size `last` to store the shifted elements.
4. Iterate through each element in the grid, calculate its new index using the formula `(idx+k)%last`, and store the element at the new index in the `dummy` array.
5. Iterate through the `dummy` array and assign its elements back to the original grid in their new positions.

**Time Complexity**
O(m*n) - We iterate through each element in the grid once to populate the `dummy` array, and then again to assign elements back to the grid. The total number of operations is proportional to the number of elements in the grid.

**Space Complexity**
O(m*n) - We create a dummy array of the same size as the grid to store the shifted elements. This requires additional space proportional to the size of the grid.

**Key Insight**
The key insight is to treat the 2D grid as a 1D array and apply a standard array rotation technique. This simplifies the problem and allows us to use a straightforward approach to shift the elements. The use of the modulo operator (`%`) to handle wrap-around cases is also crucial in this solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 6 ms (Beats 63.17%) |
| 💾 Memory | 19.6 MB (Beats 81.69%) |
| 📅 Solved | 2026-07-20 |
| 💻 Language | Python |