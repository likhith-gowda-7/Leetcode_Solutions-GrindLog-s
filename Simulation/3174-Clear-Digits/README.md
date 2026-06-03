> 📌 **Cross-listed:** Primary location is [String/3174-Clear-Digits](../../String/3174-Clear-Digits). This problem also appears under: **String**, **Stack**, **Simulation**

# 3174. Clear Digits


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/clear-digits/)


## 📝 Problem Description

You are given a string `s`.

Your task is to remove **all** digits by doing this operation repeatedly:

	- Delete the *first* digit and the **closest** **non-digit** character to its *left*.

Return the resulting string after removing all digits.

**Note** that the operation *cannot* be performed on a digit that does not have any non-digit character to its left.

 

Example 1:**

**Input:** s = "abc"

**Output:** "abc"

**Explanation:**

There is no digit in the string.

Example 2:**

**Input:** s = "cb34"

**Output:** ""

**Explanation:**

First, we apply the operation on `s[2]`, and `s` becomes `"c4"`.

Then we apply the operation on `s[1]`, and `s` becomes `""`.

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists only of lowercase English letters and digits.

	- The input is generated such that it is possible to delete all digits.

## 🧠 Solution Explanation

**Intuition**
The solution works by simulating the removal of digits from the string, maintaining a stack of non-digit characters. When a digit is encountered, the closest non-digit character to its left is removed from the stack, effectively removing it from the string.

**Approach**
1. Initialize an empty stack to store non-digit characters.
2. Iterate through the input string `s`.
3. If the current character is a non-digit (checked using `i.isalpha()`), push it onto the stack.
4. If the current character is a digit, pop the top element from the stack (which is the closest non-digit character to the left of the digit). This effectively removes the digit from the string.
5. After iterating through the entire string, the stack contains the remaining non-digit characters, which are then joined together to form the resulting string.

**Time Complexity**
O(n), where n is the length of the input string. This is because we are making a single pass through the string, performing a constant amount of work for each character.

**Space Complexity**
O(n), where n is the length of the input string. This is because in the worst case, we may need to store all non-digit characters in the stack.

**Key Insight**
The key insight is that we can simulate the removal of digits by maintaining a stack of non-digit characters, effectively "undoing" the removal of each digit by popping the corresponding non-digit character from the stack. This approach allows us to solve the problem in a single pass through the string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-10 |
| 💻 Language | Python |