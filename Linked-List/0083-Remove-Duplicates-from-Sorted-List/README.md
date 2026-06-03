# 83. Remove Duplicates from Sorted List


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)


## 📝 Problem Description

Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return *the linked list **sorted** as well*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/list1.jpg)
```

**Input:** head = [1,1,2]
**Output:** [1,2]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/list2.jpg)
```

**Input:** head = [1,1,2,3,3]
**Output:** [1,2,3]

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 300]`.

	- `-100 <= Node.val <= 100`

	- The list is guaranteed to be **sorted** in ascending order.

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating through the linked list and only adding nodes to the result list if their values are different from the previous node. This way, duplicates are effectively removed, and the resulting list remains sorted.

**Approach**
1. Create a dummy node to serve as the head of the result list. This is necessary because we need a node to start with, and we don't want to modify the original list.
2. Initialize a current pointer `curr` to the dummy node.
3. Iterate through the original list with a pointer `head`.
4. If the value of the current node `head` is different from the value of the previous node `curr`, add `head` to the result list by setting `curr.next` to `head` and moving `curr` to the next node.
5. Move `head` to the next node in the original list.
6. Once the iteration is complete, set the `next` pointer of the last node in the result list to `None` to mark the end of the list.
7. Return the `next` node of the dummy node, which is the head of the result list.

**Time Complexity**
O(n), where n is the number of nodes in the list. This is because we make a single pass through the list, and each node is visited once.

**Space Complexity**
O(1), excluding the space needed for the result list. This is because we only use a constant amount of space to store the dummy node and the current pointer, regardless of the size of the input list.

**Key Insight**
The key insight here is that we can take advantage of the fact that the input list is sorted to efficiently remove duplicates. By only adding nodes to the result list when their values are different from the previous node, we can avoid the need to compare each node with every other node, resulting in a much faster algorithm.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-11-12 |
| 💻 Language | Python |