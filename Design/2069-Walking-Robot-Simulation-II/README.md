# 2069. Walking Robot Simulation II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Design](https://img.shields.io/badge/Design-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/walking-robot-simulation-ii/)


## 📝 Problem Description

A `width x height` grid is on an XY-plane with the **bottom-left** cell at `(0, 0)` and the **top-right** cell at `(width - 1, height - 1)`. The grid is aligned with the four cardinal directions (`"North"`, `"East"`, `"South"`, and `"West"`). A robot is **initially** at cell `(0, 0)` facing direction `"East"`.

The robot can be instructed to move for a specific number of **steps**. For each step, it does the following.

	- Attempts to move **forward one** cell in the direction it is facing.

	- If the cell the robot is **moving to** is **out of bounds**, the robot instead **turns** 90 degrees **counterclockwise** and retries the step.

After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the `Robot` class:

	- `Robot(int width, int height)` Initializes the `width x height` grid with the robot at `(0, 0)` facing `"East"`.

	- `void step(int num)` Instructs the robot to move forward `num` steps.

	- `int[] getPos()` Returns the current cell the robot is at, as an array of length 2, `[x, y]`.

	- `String getDir()` Returns the current direction of the robot, `"North"`, `"East"`, `"South"`, or `"West"`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/10/09/example-1.png)
```

**Input**
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
**Output**
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

**Explanation**
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces **North** (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"

```

 

**Constraints:**

	- `2 <= width, height <= 100`

	- `1 <= num <= 10^5`

	- At most `10^4` calls **in total** will be made to `step`, `getPos`, and `getDir`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a clever approach to simulate the robot's movement by taking advantage of the grid's symmetry and the robot's turning behavior. By reducing the problem to a series of steps, the solution can efficiently calculate the final position and direction of the robot.

**Approach**
1. In the `step` method, calculate the total perimeter of the grid and take the remainder of the number of steps modulo the perimeter. This is because the robot's movement is periodic and can be reduced to a smaller number of steps.
2. Initialize a while loop that continues until the number of steps is reduced to 0.
3. Inside the loop, check the current direction of the robot and calculate the maximum x or y coordinate that the robot can reach without going out of bounds.
4. If the robot can reach the maximum coordinate, update its position and set the direction to the next one (e.g., from "East" to "North").
5. If the robot cannot reach the maximum coordinate, update its position to the maximum coordinate and change its direction to the next one.
6. Repeat steps 3-5 until the number of steps is reduced to 0.

**Time Complexity**
O(n), where n is the number of steps. The while loop runs until the number of steps is reduced to 0, and each iteration takes constant time.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the robot's position and direction.

**Key Insight**
The key insight is that the robot's movement can be reduced to a series of steps, and by taking advantage of the grid's symmetry and the robot's turning behavior, we can efficiently calculate the final position and direction of the robot. This is achieved by using the remainder of the number of steps modulo the perimeter and by updating the robot's position and direction in a way that takes into account the grid's boundaries.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 85 ms (Beats 34.43%) |
| 💾 Memory | 24.1 MB (Beats 27.51%) |
| 📅 Solved | 2026-04-07 |
| 💻 Language | Python |