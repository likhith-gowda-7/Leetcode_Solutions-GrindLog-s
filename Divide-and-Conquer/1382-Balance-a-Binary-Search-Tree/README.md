# 1382. Balance a Binary Search Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/balance-a-binary-search-tree/)


## 📝 Problem Description

Given the `root` of a binary search tree, return *a **balanced** binary search tree with the same node values*. If there is more than one answer, return **any of them**.

A binary search tree is **balanced** if the depth of the two subtrees of every node never differs by more than `1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/10/balance1-tree.jpg)
```

**Input:** root = [1,null,2,null,3,null,4,null,null]
**Output:** [2,1,3,null,null,null,4]
**Explanation:** This is not the only correct answer, [3,1,4,null,2] is also correct.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/08/10/balanced2-tree.jpg)
```

**Input:** root = [2,1,3]
**Output:** [2,1,3]

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `1 <= Node.val <= 10^5`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 31 ms (Beats 57.92%) |
| 💾 Memory | 26.8 MB (Beats 7.07%) |
| 📅 Solved | 2026-02-09 |
| 💻 Language | Python |