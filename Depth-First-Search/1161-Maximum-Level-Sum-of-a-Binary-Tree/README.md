> 📌 **Cross-listed:** Primary location is [Tree/1161-Maximum-Level-Sum-of-a-Binary-Tree](../../Tree/1161-Maximum-Level-Sum-of-a-Binary-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Tree**

# 1161. Maximum Level Sum of a Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)


## 📝 Problem Description

Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the **smallest** level `x` such that the sum of all the values of nodes at level `x` is **maximal**.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/05/03/capture.JPG)
```

**Input:** root = [1,7,0,7,-8,null,null]
**Output:** 2
**Explanation: **
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

```

Example 2:**

```

**Input:** root = [989,null,10250,98693,-89388,null,null,null,-32127]
**Output:** 2

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `-10^5 <= Node.val <= 10^5`

## 🧠 Solution Explanation

**Intuition**
This approach works by performing a level-order traversal of the binary tree and keeping track of the sum of node values at each level. The level with the maximum sum is then returned. This is a common technique for solving problems involving tree traversals.

**Approach**
1. Initialize a queue `q` to store nodes and their corresponding levels.
2. If the `root` node exists, add it to the queue with level 1.
3. Initialize a dictionary `level_sum` to store the sum of node values at each level.
4. Perform a level-order traversal of the tree:
   - Dequeue a node and its level from the queue.
   - Add the node's value to the sum of its level in the `level_sum` dictionary.
   - If the node has a left child, add it to the queue with its level incremented by 1.
   - If the node has a right child, add it to the queue with its level incremented by 1.
5. Initialize `maxi` to negative infinity and `max_level` to 0.
6. Iterate through the `level_sum` dictionary:
   - If the sum of a level is greater than `maxi`, update `maxi` and `max_level`.
7. Return `max_level`.

**Time Complexity**
O(N), where N is the number of nodes in the tree. This is because each node is visited once during the level-order traversal.

**Space Complexity**
O(N), where N is the number of nodes in the tree. This is because in the worst case, the queue will store all nodes at the last level of the tree.

**Key Insight**
The key insight here is that by performing a level-order traversal, we can efficiently compute the sum of node values at each level without having to recursively traverse the tree. This approach allows us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 35 ms (Beats 20.58%) |
| 💾 Memory | 22.8 MB (Beats 80.92%) |
| 📅 Solved | 2026-01-07 |
| 💻 Language | Python |