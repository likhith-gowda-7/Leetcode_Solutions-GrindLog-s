# 1984. Minimum Difference Between Highest and Lowest of K Scores


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`, where `nums[i]` represents the score of the `i^th` student. You are also given an integer `k`.

Pick the scores of any `k` students from the array so that the **difference** between the **highest** and the **lowest** of the `k` scores is **minimized**.

Return *the **minimum** possible difference*.

 

Example 1:**

```

**Input:** nums = [90], k = 1
**Output:** 0
**Explanation:** There is one way to pick score(s) of one student:
- [**90**]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

```

Example 2:**

```

**Input:** nums = [9,4,1,7], k = 2
**Output:** 2
**Explanation:** There are six ways to pick score(s) of two students:
- [**9**,**4**,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [**9**,4,**1**,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [**9**,4,1,**7**]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,**4**,**1**,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,**4**,1,**7**]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,**1**,**7**]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
```

 

**Constraints:**

	- `1 <= k <= nums.length <= 1000`

	- `0 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem requires us to find the minimum difference between the highest and lowest scores of k students. To achieve this, we can sort the scores in ascending order and then slide a window of size k over the sorted array. The minimum difference will be the difference between the highest and lowest scores within each window.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Subtract 1 from `k` to adjust the window size.
3. Initialize `mini` to positive infinity to store the minimum difference found so far.
4. Iterate over the sorted array starting from the k-th element (inclusive) to the end.
5. For each element, calculate the difference between the current element and the element k positions before it.
6. If the calculated difference is less than the current minimum difference, update `mini` with the new difference.
7. Return the minimum difference found.

**Time Complexity**
O(n log n) due to the sorting step, where n is the length of the input array `nums`. The subsequent iteration and calculations take O(n) time, but the sorting dominates the overall time complexity.

**Space Complexity**
O(1) since we only use a constant amount of space to store the minimum difference and other variables, regardless of the input size.

**Key Insight**
The key insight here is that by sorting the scores and sliding a window of size k over the sorted array, we can efficiently find the minimum difference between the highest and lowest scores of k students. This approach takes advantage of the fact that the sorted array allows us to quickly identify the highest and lowest scores within each window.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 96.25%) |
| 💾 Memory | 19.6 MB (Beats 14.62%) |
| 📅 Solved | 2026-01-25 |
| 💻 Language | Python |