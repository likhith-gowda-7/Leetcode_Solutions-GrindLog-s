# 2131. Longest Palindrome by Concatenating Two Letter Words


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/)


## 📝 Problem Description

You are given an array of strings `words`. Each element of `words` consists of **two** lowercase English letters.

Create the **longest possible palindrome** by selecting some elements from `words` and concatenating them in **any order**. Each element can be selected **at most once**.

Return *the **length** of the longest palindrome that you can create*. If it is impossible to create any palindrome, return `0`.

A **palindrome** is a string that reads the same forward and backward.

 

Example 1:**

```

**Input:** words = ["lc","cl","gg"]
**Output:** 6
**Explanation:** One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

```

Example 2:**

```

**Input:** words = ["ab","ty","yt","lc","cl","ab"]
**Output:** 8
**Explanation:** One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

```

Example 3:**

```

**Input:** words = ["cc","ll","xx"]
**Output:** 2
**Explanation:** One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

```

 

**Constraints:**

	- `1 <= words.length <= 10^5`

	- `words[i].length == 2`

	- `words[i]` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by counting the occurrences of each word in the input array and then constructing the longest possible palindrome by selecting words that can be paired together to form a palindrome. Words that are the same when reversed are counted as pairs, while words that are not the same when reversed are counted as pairs if their reversed versions have a higher count.

**Approach**
1. Count the occurrences of each word in the input array using a hash table (Counter).
2. Initialize the result (res) to 0 and a flag (is_exits) to False.
3. Iterate over each word in the hash table:
   - If the word is the same when reversed (e.g., "ab" and "ba"), count the number of pairs by dividing the count by 2 and multiply by 4 (since each pair contributes 4 characters to the palindrome).
   - If the word is not the same when reversed, count the minimum number of pairs between the word and its reversed version.
   - If the count of the word is odd and no word has been counted as a single character yet, set the flag to True.
4. If the flag is True, add 2 to the result (since the single character can be added to the palindrome).
5. Return the result.

**Time Complexity**
O(n), where n is the number of words in the input array. This is because we iterate over each word in the hash table once.

**Space Complexity**
O(n), where n is the number of words in the input array. This is because we store the count of each word in the hash table.

**Key Insight**
The key insight is that words that are the same when reversed can be paired together to form a palindrome, while words that are not the same when reversed can be paired with their reversed versions if available. This allows us to construct the longest possible palindrome by selecting words that can be paired together.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 45 ms (Beats 86.27%) |
| 💾 Memory | 35.8 MB (Beats 96.52%) |
| 📅 Solved | 2025-05-25 |
| 💻 Language | Python |