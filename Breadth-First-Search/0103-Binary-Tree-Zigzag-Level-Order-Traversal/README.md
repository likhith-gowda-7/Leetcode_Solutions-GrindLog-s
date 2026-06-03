> 📌 **Cross-listed:** Primary location is [Tree/0103-Binary-Tree-Zigzag-Level-Order-Traversal](../../Tree/0103-Binary-Tree-Zigzag-Level-Order-Traversal). This problem also appears under: **Tree**, **Breadth-First Search**, **Binary Tree**

# 103. Binary Tree Zigzag Level Order Traversal


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)


## 📝 Problem Description

Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [[3],[20,9],[15,7]]

```

Example 2:**

```

**Input:** root = [1]
**Output:** [[1]]

```

Example 3:**

```

**Input:** root = []
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 2000]`.

	- `-100 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
This solution uses a level-order traversal approach with a twist to achieve the zigzag effect. By alternating the direction of traversal at each level, we can efficiently collect the node values in the desired order.

**Approach**
1. Initialize a queue `q` to store nodes at each level, and a flag `rev` to track the direction of traversal.
2. If the `root` node exists, add it to the queue.
3. While the queue is not empty:
   1. Create an empty list `level` to store node values at the current level.
   2. Dequeue nodes from the queue and add their values to the `level` list.
   3. Enqueue the left and right child nodes of each dequeued node.
   4. If `rev` is 1 (i.e., the traversal direction is right-to-left), reverse the `level` list before appending it to the result.
   5. Toggle the `rev` flag for the next level.
4. Return the result list containing the zigzag level order traversal of node values.

**Time Complexity**
O(N), where N is the number of nodes in the binary tree. This is because we visit each node once during the level-order traversal.

**Space Complexity**
O(W), where W is the maximum width of the binary tree. This is because in the worst case, we need to store all nodes at the widest level in the queue.

**Key Insight**
The key to this solution is the use of a flag `rev` to alternate the direction of traversal at each level. By toggling this flag and reversing the `level` list when necessary, we can achieve the zigzag effect without modifying the basic level-order traversal algorithm.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.2 MB (Beats 100%) |
| 📅 Solved | 2025-06-08 |
| 💻 Language | Python |