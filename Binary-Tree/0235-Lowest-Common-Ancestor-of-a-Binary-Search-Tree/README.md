> 📌 **Cross-listed:** Primary location is [Tree/0235-Lowest-Common-Ancestor-of-a-Binary-Search-Tree](../../Tree/0235-Lowest-Common-Ancestor-of-a-Binary-Search-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Binary Search Tree**, **Binary Tree**

# 235. Lowest Common Ancestor of a Binary Search Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)


## 📝 Problem Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): &ldquo;The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).&rdquo;

 

Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)
```

**Input:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
**Output:** 6
**Explanation:** The LCA of nodes 2 and 8 is 6.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)
```

**Input:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
**Output:** 2
**Explanation:** The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

```

Example 3:**

```

**Input:** root = [2,1], p = 2, q = 1
**Output:** 2

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[2, 10^5]`.

	- `-10^9 <= Node.val <= 10^9`

	- All `Node.val` are **unique**.

	- `p != q`

	- `p` and `q` will exist in the BST.

## 🧠 Solution Explanation

**Intuition**
The solution leverages the property of a Binary Search Tree (BST), where all nodes to the left of a node have values less than the node's value, and all nodes to the right have values greater. This property allows us to efficiently find the lowest common ancestor (LCA) of two nodes by traversing the tree based on the values of the nodes.

**Approach**
1. Initialize the current node `curr` to the root of the tree.
2. While `curr` is not `None`:
   1. If both `p.val` and `q.val` are less than `curr.val`, move to the left child of `curr`.
   2. If both `p.val` and `q.val` are greater than `curr.val`, move to the right child of `curr`.
   3. Otherwise, return `curr` as it is the LCA of `p` and `q`.

**Time Complexity**
The time complexity of this solution is O(h), where h is the height of the tree. In the worst case, the tree is skewed, and the height is equal to the number of nodes (n). However, for a balanced BST, the height is log(n). The while loop runs until we find the LCA or reach a leaf node, which takes at most h iterations.

**Space Complexity**
The space complexity is O(1), as we only use a constant amount of space to store the current node `curr` and the input nodes `p` and `q`.

**Key Insight**
The key insight is that we can use the BST property to efficiently find the LCA by traversing the tree based on the values of the nodes. This approach avoids the need to recursively traverse the entire tree, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 55 ms (Beats 95.34%) |
| 💾 Memory | 21.1 MB (Beats 99.99%) |
| 📅 Solved | 2025-06-17 |
| 💻 Language | Python |