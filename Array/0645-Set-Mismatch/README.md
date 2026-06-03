# 645. Set Mismatch


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/set-mismatch/)


## 📝 Problem Description

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another** number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return *them in the form of an array*.

 

Example 1:**

```
**Input:** nums = [1,2,2,4]
**Output:** [2,3]

```
Example 2:**

```
**Input:** nums = [1,1]
**Output:** [1,2]

```

 

**Constraints:**

	- `2 <= nums.length <= 10^4`

	- `1 <= nums[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of a set and a simple iteration to find the duplicate and missing numbers in the array. The set is used to keep track of the numbers we've seen so far, allowing us to efficiently detect duplicates and missing numbers.

**Approach**
1. Create an empty set `check` to store the numbers we've seen so far.
2. Iterate through the input array `nums`. For each number `n`, check if it's already in the `check` set.
   - If `n` is in the `check` set, it's the duplicate number, so add it to the result list `res`.
   - If `n` is not in the `check` set, add it to the `check` set.
3. After iterating through the entire array, iterate from 1 to the length of the array (inclusive). For each number `i` in this range, check if it's not in the `check` set.
   - If `i` is not in the `check` set, it's the missing number, so add it to the result list `res` and break out of the loop.

**Time Complexity**
O(n) - The solution iterates through the input array once and then iterates from 1 to the length of the array once. The set operations (insertion and lookup) take constant time on average.

**Space Complexity**
O(n) - In the worst case, the `check` set will store all numbers from 1 to n, so its size is linear in the size of the input array.

**Key Insight**
The key insight is that we can use a set to efficiently detect duplicates and missing numbers in the array. By iterating through the array and checking if each number is in the set, we can find the duplicate number in O(n) time. Then, by iterating from 1 to the length of the array and checking if each number is in the set, we can find the missing number in O(n) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 68.64%) |
| 💾 Memory | 19.5 MB (Beats 99.99%) |
| 📅 Solved | 2025-11-14 |
| 💻 Language | Python |