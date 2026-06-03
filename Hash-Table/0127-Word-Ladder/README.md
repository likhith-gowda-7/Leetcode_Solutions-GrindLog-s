# 127. Word Ladder


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/word-ladder/)


## 📝 Problem Description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:

	- Every adjacent pair of words differs by a single letter.

	- Every `s_i` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.

	- `s_k == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *the **number of words** in the **shortest transformation sequence** from* `beginWord` *to* `endWord`*, or *`0`* if no such sequence exists.*

 

Example 1:**

```

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
**Output:** 5
**Explanation:** One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

```

Example 2:**

```

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
**Output:** 0
**Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

```

 

**Constraints:**

	- `1 <= beginWord.length <= 10`

	- `endWord.length == beginWord.length`

	- `1 <= wordList.length <= 5000`

	- `wordList[i].length == beginWord.length`

	- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.

	- `beginWord != endWord`

	- All the words in `wordList` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution uses a Breadth-First Search (BFS) approach to find the shortest transformation sequence from the `beginWord` to the `endWord`. It leverages a queue to keep track of the words to be processed and a set to keep track of the visited words. The key insight is to generate all possible one-letter changes for each word and check if the resulting word exists in the `wordList`.

**Approach**
1. Create a set `word_map` from the `wordList` for efficient lookups.
2. Check if the `endWord` and `beginWord` exist in the `word_map`. If not, return 0.
3. Initialize a queue `q` with the `endWord` and a set `seen` with the `endWord`.
4. Initialize the `shortest_sequence` to 1.
5. While the queue is not empty:
   1. Dequeue all words from the queue and process them.
   2. For each word, generate all possible one-letter changes by iterating over each character and replacing it with every alphabet letter.
   3. Check if the resulting word exists in the `word_map` and has not been visited before.
   4. If the resulting word is the `beginWord`, return the `shortest_sequence`.
   5. Add the resulting word to the queue and mark it as visited.
6. Increment the `shortest_sequence` after each iteration.
7. If the queue becomes empty without finding the `beginWord`, return 0.

**Time Complexity**
O(n \* m \* 26), where n is the number of words in the `wordList` and m is the average length of a word. This is because for each word, we generate m \* 26 possible one-letter changes, and we do this for n words.

**Space Complexity**
O(n + m), where n is the number of words in the `wordList` and m is the average length of a word. This is because we need to store the `word_map`, `seen` set, and the queue, which can grow up to n + m in the worst case.

**Key Insight**
The key insight is to generate all possible one-letter changes for each word and check if the resulting word exists in the `wordList`. This allows us to efficiently explore all possible transformation sequences and find the shortest one.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 251 ms (Beats 57.5%) |
| 💾 Memory | 18.8 MB (Beats 100%) |
| 📅 Solved | 2025-08-21 |
| 💻 Language | Python |