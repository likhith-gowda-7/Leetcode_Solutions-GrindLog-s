# 3336. Find the Number of Subsequences With Equal GCD


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Number Theory](https://img.shields.io/badge/Number%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/)


## 📝 Problem Description

You are given an integer array `nums`.

Your task is to find the number of pairs of **non-empty** subsequences `(seq1, seq2)` of `nums` that satisfy the following conditions:

	- The subsequences `seq1` and `seq2` are **disjoint**, meaning **no index** of `nums` is common between them.

	- The GCD of the elements of `seq1` is equal to the GCD of the elements of `seq2`.

Return the total number of such pairs.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

 

Example 1:**

**Input:** nums = [1,2,3,4]

**Output:** 10

**Explanation:**

The subsequence pairs which have the GCD of their elements equal to 1 are:

	- `([**1**, 2, 3, 4], [1, **2**, **3**, 4])`

	- `([**1**, 2, 3, 4], [1, **2**, **3**, **4**])`

	- `([**1**, 2, 3, 4], [1, 2, **3**, **4**])`

	- `([**1**, **2**, 3, 4], [1, 2, **3**, **4**])`

	- `([**1**, 2, 3, **4**], [1, **2**, **3**, 4])`

	- `([1, **2**, **3**, 4], [**1**, 2, 3, 4])`

	- `([1, **2**, **3**, 4], [**1**, 2, 3, **4**])`

	- `([1, **2**, **3**, **4**], [**1**, 2, 3, 4])`

	- `([1, 2, **3**, **4**], [**1**, 2, 3, 4])`

	- `([1, 2, **3**, **4**], [**1**, **2**, 3, 4])`

Example 2:**

**Input:** nums = [10,20,30]

**Output:** 2

**Explanation:**

The subsequence pairs which have the GCD of their elements equal to 10 are:

	- `([**10**, 20, 30], [10, **20**, **30**])`

	- `([10, **20**, **30**], [**10**, 20, 30])`

Example 3:**

**Input:** nums = [1,1,1,1]

**Output:** 50

 

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 200`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes dynamic programming and memoization to efficiently count the number of subsequence pairs with equal GCD. The key insight is to break down the problem into smaller subproblems by considering each element in the array and deciding whether to include it in the first or second subsequence.

**Approach**
1. Define a helper function `solve(i, g1, g2)` that takes the current index `i`, the GCD of the first subsequence `g1`, and the GCD of the second subsequence `g2`.
2. If the current index `i` is greater than or equal to the length of the array `n`, return 1 if `g1` is non-zero and equal to `g2`, and 0 otherwise (base case).
3. Skip the current element by recursively calling `solve(i+1, g1, g2)`.
4. Consider including the current element in the first subsequence by calculating the new GCD `num1` and recursively calling `solve(i+1, num1, g2)`.
5. Consider including the current element in the second subsequence by calculating the new GCD `num2` and recursively calling `solve(i+1, g1, num2)`.
6. Return the total count modulo `10^9 + 7`.

**Time Complexity**
The time complexity is O(n * 2^m * log(m)), where n is the length of the array and m is the maximum possible GCD. This is because we have at most 2^m possible GCD values, and for each GCD value, we perform a recursive call with a time complexity of O(n).

**Space Complexity**
The space complexity is O(n * 2^m * log(m)), where n is the length of the array and m is the maximum possible GCD. This is because we use a memoization table to store the results of subproblems, which requires O(n * 2^m * log(m)) space.

**Key Insight**
The key insight is to break down the problem into smaller subproblems by considering each element in the array and deciding whether to include it in the first or second subsequence. This allows us to efficiently count the number of subsequence pairs with equal GCD using dynamic programming and memoization.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3434 ms (Beats 31.82%) |
| 💾 Memory | 592.3 MB (Beats 18.18%) |
| 📅 Solved | 2026-07-15 |
| 💻 Language | Python |