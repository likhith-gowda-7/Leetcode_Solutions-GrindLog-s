# 4. Median of Two Sorted Arrays


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)


## 📝 Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

Example 1:**

```

**Input:** nums1 = [1,3], nums2 = [2]
**Output:** 2.00000
**Explanation:** merged array = [1,2,3] and median is 2.

```

Example 2:**

```

**Input:** nums1 = [1,2], nums2 = [3,4]
**Output:** 2.50000
**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

```

 

**Constraints:**

	- `nums1.length == m`

	- `nums2.length == n`

	- `0 <= m <= 1000`

	- `0 <= n <= 1000`

	- `1 <= m + n <= 2000`

	- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## 🧠 Solution Explanation

## Intuition
The solution works by using a binary search approach to find the median of two sorted arrays. It ensures that the elements on the left side of the partition in both arrays are less than or equal to the elements on the right side. This is achieved by maintaining a balance between the two arrays, where the total number of elements on the left side of the partition is equal to half the total number of elements in both arrays.

## Approach
1. Initialize two pointers, `l` and `r`, to the start and end of the longer array `A`.
2. Calculate the partition point `i` in array `A` and the corresponding partition point `j` in array `B` such that `i + j = half`, where `half` is half the total number of elements in both arrays.
3. Compare the elements at the partition points in both arrays to determine if the partition is correct.
4. If the partition is correct, calculate the median based on whether the total number of elements is odd or even.
5. If the partition is not correct, adjust the pointers `l` and `r` to continue the binary search.

## Time Complexity
The time complexity is O(log(min(m, n))), where `m` and `n` are the lengths of the two arrays. This is because the solution uses a binary search approach to find the median, and the number of iterations is proportional to the logarithm of the length of the shorter array.

## Space Complexity
The space complexity is O(1), as the solution only uses a constant amount of space to store the pointers and variables.

## Key Insight
The key insight is to use a binary search approach to find the median, rather than merging the two arrays and then finding the median. This approach takes advantage of the fact that the arrays are sorted, allowing for a more efficient solution with a time complexity of O(log(min(m, n))).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1 ms (Beats 58.59%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-03-03 |
| 💻 Language | Python |