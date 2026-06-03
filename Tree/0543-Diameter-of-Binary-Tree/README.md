# 543. Diameter of Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)


## 📝 Problem Description

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)
```

**Input:** root = [1,2,3,4,5]
**Output:** 3
**Explanation:** 3 is the length of the path [4,2,1,3] or [5,2,1,3].

```

Example 2:**

```

**Input:** root = [1,2]
**Output:** 1

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `-100 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses a recursive approach to traverse the binary tree and calculate the diameter. The key insight is to recognize that the diameter of a tree is the maximum of the following two values: (1) the diameter of the left subtree plus the diameter of the right subtree, and (2) the sum of the depths of the left and right subtrees.

**Approach**
1. Define a recursive function `recur` that takes a node as input and returns its depth.
2. If the node is `None`, return 0 (base case).
3. Recursively calculate the depth of the left and right subtrees.
4. Update the `res` variable with the maximum of the current `res` and the sum of the left and right subtree depths.
5. Return the maximum of the left and right subtree depths plus 1 (the current node's depth).
6. Call the `recur` function on the root node and return the updated `res` value.

**Time Complexity**
O(n), where n is the number of nodes in the tree. This is because each node is visited once during the recursive traversal.

**Space Complexity**
O(h), where h is the height of the tree. This is because the maximum depth of the recursive call stack is equal to the height of the tree.

**Key Insight**
The key to this solution is to recognize that the diameter of a tree is the maximum of the sum of the depths of the left and right subtrees, and the diameter of the left and right subtrees themselves. This allows us to use a simple recursive approach to calculate the diameter in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 45.34%) |
| 💾 Memory | 20.9 MB (Beats 100%) |
| 📅 Solved | 2025-05-20 |
| 💻 Language | Python |