> 📌 **Cross-listed:** Primary location is [Dynamic Programming/1373-Maximum-Sum-BST-in-Binary-Tree](../../Dynamic-Programming/1373-Maximum-Sum-BST-in-Binary-Tree). This problem also appears under: **Dynamic Programming**, **Tree**, **Depth-First Search**, **Binary Search Tree**, **Binary Tree**

# 1373. Maximum Sum BST in Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)


## 📝 Problem Description

Given a **binary tree** `root`, return *the maximum sum of all keys of **any** sub-tree which is also a Binary Search Tree (BST)*.

Assume a BST is defined as follows:

	- The left subtree of a node contains only nodes with keys **less than** the node's key.

	- The right subtree of a node contains only nodes with keys **greater than** the node's key.

	- Both the left and right subtrees must also be binary search trees.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/01/30/sample_1_1709.png)

```

**Input:** root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
**Output:** 20
**Explanation:** Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/30/sample_2_1709.png)

```

**Input:** root = [4,3,null,1,2]
**Output:** 2
**Explanation:** Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

```

Example 3:**

```

**Input:** root = [-4,-2,-5]
**Output:** 0
**Explanation:** All values are negatives. Return an empty BST.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 4 * 10^4]`.

	- `-4 * 10^4 <= Node.val <= 4 * 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to traverse the binary tree and find the maximum sum of all keys in any sub-tree that is also a Binary Search Tree (BST). The key insight is to recursively check if the left and right subtrees are BSTs and update the maximum sum accordingly.

**Approach**
1. Define a helper function `dfs` that takes a node as input and returns a tuple containing four values:
	* `bst`: a boolean indicating whether the subtree rooted at the current node is a BST
	* `sum`: the sum of all keys in the subtree rooted at the current node
	* `min`: the minimum key in the subtree rooted at the current node
	* `max`: the maximum key in the subtree rooted at the current node
2. If the current node is `None`, return `(True, 0, float("inf"), float("-inf"))`
3. Recursively call `dfs` on the left and right children of the current node, storing their results in `l_bst`, `l_sum`, `l_min`, and `l_max`, and `r_bst`, `r_sum`, `r_min`, and `r_max`, respectively
4. Check if the left and right subtrees are BSTs and if the current node's value is within the valid range (i.e., `l_max < root.val < r_min`). If so, update the maximum sum and return `(True, total, min(l_min, root.val), max(r_max, root.val))`
5. If the left or right subtree is not a BST, return `(False, 0, 0, 0)`
6. Call `dfs` on the root node and return the maximum sum found

**Time Complexity**
O(N), where N is the number of nodes in the binary tree. This is because each node is visited once during the DFS traversal.

**Space Complexity**
O(H), where H is the height of the binary tree. This is because the maximum depth of the recursion stack is H.

**Key Insight**
The key insight is to use a recursive DFS approach to check if each subtree is a BST and update the maximum sum accordingly. The use of a tuple to store the results of each recursive call allows us to efficiently keep track of the minimum and maximum keys in each subtree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 117 ms (Beats 48.66%) |
| 💾 Memory | 39 MB (Beats 99.86%) |
| 📅 Solved | 2025-06-11 |
| 💻 Language | Python |