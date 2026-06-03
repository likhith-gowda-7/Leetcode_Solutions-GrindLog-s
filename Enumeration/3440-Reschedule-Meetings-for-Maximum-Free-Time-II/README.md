> 📌 **Cross-listed:** Primary location is [Array/3440-Reschedule-Meetings-for-Maximum-Free-Time-II](../../Array/3440-Reschedule-Meetings-for-Maximum-Free-Time-II). This problem also appears under: **Array**, **Greedy**, **Enumeration**

# 3440. Reschedule Meetings for Maximum Free Time II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/)


## 📝 Problem Description

You are given an integer `eventTime` denoting the duration of an event. You are also given two integer arrays `startTime` and `endTime`, each of length `n`.

These represent the start and end times of `n` **non-overlapping** meetings that occur during the event between time `t = 0` and time `t = eventTime`, where the `i^th` meeting occurs during the time `[startTime[i], endTime[i]].`

You can reschedule **at most **one meeting by moving its start time while maintaining the **same duration**, such that the meetings remain non-overlapping, to **maximize** the **longest** *continuous period of free time* during the event.

Return the **maximum** amount of free time possible after rearranging the meetings.

**Note** that the meetings can **not** be rescheduled to a time outside the event and they should remain non-overlapping.

**Note:** *In this version*, it is **valid** for the relative ordering of the meetings to change after rescheduling one meeting.

 

Example 1:**

**Input:** eventTime = 5, startTime = [1,3], endTime = [2,5]

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/12/22/example0_rescheduled.png)

Reschedule the meeting at `[1, 2]` to `[2, 3]`, leaving no meetings during the time `[0, 2]`.

Example 2:**

**Input:** eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

**Output:** 7

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/12/22/rescheduled_example0.png)

Reschedule the meeting at `[0, 1]` to `[8, 9]`, leaving no meetings during the time `[0, 7]`.

Example 3:**

**Input:** eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

**Output:** 6

**Explanation:**

**![](https://assets.leetcode.com/uploads/2025/01/28/image3.png)**

Reschedule the meeting at `[3, 4]` to `[8, 9]`, leaving no meetings during the time `[1, 7]`.

Example 4:**

**Input:** eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

**Output:** 0

**Explanation:**

There is no time during the event not occupied by meetings.

 

**Constraints:**

	- `1 <= eventTime <= 10^9`

	- `n == startTime.length == endTime.length`

	- `2 <= n <= 10^5`

	- `0 <= startTime[i] < endTime[i] <= eventTime`

	- `endTime[i] <= startTime[i + 1]` where `i` lies in the range `[0, n - 2]`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to find the maximum free time possible after rearranging the meetings. The key idea is to maintain a priority queue of free times and try to find a meeting that can be rescheduled to maximize the continuous period of free time.

**Approach**
1. First, calculate the free time between each pair of consecutive meetings and store them in a list.
2. Initialize a priority queue (min heap) to store the free times. The priority queue will store tuples of (free time, index of the free time).
3. Iterate through the free times and push them into the priority queue. If the priority queue size exceeds 3, remove the smallest free time (the one at the top of the heap) if it is smaller than the current free time.
4. Define a helper function `find_pos` to check if a meeting can be rescheduled to a certain position. This function iterates through the priority queue and checks if there is a free time that is greater than or equal to the required length and is not adjacent to the current meeting.
5. Iterate through the meetings and calculate the maximum free time possible by trying to reschedule each meeting to a position where it does not overlap with the previous or next meeting.

**Time Complexity**
O(n log n) due to the priority queue operations (push and pop). The priority queue size is at most 3, so the time complexity is dominated by the iteration through the free times.

**Space Complexity**
O(n) for storing the free times and the priority queue.

**Key Insight**
The key insight is to maintain a priority queue of free times and use it to efficiently find a meeting that can be rescheduled to maximize the continuous period of free time. By using a priority queue, we can quickly find the smallest free time that can be used to reschedule a meeting, which is essential for achieving the optimal solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 179 ms (Beats 70.37%) |
| 💾 Memory | 38.7 MB (Beats 98.15%) |
| 📅 Solved | 2025-07-11 |
| 💻 Language | Python |