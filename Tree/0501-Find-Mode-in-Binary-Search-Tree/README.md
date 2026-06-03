# 501. Find Mode in Binary Search Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/)


## 📝 Problem Description

Given the `root` of a binary search tree (BST) with duplicates, return *all the [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) (i.e., the most frequently occurred element) in it*.

If the tree has more than one mode, return them in **any order**.

Assume a BST is defined as follows:

	- The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.

	- The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.

	- Both the left and right subtrees must also be binary search trees.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg)
```

**Input:** root = [1,null,2,2]
**Output:** [2]

```

Example 2:**

```

**Input:** root = [0]
**Output:** [0]

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `-10^5 <= Node.val <= 10^5`

 

**Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to traverse the binary search tree (BST) in-order, keeping track of the current node's value and its frequency. The idea is to maintain a counter for the current node's value and update it whenever a node with the same value is encountered. The maximum frequency and the corresponding values are updated accordingly.

**Approach**
1. Define an in-order DFS function to traverse the BST.
2. Initialize variables to keep track of the current node's value (`curr_val`), its frequency (`count`), the maximum frequency (`maxi`), and the result list (`res`).
3. Start the DFS traversal from the root node.
4. For each node, recursively traverse its left subtree, then update the current node's value and frequency, and finally traverse its right subtree.
5. If the current node's value is the same as the previous node's value, increment the frequency counter. Otherwise, reset the frequency counter to 1.
6. If the current node's frequency is equal to the maximum frequency, add its value to the result list. If the current node's frequency is greater than the maximum frequency, update the maximum frequency and reset the result list to contain only the current node's value.
7. After the DFS traversal is complete, return the result list containing the mode(s) of the BST.

**Time Complexity**
O(N), where N is the number of nodes in the BST. This is because each node is visited exactly once during the in-order DFS traversal.

**Space Complexity**
O(H), where H is the height of the BST. This is because the maximum depth of the recursive call stack is equal to the height of the BST. In the worst case, the BST is skewed to one side, resulting in a space complexity of O(N).

**Key Insight**
The key insight is to use a single DFS traversal to both count the frequency of each node's value and find the maximum frequency. This approach avoids the need for a separate pass to find the maximum frequency, making the solution more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 21.1 MB (Beats 99.87%) |
| 📅 Solved | 2025-05-29 |
| 💻 Language | Python |