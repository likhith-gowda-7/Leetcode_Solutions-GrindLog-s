> 📌 **Cross-listed:** Primary location is [Array/0055-Jump-Game](../../Array/0055-Jump-Game). This problem also appears under: **Array**, **Dynamic Programming**, **Greedy**

# 55. Jump Game


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game/)


## 📝 Problem Description

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true`* if you can reach the last index, or *`false`* otherwise*.

 

Example 1:**

```

**Input:** nums = [2,3,1,1,4]
**Output:** true
**Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

Example 2:**

```

**Input:** nums = [3,2,1,0,4]
**Output:** false
**Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `0 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

## Intuition
This approach works by starting from the end of the array and trying to find a path to the beginning. The key idea is to keep track of the "goal" index, which is the index we need to reach in order to be able to jump to the end of the array. By iteratively updating the goal index, we can determine if it's possible to reach the end from the start.

## Approach
1. Initialize the goal index to the last index of the array.
2. Iterate over the array in reverse order, checking if the current index can reach the goal index.
3. If the current index can reach the goal index, update the goal index to the current index.
4. Repeat steps 2-3 until the beginning of the array is reached.
5. If the goal index is 0 at the end of the iteration, it means we can reach the end from the start, so return True. Otherwise, return False.

## Time Complexity
The time complexity is O(n), where n is the length of the input array, because we only need to iterate over the array once in reverse order.

## Space Complexity
The space complexity is O(1), because we only use a constant amount of space to store the goal index and the loop variable, regardless of the size of the input array.

## Key Insight
The key insight behind this solution is to work backwards from the end of the array, keeping track of the "goal" index that we need to reach in order to be able to jump to the end. This allows us to avoid having to consider all possible jump paths and instead focus on finding a single path that works.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 98.37%) |
| 💾 Memory | 18.5 MB (Beats 100%) |
| 📅 Solved | 2025-10-16 |
| 💻 Language | Python |