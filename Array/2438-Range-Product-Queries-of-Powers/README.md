# 2438. Range Product Queries of Powers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/range-product-queries-of-powers/)


## 📝 Problem Description

Given a positive integer `n`, there exists a **0-indexed** array called `powers`, composed of the **minimum** number of powers of `2` that sum to `n`. The array is sorted in **non-decreasing** order, and there is **only one** way to form the array.

You are also given a **0-indexed** 2D integer array `queries`, where `queries[i] = [left_i, right_i]`. Each `queries[i]` represents a query where you have to find the product of all `powers[j]` with `left_i <= j <= right_i`.

Return* an array *`answers`*, equal in length to *`queries`*, where *`answers[i]`* is the answer to the *`i^th`* query*. Since the answer to the `i^th` query may be too large, each `answers[i]` should be returned **modulo** `10^9 + 7`.

 

Example 1:**

```

**Input:** n = 15, queries = [[0,1],[2,2],[0,3]]
**Output:** [2,4,64]
**Explanation:**
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 10^9 + 7 yields the same answer, so [2,4,64] is returned.

```

Example 2:**

```

**Input:** n = 2, queries = [[0,0]]
**Output:** [2]
**Explanation:**
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 10^9 + 7 is the same, so [2] is returned.

```

 

**Constraints:**

	- `1 <= n <= 10^9`

	- `1 <= queries.length <= 10^5`

	- `0 <= start_i <= end_i < powers.length`

## 🧠 Solution Explanation

**Intuition**
The solution works by first generating the array of powers of 2 that sum to `n` using a binary representation of `n`. Then, it calculates the product of all powers within each query range using prefix sums and modular arithmetic.

**Approach**
1. Convert `n` to binary and store it in the `binary` string.
2. Initialize an empty list `powers` to store the powers of 2 that sum to `n`.
3. Iterate through the reversed binary string. If a bit is 1, calculate the corresponding power of 2 and append it to `powers`. If the list is not empty, multiply the new power by the last element in `powers`.
4. Initialize an empty list `res` to store the results of the queries.
5. Iterate through each query in `queries`. For each query, calculate the product of all powers within the range by dividing the power at the end of the range by the power at the start of the range (if the start is not 0). Take the result modulo `10^9 + 7` to avoid overflow.
6. Append the result to `res`.

**Time Complexity**
O(n + q), where n is the number of bits in the binary representation of `n` and q is the number of queries. This is because we iterate through the binary string once to generate `powers`, and then through each query to calculate the result.

**Space Complexity**
O(n + q), where n is the number of bits in the binary representation of `n` and q is the number of queries. This is because we store the powers in a list of size n and the results in a list of size q.

**Key Insight**
The key insight is that the powers of 2 that sum to `n` can be generated efficiently using a binary representation of `n`. By iterating through the reversed binary string, we can calculate the powers in a single pass. This approach allows us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 55 ms (Beats 78.19%) |
| 💾 Memory | 48.3 MB (Beats 93.98%) |
| 📅 Solved | 2025-08-11 |
| 💻 Language | Python |