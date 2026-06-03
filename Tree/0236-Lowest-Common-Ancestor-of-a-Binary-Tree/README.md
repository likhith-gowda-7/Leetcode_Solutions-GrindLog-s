# 236. Lowest Common Ancestor of a Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)


## 📝 Problem Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): &ldquo;The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).&rdquo;

 

Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
```

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
**Output:** 3
**Explanation:** The LCA of nodes 5 and 1 is 3.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
```

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
**Output:** 5
**Explanation:** The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

```

Example 3:**

```

**Input:** root = [1,2], p = 1, q = 2
**Output:** 1

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[2, 10^5]`.

	- `-10^9 <= Node.val <= 10^9`

	- All `Node.val` are **unique**.

	- `p != q`

	- `p` and `q` will exist in the tree.

## 🧠 Solution Explanation

**Intuition**
This solution uses a Depth-First Search (DFS) approach to traverse the binary tree and find the lowest common ancestor (LCA) of two given nodes. The key insight is that the LCA must be a node that has both `p` and `q` as descendants, and it must be the lowest such node.

**Approach**
1. Define a helper function `dfs` that takes a node `root` as input.
2. If `root` is `None` or if `root` is either `p` or `q`, return `root` immediately.
3. Recursively call `dfs` on `root.left` and `root.right`.
4. If both `left` and `right` are not `None`, it means that `p` and `q` are in different subtrees of `root`, so return `root`.
5. If only `left` is not `None`, it means that `p` and `q` are in the left subtree of `root`, so return `left`.
6. If only `right` is not `None`, it means that `p` and `q` are in the right subtree of `root`, so return `right`.
7. Call `dfs` on the root node to start the traversal.

**Time Complexity**
O(N), where N is the number of nodes in the binary tree. This is because in the worst case, we visit each node once.

**Space Complexity**
O(H), where H is the height of the binary tree. This is because the maximum depth of the recursive call stack is H.

**Key Insight**
The key insight is that the LCA must be a node that has both `p` and `q` as descendants, and it must be the lowest such node. This is why we return `root` as soon as we find a node that has both `p` and `q` as descendants, because it is guaranteed to be the lowest such node.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 39 ms (Beats 99.87%) |
| 💾 Memory | 22 MB (Beats 99.96%) |
| 📅 Solved | 2025-05-30 |
| 💻 Language | Python |