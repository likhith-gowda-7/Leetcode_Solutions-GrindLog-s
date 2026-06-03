> 📌 **Cross-listed:** Primary location is [Hash Table/0763-Partition-Labels](../../Hash-Table/0763-Partition-Labels). This problem also appears under: **Hash Table**, **Two Pointers**, **String**, **Greedy**

# 763. Partition Labels


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/partition-labels/)


## 📝 Problem Description

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return *a list of integers representing the size of these parts*.

 

Example 1:**

```

**Input:** s = "ababcbacadefegdehijhklij"
**Output:** [9,7,8]
**Explanation:**
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

```

Example 2:**

```

**Input:** s = "eccbbbbdec"
**Output:** [10]

```

 

**Constraints:**

	- `1 <= s.length <= 500`

	- `s` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to partition the string into parts where each letter appears in at most one part. It keeps track of the maximum index of each character in the string and uses this information to determine when to start a new part.

**Approach**
1. Create a hash table `h1` that maps each character in the string to its index.
2. Initialize `maxi` to 0, which will store the maximum index of the current character.
3. Initialize `st` to 0, which will store the start index of the current part.
4. Initialize an empty list `res` to store the sizes of the parts.
5. Iterate over the string `s` from left to right.
6. For each character, update `maxi` to be the maximum of its current value and the index of the current character in the hash table.
7. If the current index `i` is equal to `maxi`, it means we have reached the end of the current part, so append the size of the part (i.e., `i - st + 1`) to the `res` list and update `st` to be `i + 1`.
8. Repeat steps 5-7 until the end of the string is reached.

**Time Complexity**
O(n), where n is the length of the string. This is because we are iterating over the string once.

**Space Complexity**
O(n), where n is the length of the string. This is because we are creating a hash table that stores the index of each character in the string.

**Key Insight**
The key insight is to use the maximum index of each character to determine when to start a new part. This allows us to partition the string in a greedy manner, ensuring that each letter appears in at most one part.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 85.58%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-15 |
| 💻 Language | Python |