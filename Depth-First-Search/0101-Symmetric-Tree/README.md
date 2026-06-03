> 📌 **Cross-listed:** Primary location is [Tree/0101-Symmetric-Tree](../../Tree/0101-Symmetric-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Tree**

# 101. Symmetric Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/symmetric-tree/)


## 📝 Problem Description

Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)
```

**Input:** root = [1,2,2,3,4,4,3]
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)
```

**Input:** root = [1,2,2,null,3,null,3]
**Output:** false

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 1000]`.

	- `-100 <= Node.val <= 100`

 

**Follow up:** Could you solve it both recursively and iteratively?

## 🧠 Solution Explanation

**Intuition**
The solution checks for symmetry in a binary tree by comparing the left and right subtrees of each node. If the subtrees are mirror images of each other, the tree is symmetric. This is achieved by using a stack to perform a level-order traversal of the tree, comparing nodes at the same level.

**Approach**
1.  Check if the root is `None`, in which case the tree is symmetric (base case).
2.  Initialize a stack with the root node and its mirror image (i.e., itself).
3.  While the stack is not empty:
    *   Pop two nodes from the stack.
    *   If both nodes are `None`, continue to the next iteration (no nodes to compare).
    *   If one node is `None` and the other is not, or if the node values are different, return `False` (asymmetry detected).
    *   Push the right child of the first node and the left child of the second node onto the stack.
    *   Push the left child of the first node and the right child of the second node onto the stack.
4.  If the stack is empty, return `True` (symmetry confirmed).

**Time Complexity**
O(n), where n is the number of nodes in the tree. This is because each node is visited once during the level-order traversal.

**Space Complexity**
O(n), where n is the number of nodes in the tree. This is because in the worst case (a skewed tree), the stack will store all nodes at each level.

**Key Insight**
The key insight is to use a stack to perform a level-order traversal of the tree, comparing nodes at the same level. This approach allows us to efficiently check for symmetry in the tree without recursively traversing the tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-05-27 |
| 💻 Language | Python |