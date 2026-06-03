# 713. Subarray Product Less Than K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/)


## 📝 Problem Description

Given an array of integers `nums` and an integer `k`, return *the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than *`k`.

 

Example 1:**

```

**Input:** nums = [10,5,2,6], k = 100
**Output:** 8
**Explanation:** The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

```

Example 2:**

```

**Input:** nums = [1,2,3], k = 0
**Output:** 0

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `1 <= nums[i] <= 1000`

	- `0 <= k <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to count the number of contiguous subarrays with a product less than `k`. The key insight is to maintain a running product of the subarray elements and adjust the window boundaries to keep the product below `k`.

**Approach**
1. Handle the edge case where `k` is less than or equal to 1, as there are no valid subarrays in this case.
2. Initialize the count of valid subarrays, the start of the window, and the running product.
3. Iterate through the array, multiplying the running product by the current element at each step.
4. If the running product becomes greater than or equal to `k`, divide the product by the element at the start of the window and increment the start of the window.
5. At each step, add the size of the current window (end - start + 1) to the count of valid subarrays.
6. Return the total count of valid subarrays.

**Time Complexity**
O(n), where n is the length of the input array. This is because we are iterating through the array once, and the while loop inside the for loop runs in O(1) time on average.

**Space Complexity**
O(1), as we are using a constant amount of space to store the count, start, and product variables.

**Key Insight**
The key to this solution is the use of a sliding window with a running product, which allows us to efficiently count the number of valid subarrays by adjusting the window boundaries based on the product of the subarray elements. This approach avoids the need to explicitly generate all subarrays, making it more efficient than a naive approach.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 51 ms (Beats 87.81%) |
| 💾 Memory | 19.6 MB (Beats 100%) |
| 📅 Solved | 2024-12-19 |
| 💻 Language | Python |