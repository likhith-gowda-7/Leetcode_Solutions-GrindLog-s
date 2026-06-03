# 2635. Apply Transform Over Each Element in Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/apply-transform-over-each-element-in-array/)


## 📝 Problem Description

Given an integer array `arr` and a mapping function `fn`, return a new array with a transformation applied to each element.

The returned array should be created such that `returnedArray[i] = fn(arr[i], i)`.

Please solve it without the built-in `Array.map` method.

 

Example 1:**

```

**Input:** arr = [1,2,3], fn = function plusone(n) { return n + 1; }
**Output:** [2,3,4]
**Explanation:**
const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one. 

```

Example 2:**

```

**Input:** arr = [1,2,3], fn = function plusI(n, i) { return n + i; }
**Output:** [1,3,5]
**Explanation:** The function increases each value by the index it resides in.

```

Example 3:**

```

**Input:** arr = [10,20,30], fn = function constant() { return 42; }
**Output:** [42,42,42]
**Explanation:** The function always returns 42.

```

 

**Constraints:**

	- `0 <= arr.length <= 1000`

	- `-10^9 <= arr[i] <= 10^9`

	- `fn` returns an integer.

## 🧠 Solution Explanation

**Intuition**
The solution uses a simple iterative approach to apply a given mapping function to each element in the input array. This is a fundamental concept in programming, where we need to apply a transformation to each element in a collection.

**Approach**
1. Initialize an empty array `transformarr` to store the transformed elements.
2. Iterate over the input array `arr` using a for loop, keeping track of the current index `i`.
3. For each element `arr[i]`, apply the mapping function `fn` by passing the element and its index `i` as arguments.
4. Store the result of the mapping function in the corresponding position in the `transformarr` array.
5. After iterating over all elements, return the `transformarr` array.

**Time Complexity**
O(n), where n is the length of the input array. This is because we are iterating over the array once, performing a constant amount of work for each element.

**Space Complexity**
O(n), where n is the length of the input array. This is because we are creating a new array of the same length as the input array to store the transformed elements.

**Key Insight**
The key insight here is that we can use a simple iterative approach to apply a mapping function to each element in an array, without relying on built-in functions like `Array.map`. This approach is essential in programming, as it allows us to write efficient and readable code that can be applied to a wide range of problems.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 48 ms (Beats 28.04%) |
| 💾 Memory | 49.2 MB (Beats 100%) |
| 📅 Solved | 2024-09-27 |
| 💻 Language | JavaScript |