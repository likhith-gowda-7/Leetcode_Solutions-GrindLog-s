# 25. Reverse Nodes in k-Group


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)


## 📝 Problem Description

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)
```

**Input:** head = [1,2,3,4,5], k = 2
**Output:** [2,1,4,3,5]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)
```

**Input:** head = [1,2,3,4,5], k = 3
**Output:** [3,2,1,4,5]

```

 

**Constraints:**

	- The number of nodes in the list is `n`.

	- `1 <= k <= n <= 5000`

	- `0 <= Node.val <= 1000`

 

**Follow-up:** Can you solve the problem in `O(1)` extra memory space?

## 🧠 Solution Explanation

**Intuition**
The solution uses a recursive approach to reverse the nodes of the linked list in groups of size `k`. It maintains a dummy node to simplify the edge cases and iteratively reverses the nodes in each group.

**Approach**
1. Define a helper function `has_knodes` to get the `k`-th node from the current node.
2. Initialize a dummy node and set the `prev_group_end` to the dummy node.
3. Iterate until the `k`-th node is `None`, indicating the end of the list.
4. In each iteration, reverse the nodes from the `prev_group_end` to the `k`-th node.
5. Update the `prev_group_end` to the starting node of the next group.
6. After reversing the nodes, connect the `prev_group_end` to the `k`-th node.
7. Return the modified list by returning `dummy.next`.

**Time Complexity**
O(n) where n is the length of the linked list, since we visit each node once.

**Space Complexity**
O(1) since we only use a constant amount of space to store the dummy node, `prev_group_end`, and the temporary variables.

**Key Insight**
The key insight is to use a recursive approach to reverse the nodes in each group, and to maintain a dummy node to simplify the edge cases. This approach allows us to efficiently reverse the nodes in groups of size `k` while handling the remaining nodes at the end of the list.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.6 MB (Beats 100%) |
| 📅 Solved | 2025-05-06 |
| 💻 Language | Python |