# 1732. Find the Highest Altitude


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)


## 📝 Problem Description

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i`​​​​​​ and `i + 1` for all (`0 <= i < n)`. Return *the **highest altitude** of a point.*

 

Example 1:**

```

**Input:** gain = [-5,1,5,0,-7]
**Output:** 1
**Explanation:** The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

```

Example 2:**

```

**Input:** gain = [-4,-3,-2,-1,4,3,2]
**Output:** 0
**Explanation:** The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

```

 

**Constraints:**

	- `n == gain.length`

	- `1 <= n <= 100`

	- `-100 <= gain[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a running total of the net gain in altitude and keeping track of the maximum altitude seen so far. This approach is efficient because it only requires a single pass through the input array.

**Approach**
1. Initialize two variables: `alt` to keep track of the current altitude and `maxi` to keep track of the maximum altitude seen so far.
2. Iterate through each value in the `gain` array.
3. For each value, add it to the current altitude `alt`.
4. Update the maximum altitude `maxi` if the current altitude `alt` is greater than `maxi`.
5. After iterating through all values, return the maximum altitude `maxi`.

**Time Complexity**
O(n), where n is the length of the `gain` array. This is because we only need to make a single pass through the array.

**Space Complexity**
O(1), because we only use a constant amount of space to store the `alt` and `maxi` variables, regardless of the size of the input array.

**Key Insight**
The key insight is that we can calculate the maximum altitude by simply keeping track of the maximum altitude seen so far, without needing to store the entire altitude history. This makes the solution efficient and easy to implement.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 52.19%) |
| 📅 Solved | 2026-06-19 |
| 💻 Language | Python |