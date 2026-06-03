> 📌 **Cross-listed:** Primary location is [Linked List/0143-Reorder-List](../../Linked-List/0143-Reorder-List). This problem also appears under: **Linked List**, **Two Pointers**, **Stack**, **Recursion**

# 143. Reorder List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reorder-list/)


## 📝 Problem Description

You are given the head of a singly linked-list. The list can be represented as:

```

L_0 &rarr; L_1 &rarr; &hellip; &rarr; L_n - 1 &rarr; L_n

```

*Reorder the list to be on the following form:*

```

L_0 &rarr; L_n &rarr; L_1 &rarr; L_n - 1 &rarr; L_2 &rarr; L_n - 2 &rarr; &hellip;

```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)
```

**Input:** head = [1,2,3,4]
**Output:** [1,4,2,3]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)
```

**Input:** head = [1,2,3,4,5]
**Output:** [1,5,2,4,3]

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[1, 5 * 10^4]`.

	- `1 <= Node.val <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer technique to find the middle of the linked list, then reverses the second half of the list. This allows us to reorder the list by alternating between the first half and the reversed second half.

**Approach**
1. Initialize two pointers, `slow` and `fast`, to the head of the list. The `fast` pointer moves twice as fast as the `slow` pointer.
2. When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle of the list.
3. Store the next node of the `slow` pointer in a temporary variable `temp` and set the next pointer of the `slow` pointer to `None`.
4. Reverse the second half of the list by iterating through the `temp` node and updating the next pointers of each node to point to the previous node.
5. Initialize two pointers, `first` and `last`, to the head and the last node of the first half of the list, respectively.
6. Alternate between the first half and the reversed second half by updating the next pointers of the `first` and `last` nodes.

**Time Complexity**
O(n), where n is the number of nodes in the list. We only iterate through the list twice, once to find the middle and once to reverse the second half.

**Space Complexity**
O(1), as we only use a constant amount of space to store the `slow`, `fast`, `temp`, `first`, and `last` pointers.

**Key Insight**
The key insight is to use a two-pointer technique to find the middle of the list, which allows us to reverse the second half of the list in a single pass. This approach is more efficient than reversing the entire list, which would require O(n) extra space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 23.4 MB (Beats 100%) |
| 📅 Solved | 2025-04-16 |
| 💻 Language | Python |