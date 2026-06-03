# 676. Implement Magic Dictionary


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/implement-magic-dictionary/)


## 📝 Problem Description

Design a data structure that is initialized with a list of **different** words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the `MagicDictionary` class:

	- `MagicDictionary()` Initializes the object.

	- `void buildDict(String[] dictionary)` Sets the data structure with an array of distinct strings `dictionary`.

	- `bool search(String searchWord)` Returns `true` if you can change **exactly one character** in `searchWord` to match any string in the data structure, otherwise returns `false`.

 

Example 1:**

```

**Input**
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
**Output**
[null, null, false, true, false, false]

**Explanation**
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False

```

 

**Constraints:**

	- `1 <= dictionary.length <= 100`

	- `1 <= dictionary[i].length <= 100`

	- `dictionary[i]` consists of only lower-case English letters.

	- All the strings in `dictionary` are **distinct**.

	- `1 <= searchWord.length <= 100`

	- `searchWord` consists of only lower-case English letters.

	- `buildDict` will be called only once before `search`.

	- At most `100` calls will be made to `search`.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a Trie data structure to efficiently store and query the dictionary words. The key insight is to use a Trie to store the words and then perform a depth-first search (DFS) to check if changing exactly one character in the search word matches any word in the Trie.

**Approach**
1. Initialize a Trie data structure with a root node.
2. In the `buildDict` method, iterate through each word in the dictionary and add it to the Trie using the `add` method.
3. In the `add` method, iterate through each character in the word and create a new node in the Trie if it doesn't exist.
4. In the `search` method, perform a DFS traversal of the Trie starting from the root node.
5. During the DFS, keep track of the current node and the current character index in the search word.
6. If the current character in the search word matches the current node's character, recursively call the DFS function with the next character index and the same `c` value (indicating no change).
7. If the current character in the search word does not match the current node's character, recursively call the DFS function with the next character index and `c=True` (indicating a possible change).
8. If the DFS traversal reaches the end of the search word and the current node is marked as the end of a word, return `True` if `c` is `False` (indicating no changes were made) or `True` if `c` is `True` (indicating one change was made).

**Time Complexity**
O(n \* m \* 26), where n is the length of the search word and m is the number of words in the dictionary. This is because in the worst case, we need to traverse the entire Trie for each word in the dictionary and for each character in the search word.

**Space Complexity**
O(n \* m), where n is the length of the search word and m is the number of words in the dictionary. This is because we need to store the Trie nodes for each word in the dictionary.

**Key Insight**
The key insight is to use a Trie to store the words and then perform a DFS to check if changing exactly one character in the search word matches any word in the Trie. This approach allows us to efficiently query the dictionary and check for possible changes in the search word.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 112 ms (Beats 40.44%) |
| 💾 Memory | 20.8 MB (Beats 59.75%) |
| 📅 Solved | 2025-06-23 |
| 💻 Language | Python |