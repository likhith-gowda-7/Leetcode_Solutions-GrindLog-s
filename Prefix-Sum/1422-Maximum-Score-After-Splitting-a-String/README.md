> 📌 **Cross-listed:** Primary location is [String/1422-Maximum-Score-After-Splitting-a-String](../../String/1422-Maximum-Score-After-Splitting-a-String). This problem also appears under: **String**, **Prefix Sum**

# 1422. Maximum Score After Splitting a String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-score-after-splitting-a-string/)


## 📝 Problem Description

Given a string `s` of zeros and ones, *return the maximum score after splitting the string into two **non-empty** substrings* (i.e. **left** substring and **right** substring).

The score after splitting a string is the number of **zeros** in the **left** substring plus the number of **ones** in the **right** substring.

 

Example 1:**

```

**Input:** s = "011101"
**Output:** 5 
**Explanation:** 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

```

Example 2:**

```

**Input:** s = "00111"
**Output:** 5
**Explanation:** When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

```

Example 3:**

```

**Input:** s = "1111"
**Output:** 3

```

 

**Constraints:**

	- `2 <= s.length <= 500`

	- The string `s` consists of characters `'0'` and `'1'` only.

## 🧠 Solution Explanation

**Intuition**
The approach is based on the observation that the maximum score is achieved when the number of zeros in the left substring is maximized and the number of ones in the right substring is maximized. This can be achieved by maintaining a running count of zeros and ones in the string as we iterate through it.

**Approach**
1. Initialize two variables `left` and `right` to keep track of the number of zeros in the left substring and the number of ones in the right substring, respectively.
2. Initialize `maxi` to store the maximum score found so far.
3. Iterate through the string from the second character to the second last character (inclusive).
4. For each character, if it's a zero, increment `left` by 1; otherwise, decrement `right` by 1.
5. Update `maxi` if the sum of `left` and `right` is greater than the current maximum score.
6. Return `maxi` as the maximum score.

**Time Complexity**
O(n), where n is the length of the string. This is because we only need to iterate through the string once to find the maximum score.

**Space Complexity**
O(1), since we only use a constant amount of space to store the variables `left`, `right`, and `maxi`.

**Key Insight**
The key insight is that we can maintain a running count of zeros and ones in the string as we iterate through it, which allows us to efficiently find the maximum score. This approach avoids the need to consider all possible splits of the string, making it more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.3 MB (Beats 100%) |
| 📅 Solved | 2024-12-13 |
| 💻 Language | Python |