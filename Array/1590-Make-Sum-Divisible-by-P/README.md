# 1590. Make Sum Divisible by P


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/make-sum-divisible-by-p/)


## 📝 Problem Description

Given an array of positive integers `nums`, remove the **smallest** subarray (possibly **empty**) such that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove the whole array.

Return *the length of the smallest subarray that you need to remove, or *`-1`* if it's impossible*.

A **subarray** is defined as a contiguous block of elements in the array.

 

Example 1:**

```

**Input:** nums = [3,1,4,2], p = 6
**Output:** 1
**Explanation:** The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

```

Example 2:**

```

**Input:** nums = [6,3,5,2], p = 9
**Output:** 2
**Explanation:** We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

```

Example 3:**

```

**Input:** nums = [1,2,3], p = 3
**Output:** 0
**Explanation:** Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `1 <= p <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a prefix sum approach with a hash table to efficiently find the smallest subarray that needs to be removed to make the sum of the remaining elements divisible by `p`. The key insight is to maintain a running sum of the array elements modulo `p`, which allows us to quickly identify the smallest subarray that needs to be removed.

**Approach**
1. Calculate the remainder of the sum of all array elements when divided by `p`. If the remainder is 0, return 0 as no subarray needs to be removed.
2. Initialize the result to the length of the array, assuming the whole array needs to be removed.
3. Initialize a hash table `prefix_map` with the initial prefix sum (0) mapped to -1.
4. Iterate through the array, maintaining a running sum `curr_sum` of the array elements modulo `p`.
5. For each prefix sum, calculate the target prefix sum `prefix` that would make the sum of the remaining elements divisible by `p`.
6. Check if the target prefix sum `prefix` is already in the hash table `prefix_map`. If it is, calculate the length of the subarray that needs to be removed and update the result if it's smaller.
7. Update the hash table `prefix_map` with the current prefix sum and its index.
8. Return the result if it's not equal to the length of the array, indicating that a subarray needs to be removed. Otherwise, return -1.

**Time Complexity**
O(n), where n is the length of the array. The iteration through the array and hash table operations take linear time.

**Space Complexity**
O(n), where n is the length of the array. The hash table `prefix_map` stores at most n entries.

**Key Insight**
The key insight is to maintain a running sum of the array elements modulo `p`, which allows us to quickly identify the smallest subarray that needs to be removed. This approach takes advantage of the properties of modular arithmetic to efficiently solve the problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 71 ms (Beats 93.52%) |
| 💾 Memory | 38.1 MB (Beats 100%) |
| 📅 Solved | 2025-11-30 |
| 💻 Language | Python |