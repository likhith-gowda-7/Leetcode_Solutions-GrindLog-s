# 2715. Timeout Cancellation


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/timeout-cancellation/)


## 📝 Problem Description

Given a function `fn`, an array of arguments `args`, and a timeout `t` in milliseconds, return a cancel function `cancelFn`.

After a delay of `cancelTimeMs`, the returned cancel function `cancelFn` will be invoked.

```

setTimeout(cancelFn, cancelTimeMs)

```

Initially, the execution of the function `fn` should be delayed by `t` milliseconds.

If, before the delay of `t` milliseconds, the function `cancelFn` is invoked, it should cancel the delayed execution of `fn`. Otherwise, if `cancelFn` is not invoked within the specified delay `t`, `fn` should be executed with the provided `args` as arguments.

 

Example 1:**

```

**Input:** fn = (x) => x * 5, args = [2], t = 20
**Output:** [{"time": 20, "returned": 10}]
**Explanation:** 
const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x * 5, [2], 20);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (50ms), which happened after the execution of fn(2) at 20ms.

```

Example 2:**

```

**Input:** fn = (x) => x**2, args = [2], t = 100
**Output:** []
**Explanation:** 
const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x**2, [2], 100);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (50ms), which happened before the execution of fn(2) at 100ms, resulting in fn(2) never being called.

```

Example 3:**

```

**Input:** fn = (x1, x2) => x1 * x2, args = [2,4], t = 30
**Output:** [{"time": 30, "returned": 8}]
**Explanation: 
**const cancelTimeMs = 100;
const cancelFn = cancellable((x1, x2) => x1 * x2, [2,4], 30);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (100ms), which happened after the execution of fn(2,4) at 30ms.

```

 

**Constraints:**

	- `fn` is a function

	- `args` is a valid JSON array

	- `1 <= args.length <= 10`

	- `20 <= t <= 1000`

	- `10 <= cancelTimeMs <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses a timeout to delay the execution of the function `fn` and a cancel function to cancel the delay if invoked before the specified time. This approach allows for flexible control over the execution of `fn` based on the timeout and cancel operations.

**Approach**
1. Set a timeout to execute `fn` with the provided `args` after a delay of `t` milliseconds.
2. Create a cancel function `cancelFn` that clears the timeout when invoked.
3. Return the cancel function `cancelFn`.
4. When the cancel function is invoked before the timeout, the execution of `fn` is cancelled.
5. If the cancel function is not invoked within the specified delay `t`, `fn` is executed with the provided `args` as arguments.

**Time Complexity**
O(1) - The solution involves a constant number of operations regardless of the input size.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the timeout and cancel function.

**Key Insight**
The key insight is the use of a timeout to delay the execution of `fn` and a cancel function to cancel the delay if invoked before the specified time. This approach allows for flexible control over the execution of `fn` based on the timeout and cancel operations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 67 ms (Beats 8.68%) |
| 💾 Memory | 49.3 MB (Beats 100%) |
| 📅 Solved | 2024-09-30 |
| 💻 Language | JavaScript |