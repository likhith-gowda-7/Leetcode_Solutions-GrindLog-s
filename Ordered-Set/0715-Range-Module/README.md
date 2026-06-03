> 📌 **Cross-listed:** Primary location is [Design/0715-Range-Module](../../Design/0715-Range-Module). This problem also appears under: **Design**, **Segment Tree**, **Ordered Set**

# 715. Range Module


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Design](https://img.shields.io/badge/Design-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple) ![Ordered Set](https://img.shields.io/badge/Ordered%20Set-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/range-module/)


## 📝 Problem Description

A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as **half-open intervals** and query about them.

A **half-open interval** `[left, right)` denotes all the real numbers `x` where `left <= x < right`.

Implement the `RangeModule` class:

	- `RangeModule()` Initializes the object of the data structure.

	- `void addRange(int left, int right)` Adds the **half-open interval** `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.

	- `boolean queryRange(int left, int right)` Returns `true` if every real number in the interval `[left, right)` is currently being tracked, and `false` otherwise.

	- `void removeRange(int left, int right)` Stops tracking every real number currently being tracked in the **half-open interval** `[left, right)`.

 

Example 1:**

```

**Input**
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
**Output**
[null, null, null, true, false, true]

**Explanation**
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)

```

 

**Constraints:**

	- `1 <= left < right <= 10^9`

	- At most `10^4` calls will be made to `addRange`, `queryRange`, and `removeRange`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a data structure that tracks ranges of numbers as half-open intervals. It leverages the `bisect` module to maintain a sorted list of intervals, which enables efficient insertion, query, and removal operations. The key insight is to merge overlapping intervals during insertion to minimize the number of intervals stored.

**Approach**
1. Initialize an empty list `self.interval` to store the tracked intervals.
2. In `addRange(left, right)`, use `bisect.insort` to insert the new interval into the sorted list of intervals.
3. Merge overlapping intervals by iterating through the sorted list and updating the end points of adjacent intervals.
4. In `queryRange(left, right)`, use `bisect.bisect` to find the index of the first interval that overlaps with the query range.
5. If the first overlapping interval's end point is greater than or equal to the query range's end point, return `True`.
6. In `removeRange(left, right)`, iterate through the sorted list of intervals and remove the entire interval if it is entirely within the removal range.
7. If the removal range partially overlaps with an interval, split the interval into two parts and add them back to the list.

**Time Complexity**
- `addRange(left, right)`: O(n log n) due to the sorting operation using `bisect.insort`.
- `queryRange(left, right)`: O(log n) using `bisect.bisect`.
- `removeRange(left, right)`: O(n log n) due to the sorting operation using `bisect.insort` after splitting intervals.

**Space Complexity**
- O(n) to store the sorted list of intervals, where n is the number of tracked intervals.

**Key Insight**
The key to this solution is the efficient merging of overlapping intervals during insertion, which reduces the number of intervals stored and enables fast query and removal operations. This is achieved by maintaining a sorted list of intervals and updating the end points of adjacent intervals during insertion.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 406 ms (Beats 46.68%) |
| 💾 Memory | 22.5 MB (Beats 100%) |
| 📅 Solved | 2025-06-30 |
| 💻 Language | Python |