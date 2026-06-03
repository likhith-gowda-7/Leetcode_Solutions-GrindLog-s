# 874. Walking Robot Simulation


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/walking-robot-simulation/)


## 📝 Problem Description

A robot on an infinite XY-plane starts at point `(0, 0)` facing north. The robot receives an array of integers `commands`, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:

	- `-2`: Turn left `90` degrees.

	- `-1`: Turn right `90` degrees.

	- `1 <= k <= 9`: Move forward `k` units, one unit at a time.

Some of the grid squares are `obstacles`. The `i^th` obstacle is at grid point `obstacles[i] = (x_i, y_i)`. If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the **maximum squared Euclidean distance** that the robot reaches at any point in its path (i.e. if the distance is `5`, return `25`).

**Note:**

	- There can be an obstacle at `(0, 0)`. If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to `(0, 0)` due to the obstacle.

	- North means +Y direction.

	- East means +X direction.

	- South means -Y direction.

	- West means -X direction.

 

Example 1:**

**Input:** commands = [4,-1,3], obstacles = []

**Output:** 25

**Explanation: **

The robot starts at `(0, 0)`:

	- Move north 4 units to `(0, 4)`.

	- Turn right.

	- Move east 3 units to `(3, 4)`.

The furthest point the robot ever gets from the origin is `(3, 4)`, which squared is `3^2 + 4^2 = 25` units away.

Example 2:**

**Input:** commands = [4,-1,4,-2,4], obstacles = [[2,4]]

**Output:** 65

**Explanation:**

The robot starts at `(0, 0)`:

	- Move north 4 units to `(0, 4)`.

	- Turn right.

	- Move east 1 unit and get blocked by the obstacle at `(2, 4)`, robot is at `(1, 4)`.

	- Turn left.

	- Move north 4 units to `(1, 8)`.

The furthest point the robot ever gets from the origin is `(1, 8)`, which squared is `1^2 + 8^2 = 65` units away.

Example 3:**

**Input:** commands = [6,-1,-1,6], obstacles = [[0,0]]

**Output:** 36

**Explanation:**

The robot starts at `(0, 0)`:

	- Move north 6 units to `(0, 6)`.

	- Turn right.

	- Turn right.

	- Move south 5 units and get blocked by the obstacle at `(0,0)`, robot is at `(0, 1)`.

The furthest point the robot ever gets from the origin is `(0, 6)`, which squared is `6^2 = 36` units away.

 

**Constraints:**

	- `1 <= commands.length <= 10^4`

	- `commands[i]` is either `-2`, `-1`, or an integer in the range `[1, 9]`.

	- `0 <= obstacles.length <= 10^4`

	- `-3 * 10^4 <= x_i, y_i <= 3 * 10^4`

	- The answer is guaranteed to be less than `2^31`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a simulation approach to track the robot's movement and calculate the maximum squared Euclidean distance it reaches. It iterates through the commands, updating the robot's position and direction accordingly, while checking for obstacles and updating the maximum distance.

**Approach**
1. Store obstacles in a set for efficient lookups.
2. Define the possible directions (North, East, South, West) as a list of tuples.
3. Initialize the robot's position at (0, 0) and direction as North.
4. Iterate through the commands:
	* If the command is -1, turn right by incrementing the direction modulo 4.
	* If the command is -2, turn left by incrementing the direction modulo 4.
	* Otherwise, move forward in the current direction, checking for obstacles and updating the maximum distance.
5. After iterating through all commands, return the maximum squared Euclidean distance.

**Time Complexity**
O(n), where n is the number of commands. This is because we iterate through the commands once, and each command takes constant time to process.

**Space Complexity**
O(m), where m is the number of obstacles. We store the obstacles in a set for efficient lookups, which takes O(m) space.

**Key Insight**
The key insight is to use a simulation approach to track the robot's movement, rather than trying to calculate the maximum distance analytically. This allows us to handle the obstacles and direction changes efficiently, making the solution scalable and easy to implement.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 37 ms (Beats 41.68%) |
| 💾 Memory | 23.8 MB (Beats 50.51%) |
| 📅 Solved | 2026-04-06 |
| 💻 Language | Python |