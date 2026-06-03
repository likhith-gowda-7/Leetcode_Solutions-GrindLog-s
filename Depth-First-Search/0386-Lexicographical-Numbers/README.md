# 386. Lexicographical Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lexicographical-numbers/)


## 📝 Problem Description

Given an integer `n`, return all the numbers in the range `[1, n]` sorted in lexicographical order.

You must write an algorithm that runs in `O(n)` time and uses `O(1)` extra space. 

 

Example 1:**

```
**Input:** n = 13
**Output:** [1,10,11,12,13,2,3,4,5,6,7,8,9]

```
Example 2:**

```
**Input:** n = 2
**Output:** [1,2]

```

 

**Constraints:**

	- `1 <= n <= 5 * 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a clever iterative approach to generate lexicographical numbers within the given range. It maintains a "current" number and iteratively appends it to the result list, then increments the current number to the next lexicographically smaller number. This process continues until all numbers in the range are covered.

**Approach**
1. Initialize the current number `curr` to 1 and an empty result list `res`.
2. Iterate `n` times to generate all numbers in the range.
3. In each iteration, append the current number to the result list.
4. Check if the next number (obtained by multiplying the current number by 10) is within the range. If it is, update the current number to this next number.
5. If the next number is not within the range, decrement the current number by 1 until it is less than the next number or its last digit is not 9. Then, increment the current number by 1.
6. Repeat steps 3-5 until all numbers in the range are covered.

**Time Complexity**
O(n) - The algorithm iterates `n` times to generate all numbers in the range, resulting in linear time complexity.

**Space Complexity**
O(1) - The algorithm uses a constant amount of extra space to store the current number and the result list, making the space complexity constant.

**Key Insight**
The key insight is to increment the current number to the next lexicographically smaller number by either multiplying it by 10 (if the next number is within the range) or decrementing it by 1 until it is less than the next number or its last digit is not 9. This approach allows the algorithm to generate all numbers in the range in lexicographical order with a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 97.54%) |
| 💾 Memory | 21.4 MB (Beats 99.87%) |
| 📅 Solved | 2025-06-09 |
| 💻 Language | Python |