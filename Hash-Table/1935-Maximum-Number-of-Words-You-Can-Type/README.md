# 1935. Maximum Number of Words You Can Type


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)


## 📝 Problem Description

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string `text` of words separated by a single space (no leading or trailing spaces) and a string `brokenLetters` of all **distinct** letter keys that are broken, return *the **number of words** in* `text` *you can fully type using this keyboard*.

 

Example 1:**

```

**Input:** text = "hello world", brokenLetters = "ad"
**Output:** 1
**Explanation:** We cannot type "world" because the 'd' key is broken.

```

Example 2:**

```

**Input:** text = "leet code", brokenLetters = "lt"
**Output:** 1
**Explanation:** We cannot type "leet" because the 'l' and 't' keys are broken.

```

Example 3:**

```

**Input:** text = "leet code", brokenLetters = "e"
**Output:** 0
**Explanation:** We cannot type either word because the 'e' key is broken.

```

 

**Constraints:**

	- `1 <= text.length <= 10^4`

	- `0 <= brokenLetters.length <= 26`

	- `text` consists of words separated by a single space without any leading or trailing spaces.

	- Each word only consists of lowercase English letters.

	- `brokenLetters` consists of **distinct** lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating through each word in the given text and checking if any of the broken letter keys are present in the word. If a word contains any broken keys, it cannot be typed, and we increment the count of words that can be typed.

**Approach**
1. Split the input text into individual words using the `split()` method.
2. Initialize a counter `res` to keep track of the number of words that can be typed.
3. Iterate through each word in the list of words.
4. For each word, check if any of the broken letter keys are present in the word by iterating through each broken letter key.
5. If a broken letter key is found in the word, set a flag `invalid` to `True` and break out of the inner loop.
6. If the word does not contain any broken letter keys (i.e., `invalid` is still `False`), increment the `res` counter.
7. Return the total count of words that can be typed.

**Time Complexity**
O(n*m), where n is the number of words in the text and m is the maximum length of a word. This is because we are iterating through each word and each character in the word.

**Space Complexity**
O(n), where n is the number of words in the text. This is because we are storing the list of words in memory.

**Key Insight**
The key insight here is that we only need to check if a word contains any of the broken letter keys, and we can do this by iterating through each word and each broken letter key. This approach allows us to efficiently determine which words can be typed given the broken keyboard.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-09-15 |
| 💻 Language | Python |