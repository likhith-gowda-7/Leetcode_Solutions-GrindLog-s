# 106. Construct Binary Tree from Inorder and Postorder Traversal


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Tree](https://img.shields.io/badge/Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)


## 📝 Problem Description

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return *the binary tree*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
```

**Input:** inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
**Output:** [3,9,20,null,null,15,7]

```

Example 2:**

```

**Input:** inorder = [-1], postorder = [-1]
**Output:** [-1]

```

 

**Constraints:**

	- `1 <= inorder.length <= 3000`

	- `postorder.length == inorder.length`

	- `-3000 <= inorder[i], postorder[i] <= 3000`

	- `inorder` and `postorder` consist of **unique** values.

	- Each value of `postorder` also appears in `inorder`.

	- `inorder` is **guaranteed** to be the inorder traversal of the tree.

	- `postorder` is **guaranteed** to be the postorder traversal of the tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 100%) |
| 📅 Solved | 2025-06-06 |
| 💻 Language | Python |