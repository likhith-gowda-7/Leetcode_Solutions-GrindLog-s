# 1021. Remove Outermost Parentheses


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-outermost-parentheses/)


## 📝 Problem Description

A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

	- For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `s` is primitive if it is nonempty, and there does not exist a way to split it into `s = A + B`, with `A` and `B` nonempty valid parentheses strings.

Given a valid parentheses string `s`, consider its primitive decomposition: `s = P_1 + P_2 + ... + P_k`, where `P_i` are primitive valid parentheses strings.

Return `s` *after removing the outermost parentheses of every primitive string in the primitive decomposition of *`s`.

 

Example 1:**

```

**Input:** s = "(()())(())"
**Output:** "()()()"
**Explanation:** 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

```

Example 2:**

```

**Input:** s = "(()())(())(()(()))"
**Output:** "()()()()(())"
**Explanation:** 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

```

Example 3:**

```

**Input:** s = "()()"
**Output:** ""
**Explanation:** 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is either `'('` or `')'`.

	- `s` is a valid parentheses string.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the input string and maintaining a counter to keep track of the balance of parentheses. When the counter is 0 and we encounter an opening parenthesis, we increment the counter and add the parenthesis to the result. When the counter is not 0 and we encounter a closing parenthesis, we decrement the counter and add the parenthesis to the result. This approach effectively removes the outermost parentheses of every primitive string in the primitive decomposition of the input string.

**Approach**
1. Initialize an empty string `ans` to store the result and a counter `cnt` to keep track of the balance of parentheses.
2. Iterate through the input string `s`.
3. If the counter is 0 and we encounter an opening parenthesis, increment the counter and add the parenthesis to the result.
4. If we encounter an opening parenthesis and the counter is not 0, increment the counter and add the parenthesis to the result.
5. If the counter is 1 and we encounter a closing parenthesis, decrement the counter.
6. If we encounter a closing parenthesis and the counter is not 1, decrement the counter and add the parenthesis to the result.
7. Return the result string.

**Time Complexity**
O(n), where n is the length of the input string. This is because we iterate through the input string once.

**Space Complexity**
O(n), where n is the length of the input string. This is because we store the result string in memory.

**Key Insight**
The key insight is to maintain a counter to keep track of the balance of parentheses. This allows us to effectively remove the outermost parentheses of every primitive string in the primitive decomposition of the input string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-01-27 |
| 💻 Language | Python |