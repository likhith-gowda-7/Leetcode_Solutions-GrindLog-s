# 1007. Minimum Domino Rotations For Equal Row


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)


## 📝 Problem Description

In a row of dominoes, `tops[i]` and `bottoms[i]` represent the top and bottom halves of the `i^th` domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the `i^th` domino, so that `tops[i]` and `bottoms[i]` swap values.

Return the minimum number of rotations so that all the values in `tops` are the same, or all the values in `bottoms` are the same.

If it cannot be done, return `-1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/14/domino.png)
```

**Input:** tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
**Output:** 2
**Explanation:** 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

```

Example 2:**

```

**Input:** tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
**Output:** -1
**Explanation:** 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

```

 

**Constraints:**

	- `2 <= tops.length <= 2 * 10^4`

	- `bottoms.length == tops.length`

	- `1 <= tops[i], bottoms[i] <= 6`

## 🧠 Solution Explanation

**Intuition**
The solution works by checking if it's possible to make all dominoes have the same value on either the top or bottom half. It iterates through the dominoes, counting the minimum number of rotations required to make all dominoes have the same value on either the top or bottom half.

**Approach**
1. Define a helper function `check(val)` that calculates the minimum number of rotations required to make all dominoes have the same value `val` on either the top or bottom half.
2. Initialize `top_mini` and `botm_mini` to 0, which will store the minimum number of rotations required to make all dominoes have the same value `val` on the top and bottom halves, respectively.
3. Iterate through the dominoes. For each domino, if both the top and bottom halves are not equal to `val`, return -1, indicating that it's impossible to make all dominoes have the same value.
4. If the top half is not equal to `val`, increment `top_mini` by 1, indicating that the bottom half must be equal to `val`.
5. If the bottom half is not equal to `val`, increment `botm_mini` by 1, indicating that the top half must be equal to `val`.
6. After iterating through all dominoes, return the minimum of `top_mini` and `botm_mini`, which is the minimum number of rotations required to make all dominoes have the same value on either the top or bottom half.
7. Call `check(tops[0])` and `check(bottoms[0])` to find the minimum number of rotations required to make all dominoes have the same value on either the top or bottom half.

**Time Complexity**
O(n), where n is the number of dominoes. This is because the solution iterates through the dominoes once.

**Space Complexity**
O(1), which means the space complexity is constant. This is because the solution only uses a few variables to store the minimum number of rotations required, regardless of the input size.

**Key Insight**
The key insight is that if the top half of a domino is not equal to the target value, then the bottom half must be equal to the target value, and vice versa. This allows us to count the minimum number of rotations required to make all dominoes have the same value on either the top or bottom half.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 20 ms (Beats 94.62%) |
| 💾 Memory | 18.6 MB (Beats 100%) |
| 📅 Solved | 2025-05-04 |
| 💻 Language | Python |