# 2696. Minimum String Length After Removing Substrings


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/)


## 📝 Problem Description

You are given a string `s` consisting only of **uppercase** English letters.

You can apply some operations to this string where, in one operation, you can remove **any** occurrence of one of the substrings `"AB"` or `"CD"` from `s`.

Return *the **minimum** possible length of the resulting string that you can obtain*.

**Note** that the string concatenates after removing the substring and could produce new `"AB"` or `"CD"` substrings.

 

Example 1:**

```

**Input:** s = "ABFCACDB"
**Output:** 2
**Explanation:** We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
```

Example 2:**

```

**Input:** s = "ACBBD"
**Output:** 5
**Explanation:** We cannot do any operations on the string so the length remains the same.

```

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists only of uppercase English letters.

## 🧠 Solution Explanation

**Intuition**
This solution works by simulating the removal of substrings "AB" and "CD" from the input string. It uses a stack to keep track of the characters that cannot be removed due to the presence of the other character. By iterating through the string in reverse order, it ensures that the removal of substrings is done in a way that minimizes the final string length.

**Approach**
1. Initialize an empty stack to store the characters that cannot be removed.
2. Define a dictionary `h` that maps each character to its corresponding character in the substring "AB" or "CD".
3. Iterate through the input string `s` in reverse order. For each character `i`:
   1. Check if the stack is not empty and the top of the stack is equal to the character that `i` maps to in the dictionary `h`.
   2. If the condition is true, pop the top character from the stack.
   3. Otherwise, push the character `i` onto the stack.
4. Return the length of the stack, which represents the minimum possible length of the resulting string.

**Time Complexity**
O(n), where n is the length of the input string. This is because we only iterate through the string once in reverse order.

**Space Complexity**
O(n), where n is the length of the input string. In the worst case, we might need to store all characters in the stack.

**Key Insight**
The key insight here is that by iterating through the string in reverse order and using a stack to keep track of the characters that cannot be removed, we can simulate the removal of substrings "AB" and "CD" in a way that minimizes the final string length. This approach takes advantage of the fact that the removal of substrings is done in a way that creates new substrings, which can be further removed.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-01-27 |
| 💻 Language | Python |