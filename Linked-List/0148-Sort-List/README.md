# 148. Sort List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sort-list/)


## 📝 Problem Description

Given the `head` of a linked list, return *the list after sorting it in **ascending order***.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)
```

**Input:** head = [4,2,1,3]
**Output:** [1,2,3,4]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)
```

**Input:** head = [-1,5,3,4,0]
**Output:** [-1,0,3,4,5]

```

Example 3:**

```

**Input:** head = []
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 5 * 10^4]`.

	- `-10^5 <= Node.val <= 10^5`

 

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?

## 🧠 Solution Explanation

**Intuition**
This solution works by first converting the linked list into an array of tuples, where each tuple contains the node's value, its original index, and the node itself. This allows us to sort the list in O(n log n) time using the built-in sort function. After sorting, we iterate through the array and rebuild the linked list in the correct order.

**Approach**
1. Initialize an empty list `l` to store the nodes of the linked list along with their original indices.
2. Traverse the linked list, appending each node's value, index, and the node itself to the list `l`.
3. Sort the list `l` in ascending order based on the node's value.
4. Create a dummy node and a pointer `curr` to the dummy node.
5. Iterate through the sorted list `l`, attaching each node to the end of the linked list by setting `curr.next` to the current node and updating `curr` to point to the next node.
6. Set the last node's `next` pointer to `None` to mark the end of the linked list.
7. Return the next node of the dummy node, which is the head of the sorted linked list.

**Time Complexity**
O(n log n) due to the sorting operation on the list `l`, where n is the number of nodes in the linked list.

**Space Complexity**
O(n) for storing the nodes of the linked list in the list `l`, where n is the number of nodes in the linked list.

**Key Insight**
The key insight here is that we can sort the linked list in O(n log n) time by first converting it into an array and then sorting the array. This approach allows us to take advantage of the efficient sorting algorithms available in Python, such as Timsort.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 63 ms (Beats 80.93%) |
| 💾 Memory | 37.5 MB (Beats 100%) |
| 📅 Solved | 2025-07-19 |
| 💻 Language | Python |