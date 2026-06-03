> 📌 **Cross-listed:** Primary location is [Array/1266-Minimum-Time-Visiting-All-Points](../../Array/1266-Minimum-Time-Visiting-All-Points). This problem also appears under: **Array**, **Math**, **Geometry**

# 1266. Minimum Time Visiting All Points


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Geometry](https://img.shields.io/badge/Geometry-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-time-visiting-all-points/)


## 📝 Problem Description

On a 2D plane, there are `n` points with integer coordinates `points[i] = [x_i, y_i]`. Return *the **minimum time** in seconds to visit all the points in the order given by *`points`.

You can move according to these rules:

	- In `1` second, you can either:

	
		- move vertically by one unit,

		- move horizontally by one unit, or

		- move diagonally `sqrt(2)` units (in other words, move one unit vertically then one unit horizontally in `1` second).

	
	

	- You have to visit the points in the same order as they appear in the array.

	- You are allowed to pass through points that appear later in the order, but these do not count as visits.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG)
```

**Input:** points = [[1,1],[3,4],[-1,0]]
**Output:** 7
**Explanation: **One optimal path is **[1,1]** -> [2,2] -> [3,3] -> **[3,4] **-> [2,3] -> [1,2] -> [0,1] -> **[-1,0]**   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
```

Example 2:**

```

**Input:** points = [[3,2],[-2,2]]
**Output:** 5

```

 

**Constraints:**

	- `points.length == n`

	- `1 <= n <= 100`

	- `points[i].length == 2`

	- `-1000 <= points[i][0], points[i][1] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution calculates the minimum time to visit all points by finding the maximum horizontal or vertical distance between consecutive points, as moving diagonally is not necessary. This approach works because the problem allows moving diagonally, which means the optimal path will always be a straight line between two points.

**Approach**
1. Initialize a variable `steps` to keep track of the total time taken.
2. Iterate over the list of points, starting from the second point (index 1).
3. For each pair of consecutive points, calculate the absolute difference in x-coordinates (`abs(x1-x2)`) and y-coordinates (`abs(y1-y2)`).
4. Add the maximum of these two differences to `steps`, as this represents the minimum time required to move from one point to the other.
5. Return the total `steps` after iterating over all points.

**Time Complexity**
O(n), where n is the number of points. This is because we are iterating over the list of points once, and the operations inside the loop (calculating absolute differences and updating `steps`) take constant time.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the `steps` variable and the indices of the points.

**Key Insight**
The key insight here is that the optimal path between two points is a straight line, and the minimum time required to move between them is equal to the maximum horizontal or vertical distance between them. This allows us to simplify the problem by only considering the maximum of the two differences, rather than the actual diagonal distance.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 25.55%) |
| 📅 Solved | 2026-01-12 |
| 💻 Language | Python |