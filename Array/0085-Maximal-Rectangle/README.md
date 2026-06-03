# 85. Maximal Rectangle


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximal-rectangle/)


## 📝 Problem Description

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return *its area*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)
```

**Input:** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
**Output:** 6
**Explanation:** The maximal rectangle is shown in the above picture.

```

Example 2:**

```

**Input:** matrix = [["0"]]
**Output:** 0

```

Example 3:**

```

**Input:** matrix = [["1"]]
**Output:** 1

```

 

**Constraints:**

	- `rows == matrix.length`

	- `cols == matrix[i].length`

	- `1 <= rows, cols <= 200`

	- `matrix[i][j]` is `'0'` or `'1'`.

## 🧠 Solution Explanation

### Intuition
The solution works by treating each column of the binary matrix as a histogram and finding the maximum area of the rectangle that can be formed using the histogram. This approach is based on the idea that the maximum rectangle in the binary matrix can be obtained by finding the maximum area of the rectangle in each row and then taking the maximum of these areas. The histogram approach allows us to efficiently calculate the maximum area of the rectangle for each row.

### Approach
1. Calculate the prefix sum for each column of the binary matrix, where the prefix sum at each position represents the height of the histogram.
2. For each row, use a stack-based approach to find the maximum area of the rectangle that can be formed using the histogram.
3. The stack-based approach involves iterating through the histogram and pushing the indices and heights of the bars onto the stack.
4. When a bar with a smaller height is encountered, the stack is popped and the area of the rectangle that can be formed using the popped bar is calculated.
5. The maximum area of the rectangle for each row is calculated and the maximum of these areas is taken as the final result.

### Time Complexity
The time complexity of the solution is O(n*m), where n is the number of rows and m is the number of columns in the binary matrix. This is because we are iterating through each element of the matrix once to calculate the prefix sum, and then iterating through each row to find the maximum area of the rectangle.

### Space Complexity
The space complexity of the solution is O(n*m), where n is the number of rows and m is the number of columns in the binary matrix. This is because we are storing the prefix sum for each column of the matrix, which requires O(n*m) space.

### Key Insight
The key insight behind this solution is the use of the histogram approach to find the maximum area of the rectangle in each row. By treating each column of the binary matrix as a histogram, we can efficiently calculate the maximum area of the rectangle for each row using a stack-based approach. This approach allows us to avoid iterating through all possible rectangles in the matrix, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 23 ms (Beats 99.1%) |
| 💾 Memory | 24.8 MB (Beats 6.81%) |
| 📅 Solved | 2026-01-11 |
| 💻 Language | Python |