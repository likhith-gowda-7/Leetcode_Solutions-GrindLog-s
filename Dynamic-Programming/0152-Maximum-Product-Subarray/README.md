> 📌 **Cross-listed:** Primary location is [Array/0152-Maximum-Product-Subarray](../../Array/0152-Maximum-Product-Subarray). This problem also appears under: **Array**, **Dynamic Programming**

# 152. Maximum Product Subarray


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/)


## 📝 Problem Description

Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

 

Example 1:**

```

**Input:** nums = [2,3,-2,4]
**Output:** 6
**Explanation:** [2,3] has the largest product 6.

```

Example 2:**

```

**Input:** nums = [-2,0,-1]
**Output:** 0
**Explanation:** The result cannot be 2, because [-2,-1] is not a subarray.

```

 

**Constraints:**

	- `1 <= nums.length <= 2 * 10^4`

	- `-10 <= nums[i] <= 10`

	- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

## 🧠 Solution Explanation

## Intuition
The solution works by maintaining two variables, `maxi` and `mini`, to track the maximum and minimum product of subarrays ending at each position. This approach is necessary because a negative number can turn a maximum product into a minimum product, and vice versa. By keeping track of both, we can handle these cases correctly.

## Approach
1. Initialize `res` with the maximum value in the array, and `maxi` and `mini` with the first element of the array.
2. Iterate through the array starting from the second element.
3. For each element, calculate the new maximum and minimum product by considering the current element, the product of the current element and the previous maximum product, and the product of the current element and the previous minimum product.
4. Update `maxi` and `mini` with the new maximum and minimum product, and update `res` with the maximum of the current `res` and `maxi`.

## Time Complexity
The time complexity is O(n), where n is the length of the input array, because we make a single pass through the array.

## Space Complexity
The space complexity is O(1), because we use a constant amount of space to store the variables `res`, `maxi`, `mini`, and `temp`, regardless of the size of the input array.

## Key Insight
The key insight is to maintain both the maximum and minimum product of subarrays ending at each position, because a negative number can change the maximum product to a minimum product, and vice versa. This allows us to correctly handle cases where a negative number is encountered, and ensures that we find the maximum product subarray.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 91.01%) |
| 💾 Memory | 19.7 MB (Beats 78.75%) |
| 📅 Solved | 2026-03-28 |
| 💻 Language | Python |