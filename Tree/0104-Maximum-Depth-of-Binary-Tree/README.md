# 104. Maximum Depth of Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)


## 📝 Problem Description

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)
```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** 3

```

Example 2:**

```

**Input:** root = [1,null,2]
**Output:** 2

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 10^4]`.

	- `-100 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
This solution uses a breadth-first search (BFS) approach to traverse the binary tree level by level, keeping track of the maximum depth encountered. The key insight is that the maximum depth of a binary tree is equal to the number of levels, which can be determined by the number of nodes at each level.

**Approach**
1. Check if the root node is None, if so return 0 as there are no nodes in the tree.
2. Initialize a queue with the root node and a level counter to 0.
3. While the queue is not empty, perform the following steps:
   1. Dequeue all nodes at the current level.
   2. Enqueue the left and right children of each dequeued node, if they exist.
   3. Increment the level counter.
4. Return the level counter, which represents the maximum depth of the binary tree.

**Time Complexity**
O(n), where n is the number of nodes in the binary tree. This is because each node is visited once during the BFS traversal.

**Space Complexity**
O(n), where n is the number of nodes in the binary tree. This is because in the worst case, the queue will store all nodes at the last level of the tree.

**Key Insight**
The key insight is that the maximum depth of a binary tree is equal to the number of levels, which can be determined by the number of nodes at each level. This solution uses a BFS approach to traverse the tree level by level, making it efficient for calculating the maximum depth.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 20.3 MB (Beats 24.44%) |
| 📅 Solved | 2026-01-09 |
| 💻 Language | Python |