# 108. Convert Sorted Array to Binary Search Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)


## 📝 Problem Description

Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a ****height-balanced*** *binary search tree*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)
```

**Input:** nums = [-10,-3,0,5,9]
**Output:** [0,-3,9,-10,null,5]
**Explanation:** [0,-10,5,null,-3,null,9] is also accepted:
![](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)
```

**Input:** nums = [1,3]
**Output:** [3,1]
**Explanation:** [1,null,3] and [3,1] are both height-balanced BSTs.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `nums` is sorted in a **strictly increasing** order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 20.3 MB (Beats 29.49%) |
| 📅 Solved | 2026-02-09 |
| 💻 Language | Python |