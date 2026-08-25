# 3718. Smallest Missing Multiple of K


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return the **smallest positive multiple** of `k` that is **missing** from `nums`.

A **multiple** of `k` is any positive integer divisible by `k`.

 

Example 1:**

**Input:** nums = [8,2,3,4,6], k = 2

**Output:** 10

**Explanation:**

The multiples of `k = 2` are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from `nums` is 10.

Example 2:**

**Input:** nums = [1,4,7,10,15], k = 5

**Output:** 5

**Explanation:**

The multiples of `k = 5` are 5, 10, 15, 20... and the smallest multiple missing from `nums` is 5.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

	- `1 <= k <= 100`

## 🧠 Solution Explanation

**Intuition**  
The answer is the first multiple of `k` that does not appear in the array.  
By storing all numbers in a hash set we can test membership in constant time, so we can simply walk through the multiples of `k` in increasing order until we find a gap.

**Approach**  
1. Convert `nums` to a set `S` for O(1) look‑ups.  
2. Start with `curr = 1` (the first multiplier).  
3. While `curr * k` is in `S`, increment `curr`.  
4. When the loop stops, return `curr * k` – the smallest missing multiple.

**Time Complexity**  
The set construction takes `O(n)` where `n = len(nums)`.  
The loop checks each multiple once; in the worst case we examine all multiples up to the largest present number, at most `max(nums)/k + 1 ≤ 101`.  
Thus overall time is `O(n)`.

**Space Complexity**  
The set stores all `n` numbers: `O(n)` additional space.

**Key Insight**  
The problem reduces to “find the first missing element in an increasing sequence” – by iterating over multiples of `k` and using a hash set, we can locate that missing element in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 53.35%) |
| 📅 Solved | 2026-08-25 |
| 💻 Language | Python |