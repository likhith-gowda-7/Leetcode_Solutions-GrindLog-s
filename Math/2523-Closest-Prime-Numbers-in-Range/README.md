# 2523. Closest Prime Numbers in Range


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Number Theory](https://img.shields.io/badge/Number%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/closest-prime-numbers-in-range/)


## 📝 Problem Description

Given two positive integers `left` and `right`, find the two integers `num1` and `num2` such that:

	- `left <= num1 < num2 <= right `.

	- Both `num1` and `num2` are prime numbers.

	- `num2 - num1` is the **minimum** amongst all other pairs satisfying the above conditions.

Return the positive integer array `ans = [num1, num2]`. If there are multiple pairs satisfying these conditions, return the one with the **smallest** `num1` value. If no such numbers exist, return `[-1, -1]`*.*

 

Example 1:**

```

**Input:** left = 10, right = 19
**Output:** [11,13]
**Explanation:** The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

```

Example 2:**

```

**Input:** left = 4, right = 6
**Output:** [-1,-1]
**Explanation:** There exists only one prime number in the given range, so the conditions cannot be satisfied.

```

 

**Constraints:**

	- `1 <= left <= right <= 10^6`

 

.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0; 
}
.spoiler {overflow:hidden;}
.spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
.spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
.spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}

## 🧠 Solution Explanation

**Intuition**
The solution uses the Sieve of Eratosthenes algorithm to efficiently find all prime numbers within the given range. It then iterates through the list of primes to find the closest pair with the minimum difference.

**Approach**
1. Create a boolean array `is_prime` of size `right + 1` and initialize all values to `True`.
2. Set `is_prime[0]` and `is_prime[1]` to `False` since 0 and 1 are not prime numbers.
3. Iterate from 2 to the square root of `right` and mark multiples of each prime number as non-prime.
4. Collect all prime numbers in the range `[left, right]` using a list comprehension.
5. If there are less than 2 prime numbers, return `[-1, -1]`.
6. Iterate through the list of primes and find the closest pair with the minimum difference.
7. Return the pair of primes with the minimum difference.

**Time Complexity**
O(n log log n) where n is the upper bound of the range. This is because the Sieve of Eratosthenes algorithm has a time complexity of O(n log log n) and we are iterating through the list of primes once.

**Space Complexity**
O(n) where n is the upper bound of the range. This is because we are creating a boolean array of size `right + 1` and a list of primes of size n.

**Key Insight**
The key insight is to use the Sieve of Eratosthenes algorithm to efficiently find all prime numbers within the given range. This allows us to iterate through the list of primes once to find the closest pair with the minimum difference, resulting in a time complexity of O(n log log n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1670 ms (Beats 41.03%) |
| 💾 Memory | 35.2 MB (Beats 48.4%) |
| 📅 Solved | 2025-03-08 |
| 💻 Language | Python |