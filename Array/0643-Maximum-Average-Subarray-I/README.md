# 643. Maximum Average Subarray I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)


## 📝 Problem Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return *this value*. Any answer with a calculation error less than `10^-5` will be accepted.

 

Example 1:**

```

**Input:** nums = [1,12,-5,-6,50,3], k = 4
**Output:** 12.75000
**Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

```

Example 2:**

```

**Input:** nums = [5], k = 1
**Output:** 5.00000

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= k <= n <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to efficiently calculate the maximum average subarray sum. By maintaining a running sum of the current window and subtracting the element that just left the window, we can efficiently update the sum without recalculating the entire subarray.

**Approach**
1. Initialize the maximum sum (`max_sum`) and the current sum (`curr`) to the sum of the first `k` elements in the array.
2. Iterate over the array starting from the `k`-th element.
3. For each element, add the current element to the current sum and subtract the element that just left the window (`nums[i-k]`).
4. Update the maximum sum if the current sum is greater.
5. Return the maximum sum divided by `k` to get the maximum average.

**Time Complexity**
O(n) - The solution iterates over the array once, where n is the number of elements in the array.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the maximum sum, current sum, and other variables, regardless of the input size.

**Key Insight**
The key insight is that by maintaining a running sum and updating it efficiently, we can avoid recalculating the sum of the subarray for each element, resulting in a time complexity of O(n). This is a common technique used in sliding window problems to optimize the solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 80 ms (Beats 28.03%) |
| 💾 Memory | 27.4 MB (Beats 100%) |
| 📅 Solved | 2025-03-04 |
| 💻 Language | Python |