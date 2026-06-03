# 206. Reverse Linked List


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-linked-list/)


## 📝 Problem Description

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)
```

**Input:** head = [1,2,3,4,5]
**Output:** [5,4,3,2,1]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)
```

**Input:** head = [1,2]
**Output:** [2,1]

```

Example 3:**

```

**Input:** head = []
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the list is the range `[0, 5000]`.

	- `-5000 <= Node.val <= 5000`

 

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## 🧠 Solution Explanation

**Intuition**
The solution reverses a singly linked list by iterating through the list and updating the `next` pointer of each node to point to the previous node. This process continues until the entire list is reversed.

**Approach**
1. Initialize two pointers, `prev` and `curr`, to `None` and the head of the list, respectively.
2. Iterate through the list until `curr` becomes `None`.
3. In each iteration, store the next node in `temp` to avoid losing it after updating the `next` pointer.
4. Update the `next` pointer of `curr` to point to `prev`.
5. Move `prev` and `curr` one step forward by assigning `temp` to `curr` and the previous value of `curr` to `prev`.
6. Return `prev`, which is now the head of the reversed list.

**Time Complexity**
O(n), where n is the number of nodes in the list. This is because we visit each node once during the iteration.

**Space Complexity**
O(1), as we only use a constant amount of space to store the `prev`, `curr`, and `temp` pointers.

**Key Insight**
The key to this solution is understanding that reversing a linked list is a matter of updating the `next` pointers of each node, rather than manipulating the nodes themselves. By using a temporary pointer to store the next node, we can safely update the `next` pointer of the current node without losing the connection to the previous node.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-04-13 |
| 💻 Language | Python |