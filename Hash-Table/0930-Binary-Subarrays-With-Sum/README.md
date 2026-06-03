> 📌 **Cross-listed:** Primary location is [Array/0930-Binary-Subarrays-With-Sum](../../Array/0930-Binary-Subarrays-With-Sum). This problem also appears under: **Array**, **Hash Table**, **Sliding Window**, **Prefix Sum**

# 930. Binary Subarrays With Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/)


## 📝 Problem Description

Given a binary array `nums` and an integer `goal`, return *the number of non-empty **subarrays** with a sum* `goal`.

A **subarray** is a contiguous part of the array.

 

Example 1:**

```

**Input:** nums = [1,0,1,0,1], goal = 2
**Output:** 4
**Explanation:** The 4 subarrays are bolded and underlined below:
[**1,0,1**,0,1]
[**1,0,1,0**,1]
[1,**0,1,0,1**]
[1,0,**1,0,1**]

```

Example 2:**

```

**Input:** nums = [0,0,0,0,0], goal = 0
**Output:** 15

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `nums[i]` is either `0` or `1`.

	- `0 <= goal <= nums.length`

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to store the cumulative sum of the array and its frequency. By maintaining a running sum and checking for the existence of the difference between the current sum and the goal in the hash table, we can efficiently count the number of subarrays with the target sum.

**Approach**
1. Initialize a hash table `ch` with a default value of 1 for the key 0, representing the frequency of the sum 0.
2. Initialize the running sum `prefix_sum` to 0 and the result `res` to 0.
3. Iterate through the array `nums`. For each element:
   1. Update the running sum by adding the current element.
   2. Check if the difference between the current sum and the goal exists in the hash table. If it does, increment the result by the frequency of this difference.
   3. Update the frequency of the current sum in the hash table.
4. Return the result.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we are iterating through the array once and performing constant-time operations for each element.

**Space Complexity**
O(n), where n is the length of the array `nums`. This is because in the worst case, we need to store all possible cumulative sums in the hash table.

**Key Insight**
The key insight is to use the difference between the current sum and the goal as a key in the hash table. This allows us to efficiently count the number of subarrays with the target sum by checking for the existence of this difference in the hash table.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 26 ms (Beats 92.85%) |
| 💾 Memory | 21.5 MB (Beats 55.55%) |
| 📅 Solved | 2025-03-11 |
| 💻 Language | Python |