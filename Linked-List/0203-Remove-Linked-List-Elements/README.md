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

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 100%) |
| 📅 Solved | 2025-04-13 |
| 💻 Language | Python |