# 572. Subtree of Another Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![String Matching](https://img.shields.io/badge/String%20Matching-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)


## 📝 Problem Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of` subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)
```

**Input:** root = [3,4,5,1,2], subRoot = [4,1,2]
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
```

**Input:** root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
**Output:** false

```

 

**Constraints:**

	- The number of nodes in the `root` tree is in the range `[1, 2000]`.

	- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.

	- `-10^4 <= root.val <= 10^4`

	- `-10^4 <= subRoot.val <= 10^4`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 38 ms (Beats 72.49%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-05-27 |
| 💻 Language | Python |