# 138. Copy List with Random Pointer


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/)


## 📝 Problem Description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return *the head of the copied linked list*.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

	- `val`: an integer representing `Node.val`

	- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/12/18/e1.png)
```

**Input:** head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
**Output:** [[7,null],[13,0],[11,4],[10,2],[1,0]]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2019/12/18/e2.png)
```

**Input:** head = [[1,1],[2,1]]
**Output:** [[1,1],[2,1]]

```

Example 3:**

**![](https://assets.leetcode.com/uploads/2019/12/18/e3.png)**

```

**Input:** head = [[3,null],[3,0],[3,null]]
**Output:** [[3,null],[3,0],[3,null]]

```

 

**Constraints:**

	- `0 <= n <= 1000`

	- `-10^4 <= Node.val <= 10^4`

	- `Node.random` is `null` or is pointing to some node in the linked list.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to store the mapping between original nodes and their corresponding copied nodes. This allows us to efficiently update the `next` and `random` pointers of the copied nodes.

**Approach**
1. Initialize an empty hash table `copy_of_node` to store the mapping between original nodes and their copied nodes.
2. Traverse the original linked list, creating a new node for each original node and storing the mapping in the hash table.
3. Traverse the original linked list again, updating the `next` and `random` pointers of the copied nodes using the mappings in the hash table.
4. Return the copied head node from the hash table.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. We make two passes through the linked list, each taking O(n) time.

**Space Complexity**
O(n), where n is the number of nodes in the linked list. We need to store the mapping between original nodes and their copied nodes in the hash table, which requires O(n) space.

**Key Insight**
The key insight is to use a hash table to store the mapping between original nodes and their copied nodes, allowing us to efficiently update the `next` and `random` pointers of the copied nodes. This approach avoids the need to recursively traverse the linked list, making it more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 39 ms (Beats 94.49%) |
| 💾 Memory | 18.5 MB (Beats 100%) |
| 📅 Solved | 2025-04-17 |
| 💻 Language | Python |