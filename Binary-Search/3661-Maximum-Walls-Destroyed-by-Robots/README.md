> 📌 **Cross-listed:** Primary location is [Array/3661-Maximum-Walls-Destroyed-by-Robots](../../Array/3661-Maximum-Walls-Destroyed-by-Robots). This problem also appears under: **Array**, **Binary Search**, **Dynamic Programming**, **Sorting**

# 3661. Maximum Walls Destroyed by Robots


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-walls-destroyed-by-robots/)


## 📝 Problem Description

There is an endless straight line populated with some robots and walls. You are given integer arrays `robots`, `distance`, and `walls`:

	- `robots[i]` is the position of the `i^th` robot.

	- `distance[i]` is the **maximum** distance the `i^th` robot's bullet can travel.

	- `walls[j]` is the position of the `j^th` wall.

Every robot has **one** bullet that can either fire to the left or the right **at most **`distance[i]` meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it **immediately stops** at that robot and cannot continue.

Return the **maximum** number of **unique** walls that can be destroyed by the robots.

Notes:

	- A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.

	- Robots are not destroyed by bullets.

 

Example 1:**

**Input:** robots = [4], distance = [3], walls = [1,10]

**Output:** 1

**Explanation:**

	- `robots[0] = 4` fires **left** with `distance[0] = 3`, covering `[1, 4]` and destroys `walls[0] = 1`.

	- Thus, the answer is 1.

Example 2:**

**Input:** robots = [10,2], distance = [5,1], walls = [5,2,7]

**Output:** 3

**Explanation:**

	- `robots[0] = 10` fires **left** with `distance[0] = 5`, covering `[5, 10]` and destroys `walls[0] = 5` and `walls[2] = 7`.

	- `robots[1] = 2` fires **left** with `distance[1] = 1`, covering `[1, 2]` and destroys `walls[1] = 2`.

	- Thus, the answer is 3.

Example 3:**

**Input:** robots = [1,2], distance = [100,1], walls = [10]

**Output:** 0

**Explanation:**

In this example, only `robots[0]` can reach the wall, but its shot to the **right** is blocked by `robots[1]`; thus the answer is 0.

 

**Constraints:**

	- `1 <= robots.length == distance.length <= 10^5`

	- `1 <= walls.length <= 10^5`

	- `1 <= robots[i], walls[j] <= 10^9`

	- `1 <= distance[i] <= 10^5`

	- All values in `robots` are **unique**

	- All values in `walls` are **unique**

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the maximum number of unique walls that can be destroyed by the robots. We can approach this problem by considering the maximum distance each robot's bullet can travel and the position of the walls. By analyzing the possible paths of the bullets and the positions of the walls, we can calculate the maximum number of walls that can be destroyed.

**Approach**
1. First, we create a dictionary `robots_to_distance` to store the position of each robot as the key and its corresponding maximum distance as the value.
2. We sort the robots and walls arrays in ascending order.
3. We initialize three arrays `left`, `right`, and `num` to store the number of walls that can be destroyed by each robot from the left, right, and the overlap of the two, respectively.
4. We iterate through the sorted robots array and for each robot, we calculate the number of walls that can be destroyed from the left and right using binary search.
5. We then calculate the overlap of the two and store it in the `num` array.
6. We initialize two variables `sub_left` and `sub_right` to store the maximum number of walls that can be destroyed from the left and right, respectively.
7. We iterate through the `left` and `right` arrays and update `sub_left` and `sub_right` by considering the maximum number of walls that can be destroyed from the left and right, respectively.
8. Finally, we return the maximum of `sub_left` and `sub_right`.

**Time Complexity**
The time complexity of this solution is O(n log n + m log n), where n is the number of robots and m is the number of walls. This is because we are using binary search to find the position of the walls, which takes O(log n) time, and we are iterating through the robots and walls arrays, which takes O(n) time.

**Space Complexity**
The space complexity of this solution is O(n + m), where n is the number of robots and m is the number of walls. This is because we are storing the position of each robot and wall in the `robots_to_distance` dictionary and the `left`, `right`, and `num` arrays.

**Key Insight**
The key insight of this solution is to consider the overlap of the two paths of the bullets and the position of the walls. By analyzing the possible paths of the bullets and the positions of the walls, we can calculate the maximum number of walls that can be destroyed. This is achieved by using binary search to find the position of the walls and iterating through the robots and walls arrays to calculate the number of walls that can be destroyed.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 704 ms (Beats 70.54%) |
| 💾 Memory | 48.7 MB (Beats 69.7%) |
| 📅 Solved | 2026-04-03 |
| 💻 Language | Python |