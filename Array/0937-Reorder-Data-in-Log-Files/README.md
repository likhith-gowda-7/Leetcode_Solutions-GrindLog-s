# 937. Reorder Data in Log Files


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reorder-data-in-log-files/)


## 📝 Problem Description

You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the **identifier**.

There are two types of logs:

	- **Letter-logs**: All words (except the identifier) consist of lowercase English letters.

	- **Digit-logs**: All words (except the identifier) consist of digits.

Reorder these logs so that:

	- The **letter-logs** come before all **digit-logs**.

	- The **letter-logs** are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.

	- The **digit-logs** maintain their relative ordering.

Return *the final order of the logs*.

 

Example 1:**

```

**Input:** logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
**Output:** ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
**Explanation:**
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

```

Example 2:**

```

**Input:** logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
**Output:** ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

```

 

**Constraints:**

	- `1 <= logs.length <= 100`

	- `3 <= logs[i].length <= 100`

	- All the tokens of `logs[i]` are separated by a **single** space.

	- `logs[i]` is guaranteed to have an identifier and at least one word after the identifier.

## 🧠 Solution Explanation

**Intuition**
This approach works by first separating the logs into two categories: letter-logs and digit-logs. It then sorts the letter-logs based on their contents and identifiers, while maintaining the relative ordering of the digit-logs. This ensures that the letter-logs come before the digit-logs and are sorted lexicographically.

**Approach**
1. Initialize two empty lists: `letters` to store the letter-logs and `digits` to store the digit-logs.
2. Iterate through each log in the input list `logs`.
3. Split each log into its identifier and content using the space character as a delimiter.
4. Check if the content starts with a digit. If it does, append the log to the `digits` list. Otherwise, append a tuple containing the content, identifier, and log to the `letters` list.
5. Sort the `letters` list based on the content and identifier of each log.
6. Iterate through the sorted `letters` list and replace each tuple with its corresponding log.
7. Return the sorted list of letter-logs followed by the digit-logs.

**Time Complexity**
The time complexity of this approach is O(n log n) due to the sorting of the `letters` list. Here, n is the number of logs in the input list.

**Space Complexity**
The space complexity of this approach is O(n) as we need to store the letter-logs and digit-logs in separate lists.

**Key Insight**
The key insight here is to separate the logs into two categories and sort the letter-logs based on their contents and identifiers, while maintaining the relative ordering of the digit-logs. This allows us to efficiently reorder the logs while satisfying the given conditions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-02-15 |
| 💻 Language | Python |