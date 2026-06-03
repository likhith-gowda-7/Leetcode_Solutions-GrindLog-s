# 1018. Binary Prefix Divisible By 5


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-prefix-divisible-by-5/)


## 📝 Problem Description

You are given a binary array `nums` (**0-indexed**).

We define `x_i` as the number whose binary representation is the subarray `nums[0..i]` (from most-significant-bit to least-significant-bit).

	- For example, if `nums = [1,0,1]`, then `x_0 = 1`, `x_1 = 2`, and `x_2 = 5`.

Return *an array of booleans *`answer`* where *`answer[i]`* is *`true`* if *`x_i`* is divisible by *`5`.

 

Example 1:**

```

**Input:** nums = [0,1,1]
**Output:** [true,false,false]
**Explanation:** The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

```

Example 2:**

```

**Input:** nums = [1,1,1]
**Output:** [false,false,false]

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `nums[i]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution works by simulating the process of constructing a binary number from the input array and checking if the resulting number is divisible by 5. This is done by maintaining a running binary number and updating it with each new bit from the input array. The divisibility check is performed using the modulo operator.

**Approach**
1. Initialize an empty list `res` to store the results and a variable `binary_num` to store the running binary number.
2. Iterate through each bit in the input array `nums`.
3. For each bit, update the `binary_num` by shifting the current value to the left by one bit and adding the new bit.
4. Check if the updated `binary_num` is divisible by 5 by using the modulo operator (`binary_num % 5 == 0`).
5. Append the result of the divisibility check to the `res` list.
6. Return the `res` list.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we are iterating through each bit in the array once.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because we are storing the results in a list of length n.

**Key Insight**
The key insight is that we can simulate the process of constructing a binary number from the input array and checking if the resulting number is divisible by 5 without actually constructing the binary number. This is done by maintaining a running binary number and updating it with each new bit from the input array, allowing us to perform the divisibility check efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 103 ms (Beats 32.9%) |
| 💾 Memory | 19.3 MB (Beats 100%) |
| 📅 Solved | 2025-11-24 |
| 💻 Language | Python |