> 📌 **Cross-listed:** Primary location is [Array/0852-Peak-Index-in-a-Mountain-Array](../../Array/0852-Peak-Index-in-a-Mountain-Array). This problem also appears under: **Array**, **Binary Search**

# 852. Peak Index in a Mountain Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/)


## 📝 Problem Description

You are given an integer **mountain** array `arr` of length `n` where the values increase to a **peak element** and then decrease.

Return the index of the peak element.

Your task is to solve it in `O(log(n))` time complexity.

 

Example 1:**

**Input:** arr = [0,1,0]

**Output:** 1

Example 2:**

**Input:** arr = [0,2,1,0]

**Output:** 1

Example 3:**

**Input:** arr = [0,10,5,2]

**Output:** 1

 

**Constraints:**

	- `3 <= arr.length <= 10^5`

	- `0 <= arr[i] <= 10^6`

	- `arr` is **guaranteed** to be a mountain array.

## 🧠 Solution Explanation

**Intuition**
The given problem involves finding the peak element in a mountain array. A mountain array is a special type of array where the values increase to a peak element and then decrease. The key insight is that the peak element must be the maximum element in the array, and we can use binary search to find it efficiently.

**Approach**
1. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
2. While `l` is less than `r`, calculate the midpoint `mid` of the current range `[l, r]`.
3. Compare the value at `mid` with the value at `mid + 1`.
   - If `arr[mid]` is greater than `arr[mid + 1]`, it means the peak element is in the left half of the array. Update `r` to `mid`.
   - Otherwise, the peak element is in the right half of the array. Update `l` to `mid + 1`.
4. Repeat step 3 until `l` is no longer less than `r`.
5. The index of the peak element is stored in `r`.

**Time Complexity**
O(log(n)), where n is the length of the array. This is because we divide the search space roughly in half at each step of the binary search.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointers `l` and `r`, and the midpoint `mid`.

**Key Insight**
The key insight is that the peak element must be the maximum element in the array, and we can use binary search to find it efficiently by comparing the values at the midpoint and the next element. This approach takes advantage of the mountain array property to reduce the search space at each step.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 29.6 MB (Beats 100%) |
| 📅 Solved | 2025-03-02 |
| 💻 Language | Python |