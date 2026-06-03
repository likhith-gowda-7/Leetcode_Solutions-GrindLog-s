> 📌 **Cross-listed:** Primary location is [Divide and Conquer/1382-Balance-a-Binary-Search-Tree](../../Divide-and-Conquer/1382-Balance-a-Binary-Search-Tree). This problem also appears under: **Divide and Conquer**, **Greedy**, **Tree**, **Depth-First Search**, **Binary Search Tree**, **Binary Tree**

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

## 🧠 Solution Explanation

**Intuition**
The solution works by first performing an in-order traversal of the given binary search tree, storing the node values in a list. This list is then used to construct a balanced binary search tree, where the middle element of the list becomes the root of the tree, the left half of the list becomes the left subtree, and the right half of the list becomes the right subtree.

**Approach**
1. Perform an in-order traversal of the binary search tree using a depth-first search (DFS) approach, storing the node values in a list `res`.
2. Once the in-order traversal is complete, construct a balanced binary search tree from the list `res`.
3. To construct the balanced binary search tree, use a recursive function `bst(l, r)` that takes the left and right indices of the list as parameters.
4. In the `bst(l, r)` function, calculate the middle index `mid` of the list segment `[l, r]`.
5. Create a new `TreeNode` with the value at the `mid` index and recursively construct the left and right subtrees using `bst(l, mid-1)` and `bst(mid+1, r)`, respectively.
6. Return the constructed balanced binary search tree.

**Time Complexity**
O(N log N), where N is the number of nodes in the tree. This is because the in-order traversal takes O(N) time, and the construction of the balanced binary search tree takes O(N log N) time due to the recursive nature of the `bst(l, r)` function.

**Space Complexity**
O(N), where N is the number of nodes in the tree. This is because we need to store the node values in a list `res` of size N.

**Key Insight**
The key insight is that the in-order traversal of a binary search tree produces a sorted list of node values, which can be used to construct a balanced binary search tree. By recursively dividing the list into two halves and constructing the left and right subtrees, we can ensure that the resulting tree is balanced.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 31 ms (Beats 57.92%) |
| 💾 Memory | 26.8 MB (Beats 7.07%) |
| 📅 Solved | 2026-02-09 |
| 💻 Language | Python |