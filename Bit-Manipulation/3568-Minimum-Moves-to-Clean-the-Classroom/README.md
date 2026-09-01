> 📌 **Cross-listed:** Primary location is [Array/3568-Minimum-Moves-to-Clean-the-Classroom](../../Array/3568-Minimum-Moves-to-Clean-the-Classroom). This problem also appears under: **Array**, **Hash Table**, **Bit Manipulation**, **Breadth-First Search**, **Matrix**

# 3568. Minimum Moves to Clean the Classroom


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/)


## 📝 Problem Description

You are given an `m x n` grid `classroom` where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

	- `'S'`: Starting position of the student

	- `'L'`: Litter that must be collected (once collected, the cell becomes empty)

	- `'R'`: Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)

	- `'X'`: Obstacle the student cannot pass through

	- `'.'`: Empty space

You are also given an integer `energy`, representing the student's maximum energy capacity. The student starts with this energy from the starting position `'S'`.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area `'R'`, which resets the energy to its **maximum** capacity `energy`.

Return the **minimum** number of moves required to collect all litter items, or `-1` if it's impossible.

 

Example 1:**

**Input:** classroom = ["S.", "XL"], energy = 2

**Output:** 2

**Explanation:**

	- The student starts at cell (0, 0)` with 2 units of energy.

	- Since cell `(1, 0)` contains an obstacle 'X', the student cannot move directly downward.

	- A valid sequence of moves to collect all litter is as follows:
	
		- Move 1: From `(0, 0)` &rarr; `(0, 1)` with 1 unit of energy and 1 unit remaining.

		- Move 2: From `(0, 1)` &rarr; `(1, 1)` to collect the litter `'L'`.

	
	

	- The student collects all the litter using 2 moves. Thus, the output is 2.

Example 2:**

**Input:** classroom = ["LS", "RL"], energy = 4

**Output:** 3

**Explanation:**

	- The student starts at cell (0, 1)` with 4 units of energy.

	- A valid sequence of moves to collect all litter is as follows:
	
		- Move 1: From `(0, 1)` &rarr; `(0, 0)` to collect the first litter `'L'` with 1 unit of energy used and 3 units remaining.

		- Move 2: From `(0, 0)` &rarr; `(1, 0)` to `'R'` to reset and restore energy back to 4.

		- Move 3: From `(1, 0)` &rarr; `(1, 1)` to collect the second litter 'L'`.

	
	

	- The student collects all the litter using 3 moves. Thus, the output is 3.

Example 3:**

**Input:** classroom = ["L.S", "RXL"], energy = 3

**Output:** -1

**Explanation:**

No valid path collects all `'L'`.

 

**Constraints:**

	- `1 <= m == classroom.length <= 20`

	- `1 <= n == classroom[i].length <= 20`

	- `classroom[i][j]` is one of `'S'`, `'L'`, `'R'`, `'X'`, or `'.'`

	- `1 <= energy <= 50`

	- There is exactly **one** `'S'` in the grid.

	- There are **at most** 10 `'L'` cells in the grid.

## 🧠 Solution Explanation

**Intuition**  
Collecting litter is a traveling‑salesman‑like problem, but the student can recharge at any reset cell.  
Treat each state as *where the student is, which litter has been picked, and how much energy remains*.  
A breadth‑first search over these states guarantees the first time we finish all litter is the minimum moves.

**Approach**  
1. Label every litter cell with a unique bit index.  
2. `total_mask = (1<<k)-1` represents all litter collected.  
3. Create a 3‑D array `best[r][c][mask]` storing the maximum remaining energy that can reach cell `(r,c)` having collected `mask`.  
4. Initialize BFS queue with the start position, mask = 0, energy = `energy`, moves = 0.  
5. While the queue is not empty, pop a state.  
   - For each of the four directions, skip out‑of‑bounds or obstacle cells.  
   - Consume one energy unit; if energy would drop below 0, skip.  
   - If the new cell is a reset (`'R'`), restore energy to full.  
   - If it is litter (`'L'`), set the corresponding bit in `mask`.  
   - If the new mask equals `total_mask`, return `moves+1`.  
   - If the new remaining energy is not better than `best[nr][nc][new_mask]`, skip.  
   - Otherwise, update `best` and enqueue the new state with `moves+1`.  
6. If the queue empties, return `-1` (impossible).

**Time Complexity**  
Each cell can be visited with each subset of litter (`2^k` masks).  
For every such state we examine 4 neighbors →  
`O(m · n · 2^k)` time.  

**Space Complexity**  
The `best` array stores `m · n · 2^k` integers, and the queue holds at most that many states →  
`O(m · n · 2^k)` space.  

**Key Insight**  
By keeping the *maximum* remaining energy for every (cell, mask) pair, we prune dominated states and ensure BFS explores only necessary paths, turning a potentially exponential search into a manageable `m·n·2^k` problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1536 ms (Beats 89.47%) |
| 💾 Memory | 24.7 MB (Beats 87.72%) |
| 📅 Solved | 2026-09-01 |
| 💻 Language | Python |