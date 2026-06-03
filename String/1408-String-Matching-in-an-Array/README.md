> 📌 **Cross-listed:** Primary location is [Array/1408-String-Matching-in-an-Array](../../Array/1408-String-Matching-in-an-Array). This problem also appears under: **Array**, **String**, **String Matching**

# 1408. String Matching in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![String Matching](https://img.shields.io/badge/String%20Matching-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/string-matching-in-an-array/)


## 📝 Problem Description

Given an array of string `words`, return all strings in* *`words`* *that are a substring of another word. You can return the answer in **any order**.

 

Example 1:**

```

**Input:** words = ["mass","as","hero","superhero"]
**Output:** ["as","hero"]
**Explanation:** "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

```

Example 2:**

```

**Input:** words = ["leetcode","et","code"]
**Output:** ["et","code"]
**Explanation:** "et", "code" are substring of "leetcode".

```

Example 3:**

```

**Input:** words = ["blue","green","bu"]
**Output:** []
**Explanation:** No string of words is substring of another string.

```

 

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 30`

	- `words[i]` contains only lowercase English letters.

	- All the strings of `words` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over each word in the input array and checking if it's a substring of any other word. This is done by using a nested loop to compare each pair of words.

**Approach**
1. Initialize an empty list `res` to store the result.
2. Iterate over each word `words[i]` in the input array.
3. For each word `words[i]`, iterate over the remaining words `words[j]` in the array (excluding the current word `words[i]`).
4. Check if `words[i]` is a substring of `words[j]` using the `in` operator.
5. If `words[i]` is a substring of `words[j]`, add it to the result list `res` and break the inner loop.
6. Return the result list `res`.

**Time Complexity**
O(n^2 * m), where n is the number of words in the input array and m is the maximum length of a word. This is because we're using two nested loops to compare each pair of words, and for each comparison, we're checking if one word is a substring of another, which takes O(m) time.

**Space Complexity**
O(n), where n is the number of words in the input array. This is because we're storing the result in a list of size n.

**Key Insight**
The key insight here is that we can use a simple substring check using the `in` operator to determine if one word is a substring of another. This makes the solution efficient and easy to implement, despite the quadratic time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 66.55%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-12 |
| 💻 Language | Python |