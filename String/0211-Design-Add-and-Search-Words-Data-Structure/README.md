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

## 🧠 Solution Explanation

**Intuition**
The solution uses a Trie data structure to store the words, where each node represents a character in the word. The `addWord` method adds a word to the Trie by traversing the nodes based on the characters in the word. The `search` method uses a depth-first search (DFS) approach to check if a given word matches any word in the Trie. If the word contains a dot, the DFS function is called recursively for each child node.

**Approach**
1. Initialize the Trie with a root node.
2. In the `addWord` method:
   1. Start at the root node.
   2. For each character in the word, create a new node if it doesn't exist and move to that node.
   3. Mark the end of the word by setting `End_of_word` to `True`.
3. In the `search` method:
   1. Start at the root node.
   2. If the current character is a dot, recursively call DFS for each child node.
   3. If the current character is not a dot, move to the corresponding child node.
   4. Return `True` if the DFS function returns `True` or if the end of the word is reached.

**Time Complexity**
The time complexity of the `addWord` method is O(m), where m is the length of the word, since we traverse the nodes based on the characters in the word. The time complexity of the `search` method is O(n*m), where n is the number of words in the Trie and m is the length of the word being searched, since we recursively call DFS for each child node.

**Space Complexity**
The space complexity of the solution is O(n*m), where n is the number of words in the Trie and m is the maximum length of a word, since we store each word in the Trie.

**Key Insight**
The key insight is to use a Trie data structure to efficiently store and search words, and to use a depth-first search approach to handle words with dots. This allows us to take advantage of the Trie's ability to quickly locate words and to efficiently search for words that match a given pattern.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1139 ms (Beats 24.15%) |
| 💾 Memory | 65.7 MB (Beats 81.47%) |
| 📅 Solved | 2025-06-23 |
| 💻 Language | Python |