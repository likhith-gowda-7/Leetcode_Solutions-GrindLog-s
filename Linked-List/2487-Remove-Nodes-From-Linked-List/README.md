# 2487. Remove Nodes From Linked List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-nodes-from-linked-list/)


## 📝 Problem Description

You are given the `head` of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return *the *`head`* of the modified linked list.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/10/02/drawio.png)
```

**Input:** head = [5,2,13,3,8]
**Output:** [13,8]
**Explanation:** The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

```

Example 2:**

```

**Input:** head = [1,1,1,1]
**Output:** [1,1,1,1]
**Explanation:** Every node has value 1, so no nodes are removed.

```

 

**Constraints:**

	- The number of the nodes in the given list is in the range `[1, 10^5]`.

	- `1 <= Node.val <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pass approach to remove nodes from the linked list. In the first pass, it reverses the linked list to simplify the problem. Then, in the second pass, it iterates through the reversed list and removes nodes with values less than the maximum value seen so far.

**Approach**
1. Reverse the linked list by iterating through it and updating the `next` pointers of each node to point to the previous node.
2. Initialize a `maxi` node with a value of 0 to keep track of the maximum value seen so far.
3. Iterate through the reversed linked list. For each node, check if its value is greater than or equal to the `maxi` value.
4. If the node's value is greater than or equal to the `maxi` value, update the `maxi` value and remove the node by updating its `next` pointer to point to the previous node.
5. Return the new head of the modified linked list.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because we are iterating through the linked list twice.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the `prev` and `maxi` nodes.

**Key Insight**
The key insight here is that by reversing the linked list, we can simplify the problem and make it easier to remove nodes with values less than the maximum value seen so far. This is a common technique used in linked list problems to make the solution more efficient and easier to understand.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 74 ms (Beats 99.89%) |
| 💾 Memory | 49.3 MB (Beats 100%) |
| 📅 Solved | 2025-05-02 |
| 💻 Language | Python |