> 📌 **Cross-listed:** Primary location is [Tree/0701-Insert-into-a-Binary-Search-Tree](../../Tree/0701-Insert-into-a-Binary-Search-Tree). This problem also appears under: **Tree**, **Binary Search Tree**, **Binary Tree**

# 701. Insert into a Binary Search Tree


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/)


## 📝 Problem Description

You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return *the root node of the BST after the insertion*. It is **guaranteed** that the new value does not exist in the original BST.

**Notice** that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return **any of them**.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)
```

**Input:** root = [4,2,7,1,3], val = 5
**Output:** [4,2,7,1,3,5]
**Explanation:** Another accepted tree is:
![](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)

```

Example 2:**

```

**Input:** root = [40,20,60,10,30,50,70], val = 25
**Output:** [40,20,60,10,30,50,70,null,null,25]

```

Example 3:**

```

**Input:** root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
**Output:** [4,2,7,1,3,5]

```

 

**Constraints:**

	- The number of nodes in the tree will be in the range `[0, 10^4]`.

	- `-10^8 <= Node.val <= 10^8`

	- All the values `Node.val` are **unique**.

	- `-10^8 <= val <= 10^8`

	- It's **guaranteed** that `val` does not exist in the original BST.

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to find the correct location to insert the new value into the binary search tree (BST). The key insight is that we can always find the correct location by comparing the new value with the current node's value, and then recursively searching the left or right subtree.

**Approach**
1. Create a new node with the given value.
2. If the tree is empty (i.e., the root is `None`), return the new node as the root.
3. Perform a DFS traversal of the tree, keeping track of the previous node (`prev`) visited.
4. If the current node's value is greater than the new value, recursively search the left subtree.
5. If the current node's value is less than the new value, recursively search the right subtree.
6. Once the correct location is found, insert the new node as the left or right child of the previous node.

**Time Complexity**
O(h), where h is the height of the tree. In the worst case, the tree is skewed to one side, and the DFS traversal has to go down the entire height of the tree.

**Space Complexity**
O(h), where h is the height of the tree. The recursive call stack can go up to the height of the tree in the worst case.

**Key Insight**
The key insight is that we can always find the correct location to insert the new value by comparing it with the current node's value and recursively searching the left or right subtree. This approach ensures that the tree remains a BST after insertion.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 100%) |
| 📅 Solved | 2025-06-10 |
| 💻 Language | Python |