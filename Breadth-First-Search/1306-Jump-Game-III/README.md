> 📌 **Cross-listed:** Primary location is [Array/1306-Jump-Game-III](../../Array/1306-Jump-Game-III). This problem also appears under: **Array**, **Depth-First Search**, **Breadth-First Search**

# 1306. Jump Game III


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game-iii/)


## 📝 Problem Description

Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach **any** index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:**

```

**Input:** arr = [4,2,3,0,3,1,2], start = 5
**Output:** true
**Explanation:** 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

```

Example 2:**

```

**Input:** arr = [4,2,3,0,3,1,2], start = 0
**Output:** true 
**Explanation: 
**One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

```

Example 3:**

```

**Input:** arr = [3,0,2,1,2], start = 2
**Output:** false
**Explanation: **There is no way to reach at index 1 with value 0.

```

 

**Constraints:**

	- `1 <= arr.length <= 5 * 10^4`

	- `0 <= arr[i] < arr.length`

	- `0 <= start < arr.length`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 54.4%) |
| 💾 Memory | 25.1 MB (Beats 96.96%) |
| 📅 Solved | 2026-05-17 |
| 💻 Language | Python |