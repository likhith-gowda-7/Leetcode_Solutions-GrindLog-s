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

## 🧠 Solution Explanation

**Intuition**
The solution uses a min heap to efficiently merge the k sorted linked lists into one sorted linked list. The key insight is to first flatten the linked lists into a min heap, and then pop the smallest element from the heap to construct the sorted linked list.

**Approach**
1. Check if the input list is empty, if so return None.
2. Initialize a min heap to store the node values from the linked lists.
3. Iterate through each linked list and append its node values to the min heap.
4. Heapify the min heap to maintain the heap property.
5. Create a new linked list with the smallest node value (popped from the min heap) as the root node.
6. While the min heap is not empty, pop the smallest node value, create a new node with this value, and append it to the current node's next pointer.
7. Return the root node of the merged linked list.

**Time Complexity**
O(N log k), where N is the total number of nodes across all linked lists and k is the number of linked lists. The time complexity is dominated by the heapify operation (O(k)) and the while loop (O(N log k)).

**Space Complexity**
O(N), where N is the total number of nodes across all linked lists. The space complexity is dominated by the min heap, which stores all node values from the linked lists.

**Key Insight**
The key insight is to use a min heap to efficiently merge the k sorted linked lists into one sorted linked list. By first flattening the linked lists into a min heap, we can then pop the smallest element from the heap to construct the sorted linked list in O(N log k) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 83.76%) |
| 💾 Memory | 20.4 MB (Beats 99.99%) |
| 📅 Solved | 2025-07-13 |
| 💻 Language | Python |