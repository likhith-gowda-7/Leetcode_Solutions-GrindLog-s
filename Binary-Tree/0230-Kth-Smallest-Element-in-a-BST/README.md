> 📌 **Cross-listed:** Primary location is [Tree/0230-Kth-Smallest-Element-in-a-BST](../../Tree/0230-Kth-Smallest-Element-in-a-BST). This problem also appears under: **Tree**, **Depth-First Search**, **Binary Search Tree**, **Binary Tree**

# 230. Kth Smallest Element in a BST


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)


## 📝 Problem Description

Given the `root` of a binary search tree, and an integer `k`, return *the* `k^th` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)
```

**Input:** root = [3,1,4,null,2], k = 1
**Output:** 1

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)
```

**Input:** root = [5,3,6,2,4,null,null,1], k = 3
**Output:** 3

```

 

**Constraints:**

	- The number of nodes in the tree is `n`.

	- `1 <= k <= n <= 10^4`

	- `0 <= Node.val <= 10^4`

 

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## 🧠 Solution Explanation

**Intuition**
The solution leverages the property of Binary Search Trees (BSTs) where all elements in the left subtree are smaller than the root, and all elements in the right subtree are greater than the root. This allows us to perform an in-order traversal of the BST, which visits nodes in ascending order, and stop at the kth smallest node.

**Approach**
1. Define a helper function `inorder` that performs an in-order traversal of the BST.
2. Initialize a counter `c` to keep track of the current node's index and a variable `kth` to store the kth smallest node's value.
3. Recursively traverse the left subtree, then increment the counter `c` and check if it's equal to `k`. If it is, store the current node's value in `kth` and return.
4. If the counter is not equal to `k`, recursively traverse the right subtree.
5. After the traversal, return the kth smallest node's value stored in `kth`.

**Time Complexity**
O(N), where N is the number of nodes in the BST. This is because we visit each node once during the in-order traversal.

**Space Complexity**
O(H), where H is the height of the BST. This is because the maximum depth of the recursive call stack is equal to the height of the BST.

**Key Insight**
The key insight is that the in-order traversal of a BST visits nodes in ascending order, allowing us to find the kth smallest node by simply stopping at the kth node during the traversal. This approach takes advantage of the BST's property and avoids the need for explicit sorting or searching.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 21.2 MB (Beats 99.9%) |
| 📅 Solved | 2025-05-30 |
| 💻 Language | Python |