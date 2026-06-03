# 151. Reverse Words in a String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/)


## 📝 Problem Description

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space.*

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:**

```

**Input:** s = "the sky is blue"
**Output:** "blue is sky the"

```

Example 2:**

```

**Input:** s = "  hello world  "
**Output:** "world hello"
**Explanation:** Your reversed string should not contain leading or trailing spaces.

```

Example 3:**

```

**Input:** s = "a good   example"
**Output:** "example good a"
**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

```

 

**Constraints:**

	- `1 <= s.length <= 10^4`

	- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.

	- There is **at least one** word in `s`.

 

Follow-up: **If the string data type is mutable in your language, can you solve it in-place** with O(1)` extra space?

## 🧠 Solution Explanation

**Intuition**
The solution works by first splitting the input string into a list of words, then reversing the list of words, and finally joining the reversed list back into a string with a single space between each word.

**Approach**
1. Split the input string `s` into a list of words using the `split()` method, which splits a string into a list where each word is a list item.
2. Reverse the list of words using slicing `words[::-1]`, which creates a new list that is the reverse of the original list.
3. Join the reversed list of words back into a string using the `join()` method, with a single space between each word.

**Time Complexity**
O(n), where n is the total number of characters in the input string. This is because the `split()` method iterates over the string once to split it into words, and the `join()` method iterates over the list of words once to join them back into a string.

**Space Complexity**
O(n), where n is the total number of characters in the input string. This is because we need to store the list of words, which can be up to n characters long.

**Key Insight**
The key insight here is that we can use the `split()` method to split the input string into a list of words, which makes it easy to reverse the list of words and then join them back into a string. This approach is concise and efficient, and it avoids the need to manually iterate over the input string to reverse the words.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2024-12-13 |
| 💻 Language | Python |