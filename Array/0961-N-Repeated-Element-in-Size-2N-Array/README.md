# 961. N-Repeated Element in Size 2N Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)


## 📝 Problem Description

You are given an integer array `nums` with the following properties:

	- `nums.length == 2 * n`.

	- `nums` contains `n + 1` **unique** values, `n` of which occur **exactly once** in the array.

	- Exactly one element of `nums` is repeated `n` times.

Return *the element that is repeated *`n`* times*.

 

Example 1:**

```
**Input:** nums = [1,2,3,3]
**Output:** 3

```
Example 2:**

```
**Input:** nums = [2,1,2,5,3,2]
**Output:** 2

```
Example 3:**

```
**Input:** nums = [5,1,5,2,5,3,5,4]
**Output:** 5

```

 

**Constraints:**

	- `2 <= n <= 5000`

	- `nums.length == 2 * n`

	- `0 <= nums[i] <= 10^4`

	- `nums` contains `n + 1` **unique** elements and one of them is repeated exactly `n` times.

## 🧠 Solution Explanation

**Intuition**
The solution uses a set to keep track of the elements it has seen so far. Since a set in Python has an average time complexity of O(1) for insert and search operations, we can use it to efficiently find the repeated element.

**Approach**
1. Initialize an empty set `ele` to store the elements we have seen.
2. Iterate through the `nums` array. For each element `val`, check if it is already in the set `ele`.
3. If `val` is in `ele`, it means we have seen it before, so return `val` as the repeated element.
4. If `val` is not in `ele`, add it to the set `ele`.
5. Repeat steps 2-4 until we find the repeated element.

**Time Complexity**
O(n), where n is the length of the `nums` array. This is because we are iterating through the array once, and each operation (insert and search) on the set takes constant time.

**Space Complexity**
O(n), where n is the length of the `nums` array. This is because in the worst-case scenario, we might need to store all elements in the set.

**Key Insight**
The key insight here is that since there is only one repeated element, we can use a set to efficiently find it. By checking if an element is already in the set, we can avoid unnecessary iterations and find the repeated element in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2026-01-02 |
| 💻 Language | Python |