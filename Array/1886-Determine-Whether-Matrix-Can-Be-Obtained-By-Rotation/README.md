# 1886. Determine Whether Matrix Can Be Obtained By Rotation


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/)


## 📝 Problem Description

Given two `n x n` binary matrices `mat` and `target`, return `true`* if it is possible to make *`mat`* equal to *`target`* by **rotating** *`mat`* in **90-degree increments**, or *`false`* otherwise.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/20/grid3.png)
```

**Input:** mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
**Output:** true
**Explanation: **We can rotate mat 90 degrees clockwise to make mat equal target.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/20/grid4.png)
```

**Input:** mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
**Output:** false
**Explanation:** It is impossible to make mat equal to target by rotating mat.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/05/26/grid4.png)
```

**Input:** mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
**Output:** true
**Explanation: **We can rotate mat 90 degrees clockwise two times to make mat equal target.

```

 

**Constraints:**

	- `n == mat.length == target.length`

	- `n == mat[i].length == target[i].length`

	- `1 <= n <= 10`

	- `mat[i][j]` and `target[i][j]` are either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution works by checking if the given matrix can be transformed into the target matrix by rotating it 90 degrees up to three times. This is possible because a 90-degree rotation is equivalent to transposing the matrix and then reversing each row.

**Approach**
1. First, we check if the given matrix is already equal to the target matrix. If so, we return True.
2. If not, we define a helper function `transpose()` that transposes the matrix by swapping elements across the diagonal and then reversing each row.
3. We then iterate over the possible rotations (0, 1, 2, or 3 90-degree rotations) and apply the `transpose()` function each time.
4. After each rotation, we check if the matrix is now equal to the target matrix. If so, we return True.
5. If we have tried all possible rotations and the matrix is still not equal to the target, we return False.

**Time Complexity**
O(n^2 * 4), where n is the size of the matrix. This is because we have a nested loop structure that iterates over the matrix elements, and we apply this structure up to four times (once for the initial check and three times for the rotations).

**Space Complexity**
O(1), as we only use a constant amount of space to store the matrix elements and do not allocate any additional memory that scales with the input size.

**Key Insight**
The key insight is that a 90-degree rotation is equivalent to transposing the matrix and then reversing each row. This allows us to simplify the problem of checking if a matrix can be transformed into another matrix by rotating it into a series of simple row operations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 67.8%) |
| 📅 Solved | 2026-03-22 |
| 💻 Language | Python |