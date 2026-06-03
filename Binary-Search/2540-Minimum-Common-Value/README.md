> 📌 **Cross-listed:** Primary location is [Array/2540-Minimum-Common-Value](../../Array/2540-Minimum-Common-Value). This problem also appears under: **Array**, **Hash Table**, **Two Pointers**, **Binary Search**

# 2540. Minimum Common Value


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-common-value/)


## 📝 Problem Description

Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return *the **minimum integer common** to both arrays*. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

Note that an integer is said to be **common** to `nums1` and `nums2` if both arrays have **at least one** occurrence of that integer.

 

Example 1:**

```

**Input:** nums1 = [1,2,3], nums2 = [2,4]
**Output:** 2
**Explanation:** The smallest element common to both arrays is 2, so we return 2.

```

Example 2:**

```

**Input:** nums1 = [1,2,3,6], nums2 = [2,3,4,5]
**Output:** 2
**Explanation:** There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

```

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 10^5`

	- `1 <= nums1[i], nums2[j] <= 10^9`

	- Both `nums1` and `nums2` are sorted in **non-decreasing** order.

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer technique to traverse both arrays simultaneously. By comparing the elements at the current positions of both pointers, we can efficiently find the minimum common value between the two arrays. If the elements are equal, we return the common value. If one element is smaller, we move the corresponding pointer forward.

**Approach**
1. Initialize two pointers, `i` and `j`, to the start of `nums1` and `nums2`, respectively.
2. While both pointers are within their respective arrays, compare the elements at the current positions of both pointers.
3. If the elements are equal, return the common value.
4. If the element in `nums1` is smaller, increment the pointer `i`.
5. If the element in `nums2` is smaller, increment the pointer `j`.
6. If both pointers reach the end of their respective arrays without finding a common value, return -1.

**Time Complexity**
O(n + m), where n and m are the lengths of `nums1` and `nums2`, respectively. This is because we traverse both arrays at most once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointers and the return value.

**Key Insight**
The key insight is that by using two pointers to traverse both arrays simultaneously, we can take advantage of the fact that the arrays are sorted in non-decreasing order. This allows us to efficiently find the minimum common value between the two arrays.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 79.87%) |
| 💾 Memory | 37.7 MB (Beats 75.6%) |
| 📅 Solved | 2026-05-19 |
| 💻 Language | Python |