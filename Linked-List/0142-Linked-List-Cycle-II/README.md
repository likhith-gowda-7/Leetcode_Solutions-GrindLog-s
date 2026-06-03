> 📌 **Cross-listed:** Primary location is [Hash Table/0142-Linked-List-Cycle-II](../../Hash-Table/0142-Linked-List-Cycle-II). This problem also appears under: **Hash Table**, **Linked List**, **Two Pointers**

# 142. Linked List Cycle II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)


## 📝 Problem Description

Given the `head` of a linked list, return *the node where the cycle begins. If there is no cycle, return *`null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)
```

**Input:** head = [3,2,0,-4], pos = 1
**Output:** tail connects to node index 1
**Explanation:** There is a cycle in the linked list, where tail connects to the second node.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)
```

**Input:** head = [1,2], pos = 0
**Output:** tail connects to node index 0
**Explanation:** There is a cycle in the linked list, where tail connects to the first node.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)
```

**Input:** head = [1], pos = -1
**Output:** no cycle
**Explanation:** There is no cycle in the linked list.

```

 

**Constraints:**

	- The number of the nodes in the list is in the range `[0, 10^4]`.

	- `-10^5 <= Node.val <= 10^5`

	- `pos` is `-1` or a **valid index** in the linked-list.

 

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## 🧠 Solution Explanation

**Intuition**
The solution uses a trick to detect the cycle in the linked list by marking visited nodes. Since we cannot modify the linked list, we mark the visited nodes by changing their values. If a node has already been visited, it means we have found the cycle.

**Approach**
1. Initialize a pointer `curr` to the head of the linked list.
2. While `curr` is not `None`, check if its value is `"#"`. If it is, return `curr` as it is the node where the cycle begins.
3. If `curr`'s value is not `"#"`, mark it by changing its value to `"#"`.
4. Move `curr` to the next node in the linked list.
5. If `curr` becomes `None`, return `None` as there is no cycle.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. We visit each node at most once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointer `curr` and do not use any additional data structures.

**Key Insight**
The key insight is that we can mark visited nodes by changing their values, which allows us to detect the cycle without modifying the linked list. This trick is possible because we are not required to return the cycle, but only the node where it begins.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 44 ms (Beats 93.85%) |
| 💾 Memory | 22.3 MB (Beats 42.67%) |
| 📅 Solved | 2026-05-04 |
| 💻 Language | Python |