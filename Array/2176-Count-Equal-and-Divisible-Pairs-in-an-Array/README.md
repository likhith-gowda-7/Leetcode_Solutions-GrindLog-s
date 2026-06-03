# 2176. Count Equal and Divisible Pairs in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/)


## 📝 Problem Description

Given a **0-indexed** integer array `nums` of length `n` and an integer `k`, return *the **number of pairs*** `(i, j)` *where* `0 <= i < j < n`, *such that* `nums[i] == nums[j]` *and* `(i * j)` *is divisible by* `k`.
 

Example 1:**

```

**Input:** nums = [3,1,2,2,2,1,3], k = 2
**Output:** 4
**Explanation:**
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

```

Example 2:**

```

**Input:** nums = [1,2,3,4], k = 1
**Output:** 0
**Explanation:** Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i], k <= 100`

## 🧠 Solution Explanation

**Intuition**
The approach works by utilizing a hash map to store the indices of each number in the array. For each number, it checks all previously encountered numbers to see if their product is divisible by the given number `k`. The key insight is that we only need to consider pairs where `i < j`, so we can use the stored indices to efficiently calculate the number of valid pairs.

**Approach**

1. Check if all elements in the array are unique. If so, return 0 because there are no pairs to consider.
2. Initialize a hash map `h1` to store the indices of each number in the array.
3. Iterate through the array, and for each number:
   - Check if it's already in the hash map `h1`. If so, iterate through the stored indices of this number.
   - For each stored index `i`, check if the product of `i` and the current index is divisible by `k`. If so, increment the count of valid pairs.
   - Add the current index to the list of indices for the current number in the hash map `h1`.
4. Return the total count of valid pairs.

**Time Complexity**
O(n^2) where n is the length of the array. This is because in the worst case, we might need to check all pairs of numbers in the array.

**Space Complexity**
O(n) where n is the length of the array. This is because we're using a hash map to store the indices of each number in the array.

**Key Insight**
The key insight is that we can use the stored indices in the hash map to efficiently calculate the number of valid pairs, avoiding the need to check all pairs of numbers in the array. This makes the solution more efficient than a brute-force approach.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 94.93%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-09 |
| 💻 Language | Python |