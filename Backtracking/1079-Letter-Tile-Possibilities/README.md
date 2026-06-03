> 📌 **Cross-listed:** Primary location is [Hash Table/1079-Letter-Tile-Possibilities](../../Hash-Table/1079-Letter-Tile-Possibilities). This problem also appears under: **Hash Table**, **String**, **Backtracking**, **Counting**

# 1079. Letter Tile Possibilities


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/letter-tile-possibilities/)


## 📝 Problem Description

You have `n`  `tiles`, where each tile has one letter `tiles[i]` printed on it.

Return *the number of possible non-empty sequences of letters* you can make using the letters printed on those `tiles`.

 

Example 1:**

```

**Input:** tiles = "AAB"
**Output:** 8
**Explanation: **The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

```

Example 2:**

```

**Input:** tiles = "AAABBC"
**Output:** 188

```

Example 3:**

```

**Input:** tiles = "V"
**Output:** 1

```

 

**Constraints:**

	- `1 <= tiles.length <= 7`

	- `tiles` consists of uppercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the number of possible non-empty sequences of letters that can be formed using the letters printed on the given tiles. We can use a combination of a hash table to count the frequency of each letter and a backtracking approach to generate all possible sequences.

**Approach**
1. Count the frequency of each letter in the input string using a hash table (in this case, a `Counter` object).
2. Define a recursive function `backtrack()` that takes no arguments.
3. Initialize a variable `res` to 0, which will store the total number of possible sequences.
4. Iterate over each unique letter `c` in the hash table.
5. If the count of `c` is greater than 0, decrement its count by 1 and recursively call `backtrack()`.
6. After the recursive call returns, increment `res` by 1 (to account for the current sequence) and add the result of the recursive call to `res`.
7. After the loop finishes, return `res`.

**Time Complexity**
O(2^n * n), where n is the number of unique letters in the input string. This is because in the worst case, we might need to generate all possible sequences of length up to n, and each sequence takes O(n) time to generate.

**Space Complexity**
O(n), where n is the number of unique letters in the input string. This is because we need to store the frequency of each letter in the hash table.

**Key Insight**
The key insight here is to use a backtracking approach to generate all possible sequences, and to use a hash table to efficiently count the frequency of each letter. By recursively exploring all possible sequences and counting the number of sequences at each step, we can efficiently compute the total number of possible sequences.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 39 ms (Beats 35.46%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-07-30 |
| 💻 Language | Python |