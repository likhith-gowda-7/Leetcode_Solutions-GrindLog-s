# 2635. Apply Transform Over Each Element in Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/apply-transform-over-each-element-in-array/)


## 📝 Problem Description

Given an integer array `arr` and a mapping function `fn`, return a new array with a transformation applied to each element.

The returned array should be created such that `returnedArray[i] = fn(arr[i], i)`.

Please solve it without the built-in `Array.map` method.

 

Example 1:**

```

**Input:** arr = [1,2,3], fn = function plusone(n) { return n + 1; }
**Output:** [2,3,4]
**Explanation:**
const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one. 

```

Example 2:**

```

**Input:** arr = [1,2,3], fn = function plusI(n, i) { return n + i; }
**Output:** [1,3,5]
**Explanation:** The function increases each value by the index it resides in.

```

Example 3:**

```

**Input:** arr = [10,20,30], fn = function constant() { return 42; }
**Output:** [42,42,42]
**Explanation:** The function always returns 42.

```

 

**Constraints:**

	- `0 <= arr.length <= 1000`

	- `-10^9 <= arr[i] <= 10^9`

	- `fn` returns an integer.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 48 ms (Beats 28.04%) |
| 💾 Memory | 49.2 MB (Beats 100%) |
| 📅 Solved | 2024-09-27 |
| 💻 Language | JavaScript |