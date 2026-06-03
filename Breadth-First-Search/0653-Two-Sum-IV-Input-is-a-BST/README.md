> 📌 **Cross-listed:** Primary location is [Hash Table/0653-Two-Sum-IV-Input-is-a-BST](../../Hash-Table/0653-Two-Sum-IV-Input-is-a-BST). This problem also appears under: **Hash Table**, **Two Pointers**, **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Search Tree**, **Binary Tree**

# 653. Two Sum IV - Input is a BST


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)


## 📝 Problem Description

Given the `root` of a binary search tree and an integer `k`, return `true` *if there exist two elements in the BST such that their sum is equal to* `k`, *or* `false` *otherwise*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)
```

**Input:** root = [5,3,6,2,4,null,7], k = 9
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)
```

**Input:** root = [5,3,6,2,4,null,7], k = 28
**Output:** false

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `-10^4 <= Node.val <= 10^4`

	- `root` is guaranteed to be a **valid** binary search tree.

	- `-10^5 <= k <= 10^5`

## 🧠 Solution Explanation

**Intuition**
This solution leverages the properties of a binary search tree (BST) to efficiently find two elements with a sum equal to `k`. The key insight is that in a BST, all elements to the left of a node have values less than the node's value, and all elements to the right have values greater. This allows us to use a single traversal to find a pair of elements with a sum equal to `k`.

**Approach**
1. Initialize an empty set `values` to store the node values we've seen so far.
2. Initialize a stack with the root node of the BST.
3. While the stack is not empty, pop a node from the stack and perform the following steps:
   1. Calculate the complement of the current node's value with respect to `k`.
   2. Check if the complement is in the `values` set. If it is, return `True`.
   3. Add the current node's value to the `values` set.
   4. Push the right and left children of the current node onto the stack (if they exist).
4. If the stack is empty and no pair of elements with a sum equal to `k` was found, return `False`.

**Time Complexity**
O(n), where n is the number of nodes in the BST. This is because we visit each node at most once.

**Space Complexity**
O(n), where n is the number of nodes in the BST. This is because in the worst case, we store all node values in the `values` set.

**Key Insight**
The key to this solution is recognizing that the BST's property allows us to use a single traversal to find a pair of elements with a sum equal to `k`. By using a set to store the node values we've seen, we can efficiently check if a complement exists for each node's value. This approach avoids the need for a separate traversal or sorting the BST's elements, making it more efficient than other possible solutions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.8 MB (Beats 100%) |
| 📅 Solved | 2025-05-29 |
| 💻 Language | Python |