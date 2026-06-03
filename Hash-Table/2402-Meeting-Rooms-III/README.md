> 📌 **Cross-listed:** Primary location is [Array/2402-Meeting-Rooms-III](../../Array/2402-Meeting-Rooms-III). This problem also appears under: **Array**, **Hash Table**, **Sorting**, **Heap (Priority Queue)**, **Simulation**

# 2402. Meeting Rooms III


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/meeting-rooms-iii/)


## 📝 Problem Description

You are given an integer `n`. There are `n` rooms numbered from `0` to `n - 1`.

You are given a 2D integer array `meetings` where `meetings[i] = [start_i, end_i]` means that a meeting will be held during the **half-closed** time interval `[start_i, end_i)`. All the values of `start_i` are **unique**.

Meetings are allocated to rooms in the following manner:

	- Each meeting will take place in the unused room with the **lowest** number.

	- If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the **same** duration as the original meeting.

	- When a room becomes unused, meetings that have an earlier original **start** time should be given the room.

Return* the **number** of the room that held the most meetings. *If there are multiple rooms, return* the room with the **lowest** number.*

A **half-closed interval** `[a, b)` is the interval between `a` and `b` **including** `a` and **not including** `b`.

 

Example 1:**

```

**Input:** n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
**Output:** 0
**Explanation:**
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 

```

Example 2:**

```

**Input:** n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
**Output:** 1
**Explanation:**
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

```

 

**Constraints:**

	- `1 <= n <= 100`

	- `1 <= meetings.length <= 10^5`

	- `meetings[i].length == 2`

	- `0 <= start_i < end_i <= 5 * 10^5`

	- All the values of `start_i` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The problem requires us to allocate meetings to rooms in a way that maximizes the number of meetings held in a single room. We can achieve this by maintaining a priority queue of free rooms and a priority queue of occupied rooms, along with a hash table to keep track of the frequency of each room.

**Approach**
1. Sort the meetings based on their start time.
2. Initialize a hash table `room_freq` to keep track of the frequency of each room.
3. Initialize a priority queue `free_rooms` with all room numbers from 0 to `n-1`.
4. Initialize an empty priority queue `occupied_rooms` to store occupied rooms along with their end times.
5. Iterate through the sorted meetings:
   1. Check if there are any occupied rooms that will be free by the current meeting's start time. If yes, pop them from the `occupied_rooms` queue and add them to the `free_rooms` queue.
   2. If there are free rooms, pop one from the `free_rooms` queue and assign it to the current meeting. Update the `room_freq` hash table and push the updated occupied room into the `occupied_rooms` queue.
   3. If there are no free rooms, pop the occupied room with the earliest end time from the `occupied_rooms` queue, delay it, and push it back into the `occupied_rooms` queue.
6. After iterating through all meetings, find the room with the maximum frequency and return its number.

**Time Complexity**
The time complexity is O(m log n + m log n), where m is the number of meetings. The first term comes from sorting the meetings, and the second term comes from maintaining the priority queues. Since we perform a constant number of operations for each meeting, the overall time complexity is linear.

**Space Complexity**
The space complexity is O(n + m), where n is the number of rooms and m is the number of meetings. We need to store the frequency of each room in the `room_freq` hash table, and we also need to store the occupied rooms in the `occupied_rooms` priority queue.

**Key Insight**
The key insight is to maintain a balance between the priority queue of free rooms and the priority queue of occupied rooms. By doing so, we can ensure that we always assign the meeting to the room with the lowest number that is available, which maximizes the number of meetings held in a single room.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 167 ms (Beats 94.97%) |
| 💾 Memory | 51.5 MB (Beats 98.52%) |
| 📅 Solved | 2025-07-11 |
| 💻 Language | Python |