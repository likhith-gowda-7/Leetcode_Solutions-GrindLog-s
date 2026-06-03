# 3151. Special Array I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/special-array-i/)


## 📝 Problem Description

An array is considered **special** if the *parity* of every pair of adjacent elements is different. In other words, one element in each pair **must** be even, and the other **must** be odd.

You are given an array of integers `nums`. Return `true` if `nums` is a **special** array, otherwise, return `false`.

 

Example 1:**

**Input:** nums = [1]

**Output:** true

**Explanation:**

There is only one element. So the answer is `true`.

Example 2:**

**Input:** nums = [2,1,4]

**Output:** true

**Explanation:**

There is only two pairs: `(2,1)` and `(1,4)`, and both of them contain numbers with different parity. So the answer is `true`.

Example 3:**

**Input:** nums = [4,3,1,6]

**Output:** false

**Explanation:**

`nums[1]` and `nums[2]` are both odd. So the answer is `false`.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution checks each pair of adjacent elements in the array to ensure that they have different parities (one is even and the other is odd). If any pair has the same parity, the array is not special.

**Approach**
1. Check if the array has more than one element. If not, return `True` because a single-element array is considered special.
2. Iterate through the array starting from the second element (index 1).
3. For each element, check if its parity is the same as the previous element's parity by using the modulo operator (`%`). If the parities are the same, return `False`.
4. If the loop completes without finding any pairs with the same parity, return `True`.

**Time Complexity**
O(n), where n is the number of elements in the array. This is because we only iterate through the array once.

**Space Complexity**
O(1), which means the space complexity is constant. We only use a few variables to store the current element and its index, so the space usage does not grow with the size of the input array.

**Key Insight**
The key insight is that we only need to check each pair of adjacent elements once, and we can use a simple parity check (modulo operator) to determine if they have different parities. This makes the solution efficient and easy to understand.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-01 |
| 💻 Language | Python |