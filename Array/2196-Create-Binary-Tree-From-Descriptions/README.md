# 2196. Create Binary Tree From Descriptions


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/create-binary-tree-from-descriptions/)


## 📝 Problem Description

You are given a 2D integer array `descriptions` where `descriptions[i] = [parent_i, child_i, isLeft_i]` indicates that `parent_i` is the **parent** of `child_i` in a **binary** tree of **unique** values. Furthermore,

	- If `isLeft_i == 1`, then `child_i` is the left child of `parent_i`.

	- If `isLeft_i == 0`, then `child_i` is the right child of `parent_i`.

Construct the binary tree described by `descriptions` and return *its **root***.

The test cases will be generated such that the binary tree is **valid**.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png)
```

**Input:** descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
**Output:** [50,20,80,15,17,19]
**Explanation:** The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png)
```

**Input:** descriptions = [[1,2,1],[2,3,0],[3,4,1]]
**Output:** [1,2,null,null,3,4]
**Explanation:** The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.

```

 

**Constraints:**

	- `1 <= descriptions.length <= 10^4`

	- `descriptions[i].length == 3`

	- `1 <= parent_i, child_i <= 10^5`

	- `0 <= isLeft_i <= 1`

	- The binary tree described by `descriptions` is valid.

## 🧠 Solution Explanation

**Intuition**
The solution creates a binary tree by iterating through the `descriptions` array and connecting child nodes to their respective parent nodes. The key insight is to use a hash table (dictionary in Python) to store the nodes and their children, allowing for efficient lookup and connection of nodes.

**Approach**
1. Initialize an empty dictionary `nodes` to store the nodes and their children.
2. Iterate through the `descriptions` array. For each description `[node, child, side]`:
   1. If the `node` is already in the `nodes` dictionary, update the `curr_node` to be the existing node.
   2. Otherwise, create a new `TreeNode` with the `node` value and add it to the `nodes` dictionary.
   3. If the `child` is already in the `nodes` dictionary, update the `children` to be the existing node.
   4. Otherwise, create a new `TreeNode` with the `child` value and add it to the `nodes` dictionary.
   5. Connect the `curr_node` and `children` based on the `side` value (left or right child).
3. Iterate through the `nodes` dictionary to find the root node (the node with `val[0] == False`), which is the node that was not created by the algorithm (i.e., the node that was already in the `descriptions` array).

**Time Complexity**
O(n), where n is the number of descriptions. Each description is processed once, and the operations within the loop (dictionary lookups, node creations, and connections) take constant time.

**Space Complexity**
O(n), where n is the number of descriptions. The `nodes` dictionary stores all the nodes and their children, which requires O(n) space in the worst case (when each node has a unique child).

**Key Insight**
The key insight is to use a hash table to store the nodes and their children, allowing for efficient lookup and connection of nodes. This approach enables the algorithm to create the binary tree in linear time, making it efficient for large inputs.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 156 ms (Beats 34.47%) |
| 💾 Memory | 27.7 MB (Beats 45.28%) |
| 📅 Solved | 2026-06-07 |
| 💻 Language | Python |