# 2629. Function Composition


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/function-composition/)


## 📝 Problem Description

Given an array of functions `[f1, f_2, f_3, ..., f_n]`, return a new function `fn` that is the **function composition** of the array of functions.

The **function composition** of `[f(x), g(x), h(x)]` is `fn(x) = f(g(h(x)))`.

The **function composition** of an empty list of functions is the **identity function** `f(x) = x`.

You may assume each function in the array accepts one integer as input and returns one integer as output.

 

Example 1:**

```

**Input:** functions = [x => x + 1, x => x * x, x => 2 * x], x = 4
**Output:** 65
**Explanation:**
Evaluating from right to left ...
Starting with x = 4.
2 * (4) = 8
(8) * (8) = 64
(64) + 1 = 65

```

Example 2:**

```

**Input:** functions = [x => 10 * x, x => 10 * x, x => 10 * x], x = 1
**Output:** 1000
**Explanation:**
Evaluating from right to left ...
10 * (1) = 10
10 * (10) = 100
10 * (100) = 1000

```

Example 3:**

```

**Input:** functions = [], x = 42
**Output:** 42
**Explanation:**
The composition of zero functions is the identity function
```

 

**Constraints:**

	- `-1000 <= x <= 1000`

	- `0 <= functions.length <= 1000`

	- all functions accept and return a single integer

## 🧠 Solution Explanation

**Intuition**
The solution works by reversing the order of the functions and then applying each function to the input from right to left. This is because function composition is evaluated from right to left, meaning that the output of the last function is the input to the second-to-last function, and so on.

**Approach**
1. The `compose` function takes an array of functions as input and returns a new function `fn`.
2. The returned function `fn` takes an integer `x` as input and applies each function in the input array to `x` from right to left.
3. To achieve this, the input array of functions is reversed using the `reverse()` method.
4. The `forEach` method is used to iterate over the reversed array of functions.
5. In each iteration, the current function `fn` is applied to the current value of `x`, and the result is assigned back to `x`.
6. After all functions have been applied, the final value of `x` is returned as the result.

**Time Complexity**
O(n), where n is the number of functions in the input array. This is because each function is applied once to the input.

**Space Complexity**
O(1), excluding the space required for the input array and the output. This is because the solution only uses a constant amount of space to store the current value of `x` and the current function being applied.

**Key Insight**
The key insight is that function composition is evaluated from right to left, meaning that the output of the last function is the input to the second-to-last function, and so on. By reversing the order of the functions and applying each one to the input from right to left, we can efficiently compute the function composition of the input array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 69 ms (Beats 6.01%) |
| 💾 Memory | 50 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |