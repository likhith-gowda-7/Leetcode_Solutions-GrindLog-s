> 📌 **Cross-listed:** Primary location is [String/1415-The-k-th-Lexicographical-String-of-All-Happy-Strings-of-Length-n](../../String/1415-The-k-th-Lexicographical-String-of-All-Happy-Strings-of-Length-n). This problem also appears under: **String**, **Backtracking**

# 1415. The k-th Lexicographical String of All Happy Strings of Length n


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)


## 📝 Problem Description

A **happy string** is a string that:

	- consists only of letters of the set `['a', 'b', 'c']`.

	- `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).

For example, strings **"abc", "ac", "b"** and **"abcbabcbcb"** are all happy strings and strings **"aa", "baa"** and **"ababbc"** are not happy strings.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

Return *the kth string* of this list or return an **empty string** if there are less than `k` happy strings of length `n`.

 

Example 1:**

```

**Input:** n = 1, k = 3
**Output:** "c"
**Explanation:** The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

```

Example 2:**

```

**Input:** n = 1, k = 4
**Output:** ""
**Explanation:** There are only 3 happy strings of length 1.

```

Example 3:**

```

**Input:** n = 3, k = 9
**Output:** "cab"
**Explanation:** There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9^th string = "cab"

```

 

**Constraints:**

	- `1 <= n <= 10`

	- `1 <= k <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses a backtracking approach to generate all happy strings of length `n` in lexicographical order. It keeps track of the current string being built and the number of happy strings found so far. When it reaches the desired length `n` or finds the `kth` string, it adds the string to the result list.

**Approach**
1. Initialize an empty list `res` to store the happy strings and a string `s` containing the characters 'a', 'b', 'c'.
2. Define a recursive function `backtrack` that takes the current length `c` as an argument.
3. If the current length `c` is equal to `n`, increment the counter `self.reach` and check if it's equal to `k`. If so, add the current string to the result list `res`.
4. For each character `curr` in `s`, check if it's the same as the last character in the current string `sol`. If not, add `curr` to `sol` and recursively call `backtrack` with `c+1`.
5. After the recursive call returns, remove the last character from `sol` to backtrack.
6. Call `backtrack` with `c=0` to start building the happy strings.

**Time Complexity**
O(3^n / n) due to the backtracking approach, where n is the length of the happy string. The number of happy strings of length n is approximately 3^n / n, and each string is generated in O(n) time.

**Space Complexity**
O(n) for the recursive call stack, as the maximum depth of the recursion tree is n.

**Key Insight**
The key insight is to use a backtracking approach to generate all happy strings of length n in lexicographical order. By keeping track of the current string and the number of happy strings found so far, we can efficiently find the kth string without generating all strings.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 51 ms (Beats 26.01%) |
| 💾 Memory | 19.6 MB (Beats 47.14%) |
| 📅 Solved | 2026-03-15 |
| 💻 Language | Python |