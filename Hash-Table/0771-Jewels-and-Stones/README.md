# 771. Jewels and Stones


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jewels-and-stones/)


## 📝 Problem Description

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

 

Example 1:**

```
**Input:** jewels = "aA", stones = "aAAbbbb"
**Output:** 3

```
Example 2:**

```
**Input:** jewels = "z", stones = "ZZ"
**Output:** 0

```

 

**Constraints:**

	- `1 <= jewels.length, stones.length <= 50`

	- `jewels` and `stones` consist of only English letters.

	- All the characters of `jewels` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to efficiently count the occurrences of each stone type in the `stones` string, and then iterates through the `jewels` string to sum up the counts of the stones that are also jewels. This approach takes advantage of the unique characteristics of the `jewels` string, where all characters are unique, to simplify the counting process.

**Approach**
1. Create an empty hash table `h` to store the counts of each stone type.
2. Iterate through the `stones` string and for each stone:
   - If the stone is already in the hash table, increment its count by 1.
   - If the stone is not in the hash table, add it with a count of 1.
3. Initialize a variable `res` to store the total count of jewels.
4. Iterate through the `jewels` string and for each jewel:
   - If the jewel is in the hash table, add its count to `res`.
5. Return the total count of jewels `res`.

**Time Complexity**
O(n + m), where n is the length of the `stones` string and m is the length of the `jewels` string. This is because we iterate through each string once.

**Space Complexity**
O(m), where m is the length of the `jewels` string. This is because we store the counts of each stone type in the hash table, and the maximum number of unique stone types is equal to the length of the `jewels` string.

**Key Insight**
The key insight is that we can take advantage of the unique characteristics of the `jewels` string to simplify the counting process. By storing the counts of each stone type in a hash table, we can efficiently look up the counts of the stones that are also jewels, resulting in a time complexity of O(n + m).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-01-17 |
| 💻 Language | Python |