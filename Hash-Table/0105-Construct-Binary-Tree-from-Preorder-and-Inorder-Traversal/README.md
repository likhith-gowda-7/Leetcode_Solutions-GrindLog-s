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

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing the properties of preorder and inorder traversals to construct the binary tree. Preorder traversal visits the root node first, then recursively traverses the left and right subtrees, while inorder traversal visits the left subtree, the root node, and then the right subtree. By combining these two traversals, we can determine the structure of the binary tree.

## Approach
1. Create a hash map to store the indices of the inorder traversal for efficient lookup.
2. Define a recursive depth-first search (DFS) function that takes the left and right boundaries of the current subtree as parameters.
3. Within the DFS function, create a new root node using the current preorder element and find its index in the inorder traversal.
4. Recursively call the DFS function for the left and right subtrees, updating the preorder index accordingly.
5. Return the constructed binary tree.

## Time Complexity
The time complexity is O(n), where n is the number of nodes in the tree. This is because each node is visited once during the construction process, and the hash map lookup operations take constant time.

## Space Complexity
The space complexity is O(n), where n is the number of nodes in the tree. This is due to the recursive call stack and the hash map used to store the indices of the inorder traversal.

## Key Insight
The key insight is to use the hash map to efficiently find the index of the current preorder element in the inorder traversal, allowing us to determine the boundaries of the left and right subtrees and recursively construct the binary tree. This approach enables us to avoid unnecessary iterations and achieve a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 100%) |
| 📅 Solved | 2025-06-05 |
| 💻 Language | Python |