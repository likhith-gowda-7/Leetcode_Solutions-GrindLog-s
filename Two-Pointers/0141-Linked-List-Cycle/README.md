> 📌 **Cross-listed:** Primary location is [Hash Table/0141-Linked-List-Cycle](../../Hash-Table/0141-Linked-List-Cycle). This problem also appears under: **Hash Table**, **Linked List**, **Two Pointers**

# 141. Linked List Cycle


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/linked-list-cycle/)


## 📝 Problem Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true`* if there is a cycle in the linked list*. Otherwise, return `false`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)
```

**Input:** head = [3,2,0,-4], pos = 1
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

```

Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)
```

**Input:** head = [1,2], pos = 0
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)
```

**Input:** head = [1], pos = -1
**Output:** false
**Explanation:** There is no cycle in the linked list.

```

 

**Constraints:**

	- The number of the nodes in the list is in the range `[0, 10^4]`.

	- `-10^5 <= Node.val <= 10^5`

	- `pos` is `-1` or a **valid index** in the linked-list.

 

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## 🧠 Solution Explanation

**Intuition**
The solution uses Floyd's Tortoise and Hare algorithm, also known as the "slow and fast pointer" technique, to detect a cycle in a linked list. This approach works by advancing two pointers at different speeds through the list. If there is a cycle, the fast pointer will eventually catch up to the slow pointer.

**Approach**
1. Initialize two pointers, `slow` and `fast`, to the head of the linked list.
2. Move the `slow` pointer one step at a time and the `fast` pointer two steps at a time.
3. If the `fast` pointer reaches the end of the list (i.e., `fast` or `fast.next` is `None`), there is no cycle.
4. If the `fast` pointer catches up to the `slow` pointer, there is a cycle.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because in the worst case, the fast pointer will traverse the entire list once.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the slow and fast pointers.

**Key Insight**
The key insight behind this solution is that if there is a cycle, the fast pointer will eventually catch up to the slow pointer. This is because the fast pointer is moving twice as fast as the slow pointer, so if there is a cycle, the fast pointer will eventually enter the cycle and catch up to the slow pointer.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 44 ms (Beats 95.3%) |
| 💾 Memory | 20 MB (Beats 100%) |
| 📅 Solved | 2025-04-14 |
| 💻 Language | Python |