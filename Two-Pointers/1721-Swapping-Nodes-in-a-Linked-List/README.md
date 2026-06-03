> 📌 **Cross-listed:** Primary location is [Linked List/1721-Swapping-Nodes-in-a-Linked-List](../../Linked-List/1721-Swapping-Nodes-in-a-Linked-List). This problem also appears under: **Linked List**, **Two Pointers**

# 1721. Swapping Nodes in a Linked List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)


## 📝 Problem Description

You are given the `head` of a linked list, and an integer `k`.

Return *the head of the linked list after **swapping** the values of the *`k^th` *node from the beginning and the *`k^th` *node from the end (the list is **1-indexed**).*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg)
```

**Input:** head = [1,2,3,4,5], k = 2
**Output:** [1,4,3,2,5]

```

Example 2:**

```

**Input:** head = [7,9,6,6,7,8,3,0,9,5], k = 5
**Output:** [7,9,6,6,8,7,3,0,9,5]

```

 

**Constraints:**

	- The number of nodes in the list is `n`.

	- `1 <= k <= n <= 10^5`

	- `0 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses two pointers, `left` and `right`, to traverse the linked list. The `left` pointer is used to reach the `k^th` node from the beginning, while the `right` pointer is used to reach the `k^th` node from the end. The values of these two nodes are then swapped.

**Approach**
1. Initialize two pointers, `left` and `right`, to the head of the linked list.
2. Move the `left` pointer `k-1` steps ahead to reach the node before the `k^th` node from the beginning.
3. Create a dummy node `dummy` and set it to the node after the `left` pointer. This dummy node will be used to traverse the linked list from the end.
4. Move the `right` pointer to the end of the linked list by traversing through the nodes after the `dummy` node.
5. Swap the values of the `left` and `right` nodes.
6. Return the head of the linked list.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because we traverse the linked list twice: once to move the `left` pointer `k-1` steps ahead, and once to move the `right` pointer to the end of the linked list.

**Space Complexity**
O(1), as we only use a constant amount of space to store the `left`, `right`, and `dummy` pointers.

**Key Insight**
The key insight is to use two pointers to traverse the linked list in a way that allows us to reach the `k^th` node from both the beginning and the end. This is achieved by moving the `left` pointer `k-1` steps ahead and creating a dummy node to traverse the linked list from the end.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 33 ms (Beats 99.93%) |
| 💾 Memory | 40.2 MB (Beats 100%) |
| 📅 Solved | 2025-04-29 |
| 💻 Language | Python |