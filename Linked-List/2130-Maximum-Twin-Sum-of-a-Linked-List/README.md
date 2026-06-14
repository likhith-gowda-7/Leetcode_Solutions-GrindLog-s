# 2130. Maximum Twin Sum of a Linked List


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)


## 📝 Problem Description

In a linked list of size `n`, where `n` is **even**, the `i^th` node (**0-indexed**) of the linked list is known as the **twin** of the `(n-1-i)^th` node, if `0 <= i <= (n / 2) - 1`.

	- For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1` is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The **twin sum **is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return *the **maximum twin sum** of the linked list*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/12/03/eg1drawio.png)
```

**Input:** head = [5,4,2,1]
**Output:** 6
**Explanation:**
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/12/03/eg2drawio.png)
```

**Input:** head = [4,2,2,3]
**Output:** 7
**Explanation:**
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/12/03/eg3drawio.png)
```

**Input:** head = [1,100000]
**Output:** 100001
**Explanation:**
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

```

 

**Constraints:**

	- The number of nodes in the list is an **even** integer in the range `[2, 10^5]`.

	- `1 <= Node.val <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by first storing the values of all nodes in a dictionary, where the key is the index of the node and the value is the node's value. Then, it iterates over the first half of the nodes, calculates the twin sum for each node, and keeps track of the maximum twin sum found so far.

**Approach**
1. Initialize an empty dictionary `idx_map` to store node values by their indices.
2. Initialize a variable `idx` to 0 to keep track of the current index.
3. Initialize a variable `res` to 0 to store the maximum twin sum found so far.
4. Initialize a variable `curr` to the head of the linked list.
5. Traverse the linked list, storing each node's value in `idx_map` with its index as the key, and increment `idx`.
6. Once the linked list is traversed, iterate over the first half of the nodes (i.e., `idx//2` nodes).
7. For each node, calculate its twin sum by looking up the value of its twin node in `idx_map`.
8. Update `res` with the maximum of the current `res` and the twin sum.
9. Return `res` as the maximum twin sum found.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because we traverse the linked list once to store node values in the dictionary, and then iterate over the first half of the nodes to calculate twin sums.

**Space Complexity**
O(n), where n is the number of nodes in the linked list. This is because we store node values in the dictionary, which requires O(n) space.

**Key Insight**
The key insight is that we can store node values in a dictionary and then iterate over the first half of the nodes to calculate twin sums, which allows us to avoid traversing the linked list multiple times. This approach takes advantage of the fact that the linked list has an even length, making it possible to find the twin of each node in constant time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 69 ms (Beats 43.5%) |
| 💾 Memory | 44.4 MB (Beats 92.6%) |
| 📅 Solved | 2026-06-14 |
| 💻 Language | Python |