# 1855. Maximum Distance Between a Pair of Values


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/)


## 📝 Problem Description

You are given two **non-increasing 0-indexed **integer arrays `nums1`​​​​​​ and `nums2`​​​​​​.

A pair of indices `(i, j)`, where `0 <= i < nums1.length` and `0 <= j < nums2.length`, is **valid** if both `i <= j` and `nums1[i] <= nums2[j]`. The **distance** of the pair is `j - i`​​​​.

Return *the **maximum distance** of any **valid** pair *`(i, j)`*. If there are no valid pairs, return *`0`.

An array `arr` is **non-increasing** if `arr[i-1] >= arr[i]` for every `1 <= i < arr.length`.

 

Example 1:**

```

**Input:** nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
**Output:** 2
**Explanation:** The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).

```

Example 2:**

```

**Input:** nums1 = [2,2,2], nums2 = [10,10,1]
**Output:** 1
**Explanation:** The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).

```

Example 3:**

```

**Input:** nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
**Output:** 2
**Explanation:** The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).

```

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 10^5`

	- `1 <= nums1[i], nums2[j] <= 10^5`

	- Both `nums1` and `nums2` are **non-increasing**.

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer technique to find the maximum distance between a pair of values in two non-increasing integer arrays. The key insight is to start from the beginning of both arrays and move the pointer of the array with the smaller value at each step, ensuring that the pair is valid.

**Approach**
1. Initialize two pointers `i` and `j` to 0, and two variables `n1` and `n2` to store the lengths of `nums1` and `nums2`, respectively.
2. Initialize a variable `res` to store the maximum distance found so far, and set it to 0.
3. Enter a while loop that continues as long as both `i` and `j` are within their respective array bounds.
4. Inside the loop, check if `i` is greater than `j`. If true, increment `j` and continue to the next iteration.
5. If `nums1[i]` is less than or equal to `nums2[j]`, increment `j` and update `res` with the maximum of its current value and `j - i`.
6. If `nums1[i]` is greater than `nums2[j]`, increment `i`.
7. After the loop, return `res - 1` if `res` is not 0, otherwise return 0.

**Time Complexity**
O(n1 + n2), where n1 and n2 are the lengths of `nums1` and `nums2`, respectively. This is because we are iterating through both arrays once using the two-pointer technique.

**Space Complexity**
O(1), which means the space complexity is constant. We are only using a few extra variables to store the pointers and the maximum distance, without using any additional data structures that scale with the input size.

**Key Insight**
The key insight is to start from the beginning of both arrays and move the pointer of the array with the smaller value at each step, ensuring that the pair is valid. This approach allows us to find the maximum distance between a pair of values in two non-increasing integer arrays efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 49 ms (Beats 60.19%) |
| 💾 Memory | 35.9 MB (Beats 57.21%) |
| 📅 Solved | 2026-04-19 |
| 💻 Language | Python |