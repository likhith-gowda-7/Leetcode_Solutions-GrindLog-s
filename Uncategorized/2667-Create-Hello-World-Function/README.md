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

## 🧠 Solution Explanation

### **Intuition**
This problem asks us to create a function that always returns "Hello World" regardless of any arguments passed. It tests understanding of closures and function factories in JavaScript.

### **Approach**
1. Define a function called `createHelloWorld`
2. Inside it, return a new arrow function
3. The inner function ignores all arguments using rest parameters `(...args)`
4. Return the string "Hello World" from the inner function

### **Time Complexity**
**O(1)** — The function simply returns a constant string with no computation.

### **Space Complexity**
**O(1)** — No additional data structures are used.

### **Key Insight**
This is a classic closure pattern where the returned function captures nothing from its outer scope, serving as a simple function factory that produces a constant-returning function.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 55 ms (Beats 6.98%) |
| 💾 Memory | 48 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |