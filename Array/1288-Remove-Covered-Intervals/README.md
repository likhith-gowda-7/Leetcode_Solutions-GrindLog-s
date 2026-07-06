# 1288. Remove Covered Intervals


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-covered-intervals/)


## 📝 Problem Description

Given an array `intervals` where `intervals[i] = [l_i, r_i]` represent the interval `[l_i, r_i)`, remove all intervals that are covered by another interval in the list.

The interval `[a, b)` is covered by the interval `[c, d)` if and only if `c <= a` and `b <= d`.

Return *the number of remaining intervals*.

 

Example 1:**

```

**Input:** intervals = [[1,4],[3,6],[2,8]]
**Output:** 2
**Explanation:** Interval [3,6] is covered by [2,8], therefore it is removed.

```

Example 2:**

```

**Input:** intervals = [[1,4],[2,3]]
**Output:** 1

```

 

**Constraints:**

	- `1 <= intervals.length <= 1000`

	- `intervals[i].length == 2`

	- `0 <= l_i < r_i <= 10^5`

	- All the given intervals are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting the intervals based on their start and end points. The sorting key is a tuple where the start point comes first and the end point comes second, but with a negative sign. This ensures that intervals with the same start point are sorted in descending order of their end points. Then, it iterates through the sorted intervals and increments the result count whenever it encounters an interval with an end point greater than the current maximum end point.

**Approach**
1. Sort the intervals based on their start and end points using a lambda function as the sorting key.
2. Initialize a variable `max_end` to keep track of the maximum end point seen so far, and a variable `res` to count the number of remaining intervals.
3. Iterate through the sorted intervals.
4. For each interval, check if its end point is greater than the current `max_end`.
5. If it is, increment the `res` count and update `max_end` with the current interval's end point.

**Time Complexity**
O(n log n), where n is the number of intervals. This is because the sorting step takes O(n log n) time, and the iteration through the sorted intervals takes O(n) time.

**Space Complexity**
O(1), excluding the space needed for the input and output. The solution only uses a constant amount of extra space to store the `max_end` and `res` variables.

**Key Insight**
The key insight is that by sorting the intervals based on their start and end points, we can efficiently identify the intervals that are not covered by any other interval. The sorting ensures that intervals with the same start point are sorted in descending order of their end points, which allows us to keep track of the maximum end point seen so far and increment the result count whenever we encounter an interval with an end point greater than the current maximum end point.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 77.5%) |
| 💾 Memory | 19.7 MB (Beats 13.54%) |
| 📅 Solved | 2026-07-06 |
| 💻 Language | Python |