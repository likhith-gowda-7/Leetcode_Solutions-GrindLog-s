# 1323. Maximum 69 Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-69-number/)


## 📝 Problem Description

You are given a positive integer `num` consisting only of digits `6` and `9`.

Return *the maximum number you can get by changing **at most** one digit (*`6`* becomes *`9`*, and *`9`* becomes *`6`*)*.

 

Example 1:**

```

**Input:** num = 9669
**Output:** 9969
**Explanation:** 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

```

Example 2:**

```

**Input:** num = 9996
**Output:** 9999
**Explanation:** Changing the last digit 6 to 9 results in the maximum number.

```

Example 3:**

```

**Input:** num = 9999
**Output:** 9999
**Explanation:** It is better not to apply any change.

```

 

**Constraints:**

	- `1 <= num <= 10^4`

	- `num` consists of only `6` and `9` digits.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the digits of the input number from left to right. As soon as it encounters a '6', it immediately changes it to '9' and returns the modified number. This approach ensures that the maximum number is achieved by changing at most one digit.

**Approach**
1. Convert the input number to a string to easily access and modify its digits.
2. Initialize an empty string `curr` to store the modified digits.
3. Iterate through the digits of the string from left to right.
4. If the current digit is '6', change it to '9' and break the loop.
5. If the current digit is not '6', add it to the `curr` string.
6. After the loop, append the remaining digits (if any) to the `curr` string.
7. Convert the `curr` string back to an integer and return it.

**Time Complexity**
O(n), where n is the number of digits in the input number. This is because we are iterating through the digits of the number once.

**Space Complexity**
O(n), where n is the number of digits in the input number. This is because we are storing the modified digits in the `curr` string.

**Key Insight**
The key insight is that we only need to change the first occurrence of '6' to '9' to achieve the maximum number. This is because changing any other '6' would result in a smaller number. By breaking the loop as soon as we encounter a '6', we ensure that we only change one digit.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-08-16 |
| 💻 Language | Python |