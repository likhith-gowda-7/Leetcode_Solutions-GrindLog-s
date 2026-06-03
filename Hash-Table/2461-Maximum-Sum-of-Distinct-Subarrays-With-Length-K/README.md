> 📌 **Cross-listed:** Primary location is [Array/2461-Maximum-Sum-of-Distinct-Subarrays-With-Length-K](../../Array/2461-Maximum-Sum-of-Distinct-Subarrays-With-Length-K). This problem also appears under: **Array**, **Hash Table**, **Sliding Window**

# 2461. Maximum Sum of Distinct Subarrays With Length K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `k`. Find the maximum subarray sum of all the subarrays of `nums` that meet the following conditions:

	- The length of the subarray is `k`, and

	- All the elements of the subarray are **distinct**.

Return *the maximum subarray sum of all the subarrays that meet the conditions**.* If no subarray meets the conditions, return `0`.

*A **subarray** is a contiguous non-empty sequence of elements within an array.*

 

Example 1:**

```

**Input:** nums = [1,5,4,2,9,9,9], k = 3
**Output:** 15
**Explanation:** The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

```

Example 2:**

```

**Input:** nums = [4,4,4], k = 3
**Output:** 0
**Explanation:** The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.

```

 

**Constraints:**

	- `1 <= k <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with a set to keep track of distinct elements within the window. By maintaining a set, we can efficiently check if an element is already present in the window, which is crucial for ensuring distinct elements. The solution iterates through the array, expanding the window to the right and contracting it from the left when necessary.

**Approach**
1. Initialize a set `elements` to store distinct elements within the window, a variable `curr_len` to track the current window length, and a variable `res` to store the maximum subarray sum.
2. Initialize two pointers, `l` and `r`, to the start of the array, and a variable `curr` to store the sum of the current window.
3. Iterate through the array with the right pointer `r`. For each element, add it to the window sum `curr` and increment the window length `curr_len`.
4. If the window length exceeds `k` or the current element is already in the set `elements`, contract the window from the left by removing the leftmost element from the set and subtracting it from the window sum `curr`.
5. Add the current element to the set `elements`.
6. If the window length is equal to `k`, update the maximum subarray sum `res` if the current window sum is greater.

**Time Complexity**
O(n), where n is the length of the array. The solution iterates through the array once, and the operations within the loop (set operations and variable updates) take constant time.

**Space Complexity**
O(n), where n is the length of the array. The set `elements` stores at most `k` distinct elements within the window, but in the worst case, all elements in the array are distinct, resulting in a space complexity of O(n).

**Key Insight**
The key to this solution is the use of a set to efficiently check for distinct elements within the window. By maintaining a set, we can avoid sorting or using a separate data structure to track distinct elements, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 91 ms (Beats 91.39%) |
| 💾 Memory | 34.1 MB (Beats 84.26%) |
| 📅 Solved | 2026-03-31 |
| 💻 Language | Python |