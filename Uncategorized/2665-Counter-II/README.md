# 2665. Counter II


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/counter-ii/)


## 📝 Problem Description

Write a function `createCounter`. It should accept an initial integer `init`. It should return an object with three functions.

The three functions are:

	- `increment()` increases the current value by 1 and then returns it.

	- `decrement()` reduces the current value by 1 and then returns it.

	- `reset()` sets the current value to `init` and then returns it.

 

Example 1:**

```

**Input:** init = 5, calls = ["increment","reset","decrement"]
**Output:** [6,5,4]
**Explanation:**
const counter = createCounter(5);
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4

```

Example 2:**

```

**Input:** init = 0, calls = ["increment","increment","decrement","reset","reset"]
**Output:** [1,2,1,0,0]
**Explanation:**
const counter = createCounter(0);
counter.increment(); // 1
counter.increment(); // 2
counter.decrement(); // 1
counter.reset(); // 0
counter.reset(); // 0

```

 

**Constraints:**

	- `-1000 <= init <= 1000`

	- `0 <= calls.length <= 1000`

	- `calls[i]` is one of "increment", "decrement" and "reset"

## 🧠 Solution Explanation

**Intuition**
The solution uses a closure to create a counter object with three functions: increment, decrement, and reset. The key insight is to use a mutable variable (`currentCount`) to store the initial value, and then use a non-mutable variable (`init`) to store the current count. This allows the functions to modify the current count without affecting the initial value.

**Approach**
1. Initialize a mutable variable `currentCount` with the input `init`.
2. Return an object with three functions:
   1. `increment()`: increments the current count by 1 and returns it.
   2. `reset()`: sets the current count to the initial value (`currentCount`) and returns it.
   3. `decrement()`: decrements the current count by 1 and returns it.
3. In the `increment()` and `decrement()` functions, use the non-mutable variable `init` to store the current count.

**Time Complexity**
O(1) for each function call, as the operations are constant-time.

**Space Complexity**
O(1) as the space required does not change with the size of the input, only the number of function calls.

**Key Insight**
The key insight is to use a mutable variable to store the initial value and a non-mutable variable to store the current count, allowing the functions to modify the current count without affecting the initial value. This is a common technique in functional programming to achieve mutable behavior while still using immutable data structures.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 59 ms (Beats 11.77%) |
| 💾 Memory | 51.3 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |