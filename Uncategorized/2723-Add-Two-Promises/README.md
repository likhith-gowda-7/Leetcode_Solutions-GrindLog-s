# 2723. Add Two Promises


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/add-two-promises/)


## 📝 Problem Description

Given two promises `promise1` and `promise2`, return a new promise. `promise1` and `promise2` will both resolve with a number. The returned promise should resolve with the sum of the two numbers.
 

Example 1:**

```

**Input:** 
promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20)), 
promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60))
**Output:** 7
**Explanation:** The two input promises resolve with the values of 2 and 5 respectively. The returned promise should resolve with a value of 2 + 5 = 7. The time the returned promise resolves is not judged for this problem.

```

Example 2:**

```

**Input:** 
promise1 = new Promise(resolve => setTimeout(() => resolve(10), 50)), 
promise2 = new Promise(resolve => setTimeout(() => resolve(-12), 30))
**Output:** -2
**Explanation:** The two input promises resolve with the values of 10 and -12 respectively. The returned promise should resolve with a value of 10 + -12 = -2.

```

 

**Constraints:**

	- `promise1` and `promise2` are promises that resolve with a number

## 🧠 Solution Explanation

**Intuition**
The solution utilizes the `async/await` syntax to wait for the resolution of both promises and then returns their sum. This approach leverages the fact that `async/await` can be used to write asynchronous code that looks and feels like synchronous code.

**Approach**
1. The `addTwoPromises` function is defined with the `async` keyword, allowing it to contain `await` expressions.
2. The function takes two promises, `promise1` and `promise2`, as input.
3. The function uses the `await` keyword to wait for the resolution of `promise1`, which returns its resolved value.
4. The function then uses the `await` keyword to wait for the resolution of `promise2`, which returns its resolved value.
5. The function returns the sum of the resolved values of `promise1` and `promise2`.

**Time Complexity**
O(n + m), where n and m are the times it takes for `promise1` and `promise2` to resolve, respectively. This is because the function waits for both promises to resolve before returning their sum.

**Space Complexity**
O(1), as the function only uses a constant amount of space to store the resolved values of the promises.

**Key Insight**
The key insight here is that `async/await` can be used to write asynchronous code that looks synchronous, making it easier to reason about and write asynchronous code. This allows us to write a simple and intuitive function that adds the values of two promises, without having to deal with the complexities of promise chaining.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 58 ms (Beats 30.55%) |
| 💾 Memory | 49.4 MB (Beats 100%) |
| 📅 Solved | 2024-09-29 |
| 💻 Language | JavaScript |