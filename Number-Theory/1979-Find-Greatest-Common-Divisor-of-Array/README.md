> 📌 **Cross-listed:** Primary location is [Array/1979-Find-Greatest-Common-Divisor-of-Array](../../Array/1979-Find-Greatest-Common-Divisor-of-Array). This problem also appears under: **Array**, **Math**, **Number Theory**

# 1979. Find Greatest Common Divisor of Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Number Theory](https://img.shields.io/badge/Number%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)


## 📝 Problem Description

Given an integer array `nums`, return** ***the **greatest common divisor** of the smallest number and largest number in *`nums`.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:**

```

**Input:** nums = [2,5,6,9,10]
**Output:** 2
**Explanation:**
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

```

Example 2:**

```

**Input:** nums = [7,5,6,8,3]
**Output:** 1
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

```

Example 3:**

```

**Input:** nums = [3,3]
**Output:** 3
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

```

 

**Constraints:**

	- `2 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the greatest common divisor (GCD) of the smallest and largest numbers in a given array. The GCD of two numbers is the largest positive integer that evenly divides both numbers. This problem can be solved by leveraging the built-in `gcd` function in Python, which calculates the GCD of two numbers.

**Approach**
1. Import the `math` module to access the `gcd` function.
2. Define a class `Solution` with a method `findGCD` that takes an array `nums` as input.
3. Use the built-in `min` and `max` functions to find the smallest and largest numbers in the array, respectively.
4. Pass the smallest and largest numbers to the `gcd` function to find their GCD.

**Time Complexity**
O(1) - The time complexity is constant because the `min`, `max`, and `gcd` functions all operate in constant time.

**Space Complexity**
O(1) - The space complexity is constant because the solution only uses a constant amount of space to store the smallest and largest numbers, as well as the GCD result.

**Key Insight**
The key insight is that the GCD of the smallest and largest numbers in the array is the same as the GCD of the two numbers themselves. This allows us to simplify the problem and use the built-in `gcd` function to find the solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 80.59%) |
| 📅 Solved | 2026-07-18 |
| 💻 Language | Python |