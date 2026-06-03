> 📌 **Cross-listed:** Primary location is [Tree/0111-Minimum-Depth-of-Binary-Tree](../../Tree/0111-Minimum-Depth-of-Binary-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Tree**

# 111. Minimum Depth of Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)


## 📝 Problem Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)
```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** 2

```

Example 2:**

```

**Input:** root = [2,null,3,null,4,null,5,null,6]
**Output:** 5

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 10^5]`.

	- `-1000 <= Node.val <= 1000`

## 🧠 Solution Explanation

**Intuition**
This solution uses a breadth-first search (BFS) approach to traverse the binary tree and find the minimum depth. The idea is to start from the root node and explore all nodes at each level before moving on to the next level. This way, we can find the minimum depth by stopping as soon as we reach a leaf node.

**Approach**
1. Check if the root node is `None`. If it is, return 0 because an empty tree has a minimum depth of 0.
2. Create a queue `q` and add the root node to it along with its depth (1).
3. While the queue is not empty, pop the front node and its depth from the queue.
4. If the popped node is a leaf node (i.e., it has no children), return its depth as the minimum depth.
5. If the popped node has a right child, add it to the queue along with its depth incremented by 1.
6. If the popped node has a left child, add it to the queue along with its depth incremented by 1.

**Time Complexity**
The time complexity of this solution is O(N), where N is the number of nodes in the binary tree. This is because we visit each node once.

**Space Complexity**
The space complexity of this solution is O(N), where N is the number of nodes in the binary tree. This is because in the worst case, the queue will store all nodes at the last level of the tree.

**Key Insight**
The key insight here is that we can use a queue to perform a BFS traversal of the binary tree, which allows us to find the minimum depth by stopping as soon as we reach a leaf node. This approach is more efficient than a depth-first search (DFS) approach because it avoids the overhead of recursive function calls and stack management.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 50.5 MB (Beats 11.03%) |
| 📅 Solved | 2025-06-04 |
| 💻 Language | Python |