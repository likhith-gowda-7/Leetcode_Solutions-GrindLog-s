# 799. Champagne Tower


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/champagne-tower/)


## 📝 Problem Description

We stack glasses in a pyramid, where the **first** row has `1` glass, the **second** row has `2` glasses, and so on until the 100^th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png)

Now after pouring some non-negative integer cups of champagne, return how full the `j^th` glass in the `i^th` row is (both `i` and `j` are 0-indexed.)

 

Example 1:**

```

**Input:** poured = 1, query_row = 1, query_glass = 1
**Output:** 0.00000
**Explanation:** We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

```

Example 2:**

```

**Input:** poured = 2, query_row = 1, query_glass = 1
**Output:** 0.50000
**Explanation:** We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

```

Example 3:**

```

**Input:** poured = 100000009, query_row = 33, query_glass = 17
**Output:** 1.00000

```

 

**Constraints:**

	- `0 <= poured <= 10^9`

	- `0 <= query_glass <= query_row < 100`

## 🧠 Solution Explanation

**Intuition**
This solution uses dynamic programming to simulate the champagne tower's behavior. It starts with a full top glass and iteratively calculates the amount of champagne that flows to the glasses below, ensuring that each glass remains at or below the maximum capacity of 1 cup.

**Approach**
1. Initialize a 2D array `tower` with 102 rows and 102 columns, representing the glasses in the pyramid. The first glass at the top is filled with `poured` cups of champagne.
2. Iterate through each row `r` from 0 to `query_row`, and for each column `c` in row `r`, check if the champagne level exceeds 1 cup.
3. If the champagne level is above 1 cup, calculate the excess champagne by subtracting 1 cup from the current level and dividing the result by 2 (since the excess flows equally to the left and right glasses).
4. Update the current glass's level to 1 cup and distribute the excess champagne equally to the glasses below, at positions `(r+1, c)` and `(r+1, c+1)`.
5. After iterating through all rows, return the champagne level in the specified glass at row `query_row` and column `query_glass`.

**Time Complexity**
O(query_row^2), as the solution iterates through each row and column in the pyramid.

**Space Complexity**
O(query_row^2), as the solution uses a 2D array to store the champagne levels in each glass.

**Key Insight**
The key to this solution is recognizing that the champagne tower's behavior can be simulated by iteratively distributing the excess champagne to the glasses below, ensuring that each glass remains at or below the maximum capacity of 1 cup. This insight allows us to use dynamic programming to efficiently calculate the champagne level in any glass at any row and column.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 79 ms (Beats 73.57%) |
| 💾 Memory | 19.4 MB (Beats 40.94%) |
| 📅 Solved | 2026-02-14 |
| 💻 Language | Python |