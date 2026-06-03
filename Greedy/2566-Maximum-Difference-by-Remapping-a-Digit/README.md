> 📌 **Cross-listed:** Primary location is [Math/2566-Maximum-Difference-by-Remapping-a-Digit](../../Math/2566-Maximum-Difference-by-Remapping-a-Digit). This problem also appears under: **Math**, **Greedy**

# 2566. Maximum Difference by Remapping a Digit


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/)


## 📝 Problem Description

You are given an integer `num`. You know that Bob will sneakily **remap** one of the `10` possible digits (`0` to `9`) to another digit.

Return *the difference between the maximum and minimum values Bob can make by remapping **exactly** **one** digit in *`num`.

**Notes:**

	- When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of `d1` in `num` with `d2`.

	- Bob can remap a digit to itself, in which case `num` does not change.

	- Bob can remap different digits for obtaining minimum and maximum values respectively.

	- The resulting number after remapping can contain leading zeroes.

 

**Example 1:**

```

**Input:** num = 11891
**Output:** 99009
**Explanation:** 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.

```

**Example 2:**

```

**Input:** num = 90
**Output:** 99
**Explanation:**
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
```

 

**Constraints:**

	- `1 <= num <= 10^8`

## 🧠 Solution Explanation

**Intuition**
The solution works by finding the maximum and minimum values that can be obtained by remapping exactly one digit in the given number. The key insight is that we can achieve the maximum value by remapping the smallest digit to the largest digit, and the minimum value by remapping the largest digit to the smallest digit.

**Approach**
1. Convert the input number to a string to easily access and manipulate its digits.
2. Define a helper function `check` that takes three parameters: the string representation of the number, the digit to be changed (initially `None`), and the digit to replace with (either "0" or "9").
3. Iterate through each digit in the string representation of the number.
4. If the digit to be changed is `None` and the current digit is not the digit to find, update the digit to be changed.
5. If the digit to be changed is not `None` and the current digit is the digit to be changed, replace it with the digit to replace with.
6. Return the integer value of the modified string.
7. Call the `check` function twice: once with "9" as the digit to replace with (to get the maximum value) and once with "0" as the digit to replace with (to get the minimum value).
8. Return the difference between the maximum and minimum values.

**Time Complexity**
O(n), where n is the number of digits in the input number. This is because we iterate through each digit in the string representation of the number once.

**Space Complexity**
O(n), where n is the number of digits in the input number. This is because we create a new string representation of the number for each possible remapping.

**Key Insight**
The key insight is that we can achieve the maximum value by remapping the smallest digit to the largest digit, and the minimum value by remapping the largest digit to the smallest digit. This allows us to simplify the problem and find the solution efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-06-14 |
| 💻 Language | Python |