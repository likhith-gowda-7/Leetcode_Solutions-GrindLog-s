# 19. Remove Nth Node From End of List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)


## 📝 Problem Description

Given the `head` of a linked list, remove the `n^th` node from the end of the list and return its head.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)
```

**Input:** head = [1,2,3,4,5], n = 2
**Output:** [1,2,3,5]

```

Example 2:**

```

**Input:** head = [1], n = 1
**Output:** []

```

Example 3:**

```

**Input:** head = [1,2], n = 1
**Output:** [1]

```

 

**Constraints:**

	- The number of nodes in the list is `sz`.

	- `1 <= sz <= 30`

	- `0 <= Node.val <= 100`

	- `1 <= n <= sz`

 

**Follow up:** Could you do this in one pass?

## 🧠 Solution Explanation

**Intuition**
This solution works by first finding the node that is `n` nodes before the node to be removed. Then, it updates the `next` pointer of this node to skip the node to be removed. This approach takes advantage of the fact that we can traverse the linked list in one pass.

**Approach**
1. Initialize two pointers `curr` and `k` to the head of the linked list and `n` respectively.
2. Move `curr` and decrement `k` until `k` reaches 0. This will make `curr` point to the node that is `n` nodes before the node to be removed.
3. Initialize two pointers `prev` and `s` to `None` and the head of the linked list respectively.
4. Move `prev`, `curr`, and `s` until `curr` reaches the end of the linked list. In each step, update `prev` to point to the previous node of `s`.
5. If `prev` is `None`, it means the node to be removed is the head of the linked list, so return the next node of `s`.
6. Otherwise, update the `next` pointer of `prev` to skip the node to be removed.
7. Return the head of the modified linked list.

**Time Complexity**
O(L), where L is the length of the linked list. This is because we only need to traverse the linked list once.

**Space Complexity**
O(1), because we only use a constant amount of space to store the pointers `curr`, `k`, `prev`, and `s`.

**Key Insight**
The key insight here is that we can find the node that is `n` nodes before the node to be removed by traversing the linked list in one pass. This allows us to solve the problem efficiently without needing to traverse the linked list multiple times.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 90.94%) |
| 📅 Solved | 2026-03-26 |
| 💻 Language | Python |