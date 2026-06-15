# 2095. Delete the Middle Node of a Linked List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)


## 📝 Problem Description

You are given the `head` of a linked list. **Delete** the **middle node**, and return *the* `head` *of the modified linked list*.

The **middle node** of a linked list of size `n` is the `&lfloor;n / 2&rfloor;^th` node from the **start** using **0-based indexing**, where `&lfloor;x&rfloor;` denotes the largest integer less than or equal to `x`.

	- For `n` = `1`, `2`, `3`, `4`, and `5`, the middle nodes are `0`, `1`, `1`, `2`, and `2`, respectively.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/11/16/eg1drawio.png)
```

**Input:** head = [1,3,4,7,1,2,6]
**Output:** [1,3,4,1,2,6]
**Explanation:**
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/11/16/eg2drawio.png)
```

**Input:** head = [1,2,3,4]
**Output:** [1,2,4]
**Explanation:**
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/11/16/eg3drawio.png)
```

**Input:** head = [2,1]
**Output:** [2]
**Explanation:**
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
```

 

**Constraints:**

	- The number of nodes in the list is in the range `[1, 10^5]`.

	- `1 <= Node.val <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses the "tortoise and hare" algorithm to find the node before the middle node of the linked list. This approach works because the fast pointer moves twice as fast as the slow pointer, effectively skipping over the middle node.

**Approach**
1. Check if the linked list has only one node, in which case we return `None` as there is no middle node to delete.
2. Initialize three pointers: `fast`, `slow`, and `prev`. `fast` and `slow` are used to find the middle node, while `prev` keeps track of the node before the middle node.
3. Move `fast` two nodes at a time and `slow` one node at a time. This ensures that `fast` reaches the end of the linked list before `slow` reaches the middle node.
4. When `fast` reaches the end of the linked list, `slow` will be at the middle node. Update the `next` pointer of `prev` to skip over the middle node.
5. Return the head of the modified linked list.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because we visit each node once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointers.

**Key Insight**
The key insight is that by moving the `fast` pointer twice as fast as the `slow` pointer, we can effectively find the node before the middle node without having to calculate the exact middle index. This approach is efficient and easy to implement.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 95 ms (Beats 47.33%) |
| 💾 Memory | 62.2 MB (Beats 95.23%) |
| 📅 Solved | 2026-06-15 |
| 💻 Language | Python |