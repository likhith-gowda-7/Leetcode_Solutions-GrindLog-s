> 📌 **Cross-listed:** Primary location is [Array/3483-Unique-3-Digit-Even-Numbers](../../Array/3483-Unique-3-Digit-Even-Numbers). This problem also appears under: **Array**, **Hash Table**, **Recursion**, **Enumeration**

# 3483. Unique 3-Digit Even Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers/)


## 📝 Problem Description

You are given an array of digits called `digits`. Your task is to determine the number of **distinct** three-digit even numbers that can be formed using these digits.

**Note**: Each *copy* of a digit can only be used **once per number**, and there may **not** be leading zeros.

 

Example 1:**

**Input:** digits = [1,2,3,4]

**Output:** 12

**Explanation:** The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

Example 2:**

**Input:** digits = [0,2,2]

**Output:** 2

**Explanation:** The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

Example 3:**

**Input:** digits = [6,6,6]

**Output:** 1

**Explanation:** Only 666 can be formed.

Example 4:**

**Input:** digits = [1,3,5]

**Output:** 0

**Explanation:** No even 3-digit numbers can be formed.

 

**Constraints:**

	- `3 <= digits.length <= 10`

	- `0 <= digits[i] <= 9`

## 🧠 Solution Explanation

**Intuition**  
Instead of generating permutations of the given digits, we enumerate every possible 3‑digit even number (100–998).  
For each candidate we only need to verify that the digit multiset of the candidate is a subset of the available digits. This turns the problem into a simple lookup.

**Approach**  
1. Count how many times each digit appears in `digits` with a `Counter`.  
2. For every even number `n` from 100 to 998 (step 2):  
   * Split `n` into its hundreds (`i`), tens (`j`), and units (`k`) using `divmod`.  
   * Check that the counter has enough copies:  
     - `f[i] > 0` (hundreds digit must exist)  
     - `f[j] > (i == j)` (tens digit must exist, subtract one if it equals the hundreds digit)  
     - `f[k] > (i == k) + (j == k)` (units digit must exist, subtract one for each equality with the other two digits).  
   * If all three conditions hold, increment the result.  
3. Return the final count.

**Time Complexity**  
We iterate over 450 even numbers (100–998). Each check is O(1).  
**O(450) = O(1)** (constant time relative to input size).

**Space Complexity**  
The counter stores at most 10 entries (digits 0–9).  
**O(1)** additional space.

**Key Insight**  
By brute‑forcing all 3‑digit even numbers and using the digit counts to validate each candidate, we avoid complex recursion or permutation logic. The equality checks `(i==j)`, `(i==k)`, `(j==k)` elegantly handle repeated digits.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 79 ms (Beats 19.78%) |
| 💾 Memory | 19.5 MB (Beats 13.85%) |
| 📅 Solved | 2026-09-11 |
| 💻 Language | Python |