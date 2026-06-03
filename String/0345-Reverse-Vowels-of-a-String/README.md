> 📌 **Cross-listed:** Primary location is [Two Pointers/0345-Reverse-Vowels-of-a-String](../../Two-Pointers/0345-Reverse-Vowels-of-a-String). This problem also appears under: **Two Pointers**, **String**

# 345. Reverse Vowels of a String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)


## 📝 Problem Description

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

Example 1:**

**Input:** s = "IceCreAm"

**Output:** "AceCreIm"

**Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

Example 2:**

**Input:** s = "leetcode"

**Output:** "leotcede"

 

**Constraints:**

	- `1 <= s.length <= 3 * 10^5`

	- `s` consist of **printable ASCII** characters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer approach to reverse the vowels in the string. It maintains two pointers, one at the start and one at the end of the string, and swaps the vowels found at these positions until the pointers meet.

**Approach**
1. Convert the input string to a list of characters to enable in-place modification.
2. Initialize two pointers, `i` and `j`, to the start and end of the list, respectively.
3. Enter a loop that continues until `i` is less than or equal to `j`.
4. Inside the loop, check if the character at position `j` is a vowel. If not, decrement `j` to move the pointer to the left.
5. If the character at position `i` is not a vowel, increment `i` to move the pointer to the right.
6. If both characters at positions `i` and `j` are vowels, swap them and increment `i` and decrement `j`.
7. Repeat steps 4-6 until `i` is greater than `j`.
8. Join the modified list of characters back into a string and return it.

**Time Complexity**
O(n), where n is the length of the string. This is because each character in the string is visited at most twice: once by the left pointer and once by the right pointer.

**Space Complexity**
O(n), where n is the length of the string. This is because we convert the string to a list of characters, which requires additional space proportional to the length of the string.

**Key Insight**
The key insight is that we only need to swap vowels, and we can do this efficiently by maintaining two pointers that move towards each other. This approach avoids the need to reverse the entire string or use additional data structures, making it a simple and efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 10 ms (Beats 57.24%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2024-12-06 |
| 💻 Language | Python |