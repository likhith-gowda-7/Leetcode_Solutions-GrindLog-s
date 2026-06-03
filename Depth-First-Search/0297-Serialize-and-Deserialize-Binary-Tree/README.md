> 📌 **Cross-listed:** Primary location is [String/0297-Serialize-and-Deserialize-Binary-Tree](../../String/0297-Serialize-and-Deserialize-Binary-Tree). This problem also appears under: **String**, **Tree**, **Depth-First Search**, **Breadth-First Search**, **Design**, **Binary Tree**

# 297. Serialize and Deserialize Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)


## 📝 Problem Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as [how LeetCode serializes a binary tree](https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode#h_01J5EGREAW3NAEJ14XC07GRW1A). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)
```

**Input:** root = [1,2,3,null,null,4,5]
**Output:** [1,2,3,null,null,4,5]

```

Example 2:**

```

**Input:** root = []
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 10^4]`.

	- `-1000 <= Node.val <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to serialize the binary tree into a string, and then uses another DFS to deserialize the string back into the original tree structure. This approach allows us to efficiently traverse the tree and reconstruct it from the serialized string.

**Approach**
1. The `serialize` method uses a recursive DFS function to traverse the binary tree. If the current node is `None`, it appends "N," to the result string. Otherwise, it appends the node's value and recursively calls `dfs` on the left and right children.
2. The `deserialize` method uses a queue to store the nodes' values from the serialized string. It defines a recursive DFS function that pops a value from the queue, creates a new node with that value, and recursively calls `dfs` on the left and right children.
3. The `deserialize` method returns the root node of the deserialized tree.

**Time Complexity**
The time complexity of both `serialize` and `deserialize` is O(n), where n is the number of nodes in the binary tree. This is because we visit each node once during serialization and deserialization.

**Space Complexity**
The space complexity of `serialize` is O(n) due to the recursive call stack. The space complexity of `deserialize` is also O(n) because we store the nodes' values in the queue.

**Key Insight**
The key insight is to use a recursive DFS approach to both serialize and deserialize the binary tree. This allows us to efficiently traverse the tree and reconstruct it from the serialized string. The use of a queue in the `deserialize` method helps to efficiently store and retrieve the nodes' values.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 21.2 MB (Beats 99.83%) |
| 📅 Solved | 2025-06-11 |
| 💻 Language | Python |