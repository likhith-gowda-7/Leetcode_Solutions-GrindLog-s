# 2703. Return Length of Arguments Passed


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/return-length-of-arguments-passed/)


## 📝 Problem Description

Write a function `argumentsLength` that returns the count of arguments passed to it.
 

Example 1:**

```

**Input:** args = [5]
**Output:** 1
**Explanation:**
argumentsLength(5); // 1

One value was passed to the function so it should return 1.

```

Example 2:**

```

**Input:** args = [{}, null, "3"]
**Output:** 3
**Explanation:** 
argumentsLength({}, null, "3"); // 3

Three values were passed to the function so it should return 3.

```

 

**Constraints:**

	- `args` is a valid JSON array

	- `0 <= args.length <= 100`

## 🧠 Solution Explanation

**Intuition**
The `argumentsLength` function uses a JavaScript feature called rest parameters to capture all arguments passed to it and then returns the length of the resulting array. This approach is intuitive because it leverages the built-in array length property to count the number of arguments.

**Approach**
1. The function uses the rest parameter syntax `...args` to capture all arguments passed to it.
2. The `args` variable is an array containing all the arguments.
3. The function returns the `length` property of the `args` array, which gives the count of elements in the array.

**Time Complexity**
O(1) - The function simply returns the length of the `args` array, which is a constant-time operation.

**Space Complexity**
O(n) - The function creates an array to store all the arguments, where n is the number of arguments. However, since n is bounded by the constraint `0 <= args.length <= 100`, the space complexity is effectively O(1) in practice.

**Key Insight**
The key insight is that JavaScript's rest parameter syntax allows us to capture all arguments in an array, making it easy to count them using the `length` property. This approach is concise and efficient, making it a good solution for this problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 49 ms (Beats 21.73%) |
| 💾 Memory | 49.1 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |