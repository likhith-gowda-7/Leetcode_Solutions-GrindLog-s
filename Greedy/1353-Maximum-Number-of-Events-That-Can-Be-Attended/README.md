> 📌 **Cross-listed:** Primary location is [Array/1353-Maximum-Number-of-Events-That-Can-Be-Attended](../../Array/1353-Maximum-Number-of-Events-That-Can-Be-Attended). This problem also appears under: **Array**, **Greedy**, **Sorting**, **Heap (Priority Queue)**

# 1353. Maximum Number of Events That Can Be Attended


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)


## 📝 Problem Description

You are given an array of `events` where `events[i] = [startDay_i, endDay_i]`. Every event `i` starts at `startDay_i`_ and ends at `endDay_i`.

You can attend an event `i` at any day `d` where `startDay_i <= d <= endDay_i`. You can only attend one event at any time `d`.

Return *the maximum number of events you can attend*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/02/05/e1.png)
```

**Input:** events = [[1,2],[2,3],[3,4]]
**Output:** 3
**Explanation:** You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

```

Example 2:**

```

**Input:** events= [[1,2],[2,3],[3,4],[1,2]]
**Output:** 4

```

 

**Constraints:**

	- `1 <= events.length <= 10^5`

	- `events[i].length == 2`

	- `1 <= startDay_i <= endDay_i <= 10^5`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 113 ms (Beats 92.41%) |
| 💾 Memory | 53.3 MB (Beats 96.78%) |
| 📅 Solved | 2025-07-07 |
| 💻 Language | Python |