> 📌 **Cross-listed:** Primary location is [Array/3315-Construct-the-Minimum-Bitwise-Array-II](../../Array/3315-Construct-the-Minimum-Bitwise-Array-II). This problem also appears under: **Array**, **Bit Manipulation**

# 3315. Construct the Minimum Bitwise Array II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/)


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

	- `2 <= nums[i] <= 10^9`

	- `nums[i]` is a prime number.

## 🧠 Solution Explanation

**Intuition**
The solution leverages the properties of bitwise operations to find the minimum value for each `ans[i]` that satisfies the condition `ans[i] OR (ans[i] + 1) == nums[i]`. It iterates through each number in the input array and checks the bits that are set in the number. If a bit is not set, it tries to clear the bit by performing a bitwise XOR operation.

**Approach**
1. Iterate through each number `val` in the input array `nums`.
2. If `val` is 2, set `ans[i]` to -1 and continue to the next number.
3. Iterate through each bit position `j` from 0 to 31.
4. If the bit at position `j` is not set in `val`, try to clear the bit by performing a bitwise XOR operation with `1<<j-1`.
5. If the XOR operation is successful, set `ans[i]` to the result and break the loop.
6. If no suitable value is found for `ans[i]`, set it to -1.

**Time Complexity**
O(n * 32) = O(n), where n is the length of the input array. This is because we iterate through each number in the array and each bit position up to 32.

**Space Complexity**
O(1), as we only use a constant amount of space to store the current number `val` and the result `x`.

**Key Insight**
The key insight behind this solution is that if a bit is not set in `val`, we can try to clear it by performing a bitwise XOR operation with `1<<j-1`. This is because XORing a number with a power of 2 (e.g., `1<<j-1`) will clear the bit at that position if and only if the bit is not set in the number. This allows us to efficiently find the minimum value for each `ans[i]` that satisfies the condition.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1 ms (Beats 68.42%) |
| 💾 Memory | 19.2 MB (Beats 67.25%) |
| 📅 Solved | 2026-01-21 |
| 💻 Language | Python |