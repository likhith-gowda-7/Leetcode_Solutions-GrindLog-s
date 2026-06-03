# 2579. Count Total Number of Colored Cells


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-total-number-of-colored-cells/)


## 📝 Problem Description

There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer `n`, indicating that you must do the following routine for `n` minutes:

	- At the first minute, color **any** arbitrary unit cell blue.

	- Every minute thereafter, color blue **every** uncolored cell that touches a blue cell.

Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.

![](https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png)
Return *the number of **colored cells** at the end of *`n` *minutes*.

 

Example 1:**

```

**Input:** n = 1
**Output:** 1
**Explanation:** After 1 minute, there is only 1 blue cell, so we return 1.

```

Example 2:**

```

**Input:** n = 2
**Output:** 5
**Explanation:** After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 

```

 

**Constraints:**

	- `1 <= n <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem describes a process of coloring unit cells in a grid, where each cell is colored blue if it touches a blue cell. The solution involves recognizing a pattern in the number of colored cells after each minute.

**Approach**
1. The solution starts by recognizing that the number of colored cells forms a square pattern.
2. After `n` minutes, the number of colored cells is equal to the sum of the number of cells in two squares: one with side length `n` and the other with side length `n-1`.
3. This is because each new minute adds a square of side length `n` to the existing square of side length `n-1`.

**Time Complexity**
O(1) - The solution involves a simple mathematical calculation and does not depend on the input size `n`.

**Space Complexity**
O(1) - The solution only uses a constant amount of space to store the result and does not depend on the input size `n`.

**Key Insight**
The key insight is recognizing that the number of colored cells forms a square pattern, which allows us to calculate the total number of colored cells as the sum of two squares. This pattern arises from the fact that each new minute adds a square of side length `n` to the existing square of side length `n-1`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-03-05 |
| 💻 Language | Python |