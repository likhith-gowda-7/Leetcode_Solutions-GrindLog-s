# 3756. Concatenate Non-Zero Digits and Multiply by Sum II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/)


## 📝 Problem Description

You are given a string `s` of length `m` consisting of digits. You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

For each `queries[i]`, extract the **substring** `s[l_i..r_i]`. Then, perform the following:

	- Form a new integer `x` by concatenating all the **non-zero digits** from the substring in their original order. If there are no non-zero digits, `x = 0`.

	- Let `sum` be the **sum of digits** in `x`. The answer is `x * sum`.

Return an array of integers `answer` where `answer[i]` is the answer to the `i^th` query.

Since the answers may be very large, return them **modulo** `10^9 + 7`.

 

Example 1:**

**Input:** s = "10203004", queries = [[0,7],[1,3],[4,6]]

**Output:** [12340, 4, 9]

**Explanation:**

	- `s[0..7] = "10203004"`

	
		- `x = 1234`

		- `sum = 1 + 2 + 3 + 4 = 10`

		- Therefore, answer is `1234 * 10 = 12340`.

	
	

	- `s[1..3] = "020"`
	
		- `x = 2`

		- `sum = 2`

		- Therefore, the answer is `2 * 2 = 4`.

	
	

	- `s[4..6] = "300"`
	
		- `x = 3`

		- `sum = 3`

		- Therefore, the answer is `3 * 3 = 9`.

	
	

Example 2:**

**Input:** s = "1000", queries = [[0,3],[1,1]]

**Output:** [1, 0]

**Explanation:**

	- `s[0..3] = "1000"`

	
		- `x = 1`

		- `sum = 1`

		- Therefore, the answer is `1 * 1 = 1`.

	
	

	- `s[1..1] = "0"`
	
		- `x = 0`

		- `sum = 0`

		- Therefore, the answer is `0 * 0 = 0`.

	
	

Example 3:**

**Input:** s = "9876543210", queries = [[0,9]]

**Output:** [444444137]

**Explanation:**

	- `s[0..9] = "9876543210"`

	
		- `x = 987654321`

		- `sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45`

		- Therefore, the answer is `987654321 * 45 = 44444444445`.

		- We return `44444444445 modulo (10^9 + 7) = 444444137`.

	
	

 

**Constraints:**

	- `1 <= m == s.length <= 10^5`

	- `s` consists of digits only.

	- `1 <= queries.length <= 10^5`

	- `queries[i] = [l_i, r_i]`

	- `0 <= l_i <= r_i < m`

## 🧠 Solution Explanation

**Intuition**
The solution uses a prefix sum and prefix value array to efficiently calculate the concatenated non-zero digits and their sum for each query. By storing the prefix sum of digits, prefix count of non-zero digits, and prefix value of non-zero digits, we can calculate the result for each query in constant time.

**Approach**
1. Initialize arrays to store prefix sum, prefix value, and prefix count of digits.
2. Calculate prefix sum, prefix value, and prefix count for each digit in the string.
3. For each query, calculate the length of non-zero digits, start and end values of non-zero digits, and the sum of digits.
4. Calculate the result for each query by multiplying the concatenated non-zero digits by their sum modulo 10^9 + 7.

**Time Complexity**
O(m + n), where m is the number of queries and n is the length of the string. This is because we are iterating over the string once to calculate the prefix sum, prefix value, and prefix count, and then iterating over each query to calculate the result.

**Space Complexity**
O(n), where n is the length of the string. This is because we are storing the prefix sum, prefix value, and prefix count arrays of size n + 1.

**Key Insight**
The key insight is to use prefix sum and prefix value arrays to efficiently calculate the concatenated non-zero digits and their sum for each query. By storing the prefix sum and prefix value, we can calculate the result for each query in constant time, resulting in a time complexity of O(m + n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 504 ms (Beats 48.15%) |
| 💾 Memory | 57.6 MB (Beats 33.33%) |
| 📅 Solved | 2026-07-08 |
| 💻 Language | Python |