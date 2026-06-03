# 762. Prime Number of Set Bits in Binary Representation


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)


## 📝 Problem Description

Given two integers `left` and `right`, return *the **count** of numbers in the **inclusive** range *`[left, right]`* having a **prime number of set bits** in their binary representation*.

Recall that the **number of set bits** an integer has is the number of `1`'s present when written in binary.

	- For example, `21` written in binary is `10101`, which has `3` set bits.

 

Example 1:**

```

**Input:** left = 6, right = 10
**Output:** 4
**Explanation:**
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.

```

Example 2:**

```

**Input:** left = 10, right = 15
**Output:** 5
**Explanation:**
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.

```

 

**Constraints:**

	- `1 <= left <= right <= 10^6`

	- `0 <= right - left <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the given range and checking if the number of set bits in the binary representation of each number is a prime number. This is done by using a set of known prime numbers to quickly check if the number of set bits is prime.

**Approach**
1. Define a set of known prime numbers (`primes`).
2. Initialize a counter (`res`) to keep track of the numbers with a prime number of set bits.
3. Iterate through the range from `left` to `right` (inclusive) using a for loop.
4. For each number `i` in the range, use the `bit_count()` method to get the number of set bits in its binary representation.
5. Check if the number of set bits is in the set of known prime numbers (`primes`). If it is, increment the counter (`res`).
6. After iterating through the entire range, return the counter (`res`).

**Time Complexity**
O(n), where n is the range from `left` to `right` (inclusive). This is because we are iterating through the range once.

**Space Complexity**
O(1), excluding the input, because we are using a fixed-size set of known prime numbers, regardless of the input size.

**Key Insight**
The key insight is that we only need to check if the number of set bits is in a set of known prime numbers, which makes the solution efficient. This is possible because the number of set bits in a binary representation can only be a small number, and we can precompute the set of prime numbers up to that maximum value.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 24 ms (Beats 92.24%) |
| 💾 Memory | 19.3 MB (Beats 55.17%) |
| 📅 Solved | 2026-02-21 |
| 💻 Language | Python |