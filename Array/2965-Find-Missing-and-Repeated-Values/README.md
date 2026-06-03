# 2965. Find Missing and Repeated Values


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-missing-and-repeated-values/)


## 📝 Problem Description

You are given a **0-indexed** 2D integer matrix `grid` of size `n * n` with values in the range `[1, n^2]`. Each integer appears **exactly once** except `a` which appears **twice** and `b` which is **missing**. The task is to find the repeating and missing numbers `a` and `b`.

Return *a **0-indexed **integer array *`ans`* of size *`2`* where *`ans[0]`* equals to *`a`* and *`ans[1]`* equals to *`b`*.*

 

Example 1:**

```

**Input:** grid = [[1,3],[2,2]]
**Output:** [2,4]
**Explanation:** Number 2 is repeated and number 4 is missing so the answer is [2,4].

```

Example 2:**

```

**Input:** grid = [[9,1,7],[8,9,2],[3,4,6]]
**Output:** [9,5]
**Explanation:** Number 9 is repeated and number 5 is missing so the answer is [9,5].

```

 

**Constraints:**

	- `2 <= n == grid.length == grid[i].length <= 50`

	- `1 <= grid[i][j] <= n * n`

	- For all `x` that `1 <= x <= n * n` there is exactly one `x` that is not equal to any of the grid members.

	- For all `x` that `1 <= x <= n * n` there is exactly one `x` that is equal to exactly two of the grid members.

	- For all `x` that `1 <= x <= n * n` except two of them there is exactly one pair of `i, j` that `0 <= i, j <= n - 1` and `grid[i][j] == x`.

## 🧠 Solution Explanation

**Intuition**
This solution works by utilizing the properties of a hash set to keep track of the numbers in the grid and the sum of numbers from 1 to n^2. The missing number can be found by subtracting the sum of the numbers in the grid from the total sum of numbers from 1 to n^2. The repeating number is the one that exists in the hash set.

**Approach**
1. Initialize a hash set `h` to store unique numbers from the grid and a variable `a` to store the repeating number.
2. Calculate the total sum of numbers from 1 to n^2 using the formula `b = n * (n + 1) // 2 * n`.
3. Iterate through the grid, checking each number if it exists in the hash set `h`. If a number exists, update `a` to store the repeating number.
4. If a number does not exist in the hash set, add it to `h` and subtract it from `b` to find the missing number.
5. Return the repeating number `a` and the missing number `b`.

**Time Complexity**
O(n^2) - The solution iterates through the grid once, which has n^2 elements.

**Space Complexity**
O(n^2) - The solution uses a hash set to store unique numbers from the grid, which can have up to n^2 elements.

**Key Insight**
The key insight is to use the properties of a hash set to efficiently find the repeating and missing numbers. By subtracting the sum of numbers in the grid from the total sum of numbers from 1 to n^2, we can find the missing number in constant time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 64.48%) |
| 💾 Memory | 18.3 MB (Beats 100%) |
| 📅 Solved | 2025-03-06 |
| 💻 Language | Python |