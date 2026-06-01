> 📌 **Cross-listed:** Primary location is [Array/0105-Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal](../../Array/0105-Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal). This problem also appears under: **Array**, **Hash Table**, **Divide and Conquer**, **Tree**, **Binary Tree**

# 105. Construct Binary Tree from Preorder and Inorder Traversal


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Tree](https://img.shields.io/badge/Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)


## 📝 Problem Description

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
```

**Input:** preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
**Output:** [3,9,20,null,null,15,7]

```

Example 2:**

```

**Input:** preorder = [-1], inorder = [-1]
**Output:** [-1]

```

 

**Constraints:**

	- `1 <= preorder.length <= 3000`

	- `inorder.length == preorder.length`

	- `-3000 <= preorder[i], inorder[i] <= 3000`

	- `preorder` and `inorder` consist of **unique** values.

	- Each value of `inorder` also appears in `preorder`.

	- `preorder` is **guaranteed** to be the preorder traversal of the tree.

	- `inorder` is **guaranteed** to be the inorder traversal of the tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 100%) |
| 📅 Solved | 2025-06-05 |
| 💻 Language | Python |