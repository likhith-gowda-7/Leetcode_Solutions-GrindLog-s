> 📌 **Cross-listed:** Primary location is [Hash Table/1461-Check-If-a-String-Contains-All-Binary-Codes-of-Size-K](../../Hash-Table/1461-Check-If-a-String-Contains-All-Binary-Codes-of-Size-K). This problem also appears under: **Hash Table**, **String**, **Bit Manipulation**, **Rolling Hash**, **Hash Function**

# 1461. Check If a String Contains All Binary Codes of Size K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Rolling Hash](https://img.shields.io/badge/Rolling%20Hash-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)


## 📝 Problem Description

Given a binary string `s` and an integer `k`, return `true` *if every binary code of length* `k` *is a substring of* `s`. Otherwise, return `false`.

 

Example 1:**

```

**Input:** s = "00110110", k = 2
**Output:** true
**Explanation:** The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

```

Example 2:**

```

**Input:** s = "0110", k = 1
**Output:** true
**Explanation:** The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

```

Example 3:**

```

**Input:** s = "0110", k = 2
**Output:** false
**Explanation:** The binary code "00" is of length 2 and does not exist in the array.

```

 

**Constraints:**

	- `1 <= s.length <= 5 * 10^5`

	- `s[i]` is either `'0'` or `'1'`.

	- `1 <= k <= 20`

## 🧠 Solution Explanation

**Intuition**
This solution uses a rolling hash to efficiently check if all binary codes of size `k` are present in the string `s`. The idea is to maintain a hash table where each index represents a binary code of length `k`, and we update the hash table as we iterate through the string.

**Approach**
1. Calculate the total number of unique binary codes of length `k`, which is `2^k`.
2. Initialize a hash table `seen` of size `2^k` with all elements set to `False`.
3. Initialize a mask `mask` to `2^k - 1` to perform bitwise operations.
4. Initialize a hash value `h` to 0.
5. Iterate through the string `s` character by character.
6. For each character, update the hash value `h` by shifting it left by 1 bit and performing a bitwise AND with the mask, then perform a bitwise OR with the ASCII value of the current character modulo 2.
7. If the current index `i` is greater than or equal to `k - 1` and the corresponding binary code in the hash table `seen` is not set, set it to `True` and decrement the count of unique binary codes.
8. If the count of unique binary codes reaches 0, return `True`.
9. After iterating through the entire string, return `False` if not all binary codes are found.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we iterate through the string once, and each operation inside the loop takes constant time.

**Space Complexity**
O(2^k), where k is the length of the binary code. This is because we need to store the hash table of size `2^k` to keep track of the unique binary codes.

**Key Insight**
The key insight here is the use of a rolling hash to efficiently update the hash value as we iterate through the string. By performing bitwise operations, we can avoid explicit string manipulation and achieve a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 169 ms (Beats 94.54%) |
| 💾 Memory | 28.8 MB (Beats 88.05%) |
| 📅 Solved | 2026-02-23 |
| 💻 Language | Python |