> 📌 **Cross-listed:** Primary location is [Array/3070-Count-Submatrices-with-Top-Left-Element-and-Sum-Less-Than-k](../../Array/3070-Count-Submatrices-with-Top-Left-Element-and-Sum-Less-Than-k). This problem also appears under: **Array**, **Matrix**, **Prefix Sum**

# 3070. Count Submatrices with Top-Left Element and Sum Less Than k


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/)


## 📝 Problem Description

You are given a **0-indexed** integer matrix `grid` and an integer `k`.

Return *the **number** of submatrices that contain the top-left element of the* `grid`, *and have a sum less than or equal to *`k`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2024/01/01/example1.png)
```

**Input:** grid = [[7,6,3],[6,6,1]], k = 18
**Output:** 4
**Explanation:** There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
```

Example 2:**

![](https://assets.leetcode.com/uploads/2024/01/01/example21.png)
```

**Input:** grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
**Output:** 6
**Explanation:** There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.

```

 

**Constraints:**

	- `m == grid.length `

	- `n == grid[i].length`

	- `1 <= n, m <= 1000 `

	- `0 <= grid[i][j] <= 1000`

	- `1 <= k <= 10^9`

## 🧠 Solution Explanation

**Intuition**
This solution uses a clever technique to efficiently count submatrices with a sum less than or equal to `k`. The key insight is to maintain a running prefix sum for each row and column, allowing us to quickly calculate the sum of submatrices. By iterating over the grid in a specific order, we can avoid redundant calculations and take advantage of the prefix sums to count the submatrices.

**Approach**

1. Initialize the result `res` to 0 and the top-left element `top` of the grid.
2. If the top-left element is less than or equal to `k`, increment `res` by 1.
3. Iterate over the first row of the grid, updating the prefix sum for each element and incrementing `res` if the sum is less than or equal to `k`.
4. Iterate over the first column of the grid, updating the prefix sum for each element and incrementing `res` if the sum is less than or equal to `k`.
5. Iterate over the rest of the grid, updating the prefix sum for each element by adding the sums of the element above and to the left, and subtracting the sum of the element diagonally above-left (to avoid double-counting). If the sum is less than or equal to `k`, increment `res` by 1.

**Time Complexity**
O(m \* n), where m is the number of rows and n is the number of columns in the grid. This is because we iterate over the grid once, performing a constant amount of work for each element.

**Space Complexity**
O(1), as we only use a constant amount of extra space to store the result and prefix sums.

**Key Insight**
The key to this solution is the use of prefix sums to efficiently calculate the sum of submatrices. By maintaining running prefix sums for each row and column, we can quickly determine whether a submatrix has a sum less than or equal to `k`, allowing us to count the submatrices in a single pass over the grid.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 299 ms (Beats 55.53%) |
| 💾 Memory | 65 MB (Beats 54%) |
| 📅 Solved | 2026-03-18 |
| 💻 Language | Python |