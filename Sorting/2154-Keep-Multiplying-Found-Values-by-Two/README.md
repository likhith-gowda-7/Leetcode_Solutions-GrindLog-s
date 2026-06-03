> 📌 **Cross-listed:** Primary location is [Array/2154-Keep-Multiplying-Found-Values-by-Two](../../Array/2154-Keep-Multiplying-Found-Values-by-Two). This problem also appears under: **Array**, **Hash Table**, **Sorting**, **Simulation**

# 2154. Keep Multiplying Found Values by Two


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/keep-multiplying-found-values-by-two/)


## 📝 Problem Description

You are given an array of integers `nums`. You are also given an integer `original` which is the first number that needs to be searched for in `nums`.

You then do the following steps:

	- If `original` is found in `nums`, **multiply** it by two (i.e., set `original = 2 * original`).

	- Otherwise, **stop** the process.

	- **Repeat** this process with the new number as long as you keep finding the number.

Return *the **final** value of *`original`.

 

Example 1:**

```

**Input:** nums = [5,3,6,1,12], original = 3
**Output:** 24
**Explanation:** 
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.

```

Example 2:**

```

**Input:** nums = [2,7,9], original = 4
**Output:** 4
**Explanation:**
- 4 is not found in nums. Thus, 4 is returned.

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i], original <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses a set to store the unique numbers in the input array `nums` for efficient lookup. It then enters a loop where it continuously multiplies the `original` number by 2 as long as it is found in the set. Once the `original` number is no longer found in the set, the loop breaks, and the final value is returned.

**Approach**
1. Convert the input array `nums` to a set `arr` for fast lookup.
2. Enter a loop that continues indefinitely.
3. Inside the loop, check if the current `original` number is in the set `arr`.
4. If `original` is not in the set, break the loop.
5. If `original` is in the set, multiply it by 2 and continue to the next iteration.
6. Once the loop breaks, return the final value of `original`.

**Time Complexity**
O(n) where n is the number of unique elements in the input array `nums`. This is because the set creation operation takes O(n) time, and the subsequent loop iterates at most n times.

**Space Complexity**
O(n) where n is the number of unique elements in the input array `nums`. This is because the set stores at most n unique elements.

**Key Insight**
The key insight is to use a set for efficient lookup, allowing the solution to quickly determine whether the `original` number is present in the array. This enables the solution to iterate efficiently until the final value is found.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-11-19 |
| 💻 Language | Python |