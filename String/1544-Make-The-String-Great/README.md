# 1544. Make The String Great


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/make-the-string-great/)


## 📝 Problem Description

Given a string `s` of lower and upper case English letters.

A good string is a string which doesn't have **two adjacent characters** `s[i]` and `s[i + 1]` where:

	- `0 <= i <= s.length - 2`

	- `s[i]` is a lower-case letter and `s[i + 1]` is the same letter but in upper-case or **vice-versa**.

To make the string good, you can choose **two adjacent** characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return *the string* after making it good. The answer is guaranteed to be unique under the given constraints.

**Notice** that an empty string is also good.

 

Example 1:**

```

**Input:** s = "leEeetcode"
**Output:** "leetcode"
**Explanation:** In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

```

Example 2:**

```

**Input:** s = "abBAcC"
**Output:** ""
**Explanation:** We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

```

Example 3:**

```

**Input:** s = "s"
**Output:** "s"

```

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` contains only lower and upper case English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the characters in the string. It iterates over the string in reverse order and checks if the current character is the same as the top of the stack but with a different case. If so, it pops the top of the stack, effectively removing the adjacent duplicate characters. This process continues until the stack is empty, at which point the string is good.

**Approach**
1. Check if the string is empty. If so, return it as it is already good.
2. Initialize an empty stack.
3. Iterate over the string in reverse order.
4. For each character, check if the stack is not empty and the top of the stack is not the same as the current character but with a different case.
5. If the condition in step 4 is met, pop the top of the stack.
6. Otherwise, push the current character onto the stack.
7. After iterating over the entire string, return the characters in the stack in the original order.

**Time Complexity**
O(n), where n is the length of the string. This is because we iterate over the string once in reverse order.

**Space Complexity**
O(n), where n is the length of the string. This is because in the worst case, we might need to push all characters onto the stack.

**Key Insight**
The key insight here is that we can remove adjacent duplicate characters by popping the top of the stack when we encounter a character that is the same as the top of the stack but with a different case. This allows us to effectively remove the duplicate characters without having to keep track of the entire string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-01-26 |
| 💻 Language | Python |