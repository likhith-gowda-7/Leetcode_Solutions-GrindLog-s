# 2620. Counter


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/counter/)


## 📝 Problem Description

Given an integer `n`, return a `counter` function. This `counter` function initially returns `n` and then returns 1 more than the previous value every subsequent time it is called (`n`, `n + 1`, `n + 2`, etc).

 

Example 1:**

```

**Input:** 
n = 10 
["call","call","call"]
**Output:** [10,11,12]
**Explanation: 
**counter() = 10 // The first time counter() is called, it returns n.
counter() = 11 // Returns 1 more than the previous time.
counter() = 12 // Returns 1 more than the previous time.

```

Example 2:**

```

**Input:** 
n = -2
["call","call","call","call","call"]
**Output:** [-2,-1,0,1,2]
**Explanation:** counter() initially returns -2. Then increases after each sebsequent call.

```

 

**Constraints:**

	- `-1000^ <= n <= 1000`

	- `0 <= calls.length <= 1000`

	- `calls[i] === "call"`

## 🧠 Solution Explanation

**Intuition**
This solution works by creating a function that maintains a counter variable, which is initialized to the input `n`. Each time the function is called, it returns the current value of the counter and then increments it by 1. This way, the function behaves like a counter that returns `n`, `n + 1`, `n + 2`, etc.

**Approach**
1. Create a function `createCounter` that takes an integer `n` as input.
2. Initialize a counter variable to `n` within the `createCounter` function.
3. Return a new function that takes no arguments.
4. Within the returned function, return the current value of the counter and then increment it by 1 using the `++` operator.

**Time Complexity**
O(1) - The time complexity is constant because the function performs a fixed number of operations (returning the counter value and incrementing it) regardless of the number of calls.

**Space Complexity**
O(1) - The space complexity is constant because the function only uses a fixed amount of memory to store the counter variable, regardless of the number of calls.

**Key Insight**
The key insight here is that the function `createCounter` returns a new function that maintains its own state (the counter variable). This allows the function to remember its previous value and return the next value in the sequence each time it is called. This is an example of a closure, a fundamental concept in functional programming.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 50 ms (Beats 14.42%) |
| 💾 Memory | 48.9 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |