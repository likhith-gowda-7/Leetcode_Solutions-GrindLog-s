> 📌 **Cross-listed:** Primary location is [Math/1903-Largest-Odd-Number-in-String](../../Math/1903-Largest-Odd-Number-in-String). This problem also appears under: **Math**, **String**, **Greedy**

# 1903. Largest Odd Number in String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/largest-odd-number-in-string/)


## 📝 Problem Description

You are given a string `num`, representing a large integer. Return *the **largest-valued odd** integer (as a string) that is a **non-empty substring** of *`num`*, or an empty string *`""`* if no odd integer exists*.

A **substring** is a contiguous sequence of characters within a string.

 

Example 1:**

```

**Input:** num = "52"
**Output:** "5"
**Explanation:** The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

```

Example 2:**

```

**Input:** num = "4206"
**Output:** ""
**Explanation:** There are no odd numbers in "4206".

```

Example 3:**

```

**Input:** num = "35427"
**Output:** "35427"
**Explanation:** "35427" is already an odd number.

```

 

**Constraints:**

	- `1 <= num.length <= 10^5`

	- `num` only consists of digits and does not contain any leading zeros.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 60.69%) |
| 💾 Memory | 19.1 MB (Beats 100%) |
| 📅 Solved | 2025-02-13 |
| 💻 Language | Python |