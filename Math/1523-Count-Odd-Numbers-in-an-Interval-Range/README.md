# 1523. Count Odd Numbers in an Interval Range


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)


## 📝 Problem Description

Given two non-negative integers `low` and `high`. Return the *count of odd numbers between *`low`* and *`high`* (inclusive)*.



 


Example 1:**



```

**Input:** low = 3, high = 7
**Output:** 3
**Explanation: **The odd numbers between 3 and 7 are [3,5,7].
```


Example 2:**



```

**Input:** low = 8, high = 10
**Output:** 1
**Explanation: **The odd numbers between 8 and 10 are [9].
```


 


**Constraints:**




	- `0 <= low <= high <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the fact that the number of odd numbers between two numbers is equal to the difference between the number of odd numbers up to the higher number and the number of odd numbers up to the lower number. This is because the difference between the two numbers is always an even number, and when subtracting an even number from an odd number, the result is always an odd number.

**Approach**
1. Calculate the number of odd numbers up to `high` by dividing `high` by 2 and rounding up to the nearest integer using `math.ceil`.
2. Calculate the number of odd numbers up to `low` by dividing `low` by 2 and rounding up to the nearest integer using `math.ceil`.
3. Calculate the absolute difference between the two numbers of odd numbers.
4. If `low` is an odd number, add 1 to the result because `low` itself is an odd number.

**Time Complexity**
O(1) - The solution only involves a constant number of operations, regardless of the input size.

**Space Complexity**
O(1) - The solution only uses a constant amount of space to store the variables `left`, `right`, and `res`.

**Key Insight**
The key insight is that the number of odd numbers between two numbers can be calculated by finding the difference between the number of odd numbers up to the higher number and the number of odd numbers up to the lower number. This is a clever way to avoid iterating over the range of numbers, making the solution very efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 32 ms (Beats 98.22%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-12-07 |
| 💻 Language | Python |