# 2187. Minimum Time to Complete Trips


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-time-to-complete-trips/)


## 📝 Problem Description

You are given an array `time` where `time[i]` denotes the time taken by the `i^th` bus to complete **one trip**.

Each bus can make multiple trips **successively**; that is, the next trip can start **immediately after** completing the current trip. Also, each bus operates **independently**; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer `totalTrips`, which denotes the number of trips all buses should make **in total**. Return *the **minimum time** required for all buses to complete **at least** *`totalTrips`* trips*.

 

Example 1:**

```

**Input:** time = [1,2,3], totalTrips = 5
**Output:** 3
**Explanation:**
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

```

Example 2:**

```

**Input:** time = [2], totalTrips = 1
**Output:** 2
**Explanation:**
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.

```

 

**Constraints:**

	- `1 <= time.length <= 10^5`

	- `1 <= time[i], totalTrips <= 10^7`

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach to find the minimum time required for all buses to complete at least `totalTrips` trips. The idea is to find the smallest time `t` such that the total number of trips completed by all buses is greater than or equal to `totalTrips`.

**Approach**
1. Initialize the search range to `[1, min(time) * totalTrips]`, where `min(time)` is the minimum time taken by any bus to complete one trip, and `totalTrips` is the total number of trips required.
2. While the search range is not empty, calculate the mid value `mid` of the range.
3. For each bus, calculate the number of trips completed by dividing `mid` by the time taken by the bus.
4. If the total number of trips completed by all buses is greater than or equal to `totalTrips`, update the upper bound of the search range to `mid - 1`.
5. Otherwise, update the lower bound of the search range to `mid + 1`.
6. Repeat steps 2-5 until the search range is empty.
7. Return the lower bound of the search range, which represents the minimum time required for all buses to complete at least `totalTrips` trips.

**Time Complexity**
O(n * log(min(time) * totalTrips)), where n is the number of buses. The binary search takes O(log(min(time) * totalTrips)) time, and for each iteration, we calculate the number of trips completed by each bus, which takes O(n) time.

**Space Complexity**
O(1), as we only use a constant amount of space to store the search range, mid value, and total number of trips completed.

**Key Insight**
The key insight is that we can use binary search to find the minimum time required for all buses to complete at least `totalTrips` trips, by iteratively narrowing down the search range based on the total number of trips completed by all buses.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 582 ms (Beats 97.77%) |
| 💾 Memory | 30.4 MB (Beats 100%) |
| 📅 Solved | 2025-07-08 |
| 💻 Language | Python |