> 📌 **Cross-listed:** Primary location is [Array/0853-Car-Fleet](../../Array/0853-Car-Fleet). This problem also appears under: **Array**, **Stack**, **Sorting**, **Monotonic Stack**

# 853. Car Fleet


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/car-fleet/)


## 📝 Problem Description

There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.

You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `i^th` car and `speed[i]` is the speed of the `i^th` car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.

If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:**

**Input:** target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

**Output:** 3

**Explanation:**

	- The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at `target`.

	- The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.

	- The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches `target`.

Example 2:**

**Input:** target = 10, position = [3], speed = [3]

**Output:** 1

**Explanation:**

There is only one car, hence there is only one fleet.

Example 3:**

**Input:** target = 100, position = [0,2,4], speed = [4,2,1]

**Output:** 1

**Explanation:**

	- The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.

	- Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches `target`.

 

**Constraints:**

	- `n == position.length == speed.length`

	- `1 <= n <= 10^5`

	- `0 < target <= 10^6`

	- `0 <= position[i] < target`

	- All the values of `position` are **unique**.

	- `0 < speed[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the time taken by each car fleet to reach the destination. The key insight is that a car fleet is formed when a car catches up to another car, and the speed of the fleet is the minimum speed of any car in the fleet. By sorting the cars in descending order of their positions and using a stack to keep track of the time taken by each fleet, we can efficiently count the number of car fleets that will arrive at the destination.

**Approach**
1. Combine the position and speed of each car into a list of tuples, `car_order`, and sort it in descending order of position.
2. Initialize an empty stack to keep track of the time taken by each car fleet.
3. Iterate through each car in `car_order`. For each car, calculate the time taken to reach the destination and push it onto the stack.
4. If the current time taken is less than or equal to the previous time taken (i.e., the current car catches up to the previous fleet), pop the previous time taken from the stack.
5. After iterating through all cars, the size of the stack represents the number of car fleets that will arrive at the destination.

**Time Complexity**
O(n log n) due to the sorting step, where n is the number of cars.

**Space Complexity**
O(n) for storing the sorted list of cars and the stack.

**Key Insight**
The key to this solution is the observation that a car fleet is formed when a car catches up to another car, and the speed of the fleet is the minimum speed of any car in the fleet. By using a stack to keep track of the time taken by each fleet, we can efficiently count the number of car fleets that will arrive at the destination.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 173 ms (Beats 50.01%) |
| 💾 Memory | 37.6 MB (Beats 99.32%) |
| 📅 Solved | 2025-08-05 |
| 💻 Language | Python |