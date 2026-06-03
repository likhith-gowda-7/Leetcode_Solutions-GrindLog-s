> 📌 **Cross-listed:** Primary location is [Array/1351-Count-Negative-Numbers-in-a-Sorted-Matrix](../../Array/1351-Count-Negative-Numbers-in-a-Sorted-Matrix). This problem also appears under: **Array**, **Binary Search**, **Matrix**

# 1351. Count Negative Numbers in a Sorted Matrix


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)


## 📝 Problem Description

Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return *the number of **negative** numbers in* `grid`.

 

Example 1:**

```

**Input:** grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
**Output:** 8
**Explanation:** There are 8 negatives number in the matrix.

```

Example 2:**

```

**Input:** grid = [[3,2],[1,0]]
**Output:** 0

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 100`

	- `-100 <= grid[i][j] <= 100`

 

**Follow up:** Could you find an `O(n + m)` solution?

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach to find the first negative number in each row. Since the matrix is sorted in non-increasing order, the first negative number in each row is the first number that is less than or equal to 0. By finding the index of this number, we can calculate the total number of negative numbers in the matrix.

**Approach**
1. Define a helper function `find(r, arr)` that performs binary search on the array `arr` to find the first negative number.
2. Initialize a variable `neg` to store the total number of negative numbers.
3. Iterate through each row `arr` in the matrix `grid`.
4. For each row, find the index of the first negative number using the `find(r, arr)` function.
5. The index of the first negative number is the first number that is less than or equal to 0. To find the total number of negative numbers in the row, subtract the index from the length of the row and add 1.
6. Add the total number of negative numbers in the row to the `neg` variable.
7. Return the total number of negative numbers `neg`.

**Time Complexity**
The time complexity of the solution is O(m*n log n), where m is the number of rows and n is the number of columns. This is because we perform a binary search on each row, which takes O(log n) time, and we do this for each row, resulting in a total time complexity of O(m*n log n).

**Space Complexity**
The space complexity of the solution is O(1), as we only use a constant amount of space to store the variables `neg`, `l`, `r`, and `mid`.

**Key Insight**
The key insight behind this solution is that we can use binary search to find the first negative number in each row, which allows us to efficiently count the total number of negative numbers in the matrix. This approach takes advantage of the fact that the matrix is sorted in non-increasing order, both row-wise and column-wise.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.5 MB (Beats 100%) |
| 📅 Solved | 2025-12-28 |
| 💻 Language | Python |