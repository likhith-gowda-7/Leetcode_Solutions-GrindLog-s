# 2434. Using a Robot to Print the Lexicographically Smallest String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/)


## 📝 Problem Description

You are given a string `s` and a robot that currently holds an empty string `t`. Apply one of the following operations until `s` and `t` **are both empty**:

	- Remove the **first** character of a string `s` and give it to the robot. The robot will append this character to the string `t`.

	- Remove the **last** character of a string `t` and give it to the robot. The robot will write this character on paper.

Return *the lexicographically smallest string that can be written on the paper.*

 

Example 1:**

```

**Input:** s = "zza"
**Output:** "azz"
**Explanation:** Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".

```

Example 2:**

```

**Input:** s = "bac"
**Output:** "abc"
**Explanation:** Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".

```

Example 3:**

```

**Input:** s = "bdda"
**Output:** "addb"
**Explanation:** Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of only English lowercase letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to build the lexicographically smallest string that can be written on the paper. It maintains a stack of characters that are greater than or equal to the minimum character in the string `s`. When the minimum character is encountered, it is appended to the result string and the characters in the stack that are less than or equal to the minimum character are popped and appended to the result string.

**Approach**
1. Initialize the minimum character `min_char` and its count `min_char_count` in the string `s`.
2. Initialize an empty result string `res` and an empty stack `t`.
3. Iterate over the characters in the string `s`.
4. If the current character is the minimum character, append it to the result string, decrement the count of the minimum character, and update the minimum character and its count if necessary.
5. If the count of the minimum character reaches 0, break the loop if the current index is the last index of the string.
6. If the current character is not the minimum character, push it onto the stack.
7. After the loop, append the remaining characters in the stack (in reverse order) to the result string.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we iterate over the string `s` once and perform constant-time operations for each character.

**Space Complexity**
O(n), where n is the length of the string `s`. This is because we use a stack to store characters that are greater than or equal to the minimum character.

**Key Insight**
The key insight is to maintain a stack of characters that are greater than or equal to the minimum character in the string `s`. By doing so, we can efficiently build the lexicographically smallest string that can be written on the paper. This approach allows us to avoid unnecessary comparisons and operations, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 108 ms (Beats 100%) |
| 💾 Memory | 20.9 MB (Beats 100%) |
| 📅 Solved | 2025-06-07 |
| 💻 Language | Python |