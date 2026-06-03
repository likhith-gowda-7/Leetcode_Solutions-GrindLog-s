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

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using a binary search approach, taking advantage of the fact that we can get feedback on whether our guess is higher or lower than the target number. By iteratively narrowing down the search space, we can efficiently find the target number.

**Approach**
1. Initialize two pointers, `l` and `r`, to the start and end of the search range, respectively.
2. While `l` is less than or equal to `r`, calculate the midpoint `mid` of the current search range.
3. Use the `guess` API to get feedback on our guess `mid`.
4. If the feedback indicates that our guess is correct (`g == 0`), return the guess as the target number.
5. If the feedback indicates that our guess is too high (`g == -1`), update the upper bound `r` to `mid - 1`.
6. If the feedback indicates that our guess is too low (`g == 1`), update the lower bound `l` to `mid + 1`.
7. Repeat steps 2-6 until the target number is found or the search range is exhausted.

**Time Complexity**
O(log n), where n is the size of the search range. This is because we are using a binary search approach, which reduces the search space by half with each iteration.

**Space Complexity**
O(1), as we only need a constant amount of space to store the pointers `l` and `r`, as well as the midpoint `mid`.

**Key Insight**
The key insight is that we can use the feedback from the `guess` API to iteratively narrow down the search space, effectively turning the problem into a binary search problem. This allows us to solve the problem efficiently, with a time complexity of O(log n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 34 ms (Beats 97.24%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-24 |
| 💻 Language | Python |