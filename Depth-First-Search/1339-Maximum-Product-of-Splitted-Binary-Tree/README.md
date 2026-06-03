> 📌 **Cross-listed:** Primary location is [Tree/1339-Maximum-Product-of-Splitted-Binary-Tree](../../Tree/1339-Maximum-Product-of-Splitted-Binary-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Binary Tree**

# 1339. Maximum Product of Splitted Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)


## 📝 Problem Description

Given the `root` of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return *the maximum product of the sums of the two subtrees*. Since the answer may be too large, return it **modulo** `10^9 + 7`.

**Note** that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png)
```

**Input:** root = [1,2,3,4,5,6]
**Output:** 110
**Explanation:** Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png)
```

**Input:** root = [1,null,2,3,4,null,null,5,6]
**Output:** 90
**Explanation:** Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[2, 5 * 10^4]`.

	- `1 <= Node.val <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution works by first calculating the total sum of the binary tree. Then, for each node, it calculates the product of the total sum and the sum of the subtree rooted at that node. It keeps track of the maximum product found so far and returns it modulo 10^9 + 7.

**Approach**
1. Define a helper function `find` to calculate the total sum of the binary tree using DFS.
2. Calculate the total sum of the binary tree using `find`.
3. Initialize `max_prod` to 0 to store the maximum product found so far.
4. Define a helper function `dfs` to recursively traverse the binary tree.
5. For each node, calculate the product of the total sum and the sum of the subtree rooted at that node.
6. Update `max_prod` with the maximum product found so far.
7. Return `max_prod` modulo 10^9 + 7.

**Time Complexity**
O(N) where N is the number of nodes in the binary tree. This is because we visit each node once in the `find` function and once in the `dfs` function.

**Space Complexity**
O(H) where H is the height of the binary tree. This is because of the recursive call stack in the `find` and `dfs` functions.

**Key Insight**
The key insight is to realize that the maximum product of the sums of the two subtrees is achieved by either including the current node in the left subtree or the right subtree. This is because the product of the sums of the two subtrees is maximized when the sums are as close as possible. By calculating the product of the total sum and the sum of the subtree rooted at each node, we can find the maximum product.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 78 ms (Beats 33.83%) |
| 💾 Memory | 49.1 MB (Beats 13.67%) |
| 📅 Solved | 2026-01-07 |
| 💻 Language | Python |