# 401. Binary Watch


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-watch/)


## 📝 Problem Description

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

	- For example, the below binary watch reads `"4:51"`.

![](https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg)

Given an integer `turnedOn` which represents the number of LEDs that are currently on (ignoring the PM), return *all possible times the watch could represent*. You may return the answer in **any order**.

The hour must not contain a leading zero.

	- For example, `"01:00"` is not valid. It should be `"1:00"`.

The minute must consist of two digits and may contain a leading zero.

	- For example, `"10:2"` is not valid. It should be `"10:02"`.

 

Example 1:**

```
**Input:** turnedOn = 1
**Output:** ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

```
Example 2:**

```
**Input:** turnedOn = 9
**Output:** []

```

 

**Constraints:**

	- `0 <= turnedOn <= 10`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over all possible hour and minute combinations, counting the number of set bits in the binary representation of each, and adding the times to the result list if the number of set bits matches the given `turnedOn` value.

**Approach**
1. Initialize an empty list `res` to store the valid times.
2. Iterate over all possible hours (0-11) and minutes (0-59).
3. For each hour and minute, convert them to binary using the `bin()` function.
4. Count the number of set bits in the binary representation of the hour and minute using the `count("1")` method.
5. If the total number of set bits matches the given `turnedOn` value, format the time as a string and add it to the result list.
6. Return the result list.

**Time Complexity**
O(12 * 60 * 2) = O(1440)
Justification: We iterate over all possible hour and minute combinations (12 * 60), and for each combination, we perform a constant-time operation to count the number of set bits in the binary representation.

**Space Complexity**
O(1440)
Justification: In the worst case, we store all possible times in the result list, which has a maximum size of 1440 (12 hours * 60 minutes * 2 for the colon).

**Key Insight**
The key insight is that we can count the number of set bits in the binary representation of a number using the `count("1")` method, which makes it easy to check if the number of set bits matches the given `turnedOn` value. This approach avoids the need for complex bit manipulation or recursion.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 50.87%) |
| 📅 Solved | 2026-02-17 |
| 💻 Language | Python |