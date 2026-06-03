# 1493. Longest Subarray of 1's After Deleting One Element


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)


## 📝 Problem Description

Given a binary array `nums`, you should delete one element from it.

Return *the size of the longest non-empty subarray containing only *`1`*'s in the resulting array*. Return `0` if there is no such subarray.

 

Example 1:**

```

**Input:** nums = [1,1,0,1]
**Output:** 3
**Explanation:** After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

```

Example 2:**

```

**Input:** nums = [0,1,1,1,0,1,1,0,1]
**Output:** 5
**Explanation:** After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

```

Example 3:**

```

**Input:** nums = [1,1,1]
**Output:** 2
**Explanation:** You must delete one element.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `nums[i]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with dynamic programming to find the longest subarray of 1's after deleting one element from the binary array. The key insight is to maintain a count of zeros within the current window and adjust the window boundaries accordingly.

**Approach**
1. Initialize variables to keep track of the window boundaries (`l` and `r`), the result (`res`), and the count of zeros (`zero_count`).
2. Iterate through the array from left to right (`r`).
3. If a zero is encountered, increment the `zero_count`.
4. If `zero_count` exceeds 1, update the result with the maximum length of the subarray without the current zero, and slide the window to the right by incrementing `l` until `zero_count` is less than or equal to 1.
5. After the iteration, update the result with the maximum length of the subarray without the last element.
6. Return the result.

**Time Complexity**
O(n), where n is the length of the input array. This is because we iterate through the array once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the variables.

**Key Insight**
The key to this solution is to maintain a count of zeros within the current window and adjust the window boundaries accordingly. By doing so, we can efficiently find the longest subarray of 1's after deleting one element from the binary array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 69.87%) |
| 💾 Memory | 21.7 MB (Beats 99.98%) |
| 📅 Solved | 2025-08-24 |
| 💻 Language | Python |