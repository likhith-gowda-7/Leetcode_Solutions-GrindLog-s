> 📌 **Cross-listed:** Primary location is [Array/3354-Make-Array-Elements-Equal-to-Zero](../../Array/3354-Make-Array-Elements-Equal-to-Zero). This problem also appears under: **Array**, **Simulation**, **Prefix Sum**

# 3354. Make Array Elements Equal to Zero


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/make-array-elements-equal-to-zero/)


## 📝 Problem Description

You are given an integer array `nums`.

Start by selecting a starting position `curr` such that `nums[curr] == 0`, and choose a movement **direction** of either left or right.

After that, you repeat the following process:

	- If `curr` is out of the range `[0, n - 1]`, this process ends.

	- If `nums[curr] == 0`, move in the current direction by **incrementing** `curr` if you are moving right, or **decrementing** `curr` if you are moving left.

	- Else if `nums[curr] > 0`:
	
		- Decrement `nums[curr]` by 1.

		- **Reverse** your movement direction (left becomes right and vice versa).

		- Take a step in your new direction.

	
	

A selection of the initial position `curr` and movement direction is considered **valid** if every element in `nums` becomes 0 by the end of the process.

Return the number of possible **valid** selections.

 

Example 1:**

**Input:** nums = [1,0,2,0,3]

**Output:** 2

**Explanation:**

The only possible valid selections are the following:

	- Choose `curr = 3`, and a movement direction to the left.

	
		- `[1,0,2,**0**,3] -> [1,0,**2**,0,3] -> [1,0,1,**0**,3] -> [1,0,1,0,**3**] -> [1,0,1,**0**,2] -> [1,0,**1**,0,2] -> [1,0,0,**0**,2] -> [1,0,0,0,**2**] -> [1,0,0,**0**,1] -> [1,0,**0**,0,1] -> [1,**0**,0,0,1] -> [**1**,0,0,0,1] -> [0,**0**,0,0,1] -> [0,0,**0**,0,1] -> [0,0,0,**0**,1] -> [0,0,0,0,**1**] -> [0,0,0,0,0]`.

	
	

	- Choose `curr = 3`, and a movement direction to the right.
	
		- `[1,0,2,**0**,3] -> [1,0,2,0,**3**] -> [1,0,2,**0**,2] -> [1,0,**2**,0,2] -> [1,0,1,**0**,2] -> [1,0,1,0,**2**] -> [1,0,1,**0**,1] -> [1,0,**1**,0,1] -> [1,0,0,**0**,1] -> [1,0,0,0,**1**] -> [1,0,0,**0**,0] -> [1,0,**0**,0,0] -> [1,**0**,0,0,0] -> [**1**,0,0,0,0] -> [0,0,0,0,0].`

	
	

Example 2:**

**Input:** nums = [2,3,4,0,4,1,0]

**Output:** 0

**Explanation:**

There are no possible valid selections.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`

	- There is at least one element `i` where `nums[i] == 0`.

## 🧠 Solution Explanation

**Intuition**
The problem requires us to find the number of valid selections of initial position and movement direction that can make all elements in the array equal to zero. The key insight is to use a simulation approach to explore all possible movements and count the valid ones.

**Approach**
1. Initialize a counter `res` to store the number of valid selections.
2. Define a helper function `process(d, idx)` that simulates the movement process.
3. In the `process` function, create a copy of the input array `nums` and initialize the current index `idx` to the given value.
4. While the current index is within the valid range, check if the current element is zero. If it is, move in the current direction by incrementing `idx`.
5. If the current element is positive, decrement it by 1, reverse the movement direction, and take a step in the new direction.
6. After the simulation, check if all elements in the array are zero. If they are, increment the `res` counter.
7. Iterate over the input array `nums` and call the `process` function for each zero element with both left and right movement directions.

**Time Complexity**
The time complexity of this solution is O(n * m), where n is the length of the input array and m is the maximum number of steps required to make all elements zero. In the worst case, we need to simulate all possible movements for each zero element, resulting in a quadratic time complexity.

**Space Complexity**
The space complexity of this solution is O(n), as we create a copy of the input array `nums` in the `process` function.

**Key Insight**
The key insight is to use a simulation approach to explore all possible movements and count the valid ones. By iterating over the input array and calling the `process` function for each zero element with both left and right movement directions, we can efficiently find the number of valid selections.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3477 ms (Beats 19.18%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-10-28 |
| 💻 Language | Python |