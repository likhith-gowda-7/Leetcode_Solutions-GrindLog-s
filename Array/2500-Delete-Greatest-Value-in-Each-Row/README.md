# 2500. Delete Greatest Value in Each Row


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/delete-greatest-value-in-each-row/)


## 📝 Problem Description

You are given an `m x n` matrix `grid` consisting of positive integers.

Perform the following operation until `grid` becomes empty:

	- Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.

	- Add the maximum of deleted elements to the answer.

**Note** that the number of columns decreases by one after each operation.

Return *the answer after performing the operations described above*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/10/19/q1ex1.jpg)
```

**Input:** grid = [[1,2,4],[3,3,1]]
**Output:** 8
**Explanation:** The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2022/10/19/q1ex2.jpg)
```

**Input:** grid = [[10]]
**Output:** 10
**Explanation:** The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 50`

	- `1 <= grid[i][j] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting each row in the grid, and then summing up the maximum value in each column. This approach takes advantage of the fact that the maximum value in each column will be the maximum value in the corresponding row.

**Approach**
1. Sort each row in the grid using a list comprehension.
2. Use the `zip(*grid)` function to transpose the grid, effectively swapping rows and columns.
3. Use a generator expression to find the maximum value in each column by summing up the maximum values.
4. Return the sum of the maximum values as the result.

**Time Complexity**
The time complexity of this solution is O(m*n log n), where m is the number of rows and n is the number of columns. This is because we are sorting each row, which takes O(n log n) time, and we are doing this for m rows.

**Space Complexity**
The space complexity of this solution is O(m*n), as we are creating a new sorted grid.

**Key Insight**
The key insight here is that by sorting each row, we can efficiently find the maximum value in each column by summing up the maximum values. This approach avoids the need to use a priority queue or other complex data structures, making it a simple and efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 78.92%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-01-15 |
| 💻 Language | Python |