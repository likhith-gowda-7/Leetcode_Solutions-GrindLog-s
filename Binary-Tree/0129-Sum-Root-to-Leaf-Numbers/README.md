> 📌 **Cross-listed:** Primary location is [Tree/0129-Sum-Root-to-Leaf-Numbers](../../Tree/0129-Sum-Root-to-Leaf-Numbers). This problem also appears under: **Tree**, **Depth-First Search**, **Binary Tree**

# 129. Sum Root to Leaf Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/)


## 📝 Problem Description

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

	- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return *the total sum of all root-to-leaf numbers*. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)
```

**Input:** root = [1,2,3]
**Output:** 25
**Explanation:**
The root-to-leaf path `1->2` represents the number `12`.
The root-to-leaf path `1->3` represents the number `13`.
Therefore, sum = 12 + 13 = `25`.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)
```

**Input:** root = [4,9,0,5,1]
**Output:** 1026
**Explanation:**
The root-to-leaf path `4->9->5` represents the number 495.
The root-to-leaf path `4->9->1` represents the number 491.
The root-to-leaf path `4->0` represents the number 40.
Therefore, sum = 495 + 491 + 40 = `1026`.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 1000]`.

	- `0 <= Node.val <= 9`

	- The depth of the tree will not exceed `10`.

## 🧠 Solution Explanation

**Intuition**
This solution uses a Depth-First Search (DFS) approach to traverse the binary tree and calculate the sum of all root-to-leaf numbers. The key insight is that we can represent each root-to-leaf path as a number by multiplying the current node's value by 10 and adding it to the current number.

**Approach**
1. Define a helper function `dfs` that takes a node and the current number as arguments.
2. If the node is `None`, return immediately.
3. Multiply the current number by 10 and add the node's value to get the new current number.
4. If the node is a leaf node (i.e., it has no children), add the current number to the total sum.
5. Recursively call `dfs` on the node's left and right children with the updated current number.
6. Call `dfs` on the root node with an initial current number of 0.
7. Return the total sum.

**Time Complexity**
O(N), where N is the number of nodes in the tree. This is because we visit each node once during the DFS traversal.

**Space Complexity**
O(H), where H is the height of the tree. This is because the maximum depth of the recursive call stack is equal to the height of the tree.

**Key Insight**
The key to this solution is representing each root-to-leaf path as a number by multiplying the current node's value by 10 and adding it to the current number. This allows us to easily calculate the sum of all root-to-leaf numbers.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-06-12 |
| 💻 Language | Python |