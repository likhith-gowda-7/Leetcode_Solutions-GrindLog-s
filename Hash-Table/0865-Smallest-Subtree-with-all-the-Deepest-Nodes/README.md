# 865. Smallest Subtree with all the Deepest Nodes


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)


## 📝 Problem Description

Given the `root` of a binary tree, the depth of each node is **the shortest distance to the root**.

Return *the smallest subtree* such that it contains **all the deepest nodes** in the original tree.

A node is called **the deepest** if it has the largest depth possible among any node in the entire tree.

The **subtree** of a node is a tree consisting of that node, plus the set of all descendants of that node.

 

Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png)
```

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4]
**Output:** [2,7,4]
**Explanation:** We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

```

Example 2:**

```

**Input:** root = [1]
**Output:** [1]
**Explanation:** The root is the deepest node in the tree.

```

Example 3:**

```

**Input:** root = [0,1,3,null,2]
**Output:** [2]
**Explanation:** The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.

```

 

**Constraints:**

	- The number of nodes in the tree will be in the range `[1, 500]`.

	- `0 <= Node.val <= 500`

	- The values of the nodes in the tree are **unique**.

 

**Note:** This question is the same as 1123: [https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-step approach to find the smallest subtree containing all the deepest nodes in the binary tree. First, it calculates the maximum depth of the tree using a breadth-first search (BFS) traversal. Then, it performs a depth-first search (DFS) traversal to find the smallest subtree that contains all nodes at the maximum depth.

**Approach**
1. The `find` function calculates the maximum depth of the tree using a BFS traversal:
	* Initialize a queue with the root node.
	* Perform a BFS traversal, level by level, until the queue is empty.
	* For each level, add the right and left children of each node to the queue.
	* Increment the level counter after processing each level.
2. The `subtreeWithAllDeepest` function performs a DFS traversal to find the smallest subtree containing all nodes at the maximum depth:
	* Define a helper function `dfs` that takes a node and its level as arguments.
	* If the node is `None`, return `None`.
	* If the level is equal to the maximum depth, return the node.
	* Recursively call `dfs` on the left and right children of the node, incrementing the level counter.
	* If both left and right children are not `None`, return the current node (since it contains both).
	* Otherwise, return the non-`None` child.

**Time Complexity**
O(n), where n is the number of nodes in the tree. The BFS traversal in the `find` function visits each node once, and the DFS traversal in the `subtreeWithAllDeepest` function also visits each node once.

**Space Complexity**
O(n), where n is the number of nodes in the tree. The BFS traversal in the `find` function uses a queue to store nodes at each level, and the DFS traversal in the `subtreeWithAllDeepest` function uses recursive function calls to store nodes on the call stack.

**Key Insight**
The key insight is to use a two-step approach to find the smallest subtree containing all the deepest nodes. First, calculate the maximum depth of the tree using a BFS traversal. Then, perform a DFS traversal to find the smallest subtree that contains all nodes at the maximum depth. This approach ensures that we find the smallest subtree that contains all the deepest nodes.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 39.16%) |
| 📅 Solved | 2026-01-10 |
| 💻 Language | Python |