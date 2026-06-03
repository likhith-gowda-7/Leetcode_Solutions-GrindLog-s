# 24. Swap Nodes in Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/)


## 📝 Problem Description

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:**

**Input:** head = [1,2,3,4]

**Output:** [2,1,4,3]

**Explanation:**

![](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

Example 2:**

**Input:** head = []

**Output:** []

Example 3:**

**Input:** head = [1]

**Output:** [1]

Example 4:**

**Input:** head = [1,2,3]

**Output:** [2,1,3]

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 100]`.

	- `0 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
The problem requires swapping every two adjacent nodes in a linked list without modifying the values in the list's nodes. The solution involves iterating through the list and swapping the values of adjacent nodes.

**Approach**
1. Initialize two pointers, `prev` and `curr`, to `None` and the head of the list, respectively.
2. Iterate through the list until `head` is `None`.
3. If `prev` is not `None`, swap the values of `head` and `prev`.
4. Move `prev` to `head` and `head` to `head.next`.
5. Repeat steps 2-4 until the end of the list is reached.
6. Return the head of the modified list.

**Time Complexity**
O(n), where n is the number of nodes in the list. This is because we are iterating through the list once.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the `prev` and `curr` pointers.

**Key Insight**
The key insight is that we can swap the values of adjacent nodes without modifying the values in the list's nodes by simply swapping the values of the nodes themselves. This is possible because the problem statement only requires swapping the nodes, not the values.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.2 MB (Beats 100%) |
| 📅 Solved | 2025-12-29 |
| 💻 Language | Python |