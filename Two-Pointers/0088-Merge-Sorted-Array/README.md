> 📌 **Cross-listed:** Primary location is [Array/0088-Merge-Sorted-Array](../../Array/0088-Merge-Sorted-Array). This problem also appears under: **Array**, **Two Pointers**, **Sorting**

# 88. Merge Sorted Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/merge-sorted-array/)


## 📝 Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be *stored inside the array *`nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

 

Example 1:**

```

**Input:** nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
**Output:** [1,2,2,3,5,6]
**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

```

Example 2:**

```

**Input:** nums1 = [1], m = 1, nums2 = [], n = 0
**Output:** [1]
**Explanation:** The arrays we are merging are [1] and [].
The result of the merge is [1].

```

Example 3:**

```

**Input:** nums1 = [0], m = 0, nums2 = [1], n = 1
**Output:** [1]
**Explanation:** The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

```

 

**Constraints:**

	- `nums1.length == m + n`

	- `nums2.length == n`

	- `0 <= m, n <= 200`

	- `1 <= m + n <= 200`

	- `-10^9 <= nums1[i], nums2[j] <= 10^9`

 

**Follow up: **Can you come up with an algorithm that runs in `O(m + n)` time?

## 🧠 Solution Explanation

## Intuition
This approach works by utilizing two pointers to compare elements from both arrays and placing the larger element at the end of the `nums1` array. This process continues until all elements from both arrays are merged and sorted in non-decreasing order. By starting from the end of both arrays, we can avoid shifting elements in `nums1` to make space for elements from `nums2`.

## Approach
1. Initialize pointers `i` and `j` to the last elements of the valid parts of `nums1` and `nums2`, respectively.
2. Initialize a pointer `idx` to the last element of `nums1`.
3. Compare the elements at `nums1[i]` and `nums2[j]`, and place the larger one at `nums1[idx]`.
4. Decrement the corresponding pointer (`i` or `j`) and `idx`.
5. Repeat steps 3-4 until one of the arrays is exhausted.
6. Copy any remaining elements from the non-exhausted array to `nums1`.

## Time Complexity
The time complexity is O(m + n), where m and n are the lengths of the valid parts of `nums1` and `nums2`, respectively. This is because we are scanning both arrays once.

## Space Complexity
The space complexity is O(1), as we are modifying the input array `nums1` in-place and using a constant amount of space to store the pointers.

## Key Insight
The key insight here is to start from the end of both arrays and work backwards, allowing us to avoid shifting elements in `nums1` and making the merge process more efficient. This approach takes advantage of the fact that `nums1` has enough space to hold all elements from both arrays.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 38.45%) |
| 📅 Solved | 2026-05-03 |
| 💻 Language | Python |