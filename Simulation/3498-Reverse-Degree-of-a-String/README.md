> 📌 **Cross-listed:** Primary location is [String/3498-Reverse-Degree-of-a-String](../../String/3498-Reverse-Degree-of-a-String). This problem also appears under: **String**, **Simulation**

# 3498. Reverse Degree of a String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-degree-of-a-string/)


## 📝 Problem Description

Given a string `s`, calculate its **reverse degree**.

The **reverse degree** is calculated as follows:

	- For each character, multiply its position in the *reversed* alphabet (`'a'` = 26, `'b'` = 25, ..., `'z'` = 1) with its position in the string **(1-indexed)**.

	- Sum these products for all characters in the string.

Return the **reverse degree** of `s`.

 

Example 1:**

**Input:** s = "abc"

**Output:** 148

**Explanation:**

	
		
			Letter
			Index in Reversed Alphabet
			Index in String
			Product
		
		
			`'a'`
			26
			1
			26
		
		
			`'b'`
			25
			2
			50
		
		
			`'c'`
			24
			3
			72
		
	

The reversed degree is `26 + 50 + 72 = 148`.

Example 2:**

**Input:** s = "zaza"

**Output:** 160

**Explanation:**

	
		
			Letter
			Index in Reversed Alphabet
			Index in String
			Product
		
		
			`'z'`
			1
			1
			1
		
		
			`'a'`
			26
			2
			52
		
		
			`'z'`
			1
			3
			3
		
		
			`'a'`
			26
			4
			104
		
	

The reverse degree is `1 + 52 + 3 + 104 = 160`.

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` contains only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**  
The reverse alphabet value of a letter can be obtained by a simple arithmetic trick:  
`'a'` (ASCII 97) should map to 26, `'b'` to 25, …, `'z'` (ASCII 122) to 1.  
Subtracting the ASCII code from 123 gives exactly that mapping, so we can compute each term in O(1).

**Approach**  
1. Initialize `res = 0`.  
2. For each character `c` at 1‑indexed position `i` in the string:  
   * Compute its reverse value: `rev = 123 - ord(c)`.  
   * Add `rev * i` to `res`.  
3. Return `res`.

**Time Complexity**  
The loop visits each of the `n` characters once, performing O(1) work per iteration.  
**O(n)**.

**Space Complexity**  
Only a few integer variables are used; no extra data structures grow with input size.  
**O(1)**.

**Key Insight**  
`123 - ord(c)` is a constant‑time formula that converts a letter to its reverse alphabet index, turning the problem into a single linear scan that sums weighted positions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 98.06%) |
| 💾 Memory | 19.2 MB (Beats 89.2%) |
| 📅 Solved | 2026-09-22 |
| 💻 Language | Python |