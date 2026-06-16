> 📌 **Cross-listed:** Primary location is [String/3612-Process-String-with-Special-Operations-I](../../String/3612-Process-String-with-Special-Operations-I). This problem also appears under: **String**, **Simulation**

# 3612. Process String with Special Operations I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-i/)


## 📝 Problem Description

You are given a string `s` consisting of lowercase English letters and the special characters: `*`, `#`, and `%`.

Build a new string `result` by processing `s` according to the following rules from left to right:

	- If the letter is a **lowercase** English letter append it to `result`.

	- A `'*'` **removes** the last character from `result`, if it exists.

	- A `'#'` **duplicates** the current `result` and **appends** it to itself.

	- A `'%'` **reverses** the current `result`.

Return the final string `result` after processing all characters in `s`.

 

Example 1:**

**Input:** s = "a#b%*"

**Output:** "ba"

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
		
	

Thus, the final `result` is `"ba"`.

Example 2:**

**Input:** s = "z*#"

**Output:** ""

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
		
	

Thus, the final `result` is `""`.

 

**Constraints:**

	- `1 <= s.length <= 20`

	- `s` consists of only lowercase English letters and special characters `*`, `#`, and `%`.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the input string `s` and applying the special operations to the result string `ans` accordingly. The key insight is to keep track of the current result string and update it based on the operations encountered.

**Approach**
1. Initialize an empty string `ans` to store the result.
2. Iterate through each character `ch` in the input string `s`.
3. If `ch` is a lowercase English letter, append it to `ans`.
4. If `ch` is a special character and `ans` is not empty, apply the corresponding operation:
   - If `ch` is '*', remove the last character from `ans`.
   - If `ch` is '#', duplicate `ans` and append it to itself.
   - If `ch` is '%', reverse `ans`.
5. After processing all characters in `s`, return the final string `ans`.

**Time Complexity**
O(n), where n is the length of the input string `s`. This is because we are iterating through each character in `s` once.

**Space Complexity**
O(n), where n is the length of the input string `s`. This is because in the worst case, we might need to store the entire input string `s` in `ans` after applying the operations.

**Key Insight**
The key insight is to keep track of the current result string `ans` and update it based on the operations encountered. This allows us to efficiently process the input string `s` and apply the special operations in a single pass.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 23.2 MB (Beats 82.24%) |
| 📅 Solved | 2026-06-16 |
| 💻 Language | Python |