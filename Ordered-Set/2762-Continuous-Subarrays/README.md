> 📌 **Cross-listed:** Primary location is [Array/2762-Continuous-Subarrays](../../Array/2762-Continuous-Subarrays). This problem also appears under: **Array**, **Queue**, **Sliding Window**, **Heap (Priority Queue)**, **Ordered Set**, **Monotonic Queue**

# 2762. Continuous Subarrays


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/continuous-subarrays/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`. A subarray of `nums` is called **continuous** if:

	- Let `i`, `i + 1`, ..., `j`_ be the indices in the subarray. Then, for each pair of indices `i <= i_1, i_2 <= j`, `0 <= |nums[i_1] - nums[i_2]| <= 2`.

Return *the total number of **continuous** subarrays.*

A subarray is a contiguous **non-empty** sequence of elements within an array.

 

Example 1:**

```

**Input:** nums = [5,4,2,4]
**Output:** 8
**Explanation:** 
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
There are no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.

```

 

Example 2:**

```

**Input:** nums = [1,2,3]
**Output:** 6
**Explanation:** 
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with the help of two deques (maxi and mini) to track the maximum and minimum elements within the current window. The key insight is that we can efficiently update the window boundaries by maintaining the maximum and minimum elements.

**Approach**
1. Initialize two deques (maxi and mini) to store the indices of the maximum and minimum elements within the current window.
2. Initialize two pointers, l and r, to represent the left and right boundaries of the window.
3. Iterate through the array from left to right (r = 0 to n-1).
4. For each element at index r, update the maxi and mini deques by removing elements that are smaller or larger than the current element.
5. While the difference between the maximum and minimum elements within the window is greater than 2, increment the count of continuous subarrays and update the window boundaries by removing elements from the left.
6. Increment the count of continuous subarrays by the size of the current window (r - l + 1).
7. Return the total count of continuous subarrays.

**Time Complexity**
O(n), where n is the length of the input array. This is because we iterate through the array once and perform constant-time operations for each element.

**Space Complexity**
O(n), where n is the length of the input array. This is because in the worst case, we need to store all elements in the maxi and mini deques.

**Key Insight**
The key insight is that we can efficiently update the window boundaries by maintaining the maximum and minimum elements within the window. This allows us to avoid recalculating the size of the window for each element, resulting in a linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 608 ms (Beats 39.32%) |
| 💾 Memory | 27.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-26 |
| 💻 Language | Python |