> 📌 **Cross-listed:** Primary location is [Hash Table/3518-Smallest-Palindromic-Rearrangement-II](../../Hash-Table/3518-Smallest-Palindromic-Rearrangement-II). This problem also appears under: **Hash Table**, **Math**, **String**, **Combinatorics**, **Counting**

# 3518. Smallest Palindromic Rearrangement II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Combinatorics](https://img.shields.io/badge/Combinatorics-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/)


## 📝 Problem Description

You are given a **palindromic** string `s` and an integer `k`.

Return the **k-th** **lexicographically smallest** palindromic permutation of `s`. If there are fewer than `k` distinct palindromic permutations, return an empty string.

**Note:** Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 

Example 1:**

**Input:** s = "abba", k = 2

**Output:** "baab"

**Explanation:**

	- The two distinct palindromic rearrangements of `"abba"` are `"abba"` and `"baab"`.

	- Lexicographically, `"abba"` comes before `"baab"`. Since `k = 2`, the output is `"baab"`.

Example 2:**

**Input:** s = "aa", k = 2

**Output:** ""

**Explanation:**

	- There is only one palindromic rearrangement: "aa"`.

	- The output is an empty string since `k = 2` exceeds the number of possible rearrangements.

Example 3:**

**Input:** s = "bacab", k = 1

**Output:** "abcba"

**Explanation:**

	- The two distinct palindromic rearrangements of `"bacab"` are `"abcba"` and `"bacab"`.

	- Lexicographically, `"abcba"` comes before `"bacab"`. Since `k = 1`, the output is `"abcba"`.

 

**Constraints:**

	- `1 <= s.length <= 10^4`

	- `s` consists of lowercase English letters.

	- `s` is guaranteed to be palindromic.

	- `1 <= k <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution works by first counting the frequency of each character in the input string `s`. It then identifies the middle character(s) that will not be rearranged, and the remaining characters are divided into two halves. The function `get_ways` calculates the number of distinct palindromic permutations that can be formed with the remaining characters. If the number of permutations is less than `k`, an empty string is returned. Otherwise, the function constructs the `k-th` lexicographically smallest palindromic permutation by selecting characters from the remaining pool.

**Approach**
1. Count the frequency of each character in the input string `s` using a hash table `freq`.
2. Identify the middle character(s) that will not be rearranged and store them in `mid`.
3. Create a new hash table `half` to store the frequency of each character in the first half of the permutation.
4. Calculate the number of distinct palindromic permutations that can be formed with the remaining characters using the function `get_ways`.
5. If the number of permutations is less than `k`, return an empty string.
6. Otherwise, construct the `k-th` lexicographically smallest palindromic permutation by selecting characters from the remaining pool and appending the middle character(s) and the reverse of the first half.

**Time Complexity**
O(n log n) due to the use of `math.comb` in the `get_ways` function, where n is the number of characters in the input string `s`. The `get_ways` function is called recursively, and each call involves calculating the binomial coefficient, which takes O(log n) time.

**Space Complexity**
O(n) for storing the frequency of each character in the input string `s` and the hash tables `freq` and `half`.

**Key Insight**
The key insight is to recognize that the problem can be solved by counting the number of distinct palindromic permutations that can be formed with the remaining characters and then constructing the `k-th` permutation by selecting characters from the remaining pool. This approach allows us to avoid generating all possible permutations and instead focus on finding the `k-th` permutation directly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1195 ms (Beats 19.35%) |
| 💾 Memory | 19.9 MB (Beats 25.99%) |
| 📅 Solved | 2026-07-29 |
| 💻 Language | Python |