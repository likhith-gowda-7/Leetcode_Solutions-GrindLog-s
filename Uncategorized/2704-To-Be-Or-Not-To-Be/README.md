# 2704. To Be Or Not To Be


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/to-be-or-not-to-be/)


## 📝 Problem Description

Write a function `expect` that helps developers test their code. It should take in any value `val` and return an object with the following two functions.

	- `toBe(val)` accepts another value and returns `true` if the two values `===` each other. If they are not equal, it should throw an error `"Not Equal"`.

	- `notToBe(val)` accepts another value and returns `true` if the two values `!==` each other. If they are equal, it should throw an error `"Equal"`.

 

Example 1:**

```

**Input:** func = () => expect(5).toBe(5)
**Output:** {"value": true}
**Explanation:** 5 === 5 so this expression returns true.

```

Example 2:**

```

**Input:** func = () => expect(5).toBe(null)
**Output:** {"error": "Not Equal"}
**Explanation:** 5 !== null so this expression throw the error "Not Equal".

```

Example 3:**

```

**Input:** func = () => expect(5).notToBe(null)
**Output:** {"value": true}
**Explanation:** 5 !== null so this expression returns true.

```

## 🧠 Solution Explanation

**Intuition**
This solution works by creating a function `expect` that returns an object with two methods: `toBe` and `notToBe`. These methods take in a value and compare it to the original value passed to the `expect` function. If the values are equal, `toBe` returns true, while `notToBe` throws an error. Conversely, if the values are not equal, `notToBe` returns true, while `toBe` throws an error.

**Approach**
1. The `expect` function takes in a value `val` and returns an object with two methods: `toBe` and `notToBe`.
2. The `toBe` method checks if the input value `no` is equal to the original value `val`. If they are equal, it returns true; otherwise, it throws a "Not Equal" error.
3. The `notToBe` method checks if the input value `no` is not equal to the original value `val`. If they are not equal, it returns true; otherwise, it throws an "Equal" error.

**Time Complexity**
The time complexity of this solution is O(1), as it involves a constant number of operations regardless of the input size.

**Space Complexity**
The space complexity of this solution is O(1), as it only uses a fixed amount of space to store the object returned by the `expect` function.

**Key Insight**
The key insight here is that the `expect` function returns an object with methods that can be used to perform comparisons. This allows for a more functional programming style, where the focus is on the behavior of the functions rather than the data they operate on.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 56 ms (Beats 6.54%) |
| 💾 Memory | 48.7 MB (Beats 100%) |
| 📅 Solved | 2024-09-28 |
| 💻 Language | JavaScript |