> 📌 **Cross-listed:** Primary location is [Tree/0783-Minimum-Distance-Between-BST-Nodes](../../Tree/0783-Minimum-Distance-Between-BST-Nodes). This problem also appears under: **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Search Tree**, **Binary Tree**

# 783. Minimum Distance Between BST Nodes


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)


## 📝 Problem Description

Given the `root` of a Binary Search Tree (BST), return *the minimum difference between the values of any two different nodes in the tree*.

 

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

	- The number of nodes in the tree is in the range `[2, 100]`.

	- `0 <= Node.val <= 10^5`

 

**Note:** This question is the same as 530: [https://leetcode.com/problems/minimum-absolute-difference-in-bst/](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the property of Binary Search Trees (BSTs) where all nodes to the left of a node have values less than the node, and all nodes to the right have values greater. This property allows us to perform an in-order traversal of the tree, which visits nodes in ascending order. By storing the node values in a list, we can then find the minimum difference between any two adjacent nodes in the list.

**Approach**
1. Define an in-order traversal function `inorder` that recursively visits nodes in ascending order.
2. Store the node values in a list `res` during the in-order traversal.
3. Initialize a variable `mini` to store the minimum difference found so far, set to infinity.
4. Iterate through the list `res` starting from the second element (index 1), and for each pair of adjacent elements, update `mini` with the minimum of its current value and the absolute difference between the current element and the previous element.
5. Return the minimum difference `mini` found.

**Time Complexity**
O(N), where N is the number of nodes in the tree. This is because we visit each node once during the in-order traversal.

**Space Complexity**
O(N), where N is the number of nodes in the tree. This is because we store the node values in a list of size N.

**Key Insight**
The key insight is to leverage the property of BSTs to perform an in-order traversal, which allows us to find the minimum difference between any two adjacent nodes in the list. This approach is efficient because it only requires a single pass through the tree, resulting in a linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-06-01 |
| 💻 Language | Python |