> 📌 **Cross-listed:** Primary location is [Linked List/0002-Add-Two-Numbers](../../Linked-List/0002-Add-Two-Numbers). This problem also appears under: **Linked List**, **Math**, **Recursion**

# 2. Add Two Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/add-two-numbers/)


## 📝 Problem Description

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)
```

**Input:** l1 = [2,4,3], l2 = [5,6,4]
**Output:** [7,0,8]
**Explanation:** 342 + 465 = 807.

```

Example 2:**

```

**Input:** l1 = [0], l2 = [0]
**Output:** [0]

```

Example 3:**

```

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
**Output:** [8,9,9,9,0,0,0,1]

```

 

**Constraints:**

	- The number of nodes in each linked list is in the range `[1, 100]`.

	- `0 <= Node.val <= 9`

	- It is guaranteed that the list represents a number that does not have leading zeros.

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating over both linked lists simultaneously, adding corresponding nodes together, and handling any carry values that arise from the addition. The key insight is that we can use a dummy node to simplify the code and avoid edge cases.

**Approach**
1. Initialize a `carry` variable to 0, which will store any carry values from the addition.
2. Create a dummy node `dummy` and set `curr` to `dummy`. This dummy node will be used to simplify the code and avoid edge cases.
3. Loop until both linked lists are empty.
4. In each iteration, get the values of the current nodes in both linked lists (`val1` and `val2`). If a node is `None`, use 0 as its value.
5. Add the `carry` value to the sum of `val1` and `val2` to get the `addition` value.
6. Update the `carry` value by taking the integer division of `addition` by 10.
7. Create a new node `lastdigit` with the last digit of the `addition` value (obtained by taking the modulus of `addition` by 10).
8. Set `curr.next` to `lastdigit` and update `curr` to `lastdigit`.
9. Move to the next nodes in both linked lists (`l1` and `l2`).
10. If there is a remaining `carry` value after the loop, create a new node with this value and set `curr.next` to it.
11. Return `dummy.next`, which is the head of the resulting linked list.

**Time Complexity**
O(max(m, n)), where m and n are the lengths of the two linked lists. This is because we iterate over both linked lists simultaneously, and the loop continues until both lists are empty.

**Space Complexity**
O(max(m, n)), where m and n are the lengths of the two linked lists. This is because we create a new linked list with a maximum of max(m, n) nodes.

**Key Insight**
The use of a dummy node simplifies the code and avoids edge cases, making it easier to handle the carry value and the last node in the resulting linked list.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 66.06%) |
| 💾 Memory | 17.3 MB (Beats 100%) |
| 📅 Solved | 2025-12-31 |
| 💻 Language | Python |