# 374. Guess Number Higher or Lower


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Interactive](https://img.shields.io/badge/Interactive-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/)


## 📝 Problem Description

We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

	- `-1`: Your guess is higher than the number I picked (i.e. `num > pick`).

	- `1`: Your guess is lower than the number I picked (i.e. `num < pick`).

	- `0`: your guess is equal to the number I picked (i.e. `num == pick`).

Return *the number that I picked*.

 

Example 1:**

```

**Input:** n = 10, pick = 6
**Output:** 6

```

Example 2:**

```

**Input:** n = 1, pick = 1
**Output:** 1

```

Example 3:**

```

**Input:** n = 2, pick = 1
**Output:** 1

```

 

**Constraints:**

	- `1 <= n <= 2^31 - 1`

	- `1 <= pick <= n`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 34 ms (Beats 97.31%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-24 |
| 💻 Language | Python |