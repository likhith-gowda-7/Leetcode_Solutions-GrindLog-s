# 1768. Merge Strings Alternately


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/merge-strings-alternately/)


## 📝 Problem Description

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.



Return *the merged string.*



 


Example 1:**



```

**Input:** word1 = "abc", word2 = "pqr"
**Output:** "apbqcr"
**Explanation:** The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

```


Example 2:**



```

**Input:** word1 = "ab", word2 = "pqrs"
**Output:** "apbqrs"
**Explanation:** Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

```


Example 3:**



```

**Input:** word1 = "abcd", word2 = "pq"
**Output:** "apbqcd"
**Explanation:** Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

```


 


**Constraints:**




	- `1 <= word1.length, word2.length <= 100`

	- `word1` and `word2` consist of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem requires merging two strings by adding letters in alternating order. This can be achieved by iterating through both strings simultaneously and appending the corresponding characters to the result string. If one string is longer than the other, append the remaining characters from the longer string to the end of the merged string.

**Approach**
1. Initialize two pointers, `i`, to 0, which will be used to track the current position in both strings.
2. Initialize an empty string `res` to store the merged result.
3. Enter a while loop that continues as long as both strings have characters at the current position `i`.
4. Inside the loop, append the characters at position `i` from both strings to the result string `res`.
5. Increment the position `i` to move to the next character in both strings.
6. Once one of the strings is exhausted, append the remaining characters from the other string to the end of `res`.
7. Return the merged string `res`.

**Time Complexity**
O(max(n, m)), where n and m are the lengths of the input strings. This is because we iterate through both strings simultaneously, and in the worst case, we might need to iterate through the longer string.

**Space Complexity**
O(n + m), where n and m are the lengths of the input strings. This is because we create a new string `res` that stores the merged result, which can be at most the sum of the lengths of the input strings.

**Key Insight**
The key insight here is to use two pointers to iterate through both strings simultaneously, which allows us to efficiently merge the strings in alternating order. This approach avoids unnecessary iterations and ensures that we handle the case where one string is longer than the other correctly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 33 ms (Beats 98.17%) |
| 💾 Memory | 17.5 MB (Beats 100%) |
| 📅 Solved | 2024-12-09 |
| 💻 Language | Python |