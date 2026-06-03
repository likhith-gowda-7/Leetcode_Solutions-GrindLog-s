> 📌 **Cross-listed:** Primary location is [Array/3446-Sort-Matrix-by-Diagonals](../../Array/3446-Sort-Matrix-by-Diagonals). This problem also appears under: **Array**, **Sorting**, **Matrix**

# 3446. Sort Matrix by Diagonals


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sort-matrix-by-diagonals/)


## 📝 Problem Description

You are given an `n x n` square matrix of integers `grid`. Return the matrix such that:

	- The diagonals in the **bottom-left triangle** (including the middle diagonal) are sorted in **non-increasing order**.

	- The diagonals in the **top-right triangle** are sorted in **non-decreasing order**.

 

Example 1:**

**Input:** grid = [[1,7,3],[9,8,2],[4,5,6]]

**Output:** [[8,2,3],[9,6,7],[4,5,1]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/12/29/4052example1drawio.png)

The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

	- `[1, 8, 6]` becomes `[8, 6, 1]`.

	- `[9, 5]` and `[4]` remain unchanged.

The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

	- `[7, 2]` becomes `[2, 7]`.

	- `[3]` remains unchanged.

Example 2:**

**Input:** grid = [[0,1],[1,2]]

**Output:** [[2,1],[1,0]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/12/29/4052example2adrawio.png)

The diagonals with a black arrow must be non-increasing, so `[0, 2]` is changed to `[2, 0]`. The other diagonals are already in the correct order.

Example 3:**

**Input:** grid = [[1]]

**Output:** [[1]]

**Explanation:**

Diagonals with exactly one element are already in order, so no changes are needed.

 

**Constraints:**

	- `grid.length == grid[i].length == n`

	- `1 <= n <= 10`

	- `-10^5 <= grid[i][j] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a queue to traverse the matrix diagonally, sorting the elements in each diagonal in either non-increasing or non-decreasing order depending on the triangle. The key insight is to use a single pass through the matrix to achieve this, leveraging the properties of diagonals to simplify the sorting process.

**Approach**
1. Initialize a queue with the top-right and bottom-left corners of the matrix.
2. Define two helper functions: `get_diagonals` to collect elements from a diagonal, and `write_diagonals` to replace the original elements with the sorted ones.
3. Iterate through the queue, popping each element and collecting the elements from its diagonal using `get_diagonals`.
4. Sort the collected elements in either non-increasing or non-decreasing order depending on the triangle.
5. Replace the original elements with the sorted ones using `write_diagonals`.
6. Toggle the sorting order when reaching the middle diagonal.
7. Repeat steps 3-6 until the queue is empty.

**Time Complexity**
O(n^2) - The solution visits each element in the matrix once, performing a constant amount of work for each element.

**Space Complexity**
O(n^2) - The solution uses a queue to store the diagonals, which can grow up to n^2 in the worst case.

**Key Insight**
The solution's efficiency lies in its ability to traverse the matrix diagonally, leveraging the properties of diagonals to simplify the sorting process. By using a single pass through the matrix and toggling the sorting order when reaching the middle diagonal, the solution achieves the desired sorting of diagonals in both triangles.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 49.32%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-08-28 |
| 💻 Language | Python |