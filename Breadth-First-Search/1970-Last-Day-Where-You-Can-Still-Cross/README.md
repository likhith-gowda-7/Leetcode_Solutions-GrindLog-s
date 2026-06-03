> 📌 **Cross-listed:** Primary location is [Array/1970-Last-Day-Where-You-Can-Still-Cross](../../Array/1970-Last-Day-Where-You-Can-Still-Cross). This problem also appears under: **Array**, **Binary Search**, **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Matrix**

# 1970. Last Day Where You Can Still Cross


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/last-day-where-you-can-still-cross/)


## 📝 Problem Description

There is a **1-based** binary matrix where `0` represents land and `1` represents water. You are given integers `row` and `col` representing the number of rows and columns in the matrix, respectively.

Initially on day `0`, the **entire** matrix is **land**. However, each day a new cell becomes flooded with **water**. You are given a **1-based** 2D array `cells`, where `cells[i] = [r_i, c_i]` represents that on the `i^th` day, the cell on the `r_i^th` row and `c_i^th` column (**1-based** coordinates) will be covered with **water** (i.e., changed to `1`).

You want to find the **last** day that it is possible to walk from the **top** to the **bottom** by only walking on land cells. You can start from **any** cell in the top row and end at **any** cell in the bottom row. You can only travel in the** four** cardinal directions (left, right, up, and down).

Return *the **last** day where it is possible to walk from the **top** to the **bottom** by only walking on land cells*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/27/1.png)
```

**Input:** row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
**Output:** 2
**Explanation:** The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/07/27/2.png)
```

**Input:** row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
**Output:** 1
**Explanation:** The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/07/27/3.png)
```

**Input:** row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
**Output:** 3
**Explanation:** The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.

```

 

**Constraints:**

	- `2 <= row, col <= 2 * 10^4`

	- `4 <= row * col <= 2 * 10^4`

	- `cells.length == row * col`

	- `1 <= r_i <= row`

	- `1 <= c_i <= col`

	- All the values of `cells` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the last day when it's possible to walk from the top to the bottom of a binary matrix by only walking on land cells. The key insight is that we can use binary search to find this last day. We'll simulate the flooding process for each day and check if it's possible to reach the bottom row from the top row.

**Approach**
1. First, we adjust the coordinates of the cells array to 0-based indexing for easier processing.
2. We define a helper function `find(mid)` that simulates the flooding process up to the `mid-th` day and checks if it's possible to reach the bottom row from the top row.
3. In the `find(mid)` function, we create a 2D matrix `mat` to represent the state of the binary matrix after the `mid-th` day.
4. We use a queue `q` to perform a breadth-first search (BFS) from the top row to the bottom row.
5. In the BFS, we explore all the neighboring cells of the current cell and mark them as visited by setting their value to 1 in the matrix.
6. We repeat the BFS process until we reach the bottom row or the queue becomes empty.
7. If we reach the bottom row, it means it's possible to walk from the top to the bottom, and we return `True`. Otherwise, we return `False`.
8. In the main function, we use binary search to find the last day when it's possible to walk from the top to the bottom.
9. We initialize the left and right pointers to the first and last days, respectively.
10. We iterate until the left pointer is less than or equal to the right pointer.
11. In each iteration, we calculate the mid day and call the `find(mid)` function to check if it's possible to walk from the top to the bottom.
12. If it's possible, we move the left pointer to the mid day + 1. Otherwise, we move the right pointer to the mid day - 1.
13. We repeat the process until we find the last day when it's possible to walk from the top to the bottom.

**Time Complexity**
The time complexity of the solution is O(n log m), where n is the number of days and m is the number of cells in the matrix. This is because we use binary search to find the last day, and for each day, we perform a BFS that takes O(m) time.

**Space Complexity**
The space complexity of the solution is O(m), where m is the number of cells in the matrix. This is because we use a 2D matrix to represent the state of the binary matrix and a queue to perform the BFS.

**Key Insight**
The key insight is that we can use binary search to find the last day when it's possible to walk from the top to the bottom. By simulating the flooding process for each day and checking if it's possible to reach the bottom row from the top row, we can efficiently find the last day when it's possible to walk from the top to the bottom.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 851 ms (Beats 61.6%) |
| 💾 Memory | 24.9 MB (Beats 100%) |
| 📅 Solved | 2026-01-01 |
| 💻 Language | Python |