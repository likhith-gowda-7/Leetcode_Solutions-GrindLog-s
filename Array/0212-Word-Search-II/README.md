# 212. Word Search II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/word-search-ii/)


## 📝 Problem Description

Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)
```

**Input:** board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
**Output:** ["eat","oath"]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)
```

**Input:** board = [["a","b"],["c","d"]], words = ["abcb"]
**Output:** []

```

 

**Constraints:**

	- `m == board.length`

	- `n == board[i].length`

	- `1 <= m, n <= 12`

	- `board[i][j]` is a lowercase English letter.

	- `1 <= words.length <= 3 * 10^4`

	- `1 <= words[i].length <= 10`

	- `words[i]` consists of lowercase English letters.

	- All the strings of `words` are unique.

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing a Trie data structure to efficiently store and search for words in the given list. This approach allows for fast lookup and exploration of possible word paths on the board. By combining the Trie with a backtracking algorithm, the solution can effectively explore all possible word paths and find the words that exist on the board.

## Approach
1. Create a TrieNode class to represent each node in the Trie, containing a dictionary to store child nodes and a boolean to mark the end of a word.
2. Build the Trie by iterating through each word in the given list and adding it to the Trie.
3. Define a backtracking function to explore the board and find words.
4. Iterate through each cell on the board and use the backtracking function to explore all possible word paths starting from that cell.
5. In the backtracking function, check if the current cell is out of bounds or if the current character is not in the Trie, and return if so.
6. If the current character is in the Trie, move to the corresponding child node and check if it marks the end of a word. If so, add the word to the result list and mark the node as visited to avoid duplicates.

## Time Complexity
The time complexity is O(N * M * 4^L * W), where N is the number of rows, M is the number of columns, L is the maximum length of a word, and W is the number of words. This is because in the worst case, the backtracking function explores all four directions for each cell, and for each word, it explores up to L levels deep in the Trie.

## Space Complexity
The space complexity is O(N * M + W * L), where N is the number of rows, M is the number of columns, W is the number of words, and L is the maximum length of a word. This is because the solution uses a Trie to store all words, which requires O(W * L) space, and a 2D array to store the board, which requires O(N * M) space.

## Key Insight
The key insight is to use a Trie to store the words and combine it with a backtracking algorithm to efficiently explore all possible word paths on the board. This approach allows for fast lookup and exploration of possible word paths, making it possible to solve the problem efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4715 ms (Beats 57.59%) |
| 💾 Memory | 19.3 MB (Beats 99.92%) |
| 📅 Solved | 2025-08-22 |
| 💻 Language | Python |