# 79. Word Search


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/word-search/)


## 📝 Problem Description

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)
```

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)
```

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
**Output:** true

```

Example 3:**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)
```

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
**Output:** false

```

 

**Constraints:**

	- `m == board.length`

	- `n = board[i].length`

	- `1 <= m, n <= 6`

	- `1 <= word.length <= 15`

	- `board` and `word` consists of only lowercase and uppercase English letters.

 

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

## 🧠 Solution Explanation

## Intuition
The solution works by using a backtracking approach to explore all possible paths in the grid that could form the given word. It iterates over each cell in the grid and checks if the current cell matches the first character of the word, then recursively checks the neighboring cells to form the rest of the word. This approach ensures that all possible paths are explored without using any cell more than once.

## Approach
1. Define a helper function `backtrack` that takes the current cell coordinates `i` and `j`, and the current index `word_idx` in the word.
2. Check if the current index is equal to the length of the word, if so, return `True` as the word has been found.
3. Check if the current cell is out of bounds or if the character at the current cell does not match the character at the current index in the word, if so, return `False`.
4. Mark the current cell as visited by changing its value to a special character.
5. Recursively call the `backtrack` function for the neighboring cells (up, down, left, right) with the next index in the word.
6. If any of the recursive calls return `True`, return `True`.
7. Unmark the current cell by changing its value back to the original character.
8. Iterate over each cell in the grid and call the `backtrack` function if the current cell matches the first character of the word.

## Time Complexity
The time complexity is O(m * n * 4^L), where m is the number of rows, n is the number of columns, and L is the length of the word. This is because in the worst case, we need to explore all possible paths of length L from each cell.

## Space Complexity
The space complexity is O(L), where L is the length of the word. This is because the maximum depth of the recursion call stack is L, as we need to store the current index and the current cell coordinates.

## Key Insight
The key insight is to use a backtracking approach to explore all possible paths in the grid, and to mark the current cell as visited to avoid using it more than once. This approach allows us to efficiently search for the word in the grid without exploring unnecessary paths.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3015 ms (Beats 89.76%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-07-30 |
| 💻 Language | Python |