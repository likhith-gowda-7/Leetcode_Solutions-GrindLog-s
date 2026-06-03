# 718. Maximum Length of Repeated Subarray


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)


## 📝 Problem Description

Given two integer arrays `nums1` and `nums2`, return *the maximum length of a subarray that appears in **both** arrays*.

 

Example 1:**

```

**Input:** nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
**Output:** 3
**Explanation:** The repeated subarray with maximum length is [3,2,1].

```

Example 2:**

```

**Input:** nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
**Output:** 5
**Explanation:** The repeated subarray with maximum length is [0,0,0,0,0].

```

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 1000`

	- `0 <= nums1[i], nums2[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming to find the maximum length of a repeated subarray between two given arrays. It iterates over both arrays and keeps track of the maximum length of the repeated subarray ending at the current position.

**Approach**
1. Initialize a dynamic programming (DP) array `dp` of size `n2 + 1` to store the maximum length of repeated subarrays ending at each position in `nums2`.
2. Initialize `maxi` to 0 to store the maximum length of repeated subarrays found so far.
3. Iterate over `nums1` from the second element to the last element (inclusive).
4. For each element in `nums1`, iterate over `nums2` from the last element to the first element (inclusive).
5. If the current elements in both arrays are equal, update the DP value at the current position in `nums2` to be 1 plus the DP value at the previous position.
6. Update `maxi` to be the maximum of its current value and the DP value at the current position in `nums2`.
7. If the current elements are not equal, reset the DP value at the current position in `nums2` to 0.
8. After iterating over all elements in `nums1`, return `maxi` as the maximum length of repeated subarrays.

**Time Complexity**
O(n1 * n2), where n1 and n2 are the lengths of `nums1` and `nums2` respectively. This is because we iterate over both arrays once.

**Space Complexity**
O(n2), where n2 is the length of `nums2`. This is because we use a DP array of size n2 + 1 to store the maximum length of repeated subarrays ending at each position in `nums2`.

**Key Insight**
The key insight is to use dynamic programming to keep track of the maximum length of repeated subarrays ending at each position in `nums2`. By iterating over both arrays and updating the DP values accordingly, we can efficiently find the maximum length of repeated subarrays.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1039 ms (Beats 66.43%) |
| 💾 Memory | 19.4 MB (Beats 86.79%) |
| 📅 Solved | 2026-01-17 |
| 💻 Language | Python |