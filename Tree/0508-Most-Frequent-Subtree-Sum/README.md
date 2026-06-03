> 📌 **Cross-listed:** Primary location is [Hash Table/0508-Most-Frequent-Subtree-Sum](../../Hash-Table/0508-Most-Frequent-Subtree-Sum). This problem also appears under: **Hash Table**, **Tree**, **Depth-First Search**, **Binary Tree**

# 508. Most Frequent Subtree Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/most-frequent-subtree-sum/)


## 📝 Problem Description

Given the `root` of a binary tree, return the most frequent **subtree sum**. If there is a tie, return all the values with the highest frequency in any order.

The **subtree sum** of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg)
```

**Input:** root = [5,2,-3]
**Output:** [2,-3,4]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg)
```

**Input:** root = [5,2,-5]
**Output:** [2]

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `-10^5 <= Node.val <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to traverse the binary tree, calculating the subtree sum for each node. It then uses a hash table to count the frequency of each subtree sum. The most frequent subtree sums are stored in a list, which is returned as the result.

**Approach**
1. Define a hash table `h1` to store the frequency of each subtree sum.
2. Define a list `res` to store the most frequent subtree sums.
3. Initialize a variable `maxi` to store the maximum frequency found so far.
4. Define a recursive DFS function `dfs` that takes a node `root` as input.
5. If the node is `None`, return 0 (base case).
6. Recursively call `dfs` on the left and right children of the node.
7. Calculate the subtree sum of the current node by adding the sums of its left and right children to its own value.
8. Increment the count of the subtree sum in the hash table `h1`.
9. If the count of the subtree sum is equal to `maxi`, append it to the list `res`.
10. If the count of the subtree sum is greater than `maxi`, update `maxi` and reset `res` to contain only the current subtree sum.
11. Return the subtree sum of the current node.
12. Call `dfs` on the root node to start the traversal.
13. Return the list `res` containing the most frequent subtree sums.

**Time Complexity**
O(N), where N is the number of nodes in the tree. This is because each node is visited once during the DFS traversal.

**Space Complexity**
O(N), where N is the number of nodes in the tree. This is because in the worst case, the hash table `h1` will store the subtree sum of each node, resulting in a space complexity of O(N).

**Key Insight**
The key insight is to use a hash table to count the frequency of each subtree sum, allowing us to efficiently identify the most frequent subtree sums. The recursive DFS approach enables us to traverse the tree in a bottom-up manner, calculating the subtree sum for each node and updating the frequency count in the hash table.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2 ms (Beats 84.05%) |
| 💾 Memory | 20.4 MB (Beats 100%) |
| 📅 Solved | 2025-06-05 |
| 💻 Language | Python |