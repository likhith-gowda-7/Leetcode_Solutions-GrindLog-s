# 2091. Removing Minimum and Maximum From Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/)


## 📝 Problem Description

You are given a **0-indexed** array of **distinct** integers `nums`.

There is an element in `nums` that has the **lowest** value and an element that has the **highest** value. We call them the **minimum** and **maximum** respectively. Your goal is to remove **both** these elements from the array.

A **deletion** is defined as either removing an element from the **front** of the array or removing an element from the **back** of the array.

Return *the **minimum** number of deletions it would take to remove **both** the minimum and maximum element from the array.*

 

Example 1:**

```

**Input:** nums = [2,**10**,7,5,4,**1**,8,6]
**Output:** 5
**Explanation:** 
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.

```

Example 2:**

```

**Input:** nums = [0,**-4**,**19**,1,8,-2,-3,5]
**Output:** 3
**Explanation:** 
The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.

```

Example 3:**

```

**Input:** nums = [**101**]
**Output:** 1
**Explanation:**  
There is only one element in the array, which makes it both the minimum and maximum element.
We can remove it with 1 deletion.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^5 <= nums[i] <= 10^5`

	- The integers in `nums` are **distinct**.

## 🧠 Solution Explanation

**Intuition**  
The only way to delete an element is from an end, so the cost of removing the min and max depends solely on how far they lie from the two ends.  
We only need to consider three natural strategies: take both from the left, take both from the right, or take the leftmost one from the left and the rightmost one from the right.

**Approach**  
1. Find indices `min_idx` and `max_idx` of the smallest and largest values.  
2. Let `L = min(min_idx, max_idx)` and `R = max(min_idx, max_idx)` (so `L` is the leftmost of the two).  
3. Compute three deletion counts:  
   * `remove_from_left = R + 1` – delete everything up to and including the rightmost special element.  
   * `remove_from_right = n - L` – delete everything from the leftmost special element to the end.  
   * `remove_both_ends = (L + 1) + (n - R)` – delete left side up to `L` and right side from `R`.  
4. Return the minimum of these three values.

**Time Complexity**  
Finding min/max indices takes `O(n)` time; the rest is constant work.  
Total: **O(n)**.

**Space Complexity**  
Only a few integer variables are used.  
Total: **O(1)**.

**Key Insight**  
Because deletions can only happen at the ends, the optimal strategy is always one of the three simple patterns above—no intermediate deletions can reduce the count further. This reduces the problem to a few arithmetic comparisons.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 20 ms (Beats 55.57%) |
| 💾 Memory | 33.5 MB (Beats 66.45%) |
| 📅 Solved | 2026-08-30 |
| 💻 Language | Python |