# 61. Rotate List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotate-list/)


## 📝 Problem Description

Given the `head` of a linked list, rotate the list to the right by `k` places.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)
```

**Input:** head = [1,2,3,4,5], k = 2
**Output:** [4,5,1,2,3]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)
```

**Input:** head = [0,1,2], k = 4
**Output:** [2,0,1]

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 500]`.

	- `-100 <= Node.val <= 100`

	- `0 <= k <= 2 * 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by treating the linked list as a circular list and rotating it to the right by `k` places. This is achieved by connecting the tail of the list back to the head, effectively making it a circular list. Then, we find the new head of the rotated list by traversing `k` nodes from the head in the circular list.

**Approach**
1. Check if the list is empty or `k` is 0, in which case we return the original list.
2. Find the length of the list by traversing it.
3. Connect the tail of the list back to the head, making it a circular list.
4. Calculate the effective rotation `k` by taking the remainder of `k` divided by the length of the list.
5. Traverse the circular list to find the new head by counting `k` nodes from the head.
6. When we reach the new head, set its `next` pointer to `None` to break the circular list and return the new head.

**Time Complexity**
O(n), where n is the length of the list. We traverse the list twice: once to find its length and once to find the new head.

**Space Complexity**
O(1), as we only use a constant amount of space to store the current node and the length of the list.

**Key Insight**
The key insight is to treat the linked list as a circular list and rotate it by connecting the tail back to the head. This allows us to find the new head by traversing `k` nodes from the head in the circular list.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 73.34%) |
| 📅 Solved | 2026-05-05 |
| 💻 Language | Python |