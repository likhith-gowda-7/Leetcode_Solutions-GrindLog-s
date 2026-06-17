# 3614. Process String with Special Operations II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-ii/)


## 📝 Problem Description

You are given a string `s` consisting of lowercase English letters and the special characters: `'*'`, `'#'`, and `'%'`.

You are also given an integer `k`.

Build a new string `result` by processing `s` according to the following rules from left to right:

	- If the letter is a **lowercase** English letter append it to `result`.

	- A `'*'` **removes** the last character from `result`, if it exists.

	- A `'#'` **duplicates** the current `result` and **appends** it to itself.

	- A `'%'` **reverses** the current `result`.

Return the `k^th` character of the final string `result`. If `k` is out of the bounds of `result`, return `'.'`.

 

Example 1:**

**Input:** s = "a#b%*", k = 1

**Output:** "a"

**Explanation:**

	
		
			`i`
			`s[i]`
			Operation
			Current `result`
		
	
	
		
			0
			`'a'`
			Append `'a'`
			`"a"`
		
		
			1
			`'#'`
			Duplicate `result`
			`"aa"`
		
		
			2
			`'b'`
			Append `'b'`
			`"aab"`
		
		
			3
			`'%'`
			Reverse `result`
			`"baa"`
		
		
			4
			`'*'`
			Remove the last character
			`"ba"`
		
	

The final `result` is `"ba"`. The character at index `k = 1` is `'a'`.

Example 2:**

**Input:** s = "cd%#*#", k = 3

**Output:** "d"

**Explanation:**

	
		
			`i`
			`s[i]`
			Operation
			Current `result`
		
	
	
		
			0
			`'c'`
			Append `'c'`
			`"c"`
		
		
			1
			`'d'`
			Append `'d'`
			`"cd"`
		
		
			2
			`'%'`
			Reverse `result`
			`"dc"`
		
		
			3
			`'#'`
			Duplicate `result`
			`"dcdc"`
		
		
			4
			`'*'`
			Remove the last character
			`"dcd"`
		
		
			5
			`'#'`
			Duplicate `result`
			`"dcddcd"`
		
	

The final `result` is `"dcddcd"`. The character at index `k = 3` is `'d'`.

Example 3:**

**Input:** s = "z*#", k = 0

**Output:** "."

**Explanation:**

	
		
			`i`
			`s[i]`
			Operation
			Current `result`
		
	
	
		
			0
			`'z'`
			Append `'z'`
			`"z"`
		
		
			1
			`'*'`
			Remove the last character
			`""`
		
		
			2
			`'#'`
			Duplicate the string
			`""`
		
	

The final `result` is `""`. Since index `k = 0` is out of bounds, the output is `'.'`.

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of only lowercase English letters and special characters `'*'`, `'#'`, and `'%'`.

	- `0 <= k <= 10^15`

	- The length of `result` after processing `s` will not exceed `10^15`.

## 🧠 Solution Explanation

**Intuition**
The given solution simulates the process of building the final string `result` by iterating through the input string `s` from left to right and applying the special operations. It keeps track of the length of the current `result` and uses this information to determine the kth character.

**Approach**
1. Initialize a variable `Length` to keep track of the length of the current `result`.
2. Iterate through the input string `s` from left to right:
   - If the character is a lowercase English letter, increment `Length`.
   - If the character is `'#'`, multiply `Length` by 2.
   - If the character is `'*'` and `Length` is greater than 0, decrement `Length`.
3. If `k` is greater than or equal to `Length`, return `'.'`.
4. Iterate through the input string `s` from right to left:
   - If the character is `'#'`, divide `Length` by 2 and subtract the new `Length` from `k` if `k` is greater than or equal to `Length`.
   - If the character is `'*'`, increment `Length`.
   - If the character is `'%'`, calculate the new `k` as `(Length - k) - 1`.
   - If the character is a lowercase English letter, decrement `Length`.
   - If `Length` equals `k`, return the current character.

**Time Complexity**
O(n), where n is the length of the input string `s`. This is because we iterate through the input string twice: once from left to right and once from right to left.

**Space Complexity**
O(1), as we only use a constant amount of space to store the variables `Length` and `k`.

**Key Insight**
The key insight is to keep track of the length of the current `result` and use this information to determine the kth character. This approach allows us to simulate the process of building the final string `result` efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 320 ms (Beats 91.67%) |
| 💾 Memory | 20.6 MB (Beats 95.83%) |
| 📅 Solved | 2026-06-17 |
| 💻 Language | Python |