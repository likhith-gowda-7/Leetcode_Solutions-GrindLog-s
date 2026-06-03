> 📌 **Cross-listed:** Primary location is [Linked List/0086-Partition-List](../../Linked-List/0086-Partition-List). This problem also appears under: **Linked List**, **Two Pointers**

# 86. Partition List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/partition-list/)


## 📝 Problem Description

Given the `head` of a linked list and a value `x`, partition it such that all nodes **less than** `x` come before nodes **greater than or equal** to `x`.

You should **preserve** the original relative order of the nodes in each of the two partitions.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)
```

**Input:** head = [1,4,3,2,5,2], x = 3
**Output:** [1,2,2,4,3,5]

```

Example 2:**

```

**Input:** head = [2,1], x = 2
**Output:** [1,2]

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 200]`.

	- `-100 <= Node.val <= 100`

	- `-200 <= x <= 200`

## 🧠 Solution Explanation

**Intuition**
This solution works by maintaining two pointers, one for the "less than" partition and one for the "greater than or equal to" partition. We iterate through the linked list, and for each node, we decide whether to add it to the "less than" or "greater than or equal to" partition. Finally, we connect the two partitions together.

**Approach**
1. Initialize two dummy nodes, `less_than` and `greater_than`, to serve as the starting points for the "less than" and "greater than or equal to" partitions, respectively.
2. Initialize two pointers, `st1` and `st2`, to point to the next nodes of `less_than` and `greater_than`, respectively.
3. Iterate through the linked list using a while loop, starting from the head node `curr`.
4. For each node `curr`, check if its value is less than `x`. If it is, add it to the "less than" partition by setting `st1.next` to `curr` and moving `st1` to the next node.
5. If `curr`'s value is not less than `x`, add it to the "greater than or equal to" partition by setting `st2.next` to `curr` and moving `st2` to the next node.
6. After iterating through the entire list, connect the two partitions together by setting `st1.next` to `greater_than.next` and setting `st2.next` to `None`.
7. Return the next node of `less_than`, which is the head of the partitioned list.

**Time Complexity**
O(n), where n is the number of nodes in the linked list, because we iterate through the list once.

**Space Complexity**
O(1), because we only use a constant amount of space to store the dummy nodes and pointers, regardless of the size of the input list.

**Key Insight**
The key insight here is that we can maintain two separate partitions by using two pointers and iterating through the list once. This approach allows us to preserve the original relative order of the nodes in each partition, while also meeting the constraint of partitioning the list based on the given value `x`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-04-28 |
| 💻 Language | Python |