# 1758. Minimum Changes To Make Alternating Binary String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/)


## 📝 Problem Description

You are given a string `s` consisting only of the characters `'0'` and `'1'`. In one operation, you can change any `'0'` to `'1'` or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string `"010"` is alternating, while the string `"0100"` is not.

Return *the **minimum** number of operations needed to make* `s` *alternating*.

 

Example 1:**

```

**Input:** s = "0100"
**Output:** 1
**Explanation:** If you change the last character to '1', s will be "0101", which is alternating.

```

Example 2:**

```

**Input:** s = "10"
**Output:** 0
**Explanation:** s is already alternating.

```

Example 3:**

```

**Input:** s = "1111"
**Output:** 2
**Explanation:** You need two operations to reach "0101" or "1010".

```

 

**Constraints:**

	- `1 <= s.length <= 10^4`

	- `s[i]` is either `'0'` or `'1'`.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the string and keeping track of the minimum number of operations required to make the string alternating. It uses a clever trick to simplify the problem by only considering two possible operations: changing all '0's to '1's or vice versa.

**Approach**
1. Initialize two counters `op1_cnt` and `op2_cnt` to keep track of the minimum number of operations required for the two possible operations.
2. Iterate through the string, and for each character, check if it matches the current operation (i.e., if the current character is the same as the operation's expected character).
3. If the character does not match, increment the corresponding counter.
4. After each iteration, toggle the current operation by XORing `1` with the current operation index `curr`. This ensures that we consider the alternative operation in the next iteration.
5. Finally, return the minimum of `op1_cnt` and `op2_cnt`, which represents the minimum number of operations required to make the string alternating.

**Time Complexity**
O(n), where n is the length of the string. This is because we only need to iterate through the string once to calculate the minimum number of operations.

**Space Complexity**
O(1), as we only use a constant amount of space to store the counters and the current operation index.

**Key Insight**
The key insight is that we only need to consider two possible operations, and by toggling the current operation after each iteration, we can effectively explore both possibilities in a single pass through the string. This simplifies the problem and allows us to achieve a linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 98.47%) |
| 💾 Memory | 19.3 MB (Beats 26.7%) |
| 📅 Solved | 2026-03-05 |
| 💻 Language | Python |