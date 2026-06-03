> 📌 **Cross-listed:** Primary location is [Array/2226-Maximum-Candies-Allocated-to-K-Children](../../Array/2226-Maximum-Candies-Allocated-to-K-Children). This problem also appears under: **Array**, **Binary Search**

# 2226. Maximum Candies Allocated to K Children


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/)


## 📝 Problem Description

You are given a **0-indexed** integer array `candies`. Each element in the array denotes a pile of candies of size `candies[i]`. You can divide each pile into any number of **sub piles**, but you **cannot** merge two piles together.

You are also given an integer `k`. You should allocate piles of candies to `k` children such that each child gets the **same** number of candies. Each child can be allocated candies from **only one** pile of candies and some piles of candies may go unused.

Return *the **maximum number of candies** each child can get.*

 

Example 1:**

```

**Input:** candies = [5,8,6], k = 3
**Output:** 5
**Explanation:** We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

```

Example 2:**

```

**Input:** candies = [2,5], k = 11
**Output:** 0
**Explanation:** There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.

```

 

**Constraints:**

	- `1 <= candies.length <= 10^5`

	- `1 <= candies[i] <= 10^7`

	- `1 <= k <= 10^12`

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach to find the maximum number of candies each child can get. The idea is to find the largest possible number of candies that can be evenly distributed among the children, given the constraint that each child can only get candies from one pile.

**Approach**
1. Calculate the total number of candies and check if it's less than the number of children. If so, return 0 as it's impossible to distribute candies evenly.
2. Initialize the search range `[l, r]` to `[1, total//k]`, where `total//k` is the maximum possible number of candies each child can get if they are evenly distributed.
3. Perform a binary search within the range `[l, r]` to find the maximum number of candies each child can get.
   * Calculate the middle value `mid` of the current range.
   * Initialize a counter `ch` to keep track of the total number of children that can be satisfied with the current `mid` value.
   * Iterate through each pile of candies and calculate how many children can be satisfied with the current `mid` value.
   * If the total number of satisfied children `ch` is greater than or equal to the number of children `k`, update the lower bound `l` to `mid + 1`.
   * Otherwise, update the upper bound `r` to `mid - 1`.
4. Repeat step 3 until `l` and `r` converge.
5. Return the final value of `r`, which represents the maximum number of candies each child can get.

**Time Complexity**
O(n log m), where n is the number of piles of candies and m is the total number of candies. The binary search takes O(log m) time, and the iteration through each pile of candies takes O(n) time.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the variables `l`, `r`, `mid`, and `ch`.

**Key Insight**
The key insight is to use a binary search approach to find the maximum number of candies each child can get, given the constraint that each child can only get candies from one pile. The solution iterates through each pile of candies and calculates how many children can be satisfied with the current `mid` value, and updates the search range accordingly. This approach allows the solution to efficiently find the maximum number of candies each child can get in O(n log m) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 127 ms (Beats 99.38%) |
| 💾 Memory | 29.7 MB (Beats 98.39%) |
| 📅 Solved | 2025-03-14 |
| 💻 Language | Python |