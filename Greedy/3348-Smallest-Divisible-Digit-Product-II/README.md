> 📌 **Cross-listed:** Primary location is [Math/3348-Smallest-Divisible-Digit-Product-II](../../Math/3348-Smallest-Divisible-Digit-Product-II). This problem also appears under: **Math**, **String**, **Backtracking**, **Greedy**, **Number Theory**

# 3348. Smallest Divisible Digit Product II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-ii/)


## 📝 Problem Description

You are given a string `num` which represents a **positive** integer, and an integer `t`.

A number is called **zero-free** if *none* of its digits are 0.

Return a string representing the **smallest** **zero-free** number greater than or equal to `num` such that the **product of its digits** is divisible by `t`. If no such number exists, return `"-1"`.

 

Example 1:**

**Input:** num = "1234", t = 256

**Output:** "1488"

**Explanation:**

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:**

**Input:** num = "12355", t = 50

**Output:** "12355"

**Explanation:**

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:**

**Input:** num = "11111", t = 26

**Output:** "-1"

**Explanation:**

No number greater than 11111 has the product of its digits divisible by 26.

 

**Constraints:**

	- `2 <= num.length <= 2 * 10^5`

	- `num` consists only of digits in the range `['0', '9']`.

	- `num` does not contain leading zeros.

	- `1 <= t <= 10^14`

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming to find the smallest zero-free number that meets the given conditions. It first calculates the prime factorization of the target product `t` and uses this information to construct the desired number. The solution also uses a greedy approach to minimize the number of digits in the constructed number.

**Approach**
1. Calculate the prime factorization of `t` and store the required number of each prime factor in `req2`, `req3`, `req5`, and `req7`.
2. Initialize a 2D dynamic programming table `dp` to store the minimum number of digits required to construct a zero-free number with a certain number of 2's and 3's.
3. Fill the `dp` table using a breadth-first search approach, where each cell represents the minimum number of digits required to construct a zero-free number with a certain number of 2's and 3's.
4. If the input number `num` is already zero-free and has a product of digits divisible by `t`, return `num`.
5. If `num` has a zero, find the first zero and calculate the number of 2's, 3's, 5's, and 7's required to construct the desired number.
6. Iterate through the digits of `num` from left to right, and for each digit, calculate the number of 2's, 3's, 5's, and 7's required to construct the desired number.
7. If the current digit can be replaced with a larger digit to meet the required number of 2's, 3's, 5's, and 7's, update the answer accordingly.
8. If the current digit cannot be replaced, construct the remaining digits of the desired number using a greedy approach.

**Time Complexity**
O(n \* 10^4), where n is the length of the input number `num`. The time complexity is dominated by the dynamic programming table `dp`, which has a size of 60 x 40.

**Space Complexity**
O(n \* 10^4), where n is the length of the input number `num`. The space complexity is dominated by the dynamic programming table `dp`, which has a size of 60 x 40.

**Key Insight**
The key insight is to use dynamic programming to efficiently calculate the minimum number of digits required to construct a zero-free number with a certain number of 2's and 3's. This allows us to construct the desired number in a greedy manner, minimizing the number of digits required.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2857 ms (Beats 5.36%) |
| 💾 Memory | 32.3 MB (Beats 87.5%) |
| 📅 Solved | 2026-08-07 |
| 💻 Language | Python |