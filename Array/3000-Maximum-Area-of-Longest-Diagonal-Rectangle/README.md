# 3000. Maximum Area of Longest Diagonal Rectangle


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/)


## 📝 Problem Description

You are given a 2D **0-indexed **integer array `dimensions`.

For all indices `i`, `0 <= i < dimensions.length`, `dimensions[i][0]` represents the length and `dimensions[i][1]` represents the width of the rectangle `i`.

Return *the **area** of the rectangle having the **longest** diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the **maximum** area.*

 

Example 1:**

```

**Input:** dimensions = [[9,3],[8,6]]
**Output:** 48
**Explanation:** 
For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) &asymp; 9.487.
For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.

```

Example 2:**

```

**Input:** dimensions = [[3,4],[4,3]]
**Output:** 12
**Explanation:** Length of diagonal is the same for both which is 5, so maximum area = 12.

```

 

**Constraints:**

	- `1 <= dimensions.length <= 100`

	- `dimensions[i].length == 2`

	- `1 <= dimensions[i][0], dimensions[i][1] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution iterates through each rectangle's dimensions, calculates its diagonal length, and keeps track of the maximum diagonal length and the corresponding rectangle's area. When a rectangle with a longer diagonal is found, its area is updated as the maximum area.

**Approach**
1. Initialize variables to store the maximum diagonal length and the maximum area of the rectangle with the longest diagonal.
2. Iterate through each rectangle's dimensions (length and width).
3. Calculate the diagonal length of the current rectangle using the Pythagorean theorem.
4. If the current rectangle's diagonal length is greater than the maximum diagonal length found so far, update the maximum diagonal length and the maximum area of the rectangle with the longest diagonal.
5. If the current rectangle's diagonal length is equal to the maximum diagonal length found so far, update the maximum area of the rectangle with the longest diagonal if the current rectangle's area is greater.
6. Return the maximum area of the rectangle with the longest diagonal.

**Time Complexity**
O(n), where n is the number of rectangles. This is because we are iterating through each rectangle once.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the maximum diagonal length and the maximum area of the rectangle with the longest diagonal.

**Key Insight**
The key insight is that we only need to keep track of the maximum diagonal length and the corresponding rectangle's area, as the problem asks for the area of the rectangle with the longest diagonal. This simplifies the solution and reduces the space complexity to O(1).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-08-26 |
| 💻 Language | Python |