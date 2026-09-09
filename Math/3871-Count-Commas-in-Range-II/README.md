# 3871. Count Commas in Range II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-commas-in-range-ii/)


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

**​​​​​​​**All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

 

**Constraints:**

	- `1 <= n <= 10^15`

## 🧠 Solution Explanation

**Intuition**  
Numbers that share the same number of commas form contiguous ranges:  
1‑999 have 0 commas, 1 000‑9 999 have 1 comma, 10 000‑99 999 have 2 commas, etc.  
Counting commas is therefore just counting how many numbers lie in each of these ranges and multiplying by the comma count for that range.

**Approach**  
1. `lower = 1000` (first number that needs a comma).  
2. `comma = 1` (current comma count).  
3. While `lower ≤ n`:  
   * `upper = min(n, lower*1000 - 1)` – the last number in this comma‑range.  
   * Add `(upper - lower + 1) * comma` to the result.  
   * Increment `comma` and set `lower = upper + 1` to start the next range.  
4. Return the accumulated result.

**Time Complexity**  
The loop runs once per comma group.  
The largest group occurs when `n` has `d` digits, so there are `⌊(d-1)/3⌋` groups.  
Thus `O(log₁₀ n)` time, which is ≤ 15 iterations for `n ≤ 10¹⁵`.

**Space Complexity**  
Only a few integer variables are used: `O(1)` auxiliary space.

**Key Insight**  
By treating each power‑of‑1000 block as a single “comma group,” we avoid iterating over every integer and can compute the total commas in constant work per group.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 13.61%) |
| 📅 Solved | 2026-09-09 |
| 💻 Language | Python |