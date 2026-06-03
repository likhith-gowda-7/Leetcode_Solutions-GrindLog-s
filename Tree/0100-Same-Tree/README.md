# 100. Same Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/same-tree/)


## 📝 Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)
```

**Input:** p = [1,2,3], q = [1,2,3]
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)
```

**Input:** p = [1,2], q = [1,null,2]
**Output:** false

```

Example 3:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)
```

**Input:** p = [1,2,1], q = [1,1,2]
**Output:** false

```

 

**Constraints:**

	- The number of nodes in both trees is in the range `[0, 100]`.

	- `-10^4 <= Node.val <= 10^4`

## 🧠 Solution Explanation

**Intuition**
This solution works by performing a depth-first search (DFS) on both trees simultaneously. It checks if the nodes at the current level are the same, and if so, recursively checks the left and right subtrees. If a mismatch is found, the function immediately returns, indicating that the trees are not the same.

**Approach**
1. Define a helper function `dfs` that takes two nodes `root1` and `root2` as input.
2. Check if the function has already determined that the trees are not the same (`self.same` is `False`). If so, return immediately.
3. Check if both nodes are `None`. If so, return, as this is the base case for the recursion.
4. Check if one node is `None` or if the node values are not equal. If so, set `self.same` to `False` and return.
5. Recursively call `dfs` on the left and right subtrees of `root1` and `root2`.
6. Return the result of the DFS traversal.

**Time Complexity**
O(n), where n is the number of nodes in the trees. This is because each node is visited once during the DFS traversal.

**Space Complexity**
O(h), where h is the height of the trees. This is because the maximum depth of the recursion stack is equal to the height of the trees.

**Key Insight**
The key insight is to use a helper function to perform the DFS traversal and to use an early exit strategy to immediately return when a mismatch is found. This avoids unnecessary recursive calls and makes the function more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-05-27 |
| 💻 Language | Python |