> 📌 **Cross-listed:** Primary location is [String/0020-Valid-Parentheses](../../String/0020-Valid-Parentheses). This problem also appears under: **String**, **Stack**

# 20. Valid Parentheses


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/valid-parentheses/)


## 📝 Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

	- Open brackets must be closed by the same type of brackets.

	- Open brackets must be closed in the correct order.

	- Every close bracket has a corresponding open bracket of the same type.

 

Example 1:**

**Input:** s = "()"

**Output:** true

Example 2:**

**Input:** s = "()[]{}"

**Output:** true

Example 3:**

**Input:** s = "(]"

**Output:** false

Example 4:**

**Input:** s = "([])"

**Output:** true

Example 5:**

**Input:** s = "([)]"

**Output:** false

 

**Constraints:**

	- `1 <= s.length <= 10^4`

	- `s` consists of parentheses only `'()[]{}'`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack data structure to keep track of the opening brackets encountered so far. When a closing bracket is encountered, it checks if the top of the stack contains the corresponding opening bracket. If it does, the opening bracket is popped from the stack. If not, the function returns False. After iterating through the entire string, the function returns True if the stack is empty (i.e., all opening brackets were properly closed) and False otherwise.

**Approach**
1. Initialize an empty stack to store the opening brackets.
2. Define a dictionary `close` that maps closing brackets to their corresponding opening brackets.
3. Iterate through each character `bracket` in the input string `s`.
4. If `bracket` is a closing bracket (i.e., it's in the `close` dictionary), check if the stack is not empty and its top element is the corresponding opening bracket.
5. If the top element matches, pop it from the stack. Otherwise, return False.
6. If `bracket` is an opening bracket, push it onto the stack.
7. After iterating through the entire string, return True if the stack is empty and False otherwise.

**Time Complexity**
O(n), where n is the length of the input string `s`. This is because we're iterating through the string once.

**Space Complexity**
O(n), where n is the length of the input string `s`. In the worst case, the stack will store all opening brackets encountered in the string.

**Key Insight**
The key insight is that a stack is the perfect data structure to keep track of the opening brackets because it allows us to easily check if the top element matches the current closing bracket and pop it from the stack when a matching closing bracket is encountered. This approach ensures that we can efficiently determine if the input string is valid.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-11-06 |
| 💻 Language | Python |