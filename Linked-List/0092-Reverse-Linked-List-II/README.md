# 92. Reverse Linked List II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/)


## 📝 Problem Description

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)
```

**Input:** head = [1,2,3,4,5], left = 2, right = 4
**Output:** [1,4,3,2,5]

```

Example 2:**

```

**Input:** head = [5], left = 1, right = 1
**Output:** [5]

```

 

**Constraints:**

	- The number of nodes in the list is `n`.

	- `1 <= n <= 500`

	- `-500 <= Node.val <= 500`

	- `1 <= left <= right <= n`

 

**Follow up:** Could you do it in one pass?

## 🧠 Solution Explanation

**Intuition**
The solution uses a dummy node to simplify the reversal process. It iterates through the linked list, reversing the nodes between the specified `left` and `right` positions in a single pass.

**Approach**
1. Create a dummy node to simplify the reversal process and set its `next` pointer to the head of the linked list.
2. Initialize `prev` to `None` and `curr` to the head of the linked list.
3. Initialize `st` to the dummy node and `pos` to 0.
4. Iterate through the linked list:
   - If `pos` is greater than or equal to `left`, reverse the current node by updating `curr.next` to `prev`, `prev` to `curr`, and `curr` to the next node.
   - If `pos` is less than `left`, move the `st` pointer to the next node and update `curr` to the next node.
   - If `pos` equals `right`, break the loop.
5. After the loop, connect the tail of the reversed nodes to the start of the reversed section by updating `tail.next` to `curr` and `st.next` to `prev`.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because we iterate through the linked list once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the dummy node, `prev`, `curr`, `st`, and `pos`.

**Key Insight**
The key insight is to use a dummy node to simplify the reversal process and handle the edge cases where the reversed section starts at the head of the linked list. This allows us to reverse the nodes in a single pass, making the solution efficient and easy to implement.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-04-26 |
| 💻 Language | Python |