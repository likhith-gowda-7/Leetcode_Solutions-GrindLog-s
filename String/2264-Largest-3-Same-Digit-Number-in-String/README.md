# 2264. Largest 3-Same-Digit Number in String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/largest-3-same-digit-number-in-string/)


## 📝 Problem Description

You are given a string `num` representing a large integer. An integer is **good** if it meets the following conditions:

	- It is a **substring** of `num` with length `3`.

	- It consists of only one unique digit.

Return *the **maximum good **integer as a **string** or an empty string *`""`* if no such integer exists*.

Note:

	- A **substring** is a contiguous sequence of characters within a string.

	- There may be **leading zeroes** in `num` or a good integer.

 

Example 1:**

```

**Input:** num = "6**777**133339"
**Output:** "777"
**Explanation:** There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

```

Example 2:**

```

**Input:** num = "23**000**19"
**Output:** "000"
**Explanation:** "000" is the only good integer.

```

Example 3:**

```

**Input:** num = "42352338"
**Output:** ""
**Explanation:** No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

```

 

**Constraints:**

	- `3 <= num.length <= 1000`

	- `num` only consists of digits.

## 🧠 Solution Explanation

**Intuition**
The solution iterates through the input string, maintaining a count of consecutive identical digits. When a sequence of three identical digits is found, it updates the maximum good integer if necessary. This approach works because a good integer must be a substring of length 3 with only one unique digit.

**Approach**
1. Initialize `max_good` to -1, which will store the maximum good integer, and `c` to 1, which will count consecutive identical digits.
2. Iterate through the input string `num` starting from the second character (index 1).
3. If the current character is the same as the previous one, increment `c`.
4. If `c` becomes 3, update `max_good` with the maximum of its current value and the current digit.
5. If the current character is different from the previous one, reset `c` to 1.
6. After iterating through the entire string, return the maximum good integer as a string if it exists, or an empty string otherwise.

**Time Complexity**
O(n), where n is the length of the input string. This is because we iterate through the string once.

**Space Complexity**
O(1), which means the space complexity is constant. We only use a few variables to store the maximum good integer and the count of consecutive identical digits, regardless of the input size.

**Key Insight**
The key insight is that a good integer must be a substring of length 3 with only one unique digit. By maintaining a count of consecutive identical digits, we can efficiently identify and update the maximum good integer as we iterate through the input string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-08-14 |
| 💻 Language | Python |