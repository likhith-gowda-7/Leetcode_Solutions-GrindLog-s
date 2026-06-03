# 3217. Delete Nodes From Linked List Present in Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/)


## 📝 Problem Description

You are given an array of integers `nums` and the `head` of a linked list. Return the `head` of the modified linked list after **removing** all nodes from the linked list that have a value that exists in `nums`.

 

Example 1:**

**Input:** nums = [1,2,3], head = [1,2,3,4,5]

**Output:** [4,5]

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png)**

Remove the nodes with values 1, 2, and 3.

Example 2:**

**Input:** nums = [1], head = [1,2,1,2,1,2]

**Output:** [2,2,2]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png)

Remove the nodes with value 1.

Example 3:**

**Input:** nums = [5], head = [1,2,3,4]

**Output:** [1,2,3,4]

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png)**

No node has value 5.

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- All elements in `nums` are unique.

	- The number of nodes in the given list is in the range `[1, 10^5]`.

	- `1 <= Node.val <= 10^5`

	- The input is generated such that there is at least one node in the linked list that has a value not present in `nums`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a set to store the values present in the input array `nums` and then iterates through the linked list, removing nodes with values that exist in the set. This approach is efficient because it allows for constant-time lookups in the set.

**Approach**
1. Create a set `h1` from the input array `nums` for fast lookups.
2. Initialize a dummy node `dummy` and a current node `curr` to keep track of the modified linked list.
3. Iterate through the linked list `head` until it reaches the end.
4. For each node, check if its value is present in the set `h1`. If not, add it to the modified linked list by setting `curr.next` to the current node and moving `curr` to the next node.
5. After iterating through the entire linked list, set `curr.next` to `None` to mark the end of the modified linked list.
6. Return the next node of the dummy node, which is the head of the modified linked list.

**Time Complexity**
O(n + m), where n is the number of nodes in the linked list and m is the number of elements in the input array `nums`. This is because we iterate through the linked list once and create a set from the input array, which takes constant time.

**Space Complexity**
O(m), where m is the number of elements in the input array `nums`. This is because we create a set from the input array, which requires additional space proportional to the size of the input array.

**Key Insight**
The key insight is to use a set to store the values present in the input array, allowing for fast lookups and efficient removal of nodes from the linked list. This approach makes the solution scalable and efficient for large inputs.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 52 ms (Beats 97.66%) |
| 💾 Memory | 58.2 MB (Beats 100%) |
| 📅 Solved | 2025-11-03 |
| 💻 Language | Python |