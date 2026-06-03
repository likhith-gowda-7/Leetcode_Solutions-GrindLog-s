# 110. Balanced Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/balanced-binary-tree/)


## 📝 Problem Description

Given a binary tree, determine if it is **height-balanced**.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)
```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)
```

**Input:** root = [1,2,2,3,3,null,null,4,4]
**Output:** false

```

Example 3:**

```

**Input:** root = []
**Output:** true

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 5000]`.

	- `-10^4 <= Node.val <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution checks if a binary tree is height-balanced by recursively calculating the height of the left and right subtrees. If the absolute difference between the heights of the two subtrees is greater than 1, the tree is not balanced. Otherwise, the maximum height of the two subtrees plus 1 is returned.

**Approach**
1. Define a helper function `dfs` that takes a node as input and returns its height.
2. If the node is `None`, return 0, as the height of an empty tree is 0.
3. Recursively calculate the height of the left and right subtrees using `dfs(node.left)` and `dfs(node.right)`.
4. Calculate the absolute difference between the heights of the two subtrees (`diff = abs(left - right)`).
5. If the difference is greater than 1, return `float('inf')`, indicating that the tree is not balanced.
6. Otherwise, return the maximum height of the two subtrees plus 1 (`1 + max(left, right)`).
7. Call `dfs(root)` and return `True` if the result is not `float('inf')`, indicating that the tree is balanced.

**Time Complexity**
O(n), where n is the number of nodes in the tree. This is because each node is visited once during the recursive traversal.

**Space Complexity**
O(h), where h is the height of the tree. This is because the maximum depth of the recursive call stack is equal to the height of the tree.

**Key Insight**
The key insight is that we can determine if a binary tree is balanced by checking if the absolute difference between the heights of the left and right subtrees is greater than 1. This is because a balanced tree has a height difference of at most 1 between the left and right subtrees.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 30.57%) |
| 💾 Memory | 20.7 MB (Beats 5.88%) |
| 📅 Solved | 2026-02-08 |
| 💻 Language | Python |