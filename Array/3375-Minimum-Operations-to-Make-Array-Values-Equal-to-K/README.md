# 3375. Minimum Operations to Make Array Values Equal to K


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `k`.

An integer `h` is called **valid** if all values in the array that are **strictly greater** than `h` are *identical*.

For example, if `nums = [10, 8, 10, 8]`, a **valid** integer is `h = 9` because all `nums[i] > 9` are equal to 10, but 5 is not a **valid** integer.

You are allowed to perform the following operation on `nums`:

	- Select an integer `h` that is *valid* for the **current** values in `nums`.

	- For each index `i` where `nums[i] > h`, set `nums[i]` to `h`.

Return the **minimum** number of operations required to make every element in `nums` **equal** to `k`. If it is impossible to make all elements equal to `k`, return -1.

 

Example 1:**

**Input:** nums = [5,2,5,4,5], k = 2

**Output:** 2

**Explanation:**

The operations can be performed in order using valid integers 4 and then 2.

Example 2:**

**Input:** nums = [2,1,2], k = 2

**Output:** -1

**Explanation:**

It is impossible to make all the values equal to 2.

Example 3:**

**Input:** nums = [9,7,5,3], k = 1

**Output:** 4

**Explanation:**

The operations can be performed using valid integers in the order 7, 5, 3, and 1.

 

**Constraints:**

	- `1 <= nums.length <= 100 `

	- `1 <= nums[i] <= 100`

	- `1 <= k <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by first identifying the unique elements in the array and checking if the minimum of these unique elements is less than the target value `k`. If it is, it's impossible to make all elements equal to `k`, so the function returns -1. Otherwise, it counts the number of unique elements and subtracts 1 if `k` is one of them, since all elements greater than `k` can be set to `k` in a single operation.

**Approach**
1. Create a set `unique` containing the unique elements in the array `nums`.
2. Check if the minimum element in `unique` is less than `k`. If it is, return -1.
3. Count the number of unique elements in `unique` and store it in `l`.
4. If `k` is one of the unique elements, decrement `l` by 1.
5. Return `l`, which represents the minimum number of operations required to make all elements equal to `k`.

**Time Complexity**
O(n) where n is the number of unique elements in the array. This is because creating a set of unique elements takes O(n) time.

**Space Complexity**
O(n) where n is the number of unique elements in the array. This is because a set of unique elements is created, which requires O(n) space.

**Key Insight**
The key insight is that the minimum number of operations required to make all elements equal to `k` is equal to the number of unique elements greater than `k`, minus 1 if `k` is one of these unique elements. This is because all elements greater than `k` can be set to `k` in a single operation, and the remaining elements are already equal to `k`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 63 ms (Beats 88.94%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-04-09 |
| 💻 Language | Python |