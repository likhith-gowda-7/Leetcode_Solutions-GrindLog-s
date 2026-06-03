> 📌 **Cross-listed:** Primary location is [Array/0150-Evaluate-Reverse-Polish-Notation](../../Array/0150-Evaluate-Reverse-Polish-Notation). This problem also appears under: **Array**, **Math**, **Stack**

# 150. Evaluate Reverse Polish Notation


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)


## 📝 Problem Description

You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note** that:

	- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.

	- Each operand may be an integer or another expression.

	- The division between two integers always **truncates toward zero**.

	- There will not be any division by zero.

	- The input represents a valid arithmetic expression in a reverse polish notation.

	- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

 

Example 1:**

```

**Input:** tokens = ["2","1","+","3","*"]
**Output:** 9
**Explanation:** ((2 + 1) * 3) = 9

```

Example 2:**

```

**Input:** tokens = ["4","13","5","/","+"]
**Output:** 6
**Explanation:** (4 + (13 / 5)) = 6

```

Example 3:**

```

**Input:** tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
**Output:** 22
**Explanation:** ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

```

 

**Constraints:**

	- `1 <= tokens.length <= 10^4`

	- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing a stack to store operands and then popping them off to perform operations when an operator is encountered. This approach takes advantage of the properties of Reverse Polish Notation, where operators follow their operands. By using a stack, we can efficiently evaluate the expression from left to right.

## Approach
1. Initialize an empty stack to store operands.
2. Iterate through each token in the input array.
3. If the token is an operand (not an operator), convert it to an integer and push it onto the stack.
4. If the token is an operator, pop the top two operands off the stack, perform the operation, and push the result back onto the stack.
5. After iterating through all tokens, the final result will be the only element left on the stack.

## Time Complexity
The time complexity is O(n), where n is the number of tokens in the input array. This is because we make a single pass through the input array, performing a constant amount of work for each token.

## Space Complexity
The space complexity is O(n), where n is the number of tokens in the input array. In the worst case, we may need to store all tokens on the stack (e.g., if the input array consists only of operands).

## Key Insight
The key insight is recognizing that Reverse Polish Notation allows us to evaluate expressions using a stack, where operators follow their operands. This enables us to process the expression from left to right, making it efficient to evaluate the expression using a single pass through the input array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 57.46%) |
| 💾 Memory | 19.1 MB (Beats 100%) |
| 📅 Solved | 2025-11-14 |
| 💻 Language | Python |