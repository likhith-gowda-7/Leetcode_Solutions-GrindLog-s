> 📌 **Cross-listed:** Primary location is [Array/1695-Maximum-Erasure-Value](../../Array/1695-Maximum-Erasure-Value). This problem also appears under: **Array**, **Hash Table**, **Sliding Window**

# 1695. Maximum Erasure Value


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-erasure-value/)


## 📝 Problem Description

You are given an array of positive integers `nums` and want to erase a subarray containing **unique elements**. The **score** you get by erasing the subarray is equal to the **sum** of its elements.

Return *the **maximum score** you can get by erasing **exactly one** subarray.*

An array `b` is called to be a subarray of `a` if it forms a contiguous subsequence of `a`, that is, if it is equal to `a[l],a[l+1],...,a[r]` for some `(l,r)`.

 

Example 1:**

```

**Input:** nums = [4,2,4,5,6]
**Output:** 17
**Explanation:** The optimal subarray here is [2,4,5,6].

```

Example 2:**

```

**Input:** nums = [5,2,1,2,5,2,1,2,5]
**Output:** 8
**Explanation:** The optimal subarray here is [5,2,1] or [1,2,5].

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with a set to keep track of unique elements within the window. The key insight is that we can efficiently remove elements from the window by checking if the current element is already in the set, and if so, we remove the leftmost element from the window.

**Approach**
1. Initialize variables to keep track of the maximum sum (`maxi`), the left pointer of the window (`l`), a set to store unique elements within the window (`uni`), and the current sum within the window (`curr`).
2. Iterate over the array with the right pointer (`r`).
3. For each element, add it to the current sum and the set of unique elements.
4. If the current element is already in the set, remove the leftmost element from the set and subtract its value from the current sum, and move the left pointer to the right.
5. Update the maximum sum if the current sum is greater.
6. Return the maximum sum after iterating over the entire array.

**Time Complexity**
O(n), where n is the length of the array, because we make a single pass over the array.

**Space Complexity**
O(n), where n is the length of the array, because in the worst case, we store all unique elements within the window in the set.

**Key Insight**
The key to this solution is the efficient removal of elements from the window using a set, which allows us to maintain a sliding window of unique elements and update the maximum sum in O(1) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 181 ms (Beats 43.9%) |
| 💾 Memory | 28.8 MB (Beats 100%) |
| 📅 Solved | 2025-07-22 |
| 💻 Language | Python |