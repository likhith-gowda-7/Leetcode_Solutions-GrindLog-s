> 📌 **Cross-listed:** Primary location is [Hash Table/0013-Roman-to-Integer](../../Hash-Table/0013-Roman-to-Integer). This problem also appears under: **Hash Table**, **Math**, **String**

# 13. Roman to Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/roman-to-integer/)


## 📝 Problem Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```

**Symbol**       **Value**
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

	- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 

	- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 

	- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

Example 1:**

```

**Input:** s = "III"
**Output:** 3
**Explanation:** III = 3.

```

Example 2:**

```

**Input:** s = "LVIII"
**Output:** 58
**Explanation:** L = 50, V= 5, III = 3.

```

Example 3:**

```

**Input:** s = "MCMXCIV"
**Output:** 1994
**Explanation:** M = 1000, CM = 900, XC = 90 and IV = 4.

```

 

**Constraints:**

	- `1 <= s.length <= 15`

	- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.

	- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over the Roman numeral string from left to right, keeping track of the previous numeral's value. If the current numeral's value is greater than the previous one, it means we need to subtract the previous value from the result (because in Roman numerals, a smaller numeral placed before a larger one means subtraction). Otherwise, we simply add the current value to the result.

**Approach**
1. Create a dictionary to map Roman numerals to their integer values.
2. Initialize a variable `res` to store the final result and `prev` to store the value of the previous numeral.
3. Iterate over the input string `s` from left to right.
4. For each numeral, get its value from the dictionary and store it in `curr`.
5. If `curr` is greater than `prev`, subtract `prev` from `res` and add `curr - prev` to `res`. Otherwise, add `curr` to `res`.
6. Update `prev` to be the value of the current numeral.
7. After iterating over the entire string, return the final result `res`.

**Time Complexity**
O(n), where n is the length of the input string. This is because we only need to iterate over the string once to calculate the result.

**Space Complexity**
O(1), excluding the input string. We only use a constant amount of space to store the dictionary and the variables `res` and `prev`.

**Key Insight**
The key insight here is that we can take advantage of the fact that Roman numerals use subtraction to represent certain values. By keeping track of the previous numeral's value, we can efficiently calculate the result by adding or subtracting the current value as needed. This approach avoids the need for explicit handling of each possible combination of numerals.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 81.14%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-21 |
| 💻 Language | Python |