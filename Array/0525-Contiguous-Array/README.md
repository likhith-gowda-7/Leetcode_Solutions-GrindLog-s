# 525. Contiguous Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/contiguous-array/)


## 📝 Problem Description

Given a binary array `nums`, return *the maximum length of a contiguous subarray with an equal number of *`0`* and *`1`.

 

Example 1:**

```

**Input:** nums = [0,1]
**Output:** 2
**Explanation:** [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

```

Example 2:**

```

**Input:** nums = [0,1,0]
**Output:** 2
**Explanation:** [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

```

Example 3:**

```

**Input:** nums = [0,1,1,1,1,1,0,0,0]
**Output:** 6
**Explanation:** [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `nums[i]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to store the cumulative sum of the binary array at each index. It then iterates through the array, updating the cumulative sum and checking if the current sum is already present in the hash table. If it is, it updates the maximum length of the contiguous subarray with an equal number of 0 and 1.

**Approach**
1. Initialize a hash table `h1` with the cumulative sum 0 at index -1, and a variable `maxi` to store the maximum length of the contiguous subarray.
2. Initialize a variable `curr` to store the cumulative sum at each index.
3. Iterate through the array, updating `curr` by adding 1 for each 1 and subtracting 1 for each 0.
4. Check if `curr` is already present in `h1`. If it is, update `maxi` with the maximum of the current `maxi` and the difference between the current index and the index stored in `h1` for the current cumulative sum.
5. If `curr` is not present in `h1`, add it to `h1` with the current index.
6. Return `maxi` as the maximum length of the contiguous subarray.

**Time Complexity**
O(n), where n is the length of the input array. This is because we are iterating through the array once and performing constant-time operations for each element.

**Space Complexity**
O(n), where n is the length of the input array. This is because in the worst case, we may need to store all elements of the array in the hash table.

**Key Insight**
The key insight is to use the cumulative sum of the binary array as a key in the hash table. This allows us to efficiently check if a contiguous subarray with an equal number of 0 and 1 has been seen before, and to update the maximum length of such a subarray accordingly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 73 ms (Beats 82.42%) |
| 💾 Memory | 25.2 MB (Beats 50.41%) |
| 📅 Solved | 2026-02-13 |
| 💻 Language | Python |