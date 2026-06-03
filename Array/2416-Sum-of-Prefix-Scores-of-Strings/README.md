# 2416. Sum of Prefix Scores of Strings


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Trie](https://img.shields.io/badge/Trie-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-of-prefix-scores-of-strings/)


## 📝 Problem Description

You are given an array `words` of size `n` consisting of **non-empty** strings.

We define the **score** of a string `term` as the **number** of strings `words[i]` such that `term` is a **prefix** of `words[i]`.

	- For example, if `words = ["a", "ab", "abc", "cab"]`, then the score of `"ab"` is `2`, since `"ab"` is a prefix of both `"ab"` and `"abc"`.

Return *an array *`answer`* of size *`n`* where *`answer[i]`* is the **sum** of scores of every **non-empty** prefix of *`words[i]`.

**Note** that a string is considered as a prefix of itself.

 

Example 1:**

```

**Input:** words = ["abc","ab","bc","b"]
**Output:** [5,4,3,2]
**Explanation:** The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.

```

Example 2:**

```

**Input:** words = ["abcd"]
**Output:** [4]
**Explanation:**
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.

```

 

**Constraints:**

	- `1 <= words.length <= 1000`

	- `1 <= words[i].length <= 1000`

	- `words[i]` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a Trie data structure to efficiently count the number of strings that have each prefix. By traversing the Trie, we can calculate the score of each prefix in linear time. The key insight is to use a Trie's ability to store a mapping of characters to child nodes, allowing us to count the number of strings with each prefix in a single pass.

**Approach**
1. Create a TrieNode class with a dictionary `map` to store child nodes and a `count` attribute to store the number of strings that pass through the node.
2. Create a Trie by initializing the root node and building the Trie for each word in the input array `words`.
3. Define a recursive function `get_score` to calculate the score of a prefix by traversing the Trie and summing the counts of nodes that correspond to the prefix characters.
4. For each word in `words`, call `get_score` to calculate the score of each prefix and append the result to the `res` array.

**Time Complexity**
O(n \* m \* l), where n is the number of words, m is the average number of characters in a word, and l is the maximum length of a word. This is because we build the Trie for each word, and then traverse the Trie for each word to calculate the score of each prefix.

**Space Complexity**
O(n \* m), where n is the number of words and m is the maximum length of a word. This is because we store the Trie for all words, and each node in the Trie has a constant amount of space.

**Key Insight**
The key insight is to use the Trie's ability to store a mapping of characters to child nodes, allowing us to count the number of strings with each prefix in a single pass. This is achieved by recursively traversing the Trie and summing the counts of nodes that correspond to the prefix characters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2334 ms (Beats 39.59%) |
| 💾 Memory | 307.9 MB (Beats 85.42%) |
| 📅 Solved | 2025-06-25 |
| 💻 Language | Python |