> 📌 **Cross-listed:** Primary location is [Array/3633-Earliest-Finish-Time-for-Land-and-Water-Rides-I](../../Array/3633-Earliest-Finish-Time-for-Land-and-Water-Rides-I). This problem also appears under: **Array**, **Two Pointers**, **Binary Search**, **Greedy**, **Sorting**

# 3633. Earliest Finish Time for Land and Water Rides I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/)


## 📝 Problem Description

You are given two categories of theme park attractions: land rides** and water rides**.

	Land rides**

	
		landStartTime[i]` &ndash; the earliest time the `i^th` land ride can be boarded.

		landDuration[i]` &ndash; how long the `i^th` land ride lasts.

	
	

	- Water rides**
	
		- waterStartTime[j]` &ndash; the earliest time the `j^th` water ride can be boarded.

		- waterDuration[j]` &ndash; how long the `j^th` water ride lasts.

	
	

A tourist must experience exactly one** ride from each** category, in either order**.

	A ride may be started at its opening time or any later moment**.

	If a ride is started at time t`, it finishes at time t + duration`.

	Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the earliest possible time** at which the tourist can finish both rides.

 

Example 1:**

**Input:** landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]

**Output:** 9

**Explanation:**​​​​​​​

	Plan A (land ride 0 &rarr; water ride 0):
	
		Start land ride 0 at time landStartTime[0] = 2`. Finish at 2 + landDuration[0] = 6`.

		Water ride 0 opens at time waterStartTime[0] = 6`. Start immediately at 6`, finish at 6 + waterDuration[0] = 9`.

	
	

	Plan B (water ride 0 &rarr; land ride 1):
	
		Start water ride 0 at time waterStartTime[0] = 6`. Finish at 6 + waterDuration[0] = 9`.

		Land ride 1 opens at landStartTime[1] = 8`. Start at time 9`, finish at 9 + landDuration[1] = 10`.

	
	

	Plan C (land ride 1 &rarr; water ride 0):
	
		Start land ride 1 at time landStartTime[1] = 8`. Finish at 8 + landDuration[1] = 9`.

		Water ride 0 opened at waterStartTime[0] = 6`. Start at time 9`, finish at 9 + waterDuration[0] = 12`.

	
	

	Plan D (water ride 0 &rarr; land ride 0):
	
		Start water ride 0 at time waterStartTime[0] = 6`. Finish at 6 + waterDuration[0] = 9`.

		Land ride 0 opened at landStartTime[0] = 2`. Start at time 9`, finish at 9 + landDuration[0] = 13`.

	
	

Plan A gives the earliest finish time of 9.

Example 2:**

**Input:** landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]

**Output:** 14

**Explanation:**​​​​​​​

	Plan A (water ride 0 &rarr; land ride 0):
	
		Start water ride 0 at time waterStartTime[0] = 1`. Finish at 1 + waterDuration[0] = 11`.

		Land ride 0 opened at landStartTime[0] = 5`. Start immediately at 11` and finish at 11 + landDuration[0] = 14`.

	
	

	Plan B (land ride 0 &rarr; water ride 0):
	
		Start land ride 0 at time landStartTime[0] = 5`. Finish at 5 + landDuration[0] = 8`.

		Water ride 0 opened at waterStartTime[0] = 1`. Start immediately at 8` and finish at 8 + waterDuration[0] = 18`.

	
	

Plan A provides the earliest finish time of 14.**​​​​​​​**

 

**Constraints:**

	1 <= n, m <= 100`

	landStartTime.length == landDuration.length == n`

	waterStartTime.length == waterDuration.length == m`

	1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the fact that the tourist can board the land ride or water ride immediately after finishing the other, as long as it is already open. It iteratively updates the minimum possible finish time for each category of rides and uses these values to find the earliest finish time for the tourist.

**Approach**
1. Initialize the minimum possible finish time for land rides (`minL`) and water rides (`minW`) to a large value (3000).
2. Iterate through each land ride and update `minL` to be the minimum of its current value and the finish time of the current land ride.
3. Iterate through each water ride and update `minW` to be the minimum of its current value and the finish time of the current water ride. Also, update the result (`res`) to be the minimum of its current value and the maximum of `minL` and the start time of the current water ride, plus the duration of the current water ride.
4. Iterate through each land ride again and update the result (`res`) to be the minimum of its current value and the maximum of `minW` and the start time of the current land ride, plus the duration of the current land ride.
5. Return the result, which represents the earliest finish time for the tourist.

**Time Complexity**
O(n + m), where n is the number of land rides and m is the number of water rides. This is because we iterate through each ride once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the minimum possible finish times and the result.

**Key Insight**
The key insight is that we can use the minimum possible finish times for each category of rides to find the earliest finish time for the tourist. By iteratively updating these values and using them to find the minimum possible finish time for the tourist, we can efficiently solve the problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 86.15%) |
| 💾 Memory | 19.3 MB (Beats 85.05%) |
| 📅 Solved | 2026-06-03 |
| 💻 Language | Python |