> 📌 **Cross-listed:** Primary location is [Array/2089-Find-Target-Indices-After-Sorting-Array](../../Array/2089-Find-Target-Indices-After-Sorting-Array). This problem also appears under: **Array**, **Binary Search**, **Sorting**

# 2089. Find Target Indices After Sorting Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-target-indices-after-sorting-array/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums` and a target element `target`.

A **target index** is an index `i` such that `nums[i] == target`.

Return *a list of the target indices of* `nums` after* sorting *`nums`* in **non-decreasing** order*. If there are no target indices, return *an **empty** list*. The returned list must be sorted in **increasing** order.

 

Example 1:**

```

**Input:** nums = [1,2,5,2,3], target = 2
**Output:** [1,2]
**Explanation:** After sorting, nums is [1,**2**,**2**,3,5].
The indices where nums[i] == 2 are 1 and 2.

```

Example 2:**

```

**Input:** nums = [1,2,5,2,3], target = 3
**Output:** [3]
**Explanation:** After sorting, nums is [1,2,2,**3**,5].
The index where nums[i] == 3 is 3.

```

Example 3:**

```

**Input:** nums = [1,2,5,2,3], target = 5
**Output:** [4]
**Explanation:** After sorting, nums is [1,2,2,3,**5**].
The index where nums[i] == 5 is 4.

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i], target <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by first counting the number of elements less than the target and the number of duplicates of the target. Then, it generates a list of indices by iterating over the range of indices where the target elements are located.

**Approach**
1. Initialize two counters, `less` and `dup`, to keep track of the number of elements less than the target and the number of duplicates of the target, respectively.
2. Iterate through the input array `nums` and increment `less` if an element is less than the target, and increment `dup` if an element is equal to the target.
3. Generate a list `l` of indices by iterating over the range from `less` to `less + dup`.
4. Return the list `l` of target indices.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we iterate through the array twice: once to count the elements less than and equal to the target, and once to generate the list of target indices.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because in the worst case, we need to store all elements of the array in the list of target indices.

**Key Insight**
The key insight is that after sorting the array, the target elements will be located in a contiguous block of indices. By counting the number of elements less than the target, we can determine the starting index of this block, and by counting the number of duplicates, we can determine the length of the block. This allows us to generate the list of target indices efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-27 |
| 💻 Language | Python |