> 📌 **Cross-listed:** Primary location is [Array/1295-Find-Numbers-with-Even-Number-of-Digits](../../Array/1295-Find-Numbers-with-Even-Number-of-Digits). This problem also appears under: **Array**, **Math**

# 1295. Find Numbers with Even Number of Digits


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)


## 📝 Problem Description

Given an array `nums` of integers, return how many of them contain an **even number** of digits.

 

Example 1:**

```

**Input:** nums = [12,345,2,6,7896]
**Output:** 2
**Explanation: 
**12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

```

Example 2:**

```

**Input:** nums = [555,901,482,1771]
**Output:** 1 
**Explanation: **
Only 1771 contains an even number of digits.

```

 

**Constraints:**

	- `1 <= nums.length <= 500`

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through each number in the input array, converting it to a string to easily determine the number of digits, and then checking if the number of digits is even. If it is, the solution increments a counter.

**Approach**
1. Initialize a counter `ans` to 0 to keep track of the numbers with an even number of digits.
2. Iterate through each number `i` in the input array `nums`.
3. Convert the number `i` to a string using `str(i)` to easily determine the number of digits.
4. Calculate the number of digits by getting the length of the string `ch = len(str(i))`.
5. Check if the number of digits is even by using the modulo operator `ch % 2 == 0`.
6. If the number of digits is even, increment the counter `ans` by 1.
7. After iterating through all numbers, return the counter `ans`.

**Time Complexity**
O(n*m), where n is the number of elements in the input array and m is the maximum number of digits in a number. This is because we are iterating through each number and converting it to a string, which takes O(m) time.

**Space Complexity**
O(m), where m is the maximum number of digits in a number. This is because we are converting each number to a string, which takes O(m) space.

**Key Insight**
The key insight is that converting a number to a string allows us to easily determine the number of digits, which is a crucial step in solving this problem. This approach is simple and efficient, making it a good solution for this problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-04-30 |
| 💻 Language | Python |