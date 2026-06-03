> 📌 **Cross-listed:** Primary location is [Tree/0572-Subtree-of-Another-Tree](../../Tree/0572-Subtree-of-Another-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **String Matching**, **Binary Tree**, **Hash Function**

# 572. Subtree of Another Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![String Matching](https://img.shields.io/badge/String%20Matching-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)


## 📝 Problem Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of` subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)
```

**Input:** root = [3,4,5,1,2], subRoot = [4,1,2]
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
```

**Input:** root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
**Output:** false

```

 

**Constraints:**

	- The number of nodes in the `root` tree is in the range `[1, 2000]`.

	- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.

	- `-10^4 <= root.val <= 10^4`

	- `-10^4 <= subRoot.val <= 10^4`

## 🧠 Solution Explanation

**Intuition**
This solution works by performing a depth-first search (DFS) on the main tree, and for each node, checking if it matches the structure and values of the sub-root tree. If a match is found, it returns True; otherwise, it continues searching the rest of the tree.

**Approach**
1. Define a helper function `sub_dfs` to check if two trees are identical.
2. Initialize a flag `self.is_exists` to False.
3. Define another helper function `dfs` to perform the DFS on the main tree.
4. In `dfs`, check if the current node matches the sub-root tree. If it does, set `self.is_exists` to True and return.
5. Recursively call `dfs` on the left and right children of the current node.
6. If `self.is_exists` is still False after visiting all nodes, return False.

**Time Complexity**
O(n * m), where n is the number of nodes in the main tree and m is the number of nodes in the sub-root tree. This is because for each node in the main tree, we potentially perform a DFS on the sub-root tree.

**Space Complexity**
O(h + m), where h is the height of the main tree and m is the number of nodes in the sub-root tree. This is because the maximum depth of the recursion stack is the height of the main tree plus the height of the sub-root tree.

**Key Insight**
The key insight is to use a flag to keep track of whether a match is found, and only return True if a match is found. This allows us to avoid unnecessary recursive calls and improves the efficiency of the solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 38 ms (Beats 72.49%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-05-27 |
| 💻 Language | Python |