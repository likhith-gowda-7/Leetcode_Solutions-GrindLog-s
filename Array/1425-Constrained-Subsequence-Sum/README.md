# 1425. Constrained Subsequence Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/constrained-subsequence-sum/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return the maximum sum of a **non-empty** subsequence of that array such that for every two **consecutive** integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied.

A *subsequence* of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:**

```

**Input:** nums = [10,2,-10,5,20], k = 2
**Output:** 37
**Explanation:** The subsequence is [10, 2, 5, 20].

```

Example 2:**

```

**Input:** nums = [-1,-2,-3], k = 1
**Output:** -1
**Explanation:** The subsequence must be non-empty, so we choose the largest number.

```

Example 3:**

```

**Input:** nums = [10,-2,-10,-5,20], k = 2
**Output:** 23
**Explanation:** The subsequence is [10, -2, -5, 20].

```

 

**Constraints:**

	- `1 <= k <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a deque to efficiently maintain a sliding window of indices that satisfy the condition `j - i <= k`. By keeping track of the maximum sum of the subsequence ending at each index, we can find the maximum sum of a subsequence that meets the constraint.

**Approach**
1. Initialize `res` to negative infinity and a deque `maxi` to store indices of maximum sum subsequence.
2. Iterate over the array `nums` with index `r`.
3. Update the sum at index `r` by adding the maximum sum of the subsequence ending at the index of the first element in `maxi` (or 0 if `maxi` is empty).
4. Update `res` with the maximum sum found so far.
5. Remove indices from `maxi` if the sum at the corresponding index is less than the sum at index `r`.
6. Add index `r` to `maxi` if the sum at index `r` is positive.
7. Remove the first element from `maxi` if it is outside the sliding window (i.e., `maxi[0] == r - k`).
8. Repeat steps 2-7 until the end of the array.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we make a single pass over the array, and each operation (deque insertion, deletion, and lookup) takes constant time.

**Space Complexity**
O(n), where n is the length of the array `nums`. This is because in the worst case, we need to store all indices in the deque `maxi`.

**Key Insight**
The key insight is to use a deque to efficiently maintain a sliding window of indices that satisfy the condition `j - i <= k`. By keeping track of the maximum sum of the subsequence ending at each index, we can find the maximum sum of a subsequence that meets the constraint. This approach allows us to solve the problem in linear time and space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 312 ms (Beats 33.97%) |
| 💾 Memory | 28.9 MB (Beats 100%) |
| 📅 Solved | 2025-04-07 |
| 💻 Language | Python |