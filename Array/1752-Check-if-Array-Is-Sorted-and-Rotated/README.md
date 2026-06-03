# 1752. Check if Array Is Sorted and Rotated


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)


## 📝 Problem Description

Given an array `nums`, return `true`* if the array was originally sorted in non-decreasing order, then rotated **some** number of positions (including zero)*. Otherwise, return `false`.

There may be **duplicates** in the original array.

**Note:** An array `A` rotated by `x` positions results in an array `B` of the same length such that `B[i] == A[(i+x) % A.length]` for every valid index `i`.

 

Example 1:**

```

**Input:** nums = [3,4,5,1,2]
**Output:** true
**Explanation:** [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].

```

Example 2:**

```

**Input:** nums = [2,1,3,4]
**Output:** false
**Explanation:** There is no sorted array once rotated that can make nums.

```

Example 3:**

```

**Input:** nums = [1,2,3]
**Output:** true
**Explanation:** [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by checking if the array has a non-decreasing subsequence that covers all elements, which would indicate that the array was sorted and rotated. This approach is based on the observation that if the array is sorted and rotated, it must have a non-decreasing subsequence that covers all elements.

**Approach**
1. Initialize a streak counter to 1, which represents the current non-decreasing subsequence.
2. Iterate through the array twice, considering each element as if it were part of a longer array of length `n*2`.
3. For each element, check if it is greater than or equal to the previous element. If it is, increment the streak counter.
4. If the streak counter reaches `n`, it means that the current subsequence covers all elements, and the array was sorted and rotated.
5. If the streak counter is reset to 1, it means that the current element is smaller than the previous element, and the array was not sorted and rotated.

**Time Complexity**
O(n) - The solution iterates through the array twice, resulting in a time complexity of O(n*2). However, since the array is rotated, we can reduce the time complexity to O(n) by considering each element as part of a longer array of length `n*2`.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the streak counter, resulting in a space complexity of O(1).

**Key Insight**
The key insight is that if the array is sorted and rotated, it must have a non-decreasing subsequence that covers all elements. This insight allows us to check if the array was sorted and rotated by simply looking for a non-decreasing subsequence that covers all elements.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 16.45%) |
| 📅 Solved | 2026-05-23 |
| 💻 Language | Python |