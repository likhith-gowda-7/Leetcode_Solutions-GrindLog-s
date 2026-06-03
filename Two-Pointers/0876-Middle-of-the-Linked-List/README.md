> 📌 **Cross-listed:** Primary location is [Linked List/0876-Middle-of-the-Linked-List](../../Linked-List/0876-Middle-of-the-Linked-List). This problem also appears under: **Linked List**, **Two Pointers**

# 876. Middle of the Linked List


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/)


## 📝 Problem Description

Given the `head` of a singly linked list, return *the middle node of the linked list*.

If there are two middle nodes, return **the second middle** node.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)
```

**Input:** head = [1,2,3,4,5]
**Output:** [3,4,5]
**Explanation:** The middle node of the list is node 3.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)
```

**Input:** head = [1,2,3,4,5,6]
**Output:** [4,5,6]
**Explanation:** Since the list has two middle nodes with values 3 and 4, we return the second one.

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[1, 100]`.

	- `1 <= Node.val <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses the "tortoise and hare" algorithm, a classic approach for finding the middle node of a linked list. This algorithm takes advantage of the fact that the fast pointer moves twice as fast as the slow pointer, effectively skipping over every other node.

**Approach**
1. Initialize two pointers, `fast` and `slow`, both pointing to the head of the linked list.
2. Move the `fast` pointer two nodes at a time (`fast = fast.next.next`) and the `slow` pointer one node at a time (`slow = slow.next`).
3. Continue moving the pointers until the `fast` pointer reaches the end of the list (`fast` becomes `None` or `fast.next` becomes `None`).
4. At this point, the `slow` pointer will be at the middle node of the linked list.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because we visit each node once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the `fast` and `slow` pointers.

**Key Insight**
The key insight behind this solution is that the fast pointer moves twice as fast as the slow pointer, allowing us to skip over every other node and reach the middle of the list in linear time. This is a fundamental technique in linked list algorithms and has many applications.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-04-13 |
| 💻 Language | Python |