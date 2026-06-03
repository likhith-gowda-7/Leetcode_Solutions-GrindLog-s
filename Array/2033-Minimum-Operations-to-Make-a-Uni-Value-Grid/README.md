# 2033. Minimum Operations to Make a Uni-Value Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/)


## 📝 Problem Description

You are given a 2D integer `grid` of size `m x n` and an integer `x`. In one operation, you can **add** `x` to or **subtract** `x` from any element in the `grid`.

A **uni-value grid** is a grid where all the elements of it are equal.

Return *the **minimum** number of operations to make the grid **uni-value***. If it is not possible, return `-1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt.png)
```

**Input:** grid = [[2,4],[6,8]], x = 2
**Output:** 4
**Explanation:** We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt-1.png)
```

**Input:** grid = [[1,5],[2,3]], x = 1
**Output:** 5
**Explanation:** We can make every element equal to 3.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt-2.png)
```

**Input:** grid = [[1,2],[3,4]], x = 2
**Output:** -1
**Explanation:** It is impossible to make every element equal.

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 10^5`

	- `1 <= m * n <= 10^5`

	- `1 <= x, grid[i][j] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution works by first checking if it's possible to make all elements in the grid equal by subtracting or adding `x`. If not, it returns -1. Then, it finds the median of the grid elements, which will be the target value to make all elements equal to. The solution calculates the minimum number of operations required to make all elements equal to the median by dividing the absolute difference between each element and the median by `x`.

**Approach**
1. Initialize an empty list `arr` to store all elements from the grid.
2. Iterate through the grid and append each element to `arr`.
3. Check if all elements in `arr` can be made equal by subtracting or adding `x`. If not, return -1.
4. Sort `arr` in ascending order.
5. Find the median of `arr` (middle element) and store it in `mid`.
6. Initialize `res` to 0, which will store the minimum number of operations required.
7. Iterate through `arr` and for each element, calculate the absolute difference with `mid`.
8. Divide the absolute difference by `x` and add it to `res`.
9. Return `res`.

**Time Complexity**
O(n*m*log(n*m)) where n and m are the dimensions of the grid. This is because we first need to iterate through the grid to store all elements in `arr` (O(n*m)), then sort `arr` (O(n*m*log(n*m))).

**Space Complexity**
O(n*m) where n and m are the dimensions of the grid. This is because we store all elements from the grid in `arr`.

**Key Insight**
The key insight here is that we can make all elements in the grid equal by making them equal to the median of the grid elements. This is because the median is the middle value in the sorted array, and any element that is not equal to the median can be made equal to it by adding or subtracting a certain value.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 147 ms (Beats 54.49%) |
| 💾 Memory | 41.1 MB (Beats 39.18%) |
| 📅 Solved | 2026-04-28 |
| 💻 Language | Python |