# 2667. Create Hello World Function


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/create-hello-world-function/)


## 📝 Problem Description

Write a function `createHelloWorld`. It should return a new function that always returns `"Hello World"`.
 

Example 1:**

```

**Input:** args = []
**Output:** "Hello World"
**Explanation:**
const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".

```

Example 2:**

```

**Input:** args = [{},null,42]
**Output:** "Hello World"
**Explanation:**
const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".

```

 

**Constraints:**

	- `0 <= args.length <= 10`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 55 ms (Beats 5.05%) |
| 💾 Memory | 48 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |