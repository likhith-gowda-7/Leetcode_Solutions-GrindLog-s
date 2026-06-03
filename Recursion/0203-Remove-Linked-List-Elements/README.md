> 📌 **Cross-listed:** Primary location is [Linked List/0203-Remove-Linked-List-Elements](../../Linked-List/0203-Remove-Linked-List-Elements). This problem also appears under: **Linked List**, **Recursion**

# 203. Remove Linked List Elements


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)


## 📝 Problem Description

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return *the new head*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)
```

**Input:** head = [1,2,6,3,4,5,6], val = 6
**Output:** [1,2,3,4,5]

```

Example 2:**

```

**Input:** head = [], val = 1
**Output:** []

```

Example 3:**

```

**Input:** head = [7,7,7,7], val = 7
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 10^4]`.

	- `1 <= Node.val <= 50`

	- `0 <= val <= 50`

## 🧠 Solution Explanation

**Intuition**
The solution uses a dummy node to simplify the handling of the head node. It iterates through the linked list, removing nodes with the specified value by skipping over them and updating the `next` pointer of the previous node.

**Approach**
1. Create a dummy node and set its `next` pointer to the head of the linked list.
2. Initialize a current pointer `curr` to the dummy node.
3. Iterate through the linked list until the end is reached.
4. If the current node's value matches the specified value, skip over it by updating the `head` pointer until a node with a different value is found.
5. Update the `next` pointer of the previous node (`curr`) to the new head node.
6. If the current node's value does not match the specified value, move the `curr` pointer to the next node and update the `head` pointer.
7. Return the `next` node of the dummy node, which is the new head of the linked list.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because each node is visited at most twice: once when checking if its value matches the specified value, and once when updating the `next` pointer of the previous node.

**Space Complexity**
O(1), excluding the space required for the input and output linked list. This is because a constant amount of space is used to store the dummy node and the current pointer.

**Key Insight**
The key insight is to use a dummy node to simplify the handling of the head node, allowing for a clean and efficient solution. By skipping over nodes with the specified value and updating the `next` pointer of the previous node, the solution avoids the need for explicit node deletion and manipulation.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 100%) |
| 📅 Solved | 2025-04-13 |
| 💻 Language | Python |