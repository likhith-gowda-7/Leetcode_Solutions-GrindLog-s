# 2273. Find Resultant Array After Removing Anagrams


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/)


## 📝 Problem Description

You are given a **0-indexed** string array `words`, where `words[i]` consists of lowercase English letters.

In one operation, select any index `i` such that `0 < i < words.length` and `words[i - 1]` and `words[i]` are **anagrams**, and **delete** `words[i]` from `words`. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return `words` *after performing all operations*. It can be shown that selecting the indices for each operation in **any** arbitrary order will lead to the same result.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, `"dacb"` is an anagram of `"abdc"`.

 

Example 1:**

```

**Input:** words = ["abba","baba","bbaa","cd","cd"]
**Output:** ["abba","cd"]
**Explanation:**
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.
```

Example 2:**

```

**Input:** words = ["a","b","c","d","e"]
**Output:** ["a","b","c","d","e"]
**Explanation:**
No two adjacent strings in words are anagrams of each other, so no operations are performed.
```

 

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 10`

	- `words[i]` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the words that are not anagrams of the previous word. It counts the frequency of each character in the current word and checks if it's an anagram of the previous word by comparing their character counts. If they're anagrams, it removes the current word from the stack.

**Approach**
1. Initialize an empty stack to store the words and a dictionary `h1` to store the character counts of each word.
2. Define a helper function `char_count` to count the frequency of each character in a word.
3. Iterate over each word in the input list. For each word:
   1. Count the frequency of each character in the word using `char_count`.
   2. Push the word onto the stack.
   3. While the stack has more than one word and the current word's character count is equal to the previous word's character count, pop the previous word from the stack.
4. Return the stack, which contains the words after removing anagrams.

**Time Complexity**
O(n*m), where n is the number of words and m is the maximum length of a word. This is because we're iterating over each word and counting its characters.

**Space Complexity**
O(n*m), where n is the number of words and m is the maximum length of a word. This is because we're storing the character counts of each word in the dictionary `h1`.

**Key Insight**
The key insight is to use a stack to keep track of the words that are not anagrams of the previous word. By comparing the character counts of each word, we can efficiently identify and remove anagrams from the stack. This approach allows us to solve the problem in linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 51.94%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-10-13 |
| 💻 Language | Python |