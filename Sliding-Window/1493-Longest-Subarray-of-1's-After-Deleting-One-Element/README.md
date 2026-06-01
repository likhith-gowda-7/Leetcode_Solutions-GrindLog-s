> 📌 **Cross-listed:** Primary location is [Array/1493-Longest-Subarray-of-1's-After-Deleting-One-Element](../../Array/1493-Longest-Subarray-of-1's-After-Deleting-One-Element). This problem also appears under: **Array**, **Dynamic Programming**, **Sliding Window**

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

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 69.87%) |
| 💾 Memory | 21.7 MB (Beats 99.98%) |
| 📅 Solved | 2025-08-24 |
| 💻 Language | Python |