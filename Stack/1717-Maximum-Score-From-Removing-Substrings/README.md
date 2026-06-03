> 📌 **Cross-listed:** Primary location is [String/1717-Maximum-Score-From-Removing-Substrings](../../String/1717-Maximum-Score-From-Removing-Substrings). This problem also appears under: **String**, **Stack**, **Greedy**

# 1717. Maximum Score From Removing Substrings


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-score-from-removing-substrings/)


## 📝 Problem Description

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

	- Remove substring `"ab"` and gain `x` points.

	
		- For example, when removing `"ab"` from `"cabxbae"` it becomes `"cxbae"`.

	
	

	- Remove substring `"ba"` and gain `y` points.
	
		- For example, when removing `"ba"` from `"cabxbae"` it becomes `"cabxe"`.

	
	

Return *the maximum points you can gain after applying the above operations on* `s`.

 

Example 1:**

```

**Input:** s = "cdbcbbaaabab", x = 4, y = 5
**Output:** 19
**Explanation:**
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
```

Example 2:**

```

**Input:** s = "aabbaaxybbaabb", x = 5, y = 4
**Output:** 20

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `1 <= x, y <= 10^4`

	- `s` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to maximize the points gained by removing substrings "ab" and "ba" from the given string. The key insight is to identify the optimal order in which to remove these substrings to achieve the maximum score.

**Approach**
1. Define a helper function `remove` that takes an array of characters, two characters to remove (`c1` and `c2`), and the points to gain (`points`).
2. Initialize an empty stack to keep track of the characters.
3. Iterate through the array of characters. If the current character matches `c1` and the top of the stack matches `c2`, pop the top character from the stack and increment the count by `points`.
4. Otherwise, push the current character onto the stack.
5. Return the modified stack.
6. Determine the optimal order of removal by comparing the values of `x` and `y`. If `x` is greater, set `find` to ["b", "a", x, y]. Otherwise, set `find` to ["a", "b", y, x].
7. Call the `remove` function with the original string, the first and second characters of `find`, and the second and third elements of `find`.
8. Return the total count of points gained.

**Time Complexity**
O(n), where n is the length of the string. The `remove` function iterates through the string once, and the main function calls `remove` twice.

**Space Complexity**
O(n), where n is the length of the string. In the worst case, the stack will store all characters from the string.

**Key Insight**
The key to this solution is to identify the optimal order of removal by comparing the values of `x` and `y`. By always removing the substring with the higher point value first, we can maximize the points gained.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 150 ms (Beats 91.59%) |
| 💾 Memory | 19.8 MB (Beats 100%) |
| 📅 Solved | 2025-07-23 |
| 💻 Language | Python |