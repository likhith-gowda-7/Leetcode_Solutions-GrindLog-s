# 530. Minimum Absolute Difference in BST


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)


## 📝 Problem Description

Given the `root` of a Binary Search Tree (BST), return *the minimum absolute difference between the values of any two different nodes in the tree*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)
```

**Input:** root = [4,2,6,1,3]
**Output:** 1

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)
```

**Input:** root = [1,0,48,null,null,12,49]
**Output:** 1

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[2, 10^4]`.

	- `0 <= Node.val <= 10^5`

 

**Note:** This question is the same as 783: [https://leetcode.com/problems/minimum-distance-between-bst-nodes/](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the minimum absolute difference between any two nodes in a Binary Search Tree (BST). Since a BST is a sorted tree, we can leverage this property to find the minimum difference. The key insight is to traverse the tree in-order, which visits nodes in ascending order.

**Approach**
1. Initialize a variable `mini` to store the minimum difference, and a variable `prev` to store the previous node's value.
2. Define a recursive function `dfs` to traverse the tree in-order.
3. In the `dfs` function, first traverse the left subtree.
4. If the `prev` node exists, calculate the absolute difference between the `prev` node's value and the current node's value, and update `mini` if the difference is smaller.
5. Update `prev` to the current node's value.
6. Traverse the right subtree.
7. After traversing the entire tree, return the minimum difference `mini`.

**Time Complexity**
O(N), where N is the number of nodes in the tree. This is because we visit each node once during the in-order traversal.

**Space Complexity**
O(H), where H is the height of the tree. This is because of the recursive call stack, which can go up to the height of the tree in the worst case (when the tree is skewed).

**Key Insight**
The key to solving this problem is to traverse the tree in-order, which takes advantage of the BST's sorted property. By visiting nodes in ascending order, we can easily calculate the minimum absolute difference between any two nodes.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 65.18%) |
| 💾 Memory | 19.5 MB (Beats 100%) |
| 📅 Solved | 2025-06-17 |
| 💻 Language | Python |