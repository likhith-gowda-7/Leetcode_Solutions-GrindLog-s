# 2200. Find All K-Distant Indices in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums` and two integers `key` and `k`. A **k-distant index** is an index `i` of `nums` for which there exists at least one index `j` such that `|i - j| <= k` and `nums[j] == key`.

Return *a list of all k-distant indices sorted in **increasing order***.

 

Example 1:**

```

**Input:** nums = [3,4,9,1,3,9,5], key = 9, k = 1
**Output:** [1,2,3,4,5,6]
**Explanation:** Here, `nums[2] == key` and `nums[5] == key.
- For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j` where `|0 - j| <= k` and `nums[j] == key. Thus, 0 is not a k-distant index.
- For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
- For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
- For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
- For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
- For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
- For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
`Thus, we return [1,2,3,4,5,6] which is sorted in increasing order. 

```

Example 2:**

```

**Input:** nums = [2,2,2,2,2], key = 2, k = 2
**Output:** [0,1,2,3,4]
**Explanation:** For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index. 
Hence, we return [0,1,2,3,4].

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`

	- `key` is an integer from the array `nums`.

	- `1 <= k <= nums.length`

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer approach to find all k-distant indices in the given array. It iterates through the array and keeps track of the nearest index of the target key. When it encounters the target key, it expands the window to the left and right to find all k-distant indices.

**Approach**
1. Initialize two pointers, `i` and `idx`, to 0. `i` is used to iterate through the array, and `idx` is used to expand the window.
2. Iterate through the array using `i`. When `nums[i] == key`, expand the window to the left and right using `idx`.
3. For each `idx` in the window, check if `nums[idx] == key` and if the distance between `i` and `idx` is less than or equal to `k`. If both conditions are true, add `idx` to the result list.
4. If the distance between `i` and `idx` is greater than `k` and `idx` is greater than `i`, break the inner loop.
5. If `near_key_idx` is not `None` and `near_key_idx` is greater than `i`, set `i` to `near_key_idx`. Otherwise, set `i` to the maximum of `idx` and `i + 1`.
6. Repeat steps 2-5 until `i` reaches the end of the array.

**Time Complexity**
O(n), where n is the length of the array. This is because we iterate through the array at most twice: once using `i` and once using `idx`.

**Space Complexity**
O(n), where n is the length of the array. This is because we store all k-distant indices in the result list.

**Key Insight**
The key insight is to use two pointers, `i` and `idx`, to expand the window to the left and right when we encounter the target key. This allows us to find all k-distant indices efficiently without having to iterate through the entire array multiple times.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-06-25 |
| 💻 Language | Python |