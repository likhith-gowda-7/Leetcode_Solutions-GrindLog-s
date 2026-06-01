> 📌 **Cross-listed:** Primary location is [Linked List/0023-Merge-k-Sorted-Lists](../../Linked-List/0023-Merge-k-Sorted-Lists). This problem also appears under: **Linked List**, **Divide and Conquer**, **Heap (Priority Queue)**, **Merge Sort**

# 23. Merge k Sorted Lists


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple) ![Merge Sort](https://img.shields.io/badge/Merge%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)


## 📝 Problem Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

 

Example 1:**

```

**Input:** lists = [[1,4,5],[1,3,4],[2,6]]
**Output:** [1,1,2,3,4,4,5,6]
**Explanation:** The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

```

Example 2:**

```

**Input:** lists = []
**Output:** []

```

Example 3:**

```

**Input:** lists = [[]]
**Output:** []

```

 

**Constraints:**

	- `k == lists.length`

	- `0 <= k <= 10^4`

	- `0 <= lists[i].length <= 500`

	- `-10^4 <= lists[i][j] <= 10^4`

	- `lists[i]` is sorted in **ascending order**.

	- The sum of `lists[i].length` will not exceed `10^4`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 83.76%) |
| 💾 Memory | 20.4 MB (Beats 99.99%) |
| 📅 Solved | 2025-07-13 |
| 💻 Language | Python |