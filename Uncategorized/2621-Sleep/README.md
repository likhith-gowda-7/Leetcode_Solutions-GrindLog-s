# 2621. Sleep


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/sleep/)


## 📝 Problem Description

Given a positive integer `millis`, write an asynchronous function that sleeps for `millis` milliseconds. It can resolve any value.

**Note** that *minor* deviation from `millis` in the actual sleep duration is acceptable.

 

Example 1:**

```

**Input:** millis = 100
**Output:** 100
**Explanation:** It should return a promise that resolves after 100ms.
let t = Date.now();
sleep(100).then(() => {
  console.log(Date.now() - t); // 100
});

```

Example 2:**

```

**Input:** millis = 200
**Output:** 200
**Explanation:** It should return a promise that resolves after 200ms.

```

 

**Constraints:**

	- `1 <= millis <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes the `setTimeout` function to create a promise that resolves after a specified delay. This approach leverages the asynchronous nature of JavaScript to achieve the desired sleep functionality.

**Approach**
1. Create a new promise using the `Promise` constructor.
2. Pass a callback function to the `Promise` constructor that will be executed when the promise is resolved.
3. Use `setTimeout` to schedule the callback function to be executed after a specified delay (`millis` milliseconds).
4. Pass the `resolve` function as the callback to `setTimeout`, which will resolve the promise when the delay is over.

**Time Complexity**
O(1) - The solution involves a constant number of operations, regardless of the input `millis`.

**Space Complexity**
O(1) - The solution only uses a constant amount of space to store the promise and the callback function.

**Key Insight**
The key insight is that `setTimeout` can be used to create a promise that resolves after a specified delay, allowing for asynchronous sleep functionality. This is achieved by passing the `resolve` function as the callback to `setTimeout`, which resolves the promise when the delay is over.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 57 ms (Beats 5.02%) |
| 💾 Memory | 49 MB (Beats 100%) |
| 📅 Solved | 2024-09-30 |
| 💻 Language | JavaScript |