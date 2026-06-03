> 📌 **Cross-listed:** Primary location is [Array/1390-Four-Divisors](../../Array/1390-Four-Divisors). This problem also appears under: **Array**, **Math**

# 1390. Four Divisors


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/four-divisors/)


## 📝 Problem Description

Given an integer array `nums`, return *the sum of divisors of the integers in that array that have exactly four divisors*. If there is no such integer in the array, return `0`.

 

Example 1:**

```

**Input:** nums = [21,4,7]
**Output:** 32
**Explanation:** 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

```

Example 2:**

```

**Input:** nums = [21,21]
**Output:** 64

```

Example 3:**

```

**Input:** nums = [1,2,3,4,5]
**Output:** 0

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a helper function `find` to calculate the sum of divisors for each number in the input array. It iterates through possible divisors up to the square root of the number, checks for divisors, and returns the sum of divisors if the number has exactly four divisors. The main function iterates through the input array, calls the helper function for each number, and sums up the results.

**Approach**
1. Define a helper function `find` that takes a number `num` and its square root `d` as input.
2. Initialize counters `c` and `curr` to keep track of the number of divisors and the sum of divisors, respectively.
3. Iterate through possible divisors from 1 to `d` (inclusive).
4. For each divisor `i`, check if `num` is divisible by `i` (i.e., `rem == 0`).
5. If `num` is divisible by `i`, increment the counter `c` and add `i` and `diff` (the quotient of `num` and `i`) to `curr`.
6. If the counter `c` exceeds 4, return 0 to avoid unnecessary calculations.
7. After iterating through all possible divisors, return `curr` if `c` equals 4 (indicating exactly four divisors) or 0 otherwise.
8. In the main function, iterate through the input array `nums`.
9. For each number `val` in the array, calculate its square root `s` using `math.floor(math.sqrt(val))`.
10. Call the helper function `find` with `val` and `s` as input and add the result to the running total `res`.
11. Return the final result `res`.

**Time Complexity**
O(n * sqrt(m)), where n is the length of the input array and m is the maximum value in the array. The helper function `find` iterates up to the square root of each number, resulting in a time complexity of O(sqrt(m)) for each number. Since this is done for each number in the array, the overall time complexity is O(n * sqrt(m)).

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the counters `c` and `curr`, regardless of the input size.

**Key Insight**
The key insight is that a number can have at most four divisors if it is a product of two distinct prime numbers. This is because the divisors of such a number are 1, the two prime numbers, and their product. The solution exploits this insight by iterating through possible divisors up to the square root of the number, which is sufficient to find all divisors for numbers with exactly four divisors.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 161 ms (Beats 69.76%) |
| 💾 Memory | 18.8 MB (Beats 100%) |
| 📅 Solved | 2026-01-04 |
| 💻 Language | Python |