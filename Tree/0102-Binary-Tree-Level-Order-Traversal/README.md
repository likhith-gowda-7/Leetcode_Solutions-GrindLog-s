# 102. Binary Tree Level Order Traversal


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)


## 📝 Problem Description

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [[3],[9,20],[15,7]]

```

Example 2:**

```

**Input:** root = [1]
**Output:** [[1]]

```

Example 3:**

```

**Input:** root = []
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 2000]`.

	- `-1000 <= Node.val <= 1000`

## 🧠 Solution Explanation

**Intuition**
This solution leverages a breadth-first search (BFS) approach to traverse the binary tree level by level, collecting the node values at each level. By using a queue to keep track of nodes to visit, we can efficiently process the tree in a level-order manner.

**Approach**
1. Check if the root is `None`, in which case we return an empty list since there are no nodes to process.
2. Initialize an empty list `nodes` to store the node values and their corresponding levels.
3. Create a queue `q` and enqueue the root node with its level (1).
4. While the queue is not empty, dequeue a node and its level, and append the node value and level to `nodes`.
5. If the node has a left child, enqueue it with its level incremented by 1. Similarly, if the node has a right child, enqueue it with its level incremented by 1.
6. After processing all nodes, determine the maximum level (height) from the last node in `nodes`.
7. Create a list `res` with `height` empty lists, each representing a level in the tree.
8. Iterate through `nodes` and append each node value to the corresponding level in `res`.

**Time Complexity**
O(n), where n is the number of nodes in the tree. This is because we visit each node once and perform a constant amount of work for each node.

**Space Complexity**
O(n), where n is the number of nodes in the tree. This is because in the worst case, we need to store all nodes in the `nodes` list and their corresponding levels.

**Key Insight**
The key insight here is to use a queue to keep track of nodes to visit, allowing us to efficiently process the tree in a level-order manner. By storing the node values and their corresponding levels, we can easily reconstruct the level order traversal of the tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.5 MB (Beats 100%) |
| 📅 Solved | 2025-05-29 |
| 💻 Language | Python |