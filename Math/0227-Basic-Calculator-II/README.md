# 227. Basic Calculator II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/basic-calculator-ii/)


## 📝 Problem Description

Given a string `s` which represents an expression, *evaluate this expression and return its value*. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

 

Example 1:**

```
**Input:** s = "3+2*2"
**Output:** 7

```
Example 2:**

```
**Input:** s = " 3/2 "
**Output:** 1

```
Example 3:**

```
**Input:** s = " 3+5 / 2 "
**Output:** 5

```

 

**Constraints:**

	- `1 <= s.length <= 3 * 10^5`

	- `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.

	- `s` represents **a valid expression**.

	- All the integers in the expression are non-negative integers in the range `[0, 2^31 - 1]`.

	- The answer is **guaranteed** to fit in a **32-bit integer**.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to evaluate the expression from left to right, maintaining a running total and handling the order of operations. It iterates through the string, parsing numbers and operators, and applies the correct operation at each step.

**Approach**
1. Initialize an empty stack and a variable `num` to store the current number being parsed.
2. Initialize a variable `sign` to store the current operator, defaulting to "+".
3. Append a "+" to the end of the input string to handle the last number.
4. Iterate through the string:
   - If the current character is a digit, multiply the current number by 10 and add the digit's value.
   - If the current character is an operator, apply the correct operation based on the current sign:
     - If the sign is "+", push the current number onto the stack.
     - If the sign is "-", push the negative of the current number onto the stack.
     - If the sign is "*", pop the top number from the stack, multiply it by the current number, and push the result.
     - If the sign is "/", pop the top number from the stack, divide it by the current number, and push the result.
   - Update the sign to the current operator and reset the current number to 0.
5. After iterating through the string, sum the numbers in the stack to get the final result.

**Time Complexity**
O(n), where n is the length of the input string. This is because we iterate through the string once, performing a constant amount of work for each character.

**Space Complexity**
O(n), where n is the length of the input string. This is because in the worst case, we might need to push all numbers onto the stack.

**Key Insight**
The key insight is that we can use a stack to evaluate the expression from left to right, handling the order of operations by applying the correct operation at each step. This approach avoids using any built-in function that evaluates strings as mathematical expressions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 82.9%) |
| 💾 Memory | 22 MB (Beats 80.67%) |
| 📅 Solved | 2025-01-28 |
| 💻 Language | Python |