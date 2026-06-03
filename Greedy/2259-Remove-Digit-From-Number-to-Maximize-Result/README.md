> 📌 **Cross-listed:** Primary location is [String/2259-Remove-Digit-From-Number-to-Maximize-Result](../../String/2259-Remove-Digit-From-Number-to-Maximize-Result). This problem also appears under: **String**, **Greedy**, **Enumeration**

# 2259. Remove Digit From Number to Maximize Result


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/)


## 📝 Problem Description

You are given a string `number` representing a **positive integer** and a character `digit`.

Return *the resulting string after removing **exactly one occurrence** of *`digit`* from *`number`* such that the value of the resulting string in **decimal** form is **maximized***. The test cases are generated such that `digit` occurs at least once in `number`.

 

Example 1:**

```

**Input:** number = "123", digit = "3"
**Output:** "12"
**Explanation:** There is only one '3' in "123". After removing '3', the result is "12".

```

Example 2:**

```

**Input:** number = "1231", digit = "1"
**Output:** "231"
**Explanation:** We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".

```

Example 3:**

```

**Input:** number = "551", digit = "5"
**Output:** "51"
**Explanation:** We can remove either the first or second '5' from "551".
Both result in the string "51".

```

 

**Constraints:**

	- `2 <= number.length <= 100`

	- `number` consists of digits from `'1'` to `'9'`.

	- `digit` is a digit from `'1'` to `'9'`.

	- `digit` occurs at least once in `number`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to find the maximum possible number by removing exactly one occurrence of the given digit. It iterates through the number string, removing the digit at each position and keeping track of the maximum resulting string.

**Approach**
1. Initialize an empty string `maxi` to store the maximum resulting string.
2. Iterate through the `number` string using a for loop.
3. For each position `i`, create a temporary string `temp` by removing the digit at position `i` from the original number.
4. Check if the temporary string is greater than the current maximum string `maxi`. If it is, update `maxi` with the temporary string.
5. After iterating through the entire string, return the maximum string `maxi`.

**Time Complexity**
O(n), where n is the length of the `number` string. This is because we are iterating through the string once, and the operations inside the loop (string concatenation and comparison) take constant time.

**Space Complexity**
O(n), where n is the length of the `number` string. This is because we are creating a temporary string `temp` at each position, which can potentially be as large as the original string.

**Key Insight**
The key insight is that we can remove the digit at any position and still get a valid number, so we can simply try removing the digit at each position and keep track of the maximum resulting string. This greedy approach ensures that we find the maximum possible number by removing exactly one occurrence of the given digit.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-01-29 |
| 💻 Language | Python |