> 📌 **Cross-listed:** Primary location is [Array/0056-Merge-Intervals](../../Array/0056-Merge-Intervals). This problem also appears under: **Array**, **Sorting**

# 56. Merge Intervals


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/merge-intervals/)


## 📝 Problem Description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

 

Example 1:**

```

**Input:** intervals = [[1,3],[2,6],[8,10],[15,18]]
**Output:** [[1,6],[8,10],[15,18]]
**Explanation:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

```

Example 2:**

```

**Input:** intervals = [[1,4],[4,5]]
**Output:** [[1,5]]
**Explanation:** Intervals [1,4] and [4,5] are considered overlapping.

```

Example 3:**

```

**Input:** intervals = [[4,7],[1,4]]
**Output:** [[1,7]]
**Explanation:** Intervals [1,4] and [4,7] are considered overlapping.

```

 

**Constraints:**

	- `1 <= intervals.length <= 10^4`

	- `intervals[i].length == 2`

	- `0 <= start_i <= end_i <= 10^4`

## 🧠 Solution Explanation

## Intuition
The approach to solving this problem involves sorting the intervals based on their start times and then merging any overlapping intervals. This works because once the intervals are sorted, we can easily identify which intervals overlap by comparing the end time of the current interval with the start time of the next interval.

## Approach
1. Sort the intervals based on their start times.
2. Initialize an empty list `res` to store the merged intervals and an index `idx` to track the current interval.
3. Iterate through the sorted intervals, and for each interval, check if it overlaps with the next interval.
4. If an overlap is found, update the end time of the current interval to be the maximum of its current end time and the end time of the overlapping interval.
5. Once all overlapping intervals have been merged, add the merged interval to the `res` list and move on to the next interval.

## Time Complexity
The time complexity is O(n log n) due to the sorting operation, where n is the number of intervals. The subsequent while loop has a total of n iterations across all intervals, resulting in a linear time complexity of O(n). However, this is dominated by the sorting operation.

## Space Complexity
The space complexity is O(n) for storing the merged intervals in the `res` list, where n is the number of intervals. In the worst-case scenario, if no intervals overlap, the size of the `res` list will be equal to the number of input intervals.

## Key Insight
The key insight to this solution is recognizing that sorting the intervals by their start times allows for efficient identification of overlapping intervals, enabling a simple iterative approach to merge them. This simplifies the problem and avoids unnecessary complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 25.08%) |
| 💾 Memory | 23.1 MB (Beats 38.54%) |
| 📅 Solved | 2026-05-16 |
| 💻 Language | Python |