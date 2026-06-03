# 1094. Car Pooling


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/car-pooling/)


## 📝 Problem Description

There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengers_i, from_i, to_i]` indicates that the `i^th` trip has `numPassengers_i` passengers and the locations to pick them up and drop them off are `from_i` and `to_i` respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return `true`* if it is possible to pick up and drop off all passengers for all the given trips, or *`false`* otherwise*.

 

Example 1:**

```

**Input:** trips = [[2,1,5],[3,3,7]], capacity = 4
**Output:** false

```

Example 2:**

```

**Input:** trips = [[2,1,5],[3,3,7]], capacity = 5
**Output:** true

```

 

**Constraints:**

	- `1 <= trips.length <= 1000`

	- `trips[i].length == 3`

	- `1 <= numPassengers_i <= 100`

	- `0 <= from_i < to_i <= 1000`

	- `1 <= capacity <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a simulation approach to track the number of passengers at each location. By maintaining an array to store the net number of passengers at each location, we can efficiently determine if it's possible to pick up and drop off all passengers.

**Approach**
1. Find the maximum drop-off location to determine the size of the difference array.
2. Initialize a difference array of size `maxi + 1` with all elements set to 0.
3. Iterate through each trip and update the difference array at the pick-up and drop-off locations.
   - At the pick-up location, increment the net number of passengers by the number of passengers in the trip.
   - At the drop-off location, decrement the net number of passengers by the number of passengers in the trip.
4. Iterate through the difference array and check if any location has more passengers than the capacity.
5. If a location has more passengers than the capacity, return False. Otherwise, return True.

**Time Complexity**
O(n), where n is the number of trips. We iterate through each trip twice to update the difference array and check the capacity.

**Space Complexity**
O(n), where n is the maximum drop-off location. We use a difference array of size `maxi + 1` to store the net number of passengers at each location.

**Key Insight**
The key insight is to use a simulation approach to track the net number of passengers at each location, which allows us to efficiently determine if it's possible to pick up and drop off all passengers. By maintaining a difference array, we can avoid iterating through the trips multiple times and reduce the time complexity to O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-07-12 |
| 💻 Language | Python |