# 2703. Return Length of Arguments Passed


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/return-length-of-arguments-passed/)


## 📝 Problem Description

Write a function `argumentsLength` that returns the count of arguments passed to it.
 

Example 1:**

```

**Input:** args = [5]
**Output:** 1
**Explanation:**
argumentsLength(5); // 1

One value was passed to the function so it should return 1.

```

Example 2:**

```

**Input:** args = [{}, null, "3"]
**Output:** 3
**Explanation:** 
argumentsLength({}, null, "3"); // 3

Three values were passed to the function so it should return 3.

```

 

**Constraints:**

	- `args` is a valid JSON array

	- `0 <= args.length <= 100`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 49 ms (Beats 21.73%) |
| 💾 Memory | 49.1 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |