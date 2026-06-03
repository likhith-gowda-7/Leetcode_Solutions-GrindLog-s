> 📌 **Cross-listed:** Primary location is [Array/1814-Count-Nice-Pairs-in-an-Array](../../Array/1814-Count-Nice-Pairs-in-an-Array). This problem also appears under: **Array**, **Hash Table**, **Math**, **Counting**

# 1814. Count Nice Pairs in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-nice-pairs-in-an-array/)


## 📝 Problem Description

You are given an array `nums` that consists of non-negative integers. Let us define `rev(x)` as the reverse of the non-negative integer `x`. For example, `rev(123) = 321`, and `rev(120) = 21`. A pair of indices `(i, j)` is **nice** if it satisfies all of the following conditions:

	- `0 <= i < j < nums.length`

	- `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`

Return *the number of nice pairs of indices*. Since that number can be too large, return it **modulo** `10^9 + 7`.

 

Example 1:**

```

**Input:** nums = [42,11,1,97]
**Output:** 2
**Explanation:** The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

```

Example 2:**

```

**Input:** nums = [13,10,35,24,76]
**Output:** 4

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to store the frequency of the differences between each number and its reverse. The idea is that if `nums[i]` and `nums[j]` form a nice pair, then `nums[i] - rev(nums[i])` and `nums[j] - rev(nums[j])` must be equal. By counting the frequency of these differences, we can efficiently calculate the number of nice pairs.

**Approach**
1. Initialize a hash table `h1` to store the frequency of differences between numbers and their reverses.
2. Iterate over the input array `nums`.
3. For each number `nums[i]`, calculate its difference with its reverse `val = nums[i] - int(str(nums[i])[::-1])`.
4. Increment the count of nice pairs by the frequency of `val` in the hash table `h1`.
5. Increment the frequency of `val` in the hash table `h1`.
6. Return the total count of nice pairs modulo `10^9 + 7`.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we iterate over the array once to calculate the differences and update the hash table.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because in the worst case, we need to store all differences in the hash table.

**Key Insight**
The key insight is that the difference between a number and its reverse is a unique characteristic that can be used to identify nice pairs. By counting the frequency of these differences, we can efficiently calculate the number of nice pairs without having to compare each pair individually.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 139 ms (Beats 52.85%) |
| 💾 Memory | 27.4 MB (Beats 100%) |
| 📅 Solved | 2025-02-09 |
| 💻 Language | Python |