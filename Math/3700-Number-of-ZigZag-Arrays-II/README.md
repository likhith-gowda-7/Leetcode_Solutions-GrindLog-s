# 3700. Number of ZigZag Arrays II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-ii/)


## 📝 Problem Description

You are given three integers `n`, `l`, and `r`.

A **ZigZag** array of length `n` is defined as follows:

	- Each element lies in the range `[l, r]`.

	- No **two** adjacent elements are equal.

	- No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.

Return the total number of valid **ZigZag** arrays.

Since the answer may be large, return it **modulo** `10^9 + 7`.

A **sequence** is said to be **strictly increasing** if each element is strictly greater than its previous one (if exists).

A **sequence** is said to be **strictly decreasing** if each element is strictly smaller than its previous one (if exists).

 

Example 1:**

**Input:** n = 3, l = 4, r = 5

**Output:** 2

**Explanation:**

There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`:

	- `[4, 5, 4]`

	- `[5, 4, 5]`

Example 2:**

**Input:** n = 3, l = 1, r = 3

**Output:** 10

**Explanation:**

​​​​​​​There are 10 valid ZigZag arrays of length `n = 3` using values in the range `[1, 3]`:

	- `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`

	- `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`

	- `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]`

All arrays meet the ZigZag conditions.

 

**Constraints:**

	- `3 <= n <= 10^9`

	- `1 <= l < r <= 75`​​​​​​​

## 🧠 Solution Explanation

**Intuition**
The problem asks us to count the number of valid ZigZag arrays of length `n` with elements in the range `[l, r]`. A valid ZigZag array is defined as a sequence where no two adjacent elements are equal, and no three consecutive elements form a strictly increasing or strictly decreasing sequence. We can use dynamic programming to solve this problem by representing the valid arrays as a matrix and performing matrix exponentiation to calculate the total number of valid arrays.

**Approach**
1. Initialize a matrix `T` of size `sz x sz`, where `sz = 2 * m` and `m = r - l + 1`. The matrix `T` represents the valid arrays of length 2.
2. Populate the matrix `T` by setting `T[x][m + y] = 1` for `x < y` and `T[m + x][y] = 1` for `x > y`. This represents the valid arrays of length 2.
3. Initialize a result matrix `result` of size `sz x sz` with all elements set to 1.
4. Perform matrix exponentiation to calculate the total number of valid arrays of length `n`. We use the formula `result = T^(n-1)`.
5. Calculate the sum of each row in the `result` matrix and add it to the answer. The answer is the total number of valid arrays modulo `10^9 + 7`.

**Time Complexity**
The time complexity of this solution is O(n * m^3), where n is the length of the array and m is the size of the matrix. This is because we perform matrix multiplication `n-1` times, and each matrix multiplication takes O(m^3) time.

**Space Complexity**
The space complexity of this solution is O(m^2), which is the size of the matrices `T` and `result`.

**Key Insight**
The key insight behind this solution is to represent the valid arrays as a matrix and perform matrix exponentiation to calculate the total number of valid arrays. This allows us to take advantage of the properties of matrix exponentiation to efficiently calculate the result.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 9561 ms (Beats 20.93%) |
| 💾 Memory | 20.9 MB (Beats 29.57%) |
| 📅 Solved | 2026-06-24 |
| 💻 Language | Python |