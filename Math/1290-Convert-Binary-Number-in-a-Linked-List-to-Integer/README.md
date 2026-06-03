> 📌 **Cross-listed:** Primary location is [Linked List/1290-Convert-Binary-Number-in-a-Linked-List-to-Integer](../../Linked-List/1290-Convert-Binary-Number-in-a-Linked-List-to-Integer). This problem also appears under: **Linked List**, **Math**

# 1290. Convert Binary Number in a Linked List to Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)


## 📝 Problem Description

Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either `0` or `1`. The linked list holds the binary representation of a number.

Return the *decimal value* of the number in the linked list.

The **most significant bit** is at the head of the linked list.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/12/05/graph-1.png)
```

**Input:** head = [1,0,1]
**Output:** 5
**Explanation:** (101) in base 2 = (5) in base 10

```

Example 2:**

```

**Input:** head = [0]
**Output:** 0

```

 

**Constraints:**

	- The Linked List is not empty.

	- Number of nodes will not exceed `30`.

	- Each node's value is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution leverages bit manipulation to convert the binary number represented in the linked list to its decimal equivalent. The key insight is that each node's value (0 or 1) contributes to the decimal value based on its position in the binary representation.

**Approach**
1. Initialize a variable `res` to store the decimal value and a pointer `curr` to traverse the linked list.
2. While `curr` is not `None`, perform the following operations:
   1. Shift the bits of `res` to the left by one position using the left shift operator (`<< 1`).
   2. Use the bitwise OR operator (`|`) to set the least significant bit of `res` to the value of the current node (`curr.val`).
   3. Move the pointer `curr` to the next node in the linked list.
3. Return the decimal value `res` after traversing the entire linked list.

**Time Complexity**
O(n), where n is the number of nodes in the linked list. This is because we visit each node once to calculate the decimal value.

**Space Complexity**
O(1), as we only use a constant amount of space to store the `res` and `curr` variables, regardless of the input size.

**Key Insight**
The key to this solution is understanding how bit manipulation can be used to convert binary numbers to decimal values. By shifting the bits of `res` to the left and setting the least significant bit to the current node's value, we effectively build the decimal value from the binary representation. This approach is efficient and concise, making it a great example of how bit manipulation can simplify complex problems.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-07-14 |
| 💻 Language | Python |