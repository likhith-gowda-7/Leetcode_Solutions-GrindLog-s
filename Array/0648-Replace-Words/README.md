# 648. Replace Words


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/replace-words/)


## 📝 Problem Description

In English, we have a concept called **root**, which can be followed by some other word to form another longer word - let's call this word **derivative**. For example, when the **root** `"help"` is followed by the word `"ful"`, we can form a derivative `"helpful"`.

Given a `dictionary` consisting of many **roots** and a `sentence` consisting of words separated by spaces, replace all the derivatives in the sentence with the **root** forming it. If a derivative can be replaced by more than one **root**, replace it with the **root** that has **the shortest length**.

Return *the `sentence`* after the replacement.

 

Example 1:**

```

**Input:** dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
**Output:** "the cat was rat by the bat"

```

Example 2:**

```

**Input:** dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
**Output:** "a a b c"

```

 

**Constraints:**

	- `1 <= dictionary.length <= 1000`

	- `1 <= dictionary[i].length <= 100`

	- `dictionary[i]` consists of only lower-case letters.

	- `1 <= sentence.length <= 10^6`

	- `sentence` consists of only lower-case letters and spaces.

	- The number of words in `sentence` is in the range `[1, 1000]`

	- The length of each word in `sentence` is in the range `[1, 1000]`

	- Every two consecutive words in `sentence` will be separated by exactly one space.

	- `sentence` does not have leading or trailing spaces.

## 🧠 Solution Explanation

**Intuition**
The solution uses a Trie data structure to efficiently store and search for words in the dictionary. It then iterates over each word in the sentence, replacing it with its shortest root if it exists in the Trie.

**Approach**
1. Create a TrieNode class to represent each node in the Trie, with a dictionary to store child nodes and a boolean to mark the end of a word.
2. Create a Trie class with methods to add words to the Trie and search for words in the Trie.
3. Add each word in the dictionary to the Trie using the `add` method.
4. Split the sentence into individual words and iterate over each word.
5. For each word, use the `search` method to find its shortest root if it exists in the Trie.
6. Append the shortest root or the original word to the result list.
7. Join the result list into a string and return it.

**Time Complexity**
The time complexity is O(N + M * L), where N is the number of words in the sentence, M is the number of words in the dictionary, and L is the average length of a word. This is because we iterate over each word in the sentence (O(N)) and each word in the dictionary (O(M)) to add it to the Trie, and then iterate over each word in the sentence again (O(N)) to search for its shortest root.

**Space Complexity**
The space complexity is O(M * L), where M is the number of words in the dictionary and L is the average length of a word. This is because we store each word in the dictionary in the Trie, which requires O(L) space for each word.

**Key Insight**
The key insight is to use a Trie to efficiently store and search for words in the dictionary, allowing us to find the shortest root for each word in the sentence in linear time. This approach enables us to handle a large dictionary and sentence efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 35 ms (Beats 86.86%) |
| 💾 Memory | 34.1 MB (Beats 50.85%) |
| 📅 Solved | 2025-06-22 |
| 💻 Language | Python |