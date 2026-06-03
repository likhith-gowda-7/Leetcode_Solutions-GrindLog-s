# 226. Invert Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/invert-binary-tree/)


## 📝 Problem Description

Given the `root` of a binary tree, invert the tree, and return *its root*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)
```

**Input:** root = [4,2,7,1,3,6,9]
**Output:** [4,7,2,9,6,3,1]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)
```

**Input:** root = [2,1,3]
**Output:** [2,3,1]

```

Example 3:**

```

**Input:** root = []
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 100]`.

	- `-100 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack-based approach to traverse the binary tree in a level-order manner. By swapping the left and right child nodes at each level, the tree is effectively inverted.

**Approach**
1. Initialize an empty stack to store nodes to be processed.
2. If the root node exists, push it onto the stack.
3. While the stack is not empty, pop a node from the stack.
4. If the popped node has a left child, push it onto the stack.
5. If the popped node has a right child, push it onto the stack.
6. Swap the left and right child nodes of the popped node.
7. Repeat steps 3-6 until the stack is empty.
8. Return the root node of the inverted tree.

**Time Complexity**
O(n), where n is the number of nodes in the tree. This is because each node is visited once during the traversal.

**Space Complexity**
O(n), where n is the number of nodes in the tree. This is because in the worst case, the stack will store all nodes at the last level of the tree.

**Key Insight**
The key insight is that by using a stack to traverse the tree level-order, we can efficiently swap the left and right child nodes at each level, effectively inverting the tree. This approach avoids the need for recursive function calls, making it more efficient in terms of space complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-05-17 |
| 💻 Language | Python |