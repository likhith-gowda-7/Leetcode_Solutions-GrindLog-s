# 3870. Count Commas in Range


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-commas-in-range/)


## 📝 Problem Description

You are given an integer `n`.

Return the **total** number of commas used when writing all integers from `[1, n]` (inclusive) in **standard** number formatting.

In **standard** formatting:

	- A comma is inserted after **every three** digits from the right.

	- Numbers with **fewer** than 4 digits contain no commas.

 

Example 1:**

**Input:** n = 1002

**Output:** 3

**Explanation:**

The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

Example 2:**

**Input:** n = 998

**Output:** 0

**Explanation:**

All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

 

**Constraints:**

	- `1 <= n <= 10^5`

## 🧠 Solution Explanation

**Intuition**  
Every integer with at least four digits (i.e., ≥ 1000) contains exactly one comma in standard formatting. Thus the total commas equals the count of numbers from 1000 up to n.

**Approach**  
1. If `n` is less than 1000, no number has a comma → answer is 0.  
2. Otherwise, all numbers from 1000 to `n` inclusive contribute one comma each.  
3. The count of such numbers is `n - 999`.  
4. Return `max(n - 999, 0)` to cover both cases in one expression.

**Time Complexity**  
O(1) – a constant‑time arithmetic operation.

**Space Complexity**  
O(1) – only a few integer variables are used.

**Key Insight**  
The problem reduces to counting how many integers in the range have at least four digits; each of those contributes exactly one comma, so the answer is simply `max(n-999,0)`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 86.58%) |
| 📅 Solved | 2026-09-08 |
| 💻 Language | Python |