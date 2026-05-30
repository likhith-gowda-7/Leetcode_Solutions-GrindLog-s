# 211. Design Add and Search Words Data Structure


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/)


## 📝 Problem Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

	- `WordDictionary()` Initializes the object.

	- `void addWord(word)` Adds `word` to the data structure, it can be matched later.

	- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

 

Example:**

```

**Input**
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
**Output**
[null,null,null,null,false,true,true,true]

**Explanation**
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

```

 

**Constraints:**

	- `1 <= word.length <= 25`

	- `word` in `addWord` consists of lowercase English letters.

	- `word` in `search` consist of `'.'` or lowercase English letters.

	- There will be at most `2` dots in `word` for `search` queries.

	- At most `10^4` calls will be made to `addWord` and `search`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1139 ms (Beats 24.18%) |
| 💾 Memory | 65.7 MB (Beats 81.53%) |
| 📅 Solved | 2025-06-23 |
| 💻 Language | Python |