> 📌 **Cross-listed:** Primary location is [Dynamic Programming/0124-Binary-Tree-Maximum-Path-Sum](../../Dynamic-Programming/0124-Binary-Tree-Maximum-Path-Sum). This problem also appears under: **Dynamic Programming**, **Tree**, **Depth-First Search**, **Binary Tree**

# 124. Binary Tree Maximum Path Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)


## 📝 Problem Description

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum** of any **non-empty** path*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)
```

**Input:** root = [1,2,3]
**Output:** 6
**Explanation:** The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)
```

**Input:** root = [-10,9,20,null,null,15,7]
**Output:** 42
**Explanation:** The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.

	- `-1000 <= Node.val <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a depth-first search (DFS) approach to traverse the binary tree and keep track of the maximum path sum. The key insight is to maintain a running maximum path sum that can be updated at each node, considering the maximum path sum of the left and right subtrees, as well as the current node's value.

**Approach**
1. Initialize the maximum path sum (`self.maxi`) to negative infinity.
2. Define a recursive DFS function that takes a node as input.
3. If the node is `None`, return 0 (base case).
4. Recursively call DFS on the left and right children of the node.
5. Calculate the current node's maximum path sum by considering three options:
	* The current node's value.
	* The current node's value plus the maximum path sum of the left subtree.
	* The current node's value plus the maximum path sum of the right subtree.
6. Update `self.maxi` with the maximum of the current maximum path sum and the calculated current node's maximum path sum.
7. Return the maximum of the current node's value and the current node's value plus the maximum of the left and right subtrees.
8. Call the DFS function on the root node and return `self.maxi`.

**Time Complexity**
O(n), where n is the number of nodes in the binary tree. This is because each node is visited once during the DFS traversal.

**Space Complexity**
O(h), where h is the height of the binary tree. This is because the maximum recursion depth is equal to the height of the tree. In the worst case, the tree is skewed, and the space complexity is O(n). However, for a balanced tree, the space complexity is O(log n).

**Key Insight**
The key to this solution is to maintain a running maximum path sum that can be updated at each node, considering the maximum path sum of the left and right subtrees, as well as the current node's value. This allows us to efficiently find the maximum path sum of any non-empty path in the binary tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 38.49%) |
| 💾 Memory | 23 MB (Beats 99.97%) |
| 📅 Solved | 2025-06-08 |
| 💻 Language | Python |