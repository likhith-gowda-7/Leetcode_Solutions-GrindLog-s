# 3147. Taking Maximum Energy From the Mystic Dungeon


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/)


## 📝 Problem Description

In a mystic dungeon, `n` magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician `i`, you will be instantly transported to magician `(i + k)`. This process will be repeated until you reach the magician where `(i + k)` does not exist.

In other words, you will choose a starting point and then teleport with `k` jumps until you reach the end of the magicians' sequence, **absorbing all the energy** during the journey.

You are given an array `energy` and an integer `k`. Return the **maximum** possible energy you can gain.

**Note** that when you reach a magician, you *must* take energy from them, whether it is negative or positive energy.

 

Example 1:**

**Input:**  energy = [5,2,-10,-5,1], k = 3

**Output:** 3

**Explanation:** We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

Example 2:**

**Input:** energy = [-2,-3,-1], k = 2

**Output:** -1

**Explanation:** We can gain a total energy of -1 by starting from magician 2.

 

**Constraints:**

	- `1 <= energy.length <= 10^5`

	- `-1000 <= energy[i] <= 1000`

	- `1 <= k <= energy.length - 1`

 

​​​​​​

## 🧠 Solution Explanation

**Intuition**
This solution uses dynamic programming to build up a table of maximum energy that can be gained at each position in the array. The key insight is that the maximum energy at a position is the maximum of the energy at that position plus the maximum energy that can be gained at the position `k` steps ahead.

**Approach**
1. Create a copy of the input array `energy` and store it in the `dp` array.
2. Iterate over the `dp` array from the end to the beginning, considering each position `i`.
3. If the position `i + k` is within the bounds of the array, add the maximum energy at position `i + k` to the energy at position `i`.
4. After iterating over the entire array, return the maximum value in the `dp` array.

**Time Complexity**
O(n), where n is the length of the input array. This is because we only need to iterate over the array once, and each iteration takes constant time.

**Space Complexity**
O(n), where n is the length of the input array. This is because we need to create a copy of the input array to store the dynamic programming table.

**Key Insight**
The key insight is that the maximum energy at a position is the maximum of the energy at that position plus the maximum energy that can be gained at the position `k` steps ahead. This allows us to build up a table of maximum energy that can be gained at each position in the array, and then return the maximum value in the table.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1088 ms (Beats 58.76%) |
| 💾 Memory | 31.2 MB (Beats 100%) |
| 📅 Solved | 2025-10-11 |
| 💻 Language | Python |