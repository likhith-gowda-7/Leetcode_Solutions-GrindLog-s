# 3443. Maximum Manhattan Distance After K Changes


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/)


## 📝 Problem Description

You are given a string `s` consisting of the characters `'N'`, `'S'`, `'E'`, and `'W'`, where `s[i]` indicates movements in an infinite grid:

	- `'N'` : Move north by 1 unit.

	- `'S'` : Move south by 1 unit.

	- `'E'` : Move east by 1 unit.

	- `'W'` : Move west by 1 unit.

Initially, you are at the origin `(0, 0)`. You can change **at most** `k` characters to any of the four directions.

Find the **maximum** **Manhattan distance** from the origin that can be achieved **at any time** while performing the movements **in order**.

The **Manhattan Distance** between two cells `(x_i, y_i)` and `(x_j, y_j)` is `|x_i - x_j| + |y_i - y_j|`.
 

Example 1:**

**Input:** s = "NWSE", k = 1

**Output:** 3

**Explanation:**

Change `s[2]` from `'S'` to `'N'`. The string `s` becomes `"NWNE"`.

	
		
			Movement
			Position (x, y)
			Manhattan Distance
			Maximum
		
	
	
		
			s[0] == 'N'
			(0, 1)
			0 + 1 = 1
			1
		
		
			s[1] == 'W'
			(-1, 1)
			1 + 1 = 2
			2
		
		
			s[2] == 'N'
			(-1, 2)
			1 + 2 = 3
			3
		
		
			s[3] == 'E'
			(0, 2)
			0 + 2 = 2
			3
		
	

The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

Example 2:**

**Input:** s = "NSWWEW", k = 3

**Output:** 6

**Explanation:**

Change `s[1]` from `'S'` to `'N'`, and `s[4]` from `'E'` to `'W'`. The string `s` becomes `"NNWWWW"`.

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `0 <= k <= s.length`

	- `s` consists of only `'N'`, `'S'`, `'E'`, and `'W'`.

## 🧠 Solution Explanation

**Intuition**
This solution works by maintaining a running count of the number of 'N's and 'S's, as well as the number of 'E's and 'W's, in the string. It then calculates the Manhattan distance between the current position and the origin, and updates the maximum distance if the current position is further away. The key insight is that we only need to consider the minimum of the current position and the maximum distance we can reach by changing at most k characters.

**Approach**
1. Initialize a dictionary `h1` to count the number of 'N's, 'S's, 'E's, and 'W's in the string.
2. Initialize a variable `maxi` to store the maximum Manhattan distance.
3. Iterate over the string, updating the counts in `h1` and calculating the Manhattan distance `diff`.
4. Calculate the minimum of `diff + 2k` and the current position `i + 1`, which represents the maximum distance we can reach by changing at most k characters.
5. Update `maxi` with the maximum of the current `maxi` and the minimum calculated in step 4.
6. Return `maxi` as the maximum Manhattan distance.

**Time Complexity**
O(n), where n is the length of the string. This is because we are iterating over the string once.

**Space Complexity**
O(1), since we are using a constant amount of space to store the counts and the maximum distance.

**Key Insight**
The key insight is that we only need to consider the minimum of the current position and the maximum distance we can reach by changing at most k characters. This is because we can always change at most k characters to move further away from the origin, so we only need to consider the minimum of the current position and the maximum distance we can reach by changing at most k characters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1973 ms (Beats 31.58%) |
| 💾 Memory | 18.2 MB (Beats 100%) |
| 📅 Solved | 2025-06-21 |
| 💻 Language | Python |