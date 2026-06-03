# 208. Implement Trie (Prefix Tree)


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)


## 📝 Problem Description

A [**trie**](https://en.wikipedia.org/wiki/Trie) (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

	- `Trie()` Initializes the trie object.

	- `void insert(String word)` Inserts the string `word` into the trie.

	- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.

	- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

 

Example 1:**

```

**Input**
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
**Output**
[null, null, true, false, true, null, true]

**Explanation**
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

```

 

**Constraints:**

	- `1 <= word.length, prefix.length <= 2000`

	- `word` and `prefix` consist only of lowercase English letters.

	- At most `3 * 10^4` calls **in total** will be made to `insert`, `search`, and `startsWith`.

## 🧠 Solution Explanation

**Intuition**
A Trie is a tree-like data structure that efficiently stores and retrieves strings based on their prefixes. The key insight is to use a node to represent each character in the string, and to store the children of each node in a dictionary for efficient lookup.

**Approach**
1. Initialize the Trie with a root node.
2. In the `insert` method, iterate through each character in the word:
   - If the character is not in the current node's children, create a new node and add it to the children.
   - Move to the child node corresponding to the current character.
3. After iterating through all characters, mark the final node as the end of a word.
4. In the `search` method, iterate through each character in the word:
   - If the character is not in the current node's children, return False.
   - Move to the child node corresponding to the current character.
5. After iterating through all characters, return whether the final node is marked as the end of a word.
6. In the `startsWith` method, iterate through each character in the prefix:
   - If the character is not in the current node's children, return False.
   - Move to the child node corresponding to the current character.
7. After iterating through all characters, return True.

**Time Complexity**
- `insert`: O(m), where m is the length of the word, since we iterate through each character once.
- `search` and `startsWith`: O(m), where m is the length of the word or prefix, since we iterate through each character once.

**Space Complexity**
- O(n*m), where n is the number of words and m is the average length of a word, since we store each character in the Trie.

**Key Insight**
The key to this solution is to use a TrieNode to represent each character in the string, and to store the children of each node in a dictionary for efficient lookup. This allows us to efficiently insert, search, and check prefixes for strings in the Trie.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 46 ms (Beats 31.72%) |
| 💾 Memory | 32.2 MB (Beats 80.48%) |
| 📅 Solved | 2025-06-17 |
| 💻 Language | Python |