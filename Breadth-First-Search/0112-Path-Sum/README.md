> 📌 **Cross-listed:** Primary location is [Tree/0112-Path-Sum](../../Tree/0112-Path-Sum). This problem also appears under: **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Tree**

# 112. Path Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/path-sum/)


## 📝 Problem Description

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)
```

**Input:** root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
**Output:** true
**Explanation:** The root-to-leaf path with the target sum is shown.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)
```

**Input:** root = [1,2,3], targetSum = 5
**Output:** false
**Explanation:** There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

```

Example 3:**

```

**Input:** root = [], targetSum = 0
**Output:** false
**Explanation:** Since the tree is empty, there are no root-to-leaf paths.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 5000]`.

	- `-1000 <= Node.val <= 1000`

	- `-1000 <= targetSum <= 1000`

## 🧠 Solution Explanation

**Intuition**
This problem can be solved by performing a depth-first search (DFS) on the binary tree. We'll traverse the tree, keeping track of the sum of the node values along the current path. If we reach a leaf node (a node with no children) and the sum equals the target sum, we return `True`. If we exhaust all possible paths without finding a match, we return `False`.

**Approach**
1. Define a helper function `dfs` that takes a node and the current sum as arguments.
2. If the node is `None`, return `False` (base case for DFS).
3. Add the node's value to the current sum.
4. If the node is a leaf node (no children), check if the current sum equals the target sum. If it does, return `True`.
5. Recursively call `dfs` on the node's left and right children, passing the updated current sum.
6. If either recursive call returns `True`, return `True`.
7. If all recursive calls return `False`, return `False`.

**Time Complexity**
O(N), where N is the number of nodes in the tree. This is because we visit each node once during the DFS traversal.

**Space Complexity**
O(H), where H is the height of the tree. This is because the maximum depth of the recursive call stack is equal to the height of the tree.

**Key Insight**
The key insight is to use a recursive DFS approach to traverse the tree, keeping track of the sum along each path. By checking for a match at each leaf node, we can efficiently determine whether a root-to-leaf path with the target sum exists.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.8 MB (Beats 100%) |
| 📅 Solved | 2025-12-12 |
| 💻 Language | Python |