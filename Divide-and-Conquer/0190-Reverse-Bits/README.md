# 190. Reverse Bits


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-bits/)


## 📝 Problem Description

Reverse bits of a given 32 bits signed integer.

 

Example 1:**

**Input:** n = 43261596

**Output:** 964176192

**Explanation:**

	
		
			Integer
			Binary
		
		
			43261596
			00000010100101000001111010011100
		
		
			964176192
			00111001011110000010100101000000
		
	

Example 2:**

**Input:** n = 2147483644

**Output:** 1073741822

**Explanation:**

	
		
			Integer
			Binary
		
		
			2147483644
			01111111111111111111111111111100
		
		
			1073741822
			00111111111111111111111111111110
		
	

 

**Constraints:**

	- `0 <= n <= 2^31 - 2`

	- `n` is even.

 

**Follow up:** If this function is called many times, how would you optimize it?

## 🧠 Solution Explanation

**Intuition**
The problem requires reversing the bits of a 32-bit signed integer. This can be achieved by first converting the integer to a binary string, reversing the string, and then converting it back to an integer. However, since the input integer is not guaranteed to have 32 bits, we need to pad the binary string with zeros to ensure it's always 32 bits long.

**Approach**
1. Convert the input integer `n` to a binary string using the `bin` function, removing the '0b' prefix.
2. Reverse the binary string using slicing (`[::-1]`).
3. Calculate the length of the reversed binary string.
4. Pad the binary string with zeros to ensure it's 32 bits long by iterating `32 - len(binary)` times and appending '0' to the string.
5. Convert the padded binary string back to an integer using the `int` function with base 2.

**Time Complexity**
O(1) - The time complexity is constant because we're performing a fixed number of operations regardless of the input size.

**Space Complexity**
O(1) - The space complexity is constant because we're only using a fixed amount of space to store the binary string and the padded string.

**Key Insight**
The key insight here is that we can simply reverse the binary string representation of the input integer to achieve the desired result. This approach works because the binary representation of an integer is a straightforward way to represent its bit-level structure, and reversing this representation is a simple and efficient way to reverse the bits.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 74.9%) |
| 💾 Memory | 19.3 MB (Beats 9.74%) |
| 📅 Solved | 2026-02-16 |
| 💻 Language | Python |