> 📌 **Cross-listed:** Primary location is [Array/2078-Two-Furthest-Houses-With-Different-Colors](../../Array/2078-Two-Furthest-Houses-With-Different-Colors). This problem also appears under: **Array**, **Greedy**

# 2078. Two Furthest Houses With Different Colors


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/two-furthest-houses-with-different-colors/)


## 📝 Problem Description

There are `n` houses evenly lined up on the street, and each house is beautifully painted. You are given a **0-indexed** integer array `colors` of length `n`, where `colors[i]` represents the color of the `i^th` house.

Return *the **maximum** distance between **two** houses with **different** colors*.

The distance between the `i^th` and `j^th` houses is `abs(i - j)`, where `abs(x)` is the **absolute value** of `x`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/10/31/eg1.png)
```

**Input:** colors = [**1**,1,1,**6**,1,1,1]
**Output:** 3
**Explanation:** In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/10/31/eg2.png)
```

**Input:** colors = [**1**,8,3,8,**3**]
**Output:** 4
**Explanation:** In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.

```

Example 3:**

```

**Input:** colors = [**0**,**1**]
**Output:** 1
**Explanation:** The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.

```

 

**Constraints:**

	- `n == colors.length`

	- `2 <= n <= 100`

	- `0 <= colors[i] <= 100`

	- Test data are generated such that **at least** two houses have different colors.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to find the maximum distance between two houses with different colors. It starts from both ends of the array and moves towards the center, keeping track of the first and last houses with different colors. The maximum distance is then calculated as the maximum of the distance from the first house with a different color to the last house, and the distance from the first house to the last house with a different color.

**Approach**
1. Initialize two pointers, `r` and `l`, to the last and first elements of the array, respectively.
2. While `r` is greater than 0 and the first and last houses have the same color, decrement `r`.
3. While `l` is less than the length of the array and the first and last houses have the same color, increment `l`.
4. Return the maximum of `r` and `n - l - 1`, where `n` is the length of the array.

**Time Complexity**
O(n), where n is the length of the array. This is because in the worst case, we need to traverse the entire array to find the first and last houses with different colors.

**Space Complexity**
O(1), since we only use a constant amount of space to store the pointers and the length of the array.

**Key Insight**
The key insight is that we can use a greedy approach to find the maximum distance by starting from both ends of the array and moving towards the center. This approach takes advantage of the fact that the houses are evenly lined up and the distance between them is calculated as the absolute value of their indices.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 19.51%) |
| 📅 Solved | 2026-04-20 |
| 💻 Language | Python |