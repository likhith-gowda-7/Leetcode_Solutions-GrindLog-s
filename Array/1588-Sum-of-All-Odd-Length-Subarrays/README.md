# 1588. Sum of All Odd Length Subarrays


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)


## 📝 Problem Description

Given an array of positive integers `arr`, return *the sum of all possible **odd-length subarrays** of *`arr`.

A **subarray** is a contiguous subsequence of the array.

 

Example 1:**

```

**Input:** arr = [1,4,2,5,3]
**Output:** 58
**Explanation: **The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```

Example 2:**

```

**Input:** arr = [1,2]
**Output:** 3
**Explanation: **There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
```

Example 3:**

```

**Input:** arr = [10,11,12]
**Output:** 66

```

 

**Constraints:**

	- `1 <= arr.length <= 100`

	- `1 <= arr[i] <= 1000`

 

**Follow up:**

Could you solve this problem in O(n) time complexity?

## 🧠 Solution Explanation

**Intuition**
The solution uses a clever observation to calculate the sum of all odd-length subarrays. It notes that for each element at index `i`, the total number of odd-length subarrays that include `arr[i]` is `(i+1)*(n-i)`, where `n` is the length of the array. This is because there are `i+1` odd-length subarrays starting from the beginning of the array and ending at `arr[i]`, and `n-i` odd-length subarrays starting from `arr[i]` and ending at the end of the array.

**Approach**
1. Initialize the result `res` to 0 and the length of the array `n` to `len(arr)`.
2. Iterate over each element `arr[i]` in the array.
3. For each element, calculate the total number of odd-length subarrays that include `arr[i]` using the formula `(i+1)*(n-i)`.
4. Calculate the number of odd-length subarrays that include `arr[i]` by taking the ceiling of `(total+1)/2`, which is equivalent to `(total+1)//2`.
5. Multiply the number of odd-length subarrays by `arr[i]` and add the result to `res`.
6. Return `res` as the sum of all odd-length subarrays.

**Time Complexity**
O(n), where n is the length of the array. This is because we are iterating over each element in the array once.

**Space Complexity**
O(1), which means the space complexity is constant. We are only using a few variables to store the result and the length of the array, and we are not using any data structures that grow with the size of the input.

**Key Insight**
The key insight behind this solution is the observation that the total number of odd-length subarrays that include a given element is proportional to the product of the number of elements before and after the given element. This allows us to calculate the sum of all odd-length subarrays in a single pass through the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-09 |
| 💻 Language | Python |