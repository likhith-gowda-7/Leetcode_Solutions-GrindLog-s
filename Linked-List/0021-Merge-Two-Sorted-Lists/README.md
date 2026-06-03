# 21. Merge Two Sorted Lists


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)


## 📝 Problem Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)
```

**Input:** list1 = [1,2,4], list2 = [1,3,4]
**Output:** [1,1,2,3,4,4]

```

Example 2:**

```

**Input:** list1 = [], list2 = []
**Output:** []

```

Example 3:**

```

**Input:** list1 = [], list2 = [0]
**Output:** [0]

```

 

**Constraints:**

	- The number of nodes in both lists is in the range `[0, 50]`.

	- `-100 <= Node.val <= 100`

	- Both `list1` and `list2` are sorted in **non-decreasing** order.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a two-pointer technique to merge two sorted linked lists into one sorted list. The key insight is to compare the values of the current nodes in both lists and append the smaller value to the result list.

**Approach**
1. Create a dummy node to serve as the head of the merged list.
2. Initialize a current pointer `curr` to the dummy node.
3. While both `list1` and `list2` are not empty, compare the values of the current nodes.
4. If `list1`'s value is smaller, append `list1` to the result list and move to the next node in `list1`.
5. Otherwise, append `list2` to the result list and move to the next node in `list2`.
6. Move the current pointer `curr` to the next node.
7. If one list is empty, append the remaining nodes from the other list to the result list.
8. Return the next node of the dummy node, which is the head of the merged list.

**Time Complexity**
O(n + m), where n and m are the lengths of `list1` and `list2`, respectively. This is because we are iterating through both lists once.

**Space Complexity**
O(1), excluding the space required for the output list. We are only using a constant amount of space to store the dummy node and the current pointer.

**Key Insight**
The key to this solution is to use a two-pointer technique to compare the values of the current nodes in both lists and append the smaller value to the result list. This approach ensures that the merged list remains sorted.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-04-10 |
| 💻 Language | Python |