# 2215. Find the Difference of Two Arrays


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-difference-of-two-arrays/)


## 📝 Problem Description

Given two **0-indexed** integer arrays `nums1` and `nums2`, return *a list* `answer` *of size* `2` *where:*

	- `answer[0]` *is a list of all **distinct** integers in* `nums1` *which are **not** present in* `nums2`*.*

	- `answer[1]` *is a list of all **distinct** integers in* `nums2` *which are **not** present in* `nums1`.

**Note** that the integers in the lists may be returned in **any** order.

 

Example 1:**

```

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]
**Output:** [[1,3],[4,6]]
**Explanation:
**For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
```

Example 2:**

```

**Input:** nums1 = [1,2,3,3], nums2 = [1,1,2,2]
**Output:** [[3],[]]
**Explanation:
**For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

```

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 1000`

	- `-1000 <= nums1[i], nums2[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the distinct integers in two arrays that are not present in the other array. This can be efficiently solved using set operations, as sets automatically eliminate duplicates and provide efficient membership testing.

**Approach**
1. Convert the input arrays `nums1` and `nums2` to sets `n1` and `n2`, respectively, to eliminate duplicates and improve lookup efficiency.
2. Use the `difference` method of sets to find the distinct integers in `n1` that are not present in `n2` and vice versa.
3. Convert the resulting sets back to lists using the `list` function and store them in the `res` list.
4. Return the `res` list containing the two lists of distinct integers.

**Time Complexity**
O(n + m), where n and m are the sizes of `nums1` and `nums2`, respectively. This is because set operations (conversion to sets, difference, and conversion back to lists) take linear time.

**Space Complexity**
O(n + m), as we need to store the sets `n1` and `n2` and the resulting lists in memory.

**Key Insight**
The key insight is that sets provide an efficient way to eliminate duplicates and perform membership testing, making them ideal for this problem. By converting the input arrays to sets and using set operations, we can solve the problem in linear time and space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 84.04%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2024-12-07 |
| 💻 Language | Python |