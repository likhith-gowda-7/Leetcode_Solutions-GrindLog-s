> 📌 **Cross-listed:** Primary location is [Array/3314-Construct-the-Minimum-Bitwise-Array-I](../../Array/3314-Construct-the-Minimum-Bitwise-Array-I). This problem also appears under: **Array**, **Bit Manipulation**

# 3314. Construct the Minimum Bitwise Array I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/)


## 📝 Problem Description

You are given an array `nums` consisting of `n` prime integers.

You need to construct an array `ans` of length `n`, such that, for each index `i`, the bitwise `OR` of `ans[i]` and `ans[i] + 1` is equal to `nums[i]`, i.e. `ans[i] OR (ans[i] + 1) == nums[i]`.

Additionally, you must **minimize** each value of `ans[i]` in the resulting array.

If it is *not possible* to find such a value for `ans[i]` that satisfies the **condition**, then set `ans[i] = -1`.

 

Example 1:**

**Input:** nums = [2,3,5,7]

**Output:** [-1,1,4,3]

**Explanation:**

	- For `i = 0`, as there is no value for `ans[0]` that satisfies `ans[0] OR (ans[0] + 1) = 2`, so `ans[0] = -1`.

	- For `i = 1`, the smallest `ans[1]` that satisfies `ans[1] OR (ans[1] + 1) = 3` is `1`, because `1 OR (1 + 1) = 3`.

	- For `i = 2`, the smallest `ans[2]` that satisfies `ans[2] OR (ans[2] + 1) = 5` is `4`, because `4 OR (4 + 1) = 5`.

	- For `i = 3`, the smallest `ans[3]` that satisfies `ans[3] OR (ans[3] + 1) = 7` is `3`, because `3 OR (3 + 1) = 7`.

Example 2:**

**Input:** nums = [11,13,31]

**Output:** [9,12,15]

**Explanation:**

	- For `i = 0`, the smallest `ans[0]` that satisfies `ans[0] OR (ans[0] + 1) = 11` is `9`, because `9 OR (9 + 1) = 11`.

	- For `i = 1`, the smallest `ans[1]` that satisfies `ans[1] OR (ans[1] + 1) = 13` is `12`, because `12 OR (12 + 1) = 13`.

	- For `i = 2`, the smallest `ans[2]` that satisfies `ans[2] OR (ans[2] + 1) = 31` is `15`, because `15 OR (15 + 1) = 31`.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `2 <= nums[i] <= 1000`

	- `nums[i]` is a prime number.

## 🧠 Solution Explanation

**Intuition**
The solution relies on the property of bitwise operations, specifically the XOR and left shift operators. It iterates over each number in the input array, checking if it can be represented as the bitwise OR of two consecutive numbers. If not, it tries to find the smallest number that satisfies the condition by flipping the least significant bit that is not set in the original number.

**Approach**
1. Iterate over each number `val` in the input array `nums`.
2. If `val` is 2, set `nums[i]` to -1 and continue to the next number.
3. Iterate from the least significant bit to the most significant bit (32 iterations).
4. If the current bit is not set in `val`, calculate the XOR of `val` with the bit flipped in the previous position (`1<<j-1`).
5. If the result is a valid number, set `nums[i]` to the result and break the loop.
6. If no valid number is found, `nums[i]` remains unchanged.

**Time Complexity**
O(n * 32) = O(n), where n is the number of elements in the input array. This is because we iterate over each number in the array and perform a constant number of operations for each bit.

**Space Complexity**
O(1), as we only use a constant amount of space to store the current number `val` and the result `x`.

**Key Insight**
The key insight is that we can represent any number `val` as the bitwise OR of two consecutive numbers if and only if the least significant bit that is not set in `val` is set in the next higher power of 2. This allows us to find the smallest number that satisfies the condition by flipping the least significant bit that is not set in `val`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 3.14%) |
| 📅 Solved | 2026-01-21 |
| 💻 Language | Python |