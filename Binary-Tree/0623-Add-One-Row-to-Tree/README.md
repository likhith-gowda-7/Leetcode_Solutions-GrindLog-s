> 📌 **Cross-listed:** Primary location is [Tree/0623-Add-One-Row-to-Tree](../../Tree/0623-Add-One-Row-to-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Tree**

# 623. Add One Row to Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/add-one-row-to-tree/)


## 📝 Problem Description

Given the `root` of a binary tree and two integers `val` and `depth`, add a row of nodes with value `val` at the given depth `depth`.

Note that the `root` node is at depth `1`.

The adding rule is:

	- Given the integer `depth`, for each not null tree node `cur` at the depth `depth - 1`, create two tree nodes with value `val` as `cur`'s left subtree root and right subtree root.

	- `cur`'s original left subtree should be the left subtree of the new left subtree root.

	- `cur`'s original right subtree should be the right subtree of the new right subtree root.

	- If `depth == 1` that means there is no depth `depth - 1` at all, then create a tree node with value `val` as the new root of the whole original tree, and the original tree is the new root's left subtree.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg)
```

**Input:** root = [4,2,6,3,1,5], val = 1, depth = 2
**Output:** [4,1,1,2,null,null,6,3,1,5]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg)
```

**Input:** root = [4,2,null,3,1], val = 1, depth = 3
**Output:** [4,2,null,1,1,3,null,null,1]

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- The depth of the tree is in the range `[1, 10^4]`.

	- `-100 <= Node.val <= 100`

	- `-10^5 <= val <= 10^5`

	- `1 <= depth <= the depth of tree + 1`

## 🧠 Solution Explanation

**Intuition**
The solution uses a level-order traversal (BFS) to find the nodes at the desired depth, then modifies these nodes by adding new left and right children with the given value. This approach works because it efficiently traverses the tree and allows for easy modification of the nodes at the specified depth.

**Approach**
1. If the desired depth is 1, create a new root node with the given value and set the original root as its left child.
2. Initialize a queue with the root node and its level (1).
3. Perform a level-order traversal (BFS) to find the nodes at the desired depth (depth - 1).
4. Once the nodes at the desired depth are found, modify each of these nodes by creating new left and right children with the given value.
5. The new left child's left child is set to the original left child, and the new right child's right child is set to the original right child.
6. Return the modified root node.

**Time Complexity**
O(n), where n is the number of nodes in the tree. This is because each node is visited once during the level-order traversal.

**Space Complexity**
O(n), where n is the number of nodes in the tree. This is because in the worst case, the queue will store all nodes at the desired depth.

**Key Insight**
The key insight is to use a level-order traversal to efficiently find the nodes at the desired depth, and then modify these nodes by adding new left and right children with the given value. This approach allows for a simple and efficient solution to the problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 100%) |
| 📅 Solved | 2025-06-08 |
| 💻 Language | Python |