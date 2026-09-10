# 2265. Count Nodes Equal to Average of Subtree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)


## 📝 Problem Description

Given the `root` of a binary tree, return *the number of nodes where the value of the node is equal to the **average** of the values in its **subtree***.

**Note:**

	- The **average** of `n` elements is the **sum** of the `n` elements divided by `n` and **rounded down** to the nearest integer.

	- A **subtree** of `root` is a tree consisting of `root` and all of its descendants.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png)
```

**Input:** root = [4,8,5,0,1,null,6]
**Output:** 5
**Explanation:** 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/26/image-20220326133920-1.png)
```

**Input:** root = [1]
**Output:** 1
**Explanation:** For the node with value 1: The average of its subtree is 1 / 1 = 1.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 1000]`.

	- `0 <= Node.val <= 1000`

## 🧠 Solution Explanation

**Intuition**  
To know a node’s subtree average we must know two things for that subtree: the total sum of its values and how many nodes it contains. A depth‑first search naturally aggregates these two numbers from the leaves up to the root, allowing us to compute the average at each node in one pass.

**Approach**  
1. Define a recursive helper `dfs(node)` that returns `[sum, count]` for the subtree rooted at `node`.  
2. If `node` is `None`, return `[0, 0]`.  
3. Recursively call `dfs` on `node.left` and `node.right` to obtain `[leftSum, leftCnt]` and `[rightSum, rightCnt]`.  
4. Compute `currSum = leftSum + rightSum + node.val` and `currCnt = leftCnt + rightCnt + 1`.  
5. Calculate `average = currSum // currCnt` (floor division).  
6. If `average == node.val`, increment a global counter.  
7. Return `[currSum, currCnt]` to the caller.  
8. After the initial call on `root`, return the counter.

**Time Complexity**  
Each node is visited once, and all operations inside the visit are O(1).  
**O(n)**, where *n* is the number of nodes.

**Space Complexity**  
The recursion depth equals the tree height *h*.  
**O(h)** auxiliary space (worst‑case *O(n)* for a skewed tree, best‑case *O(log n)* for a balanced tree).

**Key Insight**  
A node’s subtree average can be determined by a single bottom‑up pass that tracks both sum and count; comparing the floor‑divided average to the node’s value yields the desired count.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 54 ms (Beats 42.46%) |
| 💾 Memory | 19.7 MB (Beats 33.89%) |
| 📅 Solved | 2026-09-10 |
| 💻 Language | Python |