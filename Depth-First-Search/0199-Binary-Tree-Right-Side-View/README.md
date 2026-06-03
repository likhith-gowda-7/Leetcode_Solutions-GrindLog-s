> 📌 **Cross-listed:** Primary location is [Tree/0199-Binary-Tree-Right-Side-View](../../Tree/0199-Binary-Tree-Right-Side-View). This problem also appears under: **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Tree**

# 199. Binary Tree Right Side View


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)


## 📝 Problem Description

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

 

Example 1:**

**Input:** root = [1,2,3,null,5,null,4]

**Output:** [1,3,4]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

Example 2:**

**Input:** root = [1,2,3,4,null,null,null,5]

**Output:** [1,3,4,5]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)

Example 3:**

**Input:** root = [1,null,3]

**Output:** [1,3]

Example 4:**

**Input:** root = []

**Output:** []

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 100]`.

	- `-100 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses a breadth-first search (BFS) approach to traverse the binary tree level by level, keeping track of the last node at each level to determine the right side view.

**Approach**
1. Initialize a queue with the root node and a variable `length` to keep track of the current level size.
2. While the queue is not empty, process each node at the current level:
   - Dequeue nodes until the queue is not empty and the current level size is greater than 1.
   - For each dequeued node, enqueue its children (if any) and decrement the level size.
   - Once the queue is empty or the current level size is 1, dequeue the last node at the current level and add its value to the result list.
   - Enqueue the last node's children (if any) and update the level size.
3. Return the result list containing the right side view of the binary tree.

**Time Complexity**
O(n), where n is the number of nodes in the binary tree. This is because each node is visited once during the BFS traversal.

**Space Complexity**
O(n), where n is the number of nodes in the binary tree. This is because in the worst case, the queue will store all nodes at the last level of the tree.

**Key Insight**
The key insight is to use a BFS approach to traverse the binary tree level by level, keeping track of the last node at each level to determine the right side view. This approach ensures that each node is visited once and the result list contains the values of the nodes that can be seen from the right side of the tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-06-01 |
| 💻 Language | Python |