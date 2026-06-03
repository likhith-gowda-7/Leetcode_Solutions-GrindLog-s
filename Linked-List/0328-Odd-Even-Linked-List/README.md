# 328. Odd Even Linked List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/odd-even-linked-list/)


## 📝 Problem Description

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)
```

**Input:** head = [1,2,3,4,5]
**Output:** [1,3,5,2,4]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)
```

**Input:** head = [2,1,3,5,6,4,7]
**Output:** [2,3,6,7,1,5,4]

```

 

**Constraints:**

	- The number of nodes in the linked list is in the range `[0, 10^4]`.

	- `-10^6 <= Node.val <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining two pointers, one for the odd nodes and one for the even nodes. We swap the next pointers of the odd and even nodes to reorder the list in-place, without using any extra space.

**Approach**
1. Check if the input list is empty, and return it immediately if so.
2. Initialize two pointers, `odd` and `even`, to the head of the list and the next node of the head, respectively.
3. Initialize `even_start` to the second node of the list, which will be the start of the even nodes.
4. Traverse the list until we reach the end of the even nodes (i.e., until `even` is `None` or `even.next` is `None`).
5. Inside the loop, swap the next pointers of the odd and even nodes by setting `odd.next` to `even.next` and `even.next` to `odd.next`.
6. Move the `odd` and `even` pointers one step forward.
7. After the loop, set `odd.next` to `even_start` to connect the odd nodes to the even nodes.
8. Return the head of the reordered list.

**Time Complexity**
O(n), where n is the number of nodes in the list. We traverse the list once, and the operations inside the loop take constant time.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointers and do not use any extra data structures.

**Key Insight**
The key insight is that we can reorder the list in-place by swapping the next pointers of the odd and even nodes, without using any extra space. This is possible because we are only modifying the pointers and not creating any new nodes or data structures.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 100%) |
| 📅 Solved | 2025-04-27 |
| 💻 Language | Python |