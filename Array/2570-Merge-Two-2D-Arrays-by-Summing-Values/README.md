# 2570. Merge Two 2D Arrays by Summing Values


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/)


## 📝 Problem Description

You are given two **2D** integer arrays `nums1` and `nums2.`

	- `nums1[i] = [id_i, val_i]` indicate that the number with the id `id_i` has a value equal to `val_i`.

	- `nums2[i] = [id_i, val_i]` indicate that the number with the id `id_i` has a value equal to `val_i`.

Each array contains **unique** ids and is sorted in **ascending** order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

	- Only ids that appear in at least one of the two arrays should be included in the resulting array.

	- Each id should be included **only once** and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be `0`.

Return *the resulting array*. The returned array must be sorted in ascending order by id.

 

Example 1:**

```

**Input:** nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
**Output:** [[1,6],[2,3],[3,2],[4,6]]
**Explanation:** The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.

```

Example 2:**

```

**Input:** nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
**Output:** [[1,3],[2,4],[3,6],[4,3],[5,5]]
**Explanation:** There are no common ids, so we just include each id with its value in the resulting list.

```

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 200`

	- `nums1[i].length == nums2[j].length == 2`

	- `1 <= id_i, val_i <= 1000`

	- Both arrays contain unique ids.

	- Both arrays are in strictly ascending order by id.

## 🧠 Solution Explanation

**Intuition**
This solution works by utilizing two pointers to iterate through both arrays simultaneously, comparing the ids of the current elements. When an id match is found, the values are summed and the id is added to the result array. If no match is found, the smaller id is added to the result array. After the two arrays are fully traversed, any remaining elements are appended to the result array.

**Approach**
1. Initialize two pointers `i` and `j` to the start of `nums1` and `nums2` respectively, and an empty result array `res`.
2. Enter a while loop that continues until either `i` or `j` reaches the end of its array.
3. Inside the loop, compare the ids of the current elements at `nums1[i]` and `nums2[j]`.
   - If the ids match, append the id and the sum of the values to `res`, increment both `i` and `j`.
   - If `nums1[i][0]` is less than `nums2[j][0]`, append `nums1[i]` to `res` and increment `i`.
   - Otherwise, append `nums2[j]` to `res` and increment `j`.
4. After the loop, append any remaining elements from `nums1` and `nums2` to `res`.
5. Return the result array `res`.

**Time Complexity**
O(n + m), where n and m are the lengths of `nums1` and `nums2` respectively. This is because we are iterating through both arrays once.

**Space Complexity**
O(n + m), where n and m are the lengths of `nums1` and `nums2` respectively. This is because we are creating a new array of the same size as the combined input arrays.

**Key Insight**
The key insight here is to use two pointers to take advantage of the sorted order of the input arrays. By comparing the ids of the current elements, we can efficiently merge the two arrays while respecting the conditions of the problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-02 |
| 💻 Language | Python |