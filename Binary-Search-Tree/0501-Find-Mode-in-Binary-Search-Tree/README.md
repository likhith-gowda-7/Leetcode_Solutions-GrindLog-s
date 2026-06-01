> 📌 **Cross-listed:** Primary location is [Tree/0501-Find-Mode-in-Binary-Search-Tree](../../Tree/0501-Find-Mode-in-Binary-Search-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Binary Search Tree**, **Binary Tree**

# 501. Find Mode in Binary Search Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/)


## 📝 Problem Description

Given the `root` of a binary search tree (BST) with duplicates, return *all the [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) (i.e., the most frequently occurred element) in it*.

If the tree has more than one mode, return them in **any order**.

Assume a BST is defined as follows:

	- The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.

	- The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.

	- Both the left and right subtrees must also be binary search trees.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg)
```

**Input:** root = [1,null,2,2]
**Output:** [2]

```

Example 2:**

```

**Input:** root = [0]
**Output:** [0]

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `-10^5 <= Node.val <= 10^5`

 

**Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 21.1 MB (Beats 99.87%) |
| 📅 Solved | 2025-05-29 |
| 💻 Language | Python |