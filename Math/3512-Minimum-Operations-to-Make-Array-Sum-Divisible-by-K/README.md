> 📌 **Cross-listed:** Primary location is [Array/3512-Minimum-Operations-to-Make-Array-Sum-Divisible-by-K](../../Array/3512-Minimum-Operations-to-Make-Array-Sum-Divisible-by-K). This problem also appears under: **Array**, **Math**

# 3512. Minimum Operations to Make Array Sum Divisible by K


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `k`. You can perform the following operation any number of times:

	- Select an index `i` and replace `nums[i]` with `nums[i] - 1`.

Return the **minimum** number of operations required to make the sum of the array divisible by `k`.

 

Example 1:**

**Input:** nums = [3,9,7], k = 5

**Output:** 4

**Explanation:**

	- Perform 4 operations on `nums[1] = 9`. Now, `nums = [3, 5, 7]`.

	- The sum is 15, which is divisible by 5.

Example 2:**

**Input:** nums = [4,1,3], k = 4

**Output:** 0

**Explanation:**

	- The sum is 8, which is already divisible by 4. Hence, no operations are needed.

Example 3:**

**Input:** nums = [3,2], k = 6

**Output:** 5

**Explanation:**

	- Perform 3 operations on `nums[0] = 3` and 2 operations on `nums[1] = 2`. Now, `nums = [0, 0]`.

	- The sum is 0, which is divisible by 6.

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`

	- `1 <= k <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by leveraging the property of modular arithmetic that if `a ≡ b (mod m)`, then `a + c ≡ b + c (mod m)`. This means that the remainder of the sum of the array elements when divided by `k` is equivalent to the sum of the remainders of each element when divided by `k`. The minimum number of operations required to make the sum of the array divisible by `k` is equivalent to the remainder of the sum of the array elements when divided by `k`.

**Approach**
1. Calculate the sum of the array elements using the built-in `sum()` function.
2. Calculate the remainder of the sum when divided by `k` using the modulo operator `%`.
3. Return the remainder as the minimum number of operations required.

**Time Complexity**
O(n), where n is the number of elements in the array. This is because the `sum()` function iterates over each element in the array once.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the sum and the remainder.

**Key Insight**
The key insight is that the remainder of the sum of the array elements when divided by `k` is equivalent to the minimum number of operations required to make the sum divisible by `k`. This allows us to simplify the problem to a single calculation, making the solution very efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-11-29 |
| 💻 Language | Python |