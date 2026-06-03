# 3349. Adjacent Increasing Subarrays Detection I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/)


## 📝 Problem Description

Given an array `nums` of `n` integers and an integer `k`, determine whether there exist **two** **adjacent** subarrays of length `k` such that both subarrays are **strictly** **increasing**. Specifically, check if there are **two** subarrays starting at indices `a` and `b` (`a < b`), where:

	- Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**.

	- The subarrays must be **adjacent**, meaning `b = a + k`.

Return `true` if it is *possible* to find **two **such subarrays, and `false` otherwise.

 

Example 1:**

**Input:** nums = [2,5,7,8,9,2,3,4,3,1], k = 3

**Output:** true

**Explanation:**

	- The subarray starting at index `2` is `[7, 8, 9]`, which is strictly increasing.

	- The subarray starting at index `5` is `[2, 3, 4]`, which is also strictly increasing.

	- These two subarrays are adjacent, so the result is `true`.

Example 2:**

**Input:** nums = [1,2,3,4,4,4,4,5,6,7], k = 5

**Output:** false

 

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 < 2 * k <= nums.length`

	- `-1000 <= nums[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses a clever approach to track the increasing subarrays by maintaining a sliding window of elements. It keeps track of the maximum element seen so far and the size of the current subarray. When a new element is encountered that is greater than the maximum, it checks if the current subarray has at least two strictly increasing subarrays of length `k`.

**Approach**
1. Initialize `prev_sub` to `None`, `sub_max` to negative infinity, and `sub_size` to 0.
2. Define a helper function `check` that takes the previous subarray's end index `p`, the current index `idx`, and the current subarray's size `s`.
3. Inside the `check` function, calculate the number of subarrays of length `k` in the current subarray (`subs = s // k`).
4. If `subs` is at least 2, return `True`.
5. If `p` is not `None` and the current subarray's size is equal to `k`, check if the previous subarray's end index is within the current subarray's bounds.
6. Return `False` if none of the above conditions are met.
7. Iterate through the input array `nums`. For each element `n`, check if it is greater than `sub_max`.
8. If `n` is greater than `sub_max`, update `sub_max` to `n`, increment `sub_size`, and call the `check` function with the previous subarray's end index `prev_sub`, the current index `i`, and the current subarray's size `sub_size`.
9. If `n` is not greater than `sub_max`, reset `sub_size` to 1, update `sub_max` to `n`, and call the `check` function with the previous subarray's end index `prev_sub`, the current index `i`, and the current subarray's size `sub_size`.
10. After iterating through the entire array, check if the final subarray has at least two strictly increasing subarrays of length `k`.

**Time Complexity**
The time complexity of this solution is O(n), where n is the length of the input array `nums`. This is because we are iterating through the array once, and the `check` function is called at most once for each element.

**Space Complexity**
The space complexity of this solution is O(1), which means the space required does not grow with the size of the input array. This is because we are using a constant amount of space to store the variables `prev_sub`, `sub_max`, and `sub_size`.

**Key Insight**
The key insight behind this solution is to use a sliding window approach to track the increasing subarrays. By maintaining the maximum element seen so far and the size of the current subarray, we can efficiently check if the current subarray has at least two strictly increasing subarrays of length `k`. This approach allows us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 84 ms (Beats 81.76%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-10-14 |
| 💻 Language | Python |