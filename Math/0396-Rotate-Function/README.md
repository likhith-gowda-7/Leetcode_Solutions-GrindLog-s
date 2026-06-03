> 📌 **Cross-listed:** Primary location is [Array/0396-Rotate-Function](../../Array/0396-Rotate-Function). This problem also appears under: **Array**, **Math**, **Dynamic Programming**

# 396. Rotate Function


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotate-function/)


## 📝 Problem Description

You are given an integer array `nums` of length `n`.

Assume `arr_k` to be an array obtained by rotating `nums` by `k` positions clock-wise. We define the **rotation function** `F` on `nums` as follow:

	- `F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1].`

Return *the maximum value of* `F(0), F(1), ..., F(n-1)`.

The test cases are generated so that the answer fits in a **32-bit** integer.

 

Example 1:**

```

**Input:** nums = [4,3,2,6]
**Output:** 26
**Explanation:**
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

```

Example 2:**

```

**Input:** nums = [100]
**Output:** 0

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 10^5`

	- `-100 <= nums[i] <= 100`

## 🧠 Solution Explanation

## Intuition
The solution works by calculating the rotation function `F(k)` for each possible rotation `k` and keeping track of the maximum value. It uses a clever trick to avoid recalculating the entire sum for each rotation, instead updating the previous sum to get the new sum. This approach takes advantage of the fact that the rotation function has a simple relationship with the previous rotation.

## Approach
1. Calculate the initial sum of the rotation function `F(0)` by multiplying each element with its index and summing them up.
2. Initialize the maximum result with the initial sum.
3. Iterate over each possible rotation from `n-1` to `1`, where `n` is the length of the input array.
4. For each rotation, update the previous sum by subtracting the contribution of the last element and adding the contribution of the remaining elements.
5. Update the maximum result if the new sum is larger.

## Time Complexity
The time complexity is O(n), where n is the length of the input array. This is because we are iterating over the array once to calculate the initial sum and then iterating over the possible rotations, which is also n times.

## Space Complexity
The space complexity is O(1), which means the space required does not change with the size of the input array. This is because we are only using a constant amount of space to store the sums and the maximum result.

## Key Insight
The key insight is to recognize that the rotation function has a simple relationship with the previous rotation, allowing us to update the previous sum instead of recalculating the entire sum for each rotation. This insight enables us to solve the problem efficiently in O(n) time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 170 ms (Beats 11.23%) |
| 💾 Memory | 31 MB (Beats 61.49%) |
| 📅 Solved | 2026-05-01 |
| 💻 Language | Python |