> 📌 **Cross-listed:** Primary location is [Array/0054-Spiral-Matrix](../../Array/0054-Spiral-Matrix). This problem also appears under: **Array**, **Matrix**, **Simulation**

# 54. Spiral Matrix


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/spiral-matrix/)


## 📝 Problem Description

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)
```

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,3,6,9,8,7,4,5]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)
```

**Input:** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
**Output:** [1,2,3,4,8,12,11,10,9,5,6,7]

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 10`

	- `-100 <= matrix[i][j] <= 100`

## 🧠 Solution Explanation

## Intuition
The spiral order traversal of a matrix can be achieved by simulating the movement in a spiral direction, starting from the top-left corner. This approach works by maintaining a current direction and changing it whenever a boundary or a visited cell is encountered. The key idea is to mark visited cells and adjust the direction accordingly.

## Approach
1. Initialize the current direction to right (0, 1) and the result list.
2. Define a recursive function `dfs` to perform the spiral traversal, which takes the current position (i, j) as arguments.
3. In the `dfs` function, append the current cell's value to the result list, mark the cell as visited by setting its value to "#", and calculate the next position based on the current direction.
4. If the next position is out of bounds or visited, change the direction by incrementing the `curr_dir` index and taking its modulus with 4 to cycle through the directions (right, down, left, up).
5. Recursively call the `dfs` function with the new position if it is within bounds and not visited.

## Time Complexity
The time complexity is O(m * n), where m and n are the number of rows and columns in the matrix, respectively. This is because each cell is visited exactly once during the traversal.

## Space Complexity
The space complexity is O(m * n), which is used to store the result list and the recursive call stack in the worst case. The space used by the input matrix is not included in this calculation.

## Key Insight
The key insight behind this solution is the use of a recursive function to simulate the spiral traversal, which allows for a clean and efficient implementation of the direction changes and boundary checks. The marking of visited cells using "#" ensures that each cell is visited only once, avoiding infinite loops.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 33.69%) |
| 📅 Solved | 2026-05-16 |
| 💻 Language | Python |