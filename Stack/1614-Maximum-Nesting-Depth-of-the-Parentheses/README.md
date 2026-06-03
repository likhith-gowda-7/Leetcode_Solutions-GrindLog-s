> 📌 **Cross-listed:** Primary location is [String/1614-Maximum-Nesting-Depth-of-the-Parentheses](../../String/1614-Maximum-Nesting-Depth-of-the-Parentheses). This problem also appears under: **String**, **Stack**

# 1614. Maximum Nesting Depth of the Parentheses


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)


## 📝 Problem Description

Given a **valid parentheses string** `s`, return the **nesting depth** of* *`s`. The nesting depth is the **maximum** number of nested parentheses.

 

Example 1:**

**Input:** s = "(1+(2*3)+((8)/4))+1"

**Output:** 3

**Explanation:**

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:**

**Input:** s = "(1)+((2))+(((3)))"

**Output:** 3

**Explanation:**

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:**

**Input:** s = "()(())((()()))"

**Output:** 3

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.

	- It is guaranteed that parentheses expression `s` is a VPS.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the opening parentheses encountered so far. The maximum depth is updated whenever a closing parenthesis is encountered, which indicates that the current stack size represents the maximum nesting depth seen so far.

**Approach**
1. Initialize an empty stack and a variable `maxi` to keep track of the maximum depth.
2. Iterate over each character in the input string `s`.
3. If the character is an opening parenthesis `(`, push it onto the stack.
4. If the character is a closing parenthesis `)`, calculate the current depth by getting the length of the stack, update `maxi` if the current depth is greater, and pop the opening parenthesis from the stack.
5. After iterating over all characters, return the maximum depth `maxi`.

**Time Complexity**
O(n), where n is the length of the input string `s`. This is because we are iterating over each character in the string once.

**Space Complexity**
O(n), where n is the length of the input string `s`. In the worst case, the stack will store all opening parentheses, resulting in a space complexity of O(n).

**Key Insight**
The key insight is that the maximum depth is only updated when a closing parenthesis is encountered, which means that the stack size at that point represents the maximum nesting depth seen so far. This allows us to keep track of the maximum depth efficiently using a stack.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-02-02 |
| 💻 Language | Python |