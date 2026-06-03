# 1304. Find N Unique Integers Sum up to Zero


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)


## 📝 Problem Description

Given an integer `n`, return **any** array containing `n` **unique** integers such that they add up to `0`.

 

Example 1:**

```

**Input:** n = 5
**Output:** [-7,-1,1,3,4]
**Explanation:** These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

```

Example 2:**

```

**Input:** n = 3
**Output:** [-1,0,1]

```

Example 3:**

```

**Input:** n = 1
**Output:** [0]

```

 

**Constraints:**

	- `1 <= n <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution works by creating an array of unique integers that sum up to zero. If `n` is odd, it starts with 0 and then pairs up the positive and negative integers from 1 to `n//2`. If `n` is even, it directly pairs up the positive and negative integers from 1 to `n//2`.

**Approach**
1. Check if `n` is odd. If it is, append 0 to the array and decrement `n` by 1.
2. Iterate from 1 to `n//2` (inclusive) and for each `i`:
   - Append `i` to the array.
   - Append `-i` to the array.
3. Return the array.

**Time Complexity**
O(n) - The solution iterates from 1 to `n//2` which takes linear time.

**Space Complexity**
O(n) - The solution creates an array of size `n` to store the unique integers.

**Key Insight**
The key insight is to pair up the positive and negative integers from 1 to `n//2` to sum up to zero. This approach ensures that the array contains `n` unique integers and their sum is zero.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-09-07 |
| 💻 Language | Python |