> 📌 **Cross-listed:** Primary location is [Hash Table/0126-Word-Ladder-II](../../Hash-Table/0126-Word-Ladder-II). This problem also appears under: **Hash Table**, **String**, **Backtracking**, **Breadth-First Search**

# 126. Word Ladder II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/word-ladder-ii/)


## 📝 Problem Description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:

	- Every adjacent pair of words differs by a single letter.

	- Every `s_i` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.

	- `s_k == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *all the **shortest transformation sequences** from* `beginWord` *to* `endWord`*, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words *`[beginWord, s_1, s_2, ..., s_k]`.

 

Example 1:**

```

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
**Output:** [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
**Explanation:** There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

```

Example 2:**

```

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
**Output:** []
**Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

```

 

**Constraints:**

	- `1 <= beginWord.length <= 5`

	- `endWord.length == beginWord.length`

	- `1 <= wordList.length <= 500`

	- `wordList[i].length == beginWord.length`

	- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.

	- `beginWord != endWord`

	- All the words in `wordList` are **unique**.

	- The **sum** of all shortest transformation sequences does not exceed `10^5`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of Breadth-First Search (BFS) and Backtracking to find all the shortest transformation sequences from the `beginWord` to the `endWord`. The BFS is used to find the shortest distance to reach the `endWord`, and then the Backtracking is used to find all the possible sequences with the same distance.

**Approach**
1. Use BFS to find the shortest distance to reach the `endWord`.
   - Initialize a queue with the `beginWord` and a set to keep track of visited words.
   - Perform BFS until the `endWord` is found or the queue is empty.
   - For each word in the queue, generate all possible words by changing one character at a time and add them to the queue if they are not visited before.
   - Keep track of the distance to each word using a dictionary.
2. Backtrack to find all the possible sequences with the same distance.
   - Start from the `endWord` and recursively generate all possible words by changing one character at a time.
   - If the generated word is the `beginWord`, add the sequence to the result list.
   - If the distance to the generated word is not the same as the shortest distance, stop exploring this branch.
   - Undo the changes made in the previous step to backtrack.

**Time Complexity**
The time complexity is O(N \* M^L), where N is the number of words in the word list, M is the size of the alphabet, and L is the length of the words. This is because for each word, we generate M^L possible words by changing one character at a time.

**Space Complexity**
The space complexity is O(N \* M^L), where N is the number of words in the word list, M is the size of the alphabet, and L is the length of the words. This is because we need to store all the possible words generated during the BFS and Backtracking.

**Key Insight**
The key insight is to use BFS to find the shortest distance to reach the `endWord` and then use Backtracking to find all the possible sequences with the same distance. This approach allows us to efficiently find all the shortest transformation sequences from the `beginWord` to the `endWord`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 39 ms (Beats 15.86%) |
| 💾 Memory | 18.2 MB (Beats 100%) |
| 📅 Solved | 2025-08-23 |
| 💻 Language | Python |