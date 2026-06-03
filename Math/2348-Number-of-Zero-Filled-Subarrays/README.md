> 📌 **Cross-listed:** Primary location is [Array/2348-Number-of-Zero-Filled-Subarrays](../../Array/2348-Number-of-Zero-Filled-Subarrays). This problem also appears under: **Array**, **Math**

# 2348. Number of Zero-Filled Subarrays


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-zero-filled-subarrays/)


## 📝 Problem Description

Given an integer array `nums`, return *the number of **subarrays** filled with *`0`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

 

Example 1:**

```

**Input:** nums = [1,3,0,0,2,0,0,4]
**Output:** 6
**Explanation:** 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
```

Example 2:**

```

**Input:** nums = [0,0,0,2,0,0]
**Output:** 9
**Explanation:
**There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

```

Example 3:**

```

**Input:** nums = [2,10,2019]
**Output:** 0
**Explanation:** There is no subarray filled with 0. Therefore, we return 0.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the array and maintaining a count of consecutive zeros. Whenever a non-zero element is encountered, the count is reset to zero. The total count of zeros is incremented by the current count whenever a zero is encountered.

**Approach**
1. Initialize a variable `res` to store the total count of zero-filled subarrays and a variable `zero_count` to store the current count of consecutive zeros.
2. Append a non-zero value to the end of the array to handle the case where the array ends with zeros.
3. Iterate through the array. If the current element is not zero, reset `zero_count` to zero.
4. If the current element is zero, increment `zero_count` by one and add it to `res`.
5. Return `res` as the total count of zero-filled subarrays.

**Time Complexity**
O(n), where n is the length of the array. This is because we are iterating through the array once.

**Space Complexity**
O(1), excluding the space required for the input array. We are using a constant amount of space to store the variables `res` and `zero_count`.

**Key Insight**
The key insight is to realize that the count of consecutive zeros can be incremented by the current count whenever a zero is encountered. This allows us to avoid manually counting the number of subarrays for each possible length of zeros.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 23 ms (Beats 98.11%) |
| 💾 Memory | 28.3 MB (Beats 99.53%) |
| 📅 Solved | 2025-08-19 |
| 💻 Language | Python |