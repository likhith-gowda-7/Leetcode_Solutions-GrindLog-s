# 1022. Sum of Root To Leaf Binary Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)


## 📝 Problem Description

You are given the `root` of a binary tree where each node has a value `0` or `1`. Each root-to-leaf path represents a binary number starting with the most significant bit.

	- For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return *the sum of these numbers*.

The test cases are generated so that the answer fits in a **32-bits** integer.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png)
```

**Input:** root = [1,0,1,0,1,0,1]
**Output:** 22
**Explanation: **(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

```

Example 2:**

```

**Input:** root = [0]
**Output:** 0

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 1000]`.

	- `Node.val` is `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to traverse the binary tree and calculate the sum of all root-to-leaf binary numbers. The key insight is to represent each node's value as a binary digit and combine it with the parent node's value to form a new binary number.

**Approach**
1. Initialize a variable `self.res` to store the sum of all root-to-leaf binary numbers.
2. Define a helper function `dfs` that takes a node and a binary number as arguments.
3. If the node is a leaf node (i.e., it has no children), add the binary number to `self.res` and return `None`.
4. If the node has a left child, recursively call `dfs` on the left child with the binary number shifted left by one bit and the left child's value appended to it.
5. If the node has a right child, recursively call `dfs` on the right child with the binary number shifted left by one bit and the right child's value appended to it.
6. Call `dfs` on the root node with its value as the initial binary number.

**Time Complexity**
O(N), where N is the number of nodes in the binary tree. This is because each node is visited once during the DFS traversal.

**Space Complexity**
O(H), where H is the height of the binary tree. This is because the maximum depth of the recursive call stack is equal to the height of the tree.

**Key Insight**
The key insight is to represent each node's value as a binary digit and combine it with the parent node's value to form a new binary number. This allows us to efficiently calculate the sum of all root-to-leaf binary numbers using a DFS approach.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 27.52%) |
| 📅 Solved | 2026-02-24 |
| 💻 Language | Python |