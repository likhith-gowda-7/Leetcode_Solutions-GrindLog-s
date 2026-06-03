> 📌 **Cross-listed:** Primary location is [Array/0974-Subarray-Sums-Divisible-by-K](../../Array/0974-Subarray-Sums-Divisible-by-K). This problem also appears under: **Array**, **Hash Table**, **Prefix Sum**

# 974. Subarray Sums Divisible by K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subarray-sums-divisible-by-k/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return *the number of non-empty **subarrays** that have a sum divisible by *`k`.

A **subarray** is a **contiguous** part of an array.

 

Example 1:**

```

**Input:** nums = [4,5,0,-2,-3,1], k = 5
**Output:** 7
**Explanation:** There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

```

Example 2:**

```

**Input:** nums = [5], k = 9
**Output:** 0

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `2 <= k <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to store the prefix sums of the array modulo `k`. The key insight is that the number of subarrays with a sum divisible by `k` is equivalent to the number of times each prefix sum modulo `k` appears in the array. This is because each time we encounter a prefix sum modulo `k`, we can start a new subarray with that sum.

**Approach**
1. Initialize a hash table `prefix_map` with a default value of 0, and set `prefix_map[0] = 1` to account for the empty subarray.
2. Initialize `curr_sum` to 0, which will store the current prefix sum modulo `k`.
3. Iterate through the array `nums`. For each element `num`, update `curr_sum` by adding `num` modulo `k`.
4. For each update to `curr_sum`, increment the count of `curr_sum` in `prefix_map` and add the count to the result `res`.
5. Return the result `res` after iterating through the entire array.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we iterate through the array once, and each operation inside the loop takes constant time.

**Space Complexity**
O(k), where k is the value of the second input `k`. This is because we store at most `k` key-value pairs in the hash table `prefix_map`.

**Key Insight**
The key insight is that the number of subarrays with a sum divisible by `k` is equivalent to the number of times each prefix sum modulo `k` appears in the array. This allows us to use a hash table to efficiently count the occurrences of each prefix sum modulo `k`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 33 ms (Beats 46.79%) |
| 💾 Memory | 21 MB (Beats 100%) |
| 📅 Solved | 2025-11-30 |
| 💻 Language | Python |