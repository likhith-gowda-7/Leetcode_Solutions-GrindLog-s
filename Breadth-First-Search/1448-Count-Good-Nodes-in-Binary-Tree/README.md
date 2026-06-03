> 📌 **Cross-listed:** Primary location is [Tree/1448-Count-Good-Nodes-in-Binary-Tree](../../Tree/1448-Count-Good-Nodes-in-Binary-Tree). This problem also appears under: **Tree**, **Depth-First Search**, **Breadth-First Search**, **Binary Tree**

# 1448. Count Good Nodes in Binary Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)


## 📝 Problem Description

Given a binary tree `root`, a node *X* in the tree is named **good** if in the path from root to *X* there are no nodes with a value *greater than* X.



Return the number of **good** nodes in the binary tree.



 


Example 1:**



**![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png)**



```

**Input:** root = [3,1,4,3,null,1,5]
**Output:** 4
**Explanation:** Nodes in blue are **good**.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```


Example 2:**



**![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png)**



```

**Input:** root = [3,3,null,4,2]
**Output:** 3
**Explanation:** Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```


Example 3:**



```

**Input:** root = [1]
**Output:** 1
**Explanation:** Root is considered as **good**.
```


 


**Constraints:**




	- The number of nodes in the binary tree is in the range `[1, 10^5]`.

	- Each node's value is between `[-10^4, 10^4]`.

## 🧠 Solution Explanation

**Intuition**
This solution uses a stack-based approach to traverse the binary tree in a depth-first manner. The key insight is to keep track of the maximum value seen so far in the path from the root to the current node, and increment the count whenever we encounter a node with a value greater than or equal to this maximum.

**Approach**
1. Initialize a stack with the root node and a maximum value of negative infinity.
2. While the stack is not empty, pop the top node and its associated maximum value.
3. If the current node's value is greater than or equal to the maximum value, increment the count and update the maximum value to the current node's value.
4. Push the right and left child nodes of the current node onto the stack, along with the updated maximum value.
5. Repeat steps 2-4 until the stack is empty.

**Time Complexity**
O(N), where N is the number of nodes in the binary tree. This is because we visit each node exactly once.

**Space Complexity**
O(N), where N is the number of nodes in the binary tree. In the worst case, the stack will contain all nodes in the tree.

**Key Insight**
The key to this solution is to keep track of the maximum value seen so far in the path from the root to the current node, and increment the count whenever we encounter a node with a value greater than or equal to this maximum. This allows us to efficiently identify the good nodes in the binary tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 123 ms (Beats 80.86%) |
| 💾 Memory | 32.2 MB (Beats 9.95%) |
| 📅 Solved | 2025-06-01 |
| 💻 Language | Python |