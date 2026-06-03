> 📌 **Cross-listed:** Primary location is [Array/2553-Separate-the-Digits-in-an-Array](../../Array/2553-Separate-the-Digits-in-an-Array). This problem also appears under: **Array**, **Simulation**

# 2553. Separate the Digits in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/separate-the-digits-in-an-array/)


## 📝 Problem Description

Given an array of positive integers `nums`, return *an array *`answer`* that consists of the digits of each integer in *`nums`* after separating them in **the same order** they appear in *`nums`.

To separate the digits of an integer is to get all the digits it has in the same order.

	- For example, for the integer `10921`, the separation of its digits is `[1,0,9,2,1]`.

 

Example 1:**

```

**Input:** nums = [13,25,83,77]
**Output:** [1,3,2,5,8,3,7,7]
**Explanation:** 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

```

Example 2:**

```

**Input:** nums = [7,1,3,9]
**Output:** [7,1,3,9]
**Explanation:** The separation of each integer in nums is itself.
answer = [7,1,3,9].

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over each number in the input array, separating its digits, and appending them to the result array in the same order. This approach leverages a helper function to reverse the digits of each number, effectively "separating" them.

**Approach**
1. Initialize an empty result array `res`.
2. Define a helper function `rev(num)` that takes an integer `num` as input and separates its digits.
   - Initialize an empty deque `curr`.
   - While `num` is greater than 0, extract the last digit using `num % 10` and append it to the front of `curr` using `appendleft()`.
   - Remove the last digit from `num` using integer division `num //= 10`.
   - Extend the result array `res` with the digits in `curr`.
3. Iterate over each number in the input array `nums`.
4. Call the `rev(num)` function for each number to separate its digits and append them to the result array.
5. Return the result array.

**Time Complexity**
O(n*m), where n is the number of elements in the input array `nums` and m is the maximum number of digits in any integer. This is because we iterate over each number in the array and separate its digits, which takes O(m) time for each number.

**Space Complexity**
O(n*m), where n is the number of elements in the input array `nums` and m is the maximum number of digits in any integer. This is because we store the separated digits of each number in the result array, which can grow up to O(n*m) in the worst case.

**Key Insight**
The key insight is to use a helper function to separate the digits of each number, which allows us to reuse the same logic for each number in the input array. This approach simplifies the code and makes it more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 75.42%) |
| 💾 Memory | 19.6 MB (Beats 16.54%) |
| 📅 Solved | 2026-05-11 |
| 💻 Language | Python |