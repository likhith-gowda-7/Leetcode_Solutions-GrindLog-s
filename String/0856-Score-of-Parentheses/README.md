# 856. Score of Parentheses


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/score-of-parentheses/)


## 📝 Problem Description

Given a balanced parentheses string `s`, return *the **score** of the string*.

The **score** of a balanced parentheses string is based on the following rule:

	- `"()"` has score `1`.

	- `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.

	- `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

 

Example 1:**

```

**Input:** s = "()"
**Output:** 1

```

Example 2:**

```

**Input:** s = "(())"
**Output:** 2

```

Example 3:**

```

**Input:** s = "()()"
**Output:** 2

```

 

**Constraints:**

	- `2 <= s.length <= 50`

	- `s` consists of only `'('` and `')'`.

	- `s` is a balanced parentheses string.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the score of the parentheses string. When encountering a closing parenthesis, it calculates the score of the substring enclosed by the current opening and closing parentheses, and updates the score of the previous substring accordingly.

**Approach**
1. Initialize a stack with a single element, `0`, to represent the initial score.
2. Iterate through the input string `s`.
3. If the current character is an opening parenthesis `(`, push `0` onto the stack to represent the score of the new substring.
4. If the current character is a closing parenthesis `)`, pop the top element from the stack, which represents the score of the substring enclosed by the current opening and closing parentheses.
5. Calculate the score of the substring enclosed by the current opening and closing parentheses using `max(1, 2 * top)`, where `top` is the score of the substring.
6. Update the score of the previous substring by adding the calculated score to the second last element in the stack.
7. After iterating through the entire string, the final score is the only element left in the stack.

**Time Complexity**
O(n), where n is the length of the input string `s`. This is because we iterate through the string once.

**Space Complexity**
O(n), where n is the length of the input string `s`. This is because in the worst case, the stack will store all characters in the string.

**Key Insight**
The key insight is to use the stack to keep track of the score of the substrings enclosed by the parentheses, and update the score of the previous substring accordingly. This allows us to calculate the score of the entire string in a single pass through the input string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-02-19 |
| 💻 Language | Python |