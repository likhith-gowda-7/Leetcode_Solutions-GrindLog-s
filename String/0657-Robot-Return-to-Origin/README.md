# 657. Robot Return to Origin


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/robot-return-to-origin/)


## 📝 Problem Description

There is a robot starting at the position `(0, 0)`, the origin, on a 2D plane. Given a sequence of its moves, judge if this robot **ends up at **`(0, 0)` after it completes its moves.

You are given a string `moves` that represents the move sequence of the robot where `moves[i]` represents its `i^th` move. Valid moves are `'R'` (right), `'L'` (left), `'U'` (up), and `'D'` (down).

Return `true`* if the robot returns to the origin after it finishes all of its moves, or *`false`* otherwise*.

**Note**: The way that the robot is "facing" is irrelevant. `'R'` will always make the robot move to the right once, `'L'` will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 

Example 1:**

```

**Input:** moves = "UD"
**Output:** true
**Explanation**: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

```

Example 2:**

```

**Input:** moves = "LL"
**Output:** false
**Explanation**: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

```

 

**Constraints:**

	- `1 <= moves.length <= 2 * 10^4`

	- `moves` only contains the characters `'U'`, `'D'`, `'L'` and `'R'`.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to determine if a robot returns to the origin after a sequence of moves. We can solve this by counting the number of up and down moves, and left and right moves, and checking if they are equal. If they are, the robot must have returned to the origin.

**Approach**
1. Count the number of up moves in the sequence using `moves.count("U")`.
2. Count the number of down moves in the sequence using `moves.count("D")`.
3. Count the number of left moves in the sequence using `moves.count("L")`.
4. Count the number of right moves in the sequence using `moves.count("R")`.
5. Return `True` if the counts of up and down moves are equal, and the counts of left and right moves are equal. Otherwise, return `False`.

**Time Complexity**
O(n), where n is the length of the `moves` string. This is because we are using the `count` method, which has a time complexity of O(n) in Python.

**Space Complexity**
O(1), because we are only using a constant amount of space to store the counts of up, down, left, and right moves. The space complexity does not depend on the input size.

**Key Insight**
The key insight here is that the robot's movement is symmetrical, meaning that every up move is matched by a down move, and every left move is matched by a right move. By counting the number of up and down moves, and left and right moves, we can determine if the robot has returned to the origin.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.1 MB (Beats 86.37%) |
| 📅 Solved | 2026-04-05 |
| 💻 Language | Python |