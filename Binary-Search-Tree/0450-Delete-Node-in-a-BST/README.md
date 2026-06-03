> 📌 **Cross-listed:** Primary location is [Tree/0450-Delete-Node-in-a-BST](../../Tree/0450-Delete-Node-in-a-BST). This problem also appears under: **Tree**, **Binary Search Tree**, **Binary Tree**

# 450. Delete Node in a BST


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple) ![Binary Tree](https://img.shields.io/badge/Binary%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/)


## 📝 Problem Description

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return *the **root node reference** (possibly updated) of the BST*.

Basically, the deletion can be divided into two stages:

	- Search for a node to remove.

	- If the node is found, delete the node.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg)
```

**Input:** root = [5,3,6,2,4,null,7], key = 3
**Output:** [5,4,6,2,null,null,7]
**Explanation:** Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
![](https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg)

```

Example 2:**

```

**Input:** root = [5,3,6,2,4,null,7], key = 0
**Output:** [5,3,6,2,4,null,7]
**Explanation:** The tree does not contain a node with value = 0.

```

Example 3:**

```

**Input:** root = [], key = 0
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 10^4]`.

	- `-10^5 <= Node.val <= 10^5`

	- Each node has a **unique** value.

	- `root` is a valid binary search tree.

	- `-10^5 <= key <= 10^5`

 

**Follow up:** Could you solve it with time complexity `O(height of tree)`?

## 🧠 Solution Explanation

**Intuition**
The solution to this problem involves a recursive approach to search for the node to be deleted in the Binary Search Tree (BST). Once found, the node is deleted by replacing its value with the minimum value in its right subtree, which maintains the BST property.

**Approach**
1. If the tree is empty (i.e., `root` is `None`), return `None`.
2. If the value of the current node (`root.val`) is less than the key, recursively call `deleteNode` on the right subtree of `root`.
3. If the value of the current node (`root.val`) is greater than the key, recursively call `deleteNode` on the left subtree of `root`.
4. If the value of the current node (`root.val`) matches the key, there are three cases:
   - If the node has no right child, return the left child of `root`.
   - If the node has no left child, return the right child of `root`.
   - If the node has both left and right children, find the minimum value in the right subtree (by traversing down to the leftmost node), replace the value of the node to be deleted with this minimum value, and then recursively call `deleteNode` on the right subtree with the new value.

**Time Complexity**
The time complexity of this solution is O(h), where h is the height of the BST. In the worst case, the tree is skewed to one side, making h equal to the number of nodes in the tree (n). However, for a balanced BST, h is log(n). Therefore, the time complexity is O(log n) in the average case and O(n) in the worst case.

**Space Complexity**
The space complexity of this solution is O(h), which is the maximum depth of the recursive call stack. In the worst case, this is O(n) when the tree is skewed to one side. However, for a balanced BST, it is O(log n).

**Key Insight**
The key insight here is that when deleting a node with both left and right children, we can replace its value with the minimum value in its right subtree, which maintains the BST property. This allows us to avoid the need to rebalance the tree, making the deletion process more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 21.2 MB (Beats 99.98%) |
| 📅 Solved | 2025-06-17 |
| 💻 Language | Python |