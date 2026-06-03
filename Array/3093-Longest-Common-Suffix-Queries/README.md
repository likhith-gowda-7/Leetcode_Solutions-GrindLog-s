# 3093. Longest Common Suffix Queries


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-common-suffix-queries/)


## 📝 Problem Description

You are given two arrays of strings `wordsContainer` and `wordsQuery`.

For each `wordsQuery[i]`, you need to find a string from `wordsContainer` that has the **longest common suffix** with `wordsQuery[i]`. If there are two or more strings in `wordsContainer` that share the longest common suffix, find the string that is the **smallest** in length. If there are two or more such strings that have the **same** smallest length, find the one that occurred **earlier** in `wordsContainer`.

Return *an array of integers *`ans`*, where *`ans[i]`* is the index of the string in *`wordsContainer`* that has the **longest common suffix** with *`wordsQuery[i]`*.*

 

Example 1:**

**Input:** wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]

**Output:** [1,1,1]

**Explanation:**

Let's look at each `wordsQuery[i]` separately:

	- For `wordsQuery[0] = "cd"`, strings from `wordsContainer` that share the longest common suffix `"cd"` are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.

	- For `wordsQuery[1] = "bcd"`, strings from `wordsContainer` that share the longest common suffix `"bcd"` are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.

	- For `wordsQuery[2] = "xyz"`, there is no string from `wordsContainer` that shares a common suffix. Hence the longest common suffix is `""`, that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.

Example 2:**

**Input:** wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]

**Output:** [2,0,2]

**Explanation:**

Let's look at each `wordsQuery[i]` separately:

	- For `wordsQuery[0] = "gh"`, strings from `wordsContainer` that share the longest common suffix `"gh"` are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.

	- For `wordsQuery[1] = "acbfgh"`, only the string at index 0 shares the longest common suffix `"fgh"`. Hence it is the answer, even though the string at index 2 is shorter.

	- For `wordsQuery[2] = "acbfegh"`, strings from `wordsContainer` that share the longest common suffix `"gh"` are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.

 

**Constraints:**

	- `1 <= wordsContainer.length, wordsQuery.length <= 10^4`

	- `1 <= wordsContainer[i].length <= 5 * 10^3`

	- `1 <= wordsQuery[i].length <= 5 * 10^3`

	- `wordsContainer[i]` consists only of lowercase English letters.

	- `wordsQuery[i]` consists only of lowercase English letters.

	- Sum of `wordsContainer[i].length` is at most `5 * 10^5`.

	- Sum of `wordsQuery[i].length` is at most `5 * 10^5`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a reverse trie data structure to efficiently find the longest common suffix between each query string and the strings in the container. By reversing the strings, we can use a trie to store the suffixes of the container strings, allowing us to quickly find the longest common suffix with each query string.

**Approach**
1. Create a root node for the reverse trie.
2. Iterate through each string in the container, reversing it and building the reverse trie by iterating through each character in the reversed string.
3. For each character, create a new node in the trie if it doesn't exist, and update the current node's child pointer to point to the new node.
4. Update the current node's index to the current string's index in the container, using the `updateIndex` method to ensure that the index is the smallest, shortest, and earliest string that has the longest common suffix.
5. Iterate through each query string, reversing it and traversing the reverse trie by iterating through each character in the reversed string.
6. When a node is reached that has a child pointer for the current character, update the answer with the index stored in that node.

**Time Complexity**
O(n*m + q*m), where n is the number of strings in the container, m is the maximum length of a string in the container, and q is the number of query strings. The time complexity is dominated by the time it takes to build the reverse trie (O(n*m)) and the time it takes to process each query string (O(q*m)).

**Space Complexity**
O(n*m), where n is the number of strings in the container and m is the maximum length of a string in the container. The space complexity is dominated by the space required to store the reverse trie.

**Key Insight**
The key insight is that by reversing the strings and using a trie to store the suffixes, we can efficiently find the longest common suffix between each query string and the strings in the container. This approach allows us to solve the problem in O(n*m + q*m) time complexity, which is much faster than a brute-force approach that would have a time complexity of O(n*q*m).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1621 ms (Beats 37.55%) |
| 💾 Memory | 222.3 MB (Beats 9.26%) |
| 📅 Solved | 2026-05-28 |
| 💻 Language | Python |