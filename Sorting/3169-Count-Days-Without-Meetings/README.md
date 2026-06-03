> 📌 **Cross-listed:** Primary location is [Array/3169-Count-Days-Without-Meetings](../../Array/3169-Count-Days-Without-Meetings). This problem also appears under: **Array**, **Sorting**

# 3169. Count Days Without Meetings


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-days-without-meetings/)


## 📝 Problem Description

You are given a positive integer `days` representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array `meetings` of size `n` where, `meetings[i] = [start_i, end_i]` represents the starting and ending days of meeting `i` (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

**Note: **The meetings may overlap.

 

Example 1:**

**Input:** days = 10, meetings = [[5,7],[1,3],[9,10]]

**Output:** 2

**Explanation:**

There is no meeting scheduled on the 4^th and 8^th days.

Example 2:**

**Input:** days = 5, meetings = [[2,4],[1,3]]

**Output:** 1

**Explanation:**

There is no meeting scheduled on the 5^th day.

Example 3:**

**Input:** days = 6, meetings = [[1,6]]

**Output:** 0

**Explanation:**

Meetings are scheduled for all working days.

 

**Constraints:**

	- `1 <= days <= 10^9`

	- `1 <= meetings.length <= 10^5`

	- `meetings[i].length == 2`

	- `1 <= meetings[i][0] <= meetings[i][1] <= days`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the sorted meetings array and subtracting the number of days each meeting occupies from the total available days. The key insight is to consider the days when a meeting starts after the previous meeting ends, in which case we can simply subtract the duration of the current meeting. However, when a meeting starts before the previous meeting ends, we need to subtract the remaining days of the current meeting, ensuring we don't double-count the days.

**Approach**
1. Initialize `prev_end` to 0, representing the end of the previous meeting.
2. Sort the meetings array based on the start time of each meeting.
3. Iterate through the sorted meetings array:
   1. If the start time of the current meeting is greater than `prev_end`, subtract the duration of the current meeting from the total available days.
   2. If the start time of the current meeting is less than or equal to `prev_end`, subtract the remaining days of the current meeting from the total available days.
   3. Update `prev_end` to the maximum of its current value and the end time of the current meeting.
4. Return the total available days.

**Time Complexity**
O(n log n) due to the sorting of the meetings array, where n is the number of meetings.

**Space Complexity**
O(1) as we only use a constant amount of space to store the `prev_end` variable and the iteration variables.

**Key Insight**
The solution relies on the observation that the days when no meetings are scheduled are the days when a meeting starts after the previous meeting ends. By iterating through the sorted meetings array and subtracting the duration of each meeting, we can efficiently count the available days.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 220 ms (Beats 16.22%) |
| 💾 Memory | 52.8 MB (Beats 91.59%) |
| 📅 Solved | 2025-03-24 |
| 💻 Language | Python |