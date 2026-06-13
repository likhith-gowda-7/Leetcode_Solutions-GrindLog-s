# 3838. Weighted Word Mapping


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/weighted-word-mapping/)


## 📝 Problem Description

You are given an array of strings `words`, where each string represents a word containing lowercase English letters.

You are also given an integer array `weights` of length 26, where `weights[i]` represents the weight of the `i^th` lowercase English letter.

The **weight** of a word is defined as the **sum** of the weights of its characters.

For each word, take its weight modulo 26 and map the result to a lowercase English letter using reverse alphabetical order (`0 -> 'z', 1 -> 'y', ..., 25 -> 'a'`).

Return a string formed by concatenating the mapped characters for all words in order.

 

Example 1:**

**Input:** words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

**Output:** "rij"

**Explanation:**

	- The weight of `"abcd"` is `5 + 3 + 12 + 14 = 34`. The result modulo 26 is `34 % 26 = 8`, which maps to `'r'`.

	- The weight of `"def"` is `14 + 1 + 2 = 17`. The result modulo 26 is `17 % 26 = 17`, which maps to `'i'`.

	- The weight of `"xyz"` is `7 + 7 + 2 = 16`. The result modulo 26 is `16 % 26 = 16`, which maps to `'j'`.

Thus, the string formed by concatenating the mapped characters is `"rij"`.

Example 2:**

**Input:** words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

**Output:** "yyy"

**Explanation:**

Each word has weight 1. The result modulo 26 is `1 % 26 = 1`, which maps to `'y'`.

Thus, the string formed by concatenating the mapped characters is `"yyy"`.

Example 3:**

**Input:** words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]

**Output:** "g"

**Explanation:​​​​​​​**

The weight of `"abcd"` is `7 + 5 + 3 + 4 = 19`. The result modulo 26 is `19 % 26 = 19`, which maps to `'g'`.

Thus, the string formed by concatenating the mapped characters is `"g"`.

 

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 10`

	- `weights.length == 26`

	- `1 <= weights[i] <= 100`

	- `words[i]` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over each word in the input array, calculating the weight of each character by looking up its corresponding index in the `weights` array, and then mapping the resulting sum modulo 26 to a lowercase English letter using reverse alphabetical order.

**Approach**
1. Initialize an empty string `ans` to store the final result.
2. Iterate over each word in the input array `words`.
3. For each word, initialize a variable `c` to store the weight of the word.
4. Iterate over each character `w` in the word.
5. Calculate the index `idx` of the character in the `weights` array by subtracting 97 from the ASCII value of the character (since 'a' has an ASCII value of 97).
6. Add the weight of the character to the total weight `c`.
7. After processing all characters in the word, map the weight `c` modulo 26 to a lowercase English letter using `chr((122-c%26))` and append it to the result string `ans`.
8. Return the final result string `ans`.

**Time Complexity**
O(n*m), where n is the number of words and m is the maximum length of a word. This is because we iterate over each word and each character in the word.

**Space Complexity**
O(n), where n is the number of words. This is because we store the final result string in a variable of size n.

**Key Insight**
The key insight is to use the ASCII value of the characters to look up their corresponding indices in the `weights` array, and then use the modulo operator to map the resulting sum to a lowercase English letter. This approach allows us to efficiently calculate the weight of each word and map it to a character.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 82.33%) |
| 💾 Memory | 19.5 MB (Beats 8.53%) |
| 📅 Solved | 2026-06-13 |
| 💻 Language | Python |