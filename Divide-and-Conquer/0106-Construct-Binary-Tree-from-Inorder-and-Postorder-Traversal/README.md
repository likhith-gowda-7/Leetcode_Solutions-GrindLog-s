> 📌 **Cross-listed:** Primary location is [Array/0106-Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal](../../Array/0106-Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal). This problem also appears under: **Array**, **Hash Table**, **Divide and Conquer**, **Tree**, **Binary Tree**

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

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing the properties of inorder and postorder traversals to construct the binary tree. Inorder traversal visits the left subtree, the root, and then the right subtree, while postorder traversal visits the left subtree, the right subtree, and then the root. By combining these two traversals, we can identify the root of the tree and recursively construct its left and right subtrees.

## Approach
1. Create a hash map to store the indices of the inorder traversal for efficient lookup.
2. Initialize a pointer to the last element of the postorder traversal, which represents the root of the tree.
3. Define a recursive function `dfs` that takes the left and right boundaries of the current subtree.
4. Within `dfs`, create a new `TreeNode` with the value at the current postorder pointer, and then recursively construct its right and left subtrees based on the indices stored in the hash map.
5. Decrement the postorder pointer after processing each node to move to the next node in the postorder traversal.

## Time Complexity
The time complexity is O(n), where n is the number of nodes in the tree, since each node is visited once during the construction process. The hash map lookup and recursive function calls contribute to the overall linear time complexity.

## Space Complexity
The space complexity is O(n), where n is the number of nodes in the tree, due to the recursive call stack and the hash map used to store the indices of the inorder traversal.

## Key Insight
The key insight is to use the postorder traversal to identify the root of the tree and then use the inorder traversal to determine the boundaries of the left and right subtrees, allowing for efficient recursive construction of the binary tree. This approach enables the solution to avoid explicit tree traversal and instead focus on recursive subtree construction.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 100%) |
| 📅 Solved | 2025-06-06 |
| 💻 Language | Python |