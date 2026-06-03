> 📌 **Cross-listed:** Primary location is [Hash Table/0299-Bulls-and-Cows](../../Hash-Table/0299-Bulls-and-Cows). This problem also appears under: **Hash Table**, **String**, **Counting**

# 299. Bulls and Cows


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/bulls-and-cows/)


## 📝 Problem Description

You are playing the **[Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)** game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

	- The number of "bulls", which are digits in the guess that are in the correct position.

	- The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number `secret` and your friend's guess `guess`, return *the hint for your friend's guess*.

The hint should be formatted as `"xAyB"`, where `x` is the number of bulls and `y` is the number of cows. Note that both `secret` and `guess` may contain duplicate digits.

 

Example 1:**

```

**Input:** secret = "1807", guess = "7810"
**Output:** "1A3B"
**Explanation:** Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
```

Example 2:**

```

**Input:** secret = "1123", guess = "0111"
**Output:** "1A1B"
**Explanation:** Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

```

 

**Constraints:**

	- `1 <= secret.length, guess.length <= 1000`

	- `secret.length == guess.length`

	- `secret` and `guess` consist of digits only.

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of two passes to count the bulls and cows. The first pass identifies the bulls by checking for exact matches between the secret and guess, while the second pass identifies the cows by checking for non-bull digits that appear in the secret.

**Approach**
1. Initialize counters for bulls and cows.
2. Create a hash table (Counter) to store the frequency of each digit in the secret.
3. Iterate through the guess, and for each digit:
   - If the digit matches the corresponding digit in the secret, increment the bull counter and decrement the frequency of the digit in the hash table.
   - Mark the index of the digit as used to avoid counting it again.
4. Iterate through the guess again, and for each digit:
   - If the digit has not been used before and its frequency in the hash table is greater than 0, increment the cow counter and decrement the frequency of the digit in the hash table.
5. Return the hint as a string, formatted as "xAyB".

**Time Complexity**
O(n), where n is the length of the guess. The two passes through the guess take O(n) time each, and the operations within each pass take constant time.

**Space Complexity**
O(n), where n is the length of the secret. The hash table (Counter) stores the frequency of each digit in the secret, which requires O(n) space.

**Key Insight**
The key insight is to use a hash table to store the frequency of each digit in the secret, allowing for efficient counting of cows by checking the remaining frequency of each digit. This approach avoids the need for a brute-force comparison of all possible permutations of the guess.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 44.57%) |
| 💾 Memory | 17.2 MB (Beats 100%) |
| 📅 Solved | 2025-12-27 |
| 💻 Language | Python |