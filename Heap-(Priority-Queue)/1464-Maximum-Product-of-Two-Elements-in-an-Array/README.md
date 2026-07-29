> 📌 **Cross-listed:** Primary location is [Array/1464-Maximum-Product-of-Two-Elements-in-an-Array](../../Array/1464-Maximum-Product-of-Two-Elements-in-an-Array). This problem also appears under: **Array**, **Sorting**, **Heap (Priority Queue)**

# 1464. Maximum Product of Two Elements in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)


## 📝 Problem Description

Given the array of integers `nums`, you will choose two different indices `i` and `j` of that array. *Return the maximum value of* `(nums[i]-1)*(nums[j]-1)`.
 

Example 1:**

```

**Input:** nums = [3,4,5,2]
**Output:** 12 
**Explanation:** If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

```

Example 2:**

```

**Input:** nums = [1,5,4,5]
**Output:** 16
**Explanation:** Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

```

Example 3:**

```

**Input:** nums = [3,7]
**Output:** 12

```

 

**Constraints:**

	- `2 <= nums.length <= 500`

	- `1 <= nums[i] <= 10^3`

## 🧠 Solution Explanation

**Intuition**
The solution exploits the fact that the maximum product of two elements in the array can be achieved by choosing the two largest numbers in the array, subtracting 1 from each of them, and then multiplying the results. This approach is based on the observation that the product of two numbers is maximized when the numbers are as large as possible.

**Approach**
1. Initialize two variables `max1` and `max2` to store the maximum and second maximum values in the array, respectively.
2. Iterate through the array `nums`. For each element `val`, check if it is greater than `max1`.
   - If `val` is greater than `max1`, update `max2` to be the old value of `max1`, and update `max1` to be `val - 1`.
   - If `val` is not greater than `max1` but is greater than `max2`, update `max2` to be `val - 1`.
3. After iterating through the entire array, return the product of `max1` and `max2`.

**Time Complexity**
O(n), where n is the number of elements in the array. This is because the solution iterates through the array once.

**Space Complexity**
O(1), as the solution uses a constant amount of space to store the `max1` and `max2` variables.

**Key Insight**
The key insight behind this solution is that the maximum product of two elements in the array can be achieved by choosing the two largest numbers in the array, subtracting 1 from each of them, and then multiplying the results. This approach allows us to avoid sorting the entire array, making the solution more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 60.58%) |
| 📅 Solved | 2026-07-29 |
| 💻 Language | Python |