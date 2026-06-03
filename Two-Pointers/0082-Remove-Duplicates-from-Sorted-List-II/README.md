> 📌 **Cross-listed:** Primary location is [Linked List/0082-Remove-Duplicates-from-Sorted-List-II](../../Linked-List/0082-Remove-Duplicates-from-Sorted-List-II). This problem also appears under: **Linked List**, **Two Pointers**

# 82. Remove Duplicates from Sorted List II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)


## 📝 Problem Description

Given the `head` of a sorted linked list, *delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list*. Return *the linked list **sorted** as well*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)
```

**Input:** head = [1,2,3,3,4,4,5]
**Output:** [1,2,5]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)
```

**Input:** head = [1,1,1,2,3]
**Output:** [2,3]

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 300]`.

	- `-100 <= Node.val <= 100`

	- The list is guaranteed to be **sorted** in ascending order.

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating through the linked list and keeping track of the count of consecutive duplicates. When a new distinct number is encountered, it is added to the result list. This approach takes advantage of the fact that the input list is sorted, allowing for efficient detection of duplicates.

**Approach**
1. Create a dummy node to serve as the start of the result list.
2. Initialize a counter `c` to keep track of consecutive duplicates.
3. Iterate through the input list, incrementing `c` for each duplicate encountered.
4. When a new distinct number is encountered (`head.val != head.next.val`), add the previous distinct number to the result list (`curr.next = head`) and reset `c`.
5. After iterating through the entire list, add the last distinct number to the result list if it is not a duplicate (`c == 0`).
6. Return the next node of the dummy node, which is the start of the result list.

**Time Complexity**
O(n), where n is the number of nodes in the list. This is because we are iterating through the list once.

**Space Complexity**
O(1), excluding the space required for the input and output lists. This is because we are only using a constant amount of space to store the dummy node, counter, and current node.

**Key Insight**
The key insight here is that we can take advantage of the fact that the input list is sorted to efficiently detect duplicates. By keeping track of the count of consecutive duplicates, we can add distinct numbers to the result list in a single pass through the input list. This approach has a linear time complexity and uses constant space, making it efficient for large input lists.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-04-23 |
| 💻 Language | Python |