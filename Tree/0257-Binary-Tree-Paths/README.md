> 📌 **Cross-listed:** Primary location is [String/0257-Binary-Tree-Paths](../../String/0257-Binary-Tree-Paths). This problem also appears under: **String**, **Backtracking**, **Tree**, **Depth-First Search**, **Binary Tree**

# 257. Binary Tree Paths


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-tree-paths/)


## 📝 Problem Description

Given the `root` of a binary tree, return *all root-to-leaf paths in **any order***.

A **leaf** is a node with no children.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg)
```

**Input:** root = [1,2,3,null,5]
**Output:** ["1->2->5","1->3"]

```

Example 2:**

```

**Input:** root = [1]
**Output:** ["1"]

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 100]`.

	- `-100 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
This solution uses a depth-first search (DFS) approach to traverse the binary tree and construct all root-to-leaf paths. The key insight is to use a string `s` to store the current path and update it at each node.

**Approach**
1. Define a helper function `dfs` that takes a node `root` and a string `s` representing the current path.
2. If the node is `None`, return `None` to indicate the end of a path.
3. Append the node's value to the current path `s` and update `s` with `#` as a separator.
4. Recursively call `dfs` on the left and right children of the node, passing the updated path `s`.
5. If both left and right children are `None`, it means we've reached a leaf node. Split the path `s` by `#` and join the remaining values with `->` to form a root-to-leaf path. Add this path to the result list `res`.
6. Return the current node to continue the DFS traversal.

**Time Complexity**
O(N), where N is the number of nodes in the binary tree. This is because we visit each node once during the DFS traversal.

**Space Complexity**
O(H), where H is the height of the binary tree. This is because the maximum depth of the recursion stack is equal to the height of the tree. In the worst case, the tree is skewed and H = N.

**Key Insight**
The key insight is to use a string `s` to store the current path and update it at each node. This allows us to efficiently construct all root-to-leaf paths without storing the entire tree in memory.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-07-20 |
| 💻 Language | Python |