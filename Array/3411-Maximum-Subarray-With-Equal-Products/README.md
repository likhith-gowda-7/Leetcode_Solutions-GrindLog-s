# 3411. Maximum Subarray With Equal Products


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products/)


## 📝 Problem Description

You are given an array of **positive** integers `nums`.

An array `arr` is called **product equivalent** if `prod(arr) == lcm(arr) * gcd(arr)`, where:

	- `prod(arr)` is the product of all elements of `arr`.

	- `gcd(arr)` is the GCD of all elements of `arr`.

	- `lcm(arr)` is the LCM of all elements of `arr`.

Return the length of the **longest** **product equivalent** subarray of `nums`.

 

Example 1:**

**Input:** nums = [1,2,1,2,1,1,1]

**Output:** 5

**Explanation:** 

The longest product equivalent subarray is `[1, 2, 1, 1, 1]`, where `prod([1, 2, 1, 1, 1]) = 2`, `gcd([1, 2, 1, 1, 1]) = 1`, and `lcm([1, 2, 1, 1, 1]) = 2`.

Example 2:**

**Input:** nums = [2,3,4,5,6]

**Output:** 3

**Explanation:** 

The longest product equivalent subarray is `[3, 4, 5].`

Example 3:**

**Input:** nums = [1,2,3,1,4,5,1]

**Output:** 5

 

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 <= nums[i] <= 10`

## 🧠 Solution Explanation

**Intuition**
The solution uses a brute-force approach to find the longest product equivalent subarray by iterating over all possible subarrays and checking if they are product equivalent. This works because the problem only asks for the length of the longest product equivalent subarray, not the subarray itself.

**Approach**
1. Initialize variables to keep track of the longest product equivalent subarray found so far (`longest`).
2. Iterate over the array `nums` using two nested loops to generate all possible subarrays.
3. For each subarray, calculate the product (`p`), GCD (`g`), and LCM (`l`) of the elements.
4. Check if the product is equal to the product of the GCD and LCM (`p == g * l`). If true, update `longest` with the length of the current subarray.
5. After checking all subarrays, return the length of the longest product equivalent subarray found.

**Time Complexity**
O(n^2), where n is the length of the input array `nums`. This is because the solution uses two nested loops to generate all possible subarrays.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the variables `longest`, `p`, `g`, and `l`.

**Key Insight**
The key insight here is that we only need to check if the product of the subarray is equal to the product of the GCD and LCM, which is a much simpler condition than checking if the subarray is product equivalent. This allows us to use a brute-force approach to find the longest product equivalent subarray.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 32 ms (Beats 64.07%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-03-04 |
| 💻 Language | Python |