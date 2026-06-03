> 📌 **Cross-listed:** Primary location is [Array/1652-Defuse-the-Bomb](../../Array/1652-Defuse-the-Bomb). This problem also appears under: **Array**, **Sliding Window**

# 1652. Defuse the Bomb


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/defuse-the-bomb/)


## 📝 Problem Description

You have a bomb to defuse, and your time is running out! Your informer will provide you with a **circular** array `code` of length of `n` and a key `k`.

To decrypt the code, you must replace every number. All the numbers are replaced **simultaneously**.

	- If `k > 0`, replace the `i^th` number with the sum of the **next** `k` numbers.

	- If `k < 0`, replace the `i^th` number with the sum of the **previous** -`k` numbers.

	- If `k == 0`, replace the `i^th` number with `0`.

As `code` is circular, the next element of `code[n-1]` is `code[0]`, and the previous element of `code[0]` is `code[n-1]`.

Given the **circular** array `code` and an integer key `k`, return *the decrypted code to defuse the bomb*!

 

Example 1:**

```

**Input:** code = [5,7,1,4], k = 3
**Output:** [12,10,16,13]
**Explanation:** Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

```

Example 2:**

```

**Input:** code = [1,2,3,4], k = 0
**Output:** [0,0,0,0]
**Explanation:** When k is zero, the numbers are replaced by 0. 

```

Example 3:**

```

**Input:** code = [2,4,9,3], k = -2
**Output:** [12,5,6,13]
**Explanation:** The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the **previous** numbers.

```

 

**Constraints:**

	- `n == code.length`

	- `1 <= n <= 100`

	- `1 <= code[i] <= 100`

	- `-(n - 1) <= k <= n - 1`

## 🧠 Solution Explanation

**Intuition**
The problem requires us to decrypt a circular array `code` based on a given key `k`. The decryption process involves replacing each number with the sum of the next `k` numbers (if `k > 0`) or the previous `-k` numbers (if `k < 0`). The key insight is to use a sliding window approach to efficiently calculate the sum of the required numbers.

**Approach**
1. If `k` is 0, return an array of zeros with the same length as `code`.
2. Initialize an array `res` to store the decrypted code and a variable `window` to store the sum of the numbers in the sliding window.
3. If `k` is negative, adjust the start and end indices of the sliding window accordingly.
4. Calculate the initial sum of the numbers in the sliding window.
5. Iterate through the `code` array, updating the `res` array with the current sum of the sliding window and adjusting the `window` by adding the next number and subtracting the previous number (wrapping around to the beginning of the array if necessary).
6. Return the decrypted code stored in the `res` array.

**Time Complexity**
O(n), where n is the length of the `code` array. This is because we are iterating through the array once to calculate the initial sum and once to update the `res` array.

**Space Complexity**
O(n), where n is the length of the `code` array. This is because we are creating an array `res` to store the decrypted code, which has the same length as the input array.

**Key Insight**
The key to this solution is the use of a sliding window approach to efficiently calculate the sum of the required numbers. By maintaining a running sum of the numbers in the window, we can update the `res` array in O(1) time, resulting in a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-03-05 |
| 💻 Language | Python |