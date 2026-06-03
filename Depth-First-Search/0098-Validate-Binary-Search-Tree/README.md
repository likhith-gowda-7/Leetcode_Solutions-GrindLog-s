> 📌 **Cross-listed:** Primary location is [Tree/0098-Validate-Binary-Search-Tree](../../Tree/0098-Validate-Binary-Search-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Binary Search Tree**, **Binary Tree**

# 98. Validate Binary Search Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)


## 📝 Problem Description

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

	- The left subtree of a node contains only nodes with keys **strictly less than** the node's key.

	- The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.

	- Both the left and right subtrees must also be binary search trees.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)
```

**Input:** root = [2,1,3]
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)
```

**Input:** root = [5,1,4,null,null,3,6]
**Output:** false
**Explanation:** The root node's value is 5 but its right child's value is 4.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `-2^31 <= Node.val <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
The solution uses an in-order traversal of the binary tree to check if it's a valid binary search tree (BST). This approach works because an in-order traversal visits nodes in ascending order, which is a key property of a BST. By checking if each node's value is greater than the previous node's value, we can determine if the tree is a valid BST.

**Approach**
1. Initialize a `prev` variable to store the previous node's value and a `bst` flag to track if the tree is a BST.
2. Define an in-order traversal function `inorder` that takes a node as input and recursively visits its left subtree, then the current node, and finally the right subtree.
3. In the `inorder` function, if the current node is `None` or the tree is not a BST (`bst` is `False`), return immediately.
4. Recursively call `inorder` on the left subtree.
5. If the previous node's value is not `None` and it's greater than or equal to the current node's value, set `bst` to `False` and return.
6. Update the `prev` variable with the current node's value.
7. Recursively call `inorder` on the right subtree.
8. Call the `inorder` function on the root node.
9. Return the `bst` flag.

**Time Complexity**
O(N), where N is the number of nodes in the tree. This is because we visit each node once during the in-order traversal.

**Space Complexity**
O(H), where H is the height of the tree. This is because the maximum depth of the recursion call stack is the height of the tree.

**Key Insight**
The key insight is that an in-order traversal visits nodes in ascending order, which allows us to check if each node's value is greater than the previous node's value, ensuring that the tree is a valid BST. This approach takes advantage of the property that a valid BST has nodes with keys strictly less than the node's key in the left subtree and strictly greater than the node's key in the right subtree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.7 MB (Beats 100%) |
| 📅 Solved | 2025-12-22 |
| 💻 Language | Python |