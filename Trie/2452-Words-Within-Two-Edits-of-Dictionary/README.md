> 📌 **Cross-listed:** Primary location is [Array/2452-Words-Within-Two-Edits-of-Dictionary](../../Array/2452-Words-Within-Two-Edits-of-Dictionary). This problem also appears under: **Array**, **String**, **Trie**

# 2452. Words Within Two Edits of Dictionary


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/words-within-two-edits-of-dictionary/)


## 📝 Problem Description

You are given two string arrays, `queries` and `dictionary`. All words in each array comprise of lowercase English letters and have the same length.

In one **edit** you can take a word from `queries`, and change any letter in it to any other letter. Find all words from `queries` that, after a **maximum** of two edits, equal some word from `dictionary`.

Return* a list of all words from *`queries`*, **that match with some word from *`dictionary`* after a maximum of **two edits***. Return the words in the **same order** they appear in `queries`.

 

Example 1:**

```

**Input:** queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
**Output:** ["word","note","wood"]
**Explanation:**
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].

```

Example 2:**

```

**Input:** queries = ["yes"], dictionary = ["not"]
**Output:** []
**Explanation:**
Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.

```

 

**Constraints:**

	- `1 <= queries.length, dictionary.length <= 100`

	- `n == queries[i].length == dictionary[j].length`

	- `1 <= n <= 100`

	- All `queries[i]` and `dictionary[j]` are composed of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution iterates through each query word and dictionary word, counting the number of differences between them. If the number of differences is less than 3, it adds the query word to the result list. This approach works because it checks all possible edits within two steps.

**Approach**
1. Initialize an empty result list `res`.
2. Iterate through each query word `q` in `queries`.
3. For each query word `q`, iterate through each dictionary word `word` in `dictionary`.
4. Initialize a difference counter `diff` to 0.
5. Iterate through each character in the dictionary word `word` and query word `q`.
6. If the characters at the current position are different, increment the difference counter `diff`.
7. If the difference counter `diff` is less than 3, add the query word `q` to the result list `res` and break the inner loop.
8. Return the result list `res`.

**Time Complexity**
O(n * m * len(word)), where n is the number of query words, m is the number of dictionary words, and len(word) is the length of each word. This is because we iterate through each query word, each dictionary word, and each character in each word.

**Space Complexity**
O(n), where n is the number of query words. This is because we store the result list of query words.

**Key Insight**
The key insight is that we only need to check if the difference between the query word and the dictionary word is less than 3, which allows us to avoid unnecessary comparisons and improve efficiency.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 91 ms (Beats 35.31%) |
| 💾 Memory | 19.4 MB (Beats 43.2%) |
| 📅 Solved | 2026-04-22 |
| 💻 Language | Python |