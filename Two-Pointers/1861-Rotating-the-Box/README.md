> 📌 **Cross-listed:** Primary location is [Array/1861-Rotating-the-Box](../../Array/1861-Rotating-the-Box). This problem also appears under: **Array**, **Two Pointers**, **Matrix**

# 1861. Rotating the Box


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotating-the-box/)


## 📝 Problem Description

You are given an `m x n` matrix of characters `boxGrid` representing a side-view of a box. Each cell of the box is one of the following:

	- A stone `'#'`

	- A stationary obstacle `'*'`

	- Empty `'.'`

The box is rotated **90 degrees clockwise**, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity **does not** affect the obstacles' positions, and the inertia from the box's rotation **does not **affect the stones' horizontal positions.

It is **guaranteed** that each stone in `boxGrid` rests on an obstacle, another stone, or the bottom of the box.

Return *an *`n x m`* matrix representing the box after the rotation described above*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png)

```

**Input:** boxGrid = [["#",".","#"]]
**Output:** [["."],
         ["#"],
         ["#"]]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png)

```

**Input:** boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
**Output:** [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png)

```

**Input:** boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
**Output:** [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

```

 

**Constraints:**

	- `m == boxGrid.length`

	- `n == boxGrid[i].length`

	- `1 <= m, n <= 500`

	- `boxGrid[i][j]` is either `'#'`, `'*'`, or `'.'`.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the input grid from bottom to top and from right to left. It maintains a pointer `p` to keep track of the current position where a stone should be placed. When it encounters an obstacle or a stone, it places it at the current position and updates the pointer.

**Approach**
1. Initialize an empty result grid `res` with dimensions `n x m`, where `n` and `m` are the number of columns and rows in the input grid, respectively.
2. Iterate through each row `r` in the input grid from bottom to top.
3. Initialize a pointer `p` to the last column `cols - 1`.
4. Iterate through each column `c` in the row from right to left.
5. If the current cell is an obstacle `'*'`, place it at the corresponding position in the result grid and update the pointer `p` to the previous column.
6. If the current cell is a stone `'#'`, place it at the current position in the result grid and decrement the pointer `p`.
7. Repeat steps 4-6 until all columns in the row have been processed.
8. Return the result grid.

**Time Complexity**
O(m \* n), where m and n are the number of rows and columns in the input grid. This is because we iterate through each cell in the grid once.

**Space Complexity**
O(m \* n), where m and n are the number of rows and columns in the input grid. This is because we create a new grid of the same dimensions to store the result.

**Key Insight**
The key insight is to iterate through the input grid from bottom to top and from right to left, which allows us to take advantage of the fact that the stones fall due to gravity. By maintaining a pointer `p` to keep track of the current position where a stone should be placed, we can efficiently place each stone at its correct position in the result grid.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 73 ms (Beats 84.95%) |
| 💾 Memory | 57.1 MB (Beats 7.5%) |
| 📅 Solved | 2026-05-06 |
| 💻 Language | Python |