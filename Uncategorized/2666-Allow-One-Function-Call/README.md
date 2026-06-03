# 2666. Allow One Function Call


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/allow-one-function-call/)


## 📝 Problem Description

Given a function `fn`, return a new function that is identical to the original function except that it ensures `fn` is called at most once.

	- The first time the returned function is called, it should return the same result as `fn`.

	- Every subsequent time it is called, it should return `undefined`.

 

Example 1:**

```

**Input:** fn = (a,b,c) => (a + b + c), calls = [[1,2,3],[2,3,6]]
**Output:** [{"calls":1,"value":6}]
**Explanation:**
const onceFn = once(fn);
onceFn(1, 2, 3); // 6
onceFn(2, 3, 6); // undefined, fn was not called

```

Example 2:**

```

**Input:** fn = (a,b,c) => (a * b * c), calls = [[5,7,4],[2,3,6],[4,6,8]]
**Output:** [{"calls":1,"value":140}]
**Explanation:**
const onceFn = once(fn);
onceFn(5, 7, 4); // 140
onceFn(2, 3, 6); // undefined, fn was not called
onceFn(4, 6, 8); // undefined, fn was not called

```

 

**Constraints:**

	- `calls` is a valid JSON array

	- `1 <= calls.length <= 10`

	- `1 <= calls[i].length <= 100`

	- `2 <= JSON.stringify(calls).length <= 1000`

## 🧠 Solution Explanation

**Intuition**
The `once` function creates a new function that wraps the original function `fn`. This new function ensures that `fn` is called at most once, returning the result of the first call and `undefined` for all subsequent calls.

**Approach**
1. Initialize a flag `used` to track whether the original function `fn` has been called.
2. Return a new function that takes any number of arguments `...args`.
3. Inside the new function, check if `used` is `false`.
4. If `used` is `false`, set `used` to `true` and call the original function `fn` with the provided arguments `...args`, returning the result.
5. If `used` is `true`, return `undefined`.

**Time Complexity**
O(1) - The time complexity is constant because the new function only performs a constant number of operations, regardless of the number of arguments or the number of calls.

**Space Complexity**
O(1) - The space complexity is constant because the new function only uses a small amount of memory to store the `used` flag, regardless of the input size.

**Key Insight**
The key insight is that the `used` flag serves as a simple and efficient way to track whether the original function `fn` has been called. By setting `used` to `true` after the first call, the new function can easily determine whether to return the result of the original function or `undefined` for subsequent calls.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 54 ms (Beats 7.32%) |
| 💾 Memory | 48.4 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |