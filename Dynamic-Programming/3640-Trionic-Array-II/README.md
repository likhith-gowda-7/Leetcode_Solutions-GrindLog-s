> 📌 **Cross-listed:** Primary location is [Array/3640-Trionic-Array-II](../../Array/3640-Trionic-Array-II). This problem also appears under: **Array**, **Dynamic Programming**

# 3640. Trionic Array II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/trionic-array-ii/)


## 📝 Problem Description

You are given an integer array nums` of length n`.

A trionic subarray** is a contiguous subarray nums[l...r]` (with 0 <= l < r < n`) for which there exist indices `l < p < q < r` such that:

	nums[l...p]` is **strictly** increasing,

	nums[p...q]` is **strictly** decreasing,

	nums[q...r]` is **strictly** increasing.

Return the **maximum** sum of any trionic subarray in nums`.

 

Example 1:**

**Input:** nums = [0,-2,-1,-3,0,2,-1]

**Output:** -4

**Explanation:**

Pick l = 1`, p = 2`, q = 3`, r = 5`:

	nums[l...p] = nums[1...2] = [-2, -1]` is strictly increasing (-2 < -1`).

	nums[p...q] = nums[2...3] = [-1, -3]` is strictly decreasing (-1 > -3`)

	nums[q...r] = nums[3...5] = [-3, 0, 2]` is strictly increasing (-3 < 0 < 2`).

	Sum = `(-2) + (-1) + (-3) + 0 + 2 = -4`.

Example 2:**

**Input:** nums = [1,4,2,7]

**Output:** 14

**Explanation:**

Pick l = 0`, p = 1`, q = 2`, r = 3`:

	nums[l...p] = nums[0...1] = [1, 4]` is strictly increasing (1 < 4`).

	nums[p...q] = nums[1...2] = [4, 2]` is strictly decreasing (4 > 2`).

	nums[q...r] = nums[2...3] = [2, 7]` is strictly increasing (2 < 7`).

	Sum = `1 + 4 + 2 + 7 = 14`.

 

**Constraints:**

	4 <= n = nums.length <= 10^5`

	-10^9 <= nums[i] <= 10^9`

	It is guaranteed that at least one trionic subarray exists.

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming to track the maximum sum of three subarrays: `nums[l...p]`, `nums[p...q]`, and `nums[q...r]`. It iterates through the array, maintaining three variables `a`, `b`, and `c` to store the maximum sum of these subarrays. The key insight is to update these variables based on the current element's relationship with the previous element.

**Approach**
1. Initialize variables `result`, `a`, `b`, `c`, and `INF` (negative infinity) to keep track of the maximum sum and the maximum sum of the three subarrays.
2. Iterate through the array starting from the second element (index 1).
3. For each element, check if it's greater than the previous element. If so, update `na` (the maximum sum of `nums[l...p]`) to be the maximum of the current `a` and the previous element, plus the current element.
4. Update `nc` (the maximum sum of `nums[q...r]`) to be the maximum of the current `c` and `na`, plus the current element.
5. If the current element is less than the previous element, update `nb` (the maximum sum of `nums[p...q]`) to be the maximum of the current `a` and `b`, plus the current element.
6. Update `a`, `b`, and `c` to be `na`, `nb`, and `nc`, respectively.
7. Update `result` to be the maximum of the current `result` and `c`.
8. Repeat steps 3-7 until the end of the array.

**Time Complexity**
O(n), where n is the length of the array. This is because we're iterating through the array once, and each operation within the loop takes constant time.

**Space Complexity**
O(1), as we're using a constant amount of space to store the variables `result`, `a`, `b`, `c`, and `INF`.

**Key Insight**
The key insight is to update the variables `a`, `b`, and `c` based on the current element's relationship with the previous element. This allows us to efficiently track the maximum sum of the three subarrays and find the maximum sum of any trionic subarray.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 155 ms (Beats 81.15%) |
| 💾 Memory | 31.2 MB (Beats 94.76%) |
| 📅 Solved | 2026-02-04 |
| 💻 Language | Python |