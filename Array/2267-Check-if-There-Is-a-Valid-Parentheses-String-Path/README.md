# 2267.  Check if There Is a Valid Parentheses String Path


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Bracket Sequences](https://img.shields.io/badge/Bracket%20Sequences-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)


## 📝 Problem Description

A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is **valid** if **any** of the following conditions is **true**:

	- It is `()`.

	- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.

	- It can be written as `(A)`, where `A` is a valid parentheses string.

You are given an `m x n` matrix of parentheses `grid`. A **valid parentheses string path** in the grid is a path satisfying **all** of the following conditions:

	- The path starts from the upper left cell `(0, 0)`.

	- The path ends at the bottom-right cell `(m - 1, n - 1)`.

	- The path only ever moves **down** or **right**.

	- The resulting parentheses string formed by the path is **valid**.

Return `true` *if there exists a **valid parentheses string path** in the grid.* Otherwise, return `false`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/03/15/example1drawio.png)
```

**Input:** grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
**Output:** true
**Explanation:** The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/15/example2drawio.png)
```

**Input:** grid = [[")",")"],["(","("]]
**Output:** false
**Explanation:** The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 100`

	- `grid[i][j]` is either `'('` or `')'`.

## 🧠 Solution Explanation

**Intuition**  
A valid parentheses string keeps a running balance: `(` adds +1, `)` subtracts –1, and the balance must never go negative and end at 0.  
Thus, while walking the grid we only need to know the current balance; if it ever becomes negative the path can’t be valid.

**Approach**  
1. Recursively explore from `(0,0)` to `(m‑1,n‑1)` moving only **down** or **right**.  
2. Keep a `validity` counter (the current balance).  
3. At each cell:  
   * If `grid[row][col] == '('`, increment `validity`; else decrement.  
   * If the counter is negative or we’re out of bounds → prune.  
4. If we reach the bottom‑right and `validity == 0`, return `True`.  
5. Otherwise, recursively check the two possible moves (`down`, `right`).  
6. Memoize results for `(row, col, validity)` with `@cache` to avoid recomputation.

**Time Complexity**  
Each state `(row, col, validity)` is evaluated once.  
`row` ∈ `[0, m)`, `col` ∈ `[0, n)`, `validity` ∈ `[0, m+n]` (balance can’t exceed the path length).  
Hence **O(m · n · (m+n))** operations in the worst case.

**Space Complexity**  
The recursion stack depth is at most `m+n`.  
Memoization stores at most `m · n · (m+n)` states.  
Thus **O(m · n · (m+n))** auxiliary space.

**Key Insight**  
A path’s validity depends solely on the current balance; by pruning negative balances and memoizing `(row, col, balance)`, we transform an exponential search into a manageable dynamic‑programming problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2873 ms (Beats 5%) |
| 💾 Memory | 687.5 MB (Beats 6%) |
| 📅 Solved | 2026-09-30 |
| 💻 Language | Python |