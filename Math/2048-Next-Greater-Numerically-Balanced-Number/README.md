> 📌 **Cross-listed:** Primary location is [Hash Table/2048-Next-Greater-Numerically-Balanced-Number](../../Hash-Table/2048-Next-Greater-Numerically-Balanced-Number). This problem also appears under: **Hash Table**, **Math**, **Backtracking**, **Counting**, **Enumeration**

# 2048. Next Greater Numerically Balanced Number


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/next-greater-numerically-balanced-number/)


## 📝 Problem Description

An integer `x` is **numerically balanced** if for every digit `d` in the number `x`, there are **exactly** `d` occurrences of that digit in `x`.

Given an integer `n`, return *the **smallest numerically balanced** number **strictly greater** than *`n`*.*

 

Example 1:**

```

**Input:** n = 1
**Output:** 22
**Explanation:** 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.

```

Example 2:**

```

**Input:** n = 1000
**Output:** 1333
**Explanation:** 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.

```

Example 3:**

```

**Input:** n = 3000
**Output:** 3133
**Explanation:** 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.

```

 

**Constraints:**

	- `0 <= n <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution uses a helper function `find` to check if a number is numerically balanced. It then iterates through numbers starting from `n+1` and returns the first numerically balanced number found. The key insight is that we can generate numerically balanced numbers by incrementing the count of each digit in the number.

**Approach**
1. Define a helper function `find` that takes a number `num` as input and returns `True` if the number is numerically balanced, `False` otherwise.
2. Initialize a count array `count` of size 10 to store the frequency of each digit in the number.
3. Iterate through the digits of the number from right to left, updating the count array accordingly.
4. Check if the count of any digit `i` is greater than 0 and not equal to `i`. If so, return `False`.
5. If the count of the digit 0 is greater than 0, return `False`.
6. If the number passes all checks, return `True`.
7. Iterate through numbers starting from `n+1` and use the `find` function to check if each number is numerically balanced.
8. Return the first numerically balanced number found.

**Time Complexity**
O(n \* log(n)) where n is the number of digits in the input number. This is because we iterate through numbers starting from `n+1` and for each number, we iterate through its digits to check if it's numerically balanced.

**Space Complexity**
O(1) because we use a fixed-size array `count` to store the frequency of each digit, regardless of the size of the input number.

**Key Insight**
The key insight is that we can generate numerically balanced numbers by incrementing the count of each digit in the number. This is because a numerically balanced number must have exactly `d` occurrences of the digit `d` for each digit `d` in the number. By incrementing the count of each digit, we can systematically generate all possible numerically balanced numbers.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1919 ms (Beats 52.84%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-10-25 |
| 💻 Language | Python |