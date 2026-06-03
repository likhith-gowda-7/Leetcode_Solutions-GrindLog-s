# 966. Vowel Spellchecker


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/vowel-spellchecker/)


## 📝 Problem Description

Given a `wordlist`, we want to implement a spellchecker that converts a query word into a correct word.

For a given `query` word, the spell checker handles two categories of spelling mistakes:

	- Capitalization: If the query matches a word in the wordlist (**case-insensitive**), then the query word is returned with the same case as the case in the wordlist.

	
		- Example: `wordlist = ["yellow"]`, `query = "YellOw"`: `correct = "yellow"`

		- Example: `wordlist = ["Yellow"]`, `query = "yellow"`: `correct = "Yellow"`

		- Example: `wordlist = ["yellow"]`, `query = "yellow"`: `correct = "yellow"`

	
	

	- Vowel Errors: If after replacing the vowels `('a', 'e', 'i', 'o', 'u')` of the query word with any vowel individually, it matches a word in the wordlist (**case-insensitive**), then the query word is returned with the same case as the match in the wordlist.
	
		- Example: `wordlist = ["YellOw"]`, `query = "yollow"`: `correct = "YellOw"`

		- Example: `wordlist = ["YellOw"]`, `query = "yeellow"`: `correct = ""` (no match)

		- Example: `wordlist = ["YellOw"]`, `query = "yllw"`: `correct = ""` (no match)

	
	

In addition, the spell checker operates under the following precedence rules:

	- When the query exactly matches a word in the wordlist (**case-sensitive**), you should return the same word back.

	- When the query matches a word up to capitalization, you should return the first such match in the wordlist.

	- When the query matches a word up to vowel errors, you should return the first such match in the wordlist.

	- If the query has no matches in the wordlist, you should return the empty string.

Given some `queries`, return a list of words `answer`, where `answer[i]` is the correct word for `query = queries[i]`.

 

Example 1:**

```
**Input:** wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
**Output:** ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

```
Example 2:**

```
**Input:** wordlist = ["yellow"], queries = ["YellOw"]
**Output:** ["yellow"]

```

 

**Constraints:**

	- `1 <= wordlist.length, queries.length <= 5000`

	- `1 <= wordlist[i].length, queries[i].length <= 7`

	- `wordlist[i]` and `queries[i]` consist only of only English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of two hash maps to store the wordlist: one for exact word matches and another for case-insensitive and vowel-replaced word matches. This approach allows for efficient lookups and handling of both capitalization and vowel errors.

**Approach**
1. Initialize two hash maps: `exact_word` to store the wordlist for exact matches and `case_map` to store case-insensitive and vowel-replaced word matches.
2. Iterate through the wordlist, adding each word to `exact_word` and checking if its lowercase version is already in `case_map`. If not, add the word to `case_map` with its original case.
3. For each word in the wordlist, replace its vowels with '*' and add the result to `case_map` if it's not already present.
4. Iterate through the queries, replacing vowels in each query word and checking if it matches a word in `exact_word` or `case_map`. Return the original query word if it's an exact match, the word from `case_map` if it's a case-insensitive match, or the word from `case_map` if it's a vowel-replaced match.

**Time Complexity**
O(n + m), where n is the number of queries and m is the number of words in the wordlist. This is because we iterate through the wordlist once to populate the hash maps and then iterate through the queries once to find the matches.

**Space Complexity**
O(n + m), where n is the number of queries and m is the number of words in the wordlist. This is because we store the wordlist in two hash maps, each with a size of O(m), and the results in an array of size O(n).

**Key Insight**
The key to this solution is the use of two hash maps to store the wordlist, allowing for efficient lookups and handling of both capitalization and vowel errors. By replacing vowels with '*' and storing the result in a separate hash map, we can efficiently handle vowel errors.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 47 ms (Beats 40.15%) |
| 💾 Memory | 20.2 MB (Beats 100%) |
| 📅 Solved | 2025-09-14 |
| 💻 Language | Python |