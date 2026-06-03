# 2239. Find Closest Number to Zero


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-closest-number-to-zero/)


## 📝 Problem Description

Given an integer array `nums` of size `n`, return *the number with the value **closest** to *`0`* in *`nums`. If there are multiple answers, return *the number with the **largest** value*.

 

Example 1:**

```

**Input:** nums = [-4,-2,1,4,8]
**Output:** 1
**Explanation:**
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

```

Example 2:**

```

**Input:** nums = [2,-1,1]
**Output:** 1
**Explanation:** 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

```

 

**Constraints:**

	- `1 <= n <= 1000`

	- `-10^5 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution iterates through the input array, keeping track of the number with the smallest absolute difference to zero. If there are multiple numbers with the same smallest absolute difference, it keeps track of the largest one.

**Approach**
1. Initialize a list `mini` with two elements: the smallest absolute difference found so far (`mini[0]`) and the corresponding number (`mini[1]`).
2. Iterate through the input array `nums`.
3. For each number, calculate its absolute difference to zero (`diff`).
4. If `diff` is less than or equal to `mini[0]`, update `mini` accordingly:
   - If `diff` is equal to `mini[0]`, update `mini[1]` to be the maximum of its current value and the current number.
   - Otherwise, update `mini` to be `[diff, current number]`.
5. After iterating through the entire array, return `mini[1]`, which is the number with the smallest absolute difference to zero (or the largest one if there are multiple).

**Time Complexity**
O(n), where n is the length of the input array. This is because we iterate through the array once.

**Space Complexity**
O(1), excluding the input array. We use a constant amount of space to store the `mini` list, regardless of the input size.

**Key Insight**
The key insight is to use a single pass through the array to find the number with the smallest absolute difference to zero, and to keep track of the largest number in case of a tie. This approach avoids the need for sorting or using additional data structures, making it efficient and simple.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 44.71%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-07-05 |
| 💻 Language | Python |