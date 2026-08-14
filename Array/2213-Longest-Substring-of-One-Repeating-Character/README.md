# 2213. Longest Substring of One Repeating Character


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple) ![Ordered Set](https://img.shields.io/badge/Ordered%20Set-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)


## 📝 Problem Description

You are given a **0-indexed** string `s`. You are also given a **0-indexed** string `queryCharacters` of length `k` and a **0-indexed** array of integer **indices** `queryIndices` of length `k`, both of which are used to describe `k` queries.

The `i^th` query updates the character in `s` at index `queryIndices[i]` to the character `queryCharacters[i]`.

Return *an array* `lengths` *of length *`k`* where* `lengths[i]` *is the **length** of the **longest substring** of *`s`* consisting of **only one repeating** character **after** the* `i^th` *query** is performed.*

 

Example 1:**

```

**Input:** s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
**Output:** [3,3,4]
**Explanation:** 
- 1^st query updates s = "b**b**bacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2^nd query updates s = "bbb**c**cc". 
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3^rd query updates s = "bbb**b**cc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].

```

Example 2:**

```

**Input:** s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
**Output:** [2,3]
**Explanation:**
- 1^st query updates s = "ab**a**zz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2^nd query updates s = "a**a**azz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters.

	- `k == queryCharacters.length == queryIndices.length`

	- `1 <= k <= 10^5`

	- `queryCharacters` consists of lowercase English letters.

	- `0 <= queryIndices[i] < s.length`

## 🧠 Solution Explanation

**Intuition**  
A segment tree lets us keep, for every interval, the longest run of identical characters that can cross the interval’s borders. After a point update we only need to recompute the path to the root, so the global maximum is instantly available at the root node.

**Approach**  
1. **Node representation** – For a segment `[l,r]` store:  
   - `lc, rc`: leftmost and rightmost characters.  
   - `len`: segment length.  
   - `pref`: length of the longest prefix of equal chars.  
   - `suff`: length of the longest suffix of equal chars.  
   - `best`: maximum run length inside the segment.  
2. **Merge two children** –  
   - `len = left.len + right.len`.  
   - `pref` is `left.pref` if `left.pref < left.len` or the left child is all one char; otherwise it extends into the right child (`left.len + right.pref`).  
   - `suff` is analogous.  
   - `best` is the maximum of `left.best`, `right.best`, and a cross‑segment run `left.suff + right.pref` when `left.rc == right.lc`.  
3. **Build** – Recursively build the tree from the initial string.  
4. **Update** – For a query `(idx, ch)` replace the leaf’s data with the new character and propagate merges up to the root.  
5. **Answer** – After each update, the root’s `best` field is the longest repeating substring length; append it to the result list.

**Time Complexity**  
Building the tree: `O(n)`.  
Each query requires `O(log n)` updates.  
Total: `O((n + k) log n)`.

**Space Complexity**  
The segment tree stores `4n` nodes, each with constant data → `O(n)` space.

**Key Insight**  
By storing prefix, suffix, and best lengths per segment, we can combine two halves in constant time, allowing point updates to propagate quickly while always knowing the global maximum at the root.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3125 ms (Beats 48.48%) |
| 💾 Memory | 105.4 MB (Beats 25.76%) |
| 📅 Solved | 2026-08-13 |
| 💻 Language | Python |