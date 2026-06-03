# 2626. Array Reduce Transformation


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/array-reduce-transformation/)


## 📝 Problem Description

Given an integer array `nums`, a reducer function `fn`, and an initial value `init`, return the final result obtained by executing the `fn` function on each element of the array, sequentially, passing in the return value from the calculation on the preceding element.

This result is achieved through the following operations: `val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ...` until every element in the array has been processed. The ultimate value of `val` is then returned.

If the length of the array is 0, the function should return `init`.

Please solve it without using the built-in `Array.reduce` method.

 

Example 1:**

```

**Input:** 
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0
**Output:** 10
**Explanation:**
initially, the value is init=0.
(0) + nums[0] = 1
(1) + nums[1] = 3
(3) + nums[2] = 6
(6) + nums[3] = 10
The final answer is 10.

```

Example 2:**

```

**Input:** 
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr * curr; }
init = 100
**Output:** 130
**Explanation:**
initially, the value is init=100.
(100) + nums[0] * nums[0] = 101
(101) + nums[1] * nums[1] = 105
(105) + nums[2] * nums[2] = 114
(114) + nums[3] * nums[3] = 130
The final answer is 130.

```

Example 3:**

```

**Input:** 
nums = []
fn = function sum(accum, curr) { return 0; }
init = 25
**Output:** 25
**Explanation:** For empty arrays, the answer is always init.

```

 

**Constraints:**

	- `0 <= nums.length <= 1000`

	- `0 <= nums[i] <= 1000`

	- `0 <= init <= 1000`

## 🧠 Solution Explanation

**Intuition**
This solution works by iteratively applying the reducer function `fn` to the initial value `init` and each element of the input array `nums`, accumulating the result in a variable `sum`. This process continues until all elements in the array have been processed, at which point the final value of `sum` is returned.

**Approach**
1. Initialize a variable `sum` to the initial value `init`.
2. Iterate over each element in the input array `nums` using a `for` loop.
3. For each element, apply the reducer function `fn` to the current value of `sum` and the current element, and assign the result back to `sum`.
4. After iterating over all elements, return the final value of `sum`.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we are iterating over each element in the array once.

**Space Complexity**
O(1), excluding the input array and function. We are only using a constant amount of space to store the `sum` variable, regardless of the size of the input array.

**Key Insight**
The key insight here is that we can achieve the same result as the `Array.reduce` method by simply iterating over the input array and applying the reducer function to each element, accumulating the result in a variable. This approach is straightforward and efficient, making it a good solution for this problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 65 ms (Beats 5.39%) |
| 💾 Memory | 49.4 MB (Beats 99.99%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |