# 2559. Count Vowel Strings in Ranges


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-vowel-strings-in-ranges/)


## 📝 Problem Description

You are given a **0-indexed** array of strings `words` and a 2D array of integers `queries`.

Each query `queries[i] = [l_i, r_i]` asks us to find the number of strings present at the indices ranging from `l_i` to `r_i` (both **inclusive**) of `words` that start and end with a vowel.

Return *an array *`ans`* of size *`queries.length`*, where *`ans[i]`* is the answer to the *`i`^th* query*.

**Note** that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

 

Example 1:**

```

**Input:** words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
**Output:** [2,3,0]
**Explanation:** The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

```

Example 2:**

```

**Input:** words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
**Output:** [3,2,1]
**Explanation:** Every string satisfies the conditions, so we return [3,2,1].
```

 

**Constraints:**

	- `1 <= words.length <= 10^5`

	- `1 <= words[i].length <= 40`

	- `words[i]` consists only of lowercase English letters.

	- `sum(words[i].length) <= 3 * 10^5`

	- `1 <= queries.length <= 10^5`

	- `0 <= l_i <= r_i < words.length`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a prefix sum approach to efficiently calculate the number of strings in each query range that start and end with a vowel. By precomputing the cumulative count of such strings, we can quickly determine the answer for each query.

**Approach**
1. Initialize an empty set `s` containing the vowel letters `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.
2. Create an array `rang` of the same length as `words`, initialized with zeros. This array will store the cumulative count of strings that start and end with a vowel.
3. Iterate through `words` and for each string `w`, check if it starts and ends with a vowel. If so, increment the cumulative count `prev` and store it in `rang` at the current index.
4. Initialize an array `res` of the same length as `queries`, filled with zeros. This array will store the answers to each query.
5. Iterate through `queries` and for each query `[l, r]`, check if `l` is 0. If so, the answer is the cumulative count at index `r`. Otherwise, the answer is the difference between the cumulative counts at indices `r` and `l-1`.

**Time Complexity**
O(n + m), where n is the length of `words` and m is the number of queries. This is because we iterate through `words` once to precompute the cumulative count, and then iterate through `queries` once to calculate the answers.

**Space Complexity**
O(n + m), where n is the length of `words` and m is the number of queries. This is because we create two arrays of the same length as `words` and `queries`, respectively.

**Key Insight**
The key insight is to use a prefix sum approach to precompute the cumulative count of strings that start and end with a vowel. This allows us to efficiently calculate the answer for each query by simply looking up the cumulative counts at the query range boundaries.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 97.65%) |
| 💾 Memory | 49.5 MB (Beats 12.72%) |
| 📅 Solved | 2025-01-20 |
| 💻 Language | Python |