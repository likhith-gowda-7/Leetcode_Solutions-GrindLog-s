# 3461. Check If Digits Are Equal in String After Operations I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple) ![Combinatorics](https://img.shields.io/badge/Combinatorics-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/)


## 📝 Problem Description

You are given a string `s` consisting of digits. Perform the following operation repeatedly until the string has **exactly** two digits:

	- For each pair of consecutive digits in `s`, starting from the first digit, calculate a new digit as the sum of the two digits **modulo** 10.

	- Replace `s` with the sequence of newly calculated digits, *maintaining the order* in which they are computed.

Return `true` if the final two digits in `s` are the **same**; otherwise, return `false`.

 

Example 1:**

**Input:** s = "3902"

**Output:** true

**Explanation:**

	- Initially, `s = "3902"`

	- First operation:
	
		- `(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2`

		- `(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9`

		- `(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2`

		- `s` becomes `"292"`

	
	

	- Second operation:
	
		- `(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1`

		- `(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1`

		- `s` becomes `"11"`

	
	

	- Since the digits in `"11"` are the same, the output is `true`.

Example 2:**

**Input:** s = "34789"

**Output:** false

**Explanation:**

	- Initially, `s = "34789"`.

	- After the first operation, `s = "7157"`.

	- After the second operation, `s = "862"`.

	- After the third operation, `s = "48"`.

	- Since `'4' != '8'`, the output is `false`.

 

**Constraints:**

	- `3 <= s.length <= 100`

	- `s` consists of only digits.

## 🧠 Solution Explanation

**Intuition**
The solution works by simulating the repeated operation of calculating the sum of consecutive digits modulo 10 until the string has exactly two digits. The key insight is that the final two digits will be the same if and only if the sequence of operations leads to a cycle where the first two digits repeat.

**Approach**
1. Convert the input string to a list of integers for easier manipulation.
2. Initialize a while loop that continues until the list has exactly two elements.
3. Inside the loop, create a new list `curr` to store the newly calculated digits.
4. Iterate over the list (excluding the first element) and calculate the sum of each pair of consecutive digits modulo 10.
5. Append the calculated digit to the `curr` list.
6. Update the original list `num` with the `curr` list and decrement the length `n` by 1.
7. Repeat steps 3-6 until the list has exactly two elements.
8. Return `True` if the first two elements are the same, and `False` otherwise.

**Time Complexity**
O(n^2), where n is the length of the input string. This is because in the worst case, we need to iterate over the list n-1 times, and within each iteration, we iterate over the list n-1 times.

**Space Complexity**
O(n), where n is the length of the input string. This is because we need to store the list of integers and the temporary list `curr`.

**Key Insight**
The key insight is that the final two digits will be the same if and only if the sequence of operations leads to a cycle where the first two digits repeat. This is because the operation of calculating the sum of consecutive digits modulo 10 is a deterministic function, and if the sequence repeats, the final two digits will be the same.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 90.91%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-10-23 |
| 💻 Language | Python |