# 1047. Remove All Adjacent Duplicates In String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)


## 📝 Problem Description

You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.

We repeatedly make **duplicate removals** on `s` until we no longer can.

Return *the final string after all such duplicate removals have been made*. It can be proven that the answer is **unique**.

 

Example 1:**

```

**Input:** s = "abbaca"
**Output:** "ca"
**Explanation:** 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

```

Example 2:**

```

**Input:** s = "azxxzy"
**Output:** "ay"

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a stack data structure to efficiently remove adjacent duplicate characters from the input string. By continuously popping characters from the stack when a duplicate is found, we effectively eliminate consecutive duplicates.

**Approach**
1. Initialize a stack with the first character of the input string.
2. Iterate through the input string starting from the second character.
3. For each character, check if the top of the stack matches the current character.
   - If a match is found, pop the top character from the stack (remove the duplicate).
   - If no match is found, push the current character onto the stack.
4. After iterating through the entire string, the stack will contain the final string with all adjacent duplicates removed.
5. Join the characters in the stack into a single string and return it.

**Time Complexity**
O(n), where n is the length of the input string. This is because we make a single pass through the string, performing constant-time operations for each character.

**Space Complexity**
O(n), where n is the length of the input string. In the worst case, the stack will store all characters from the input string.

**Key Insight**
The key to this solution is recognizing that a stack is an ideal data structure for this problem, as it allows us to efficiently remove characters from the end of the string (i.e., the top of the stack) when a duplicate is found. This approach ensures that we process the input string in a single pass, resulting in a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 16 ms (Beats 87.22%) |
| 💾 Memory | 19 MB (Beats 100%) |
| 📅 Solved | 2025-01-25 |
| 💻 Language | Python |