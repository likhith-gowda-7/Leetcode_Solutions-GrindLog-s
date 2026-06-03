> 📌 **Cross-listed:** Primary location is [String/1404-Number-of-Steps-to-Reduce-a-Number-in-Binary-Representation-to-One](../../String/1404-Number-of-Steps-to-Reduce-a-Number-in-Binary-Representation-to-One). This problem also appears under: **String**, **Bit Manipulation**, **Simulation**

# 1404. Number of Steps to Reduce a Number in Binary Representation to One


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)


## 📝 Problem Description

Given the binary representation of an integer as a string `s`, return *the number of steps to reduce it to *`1`* under the following rules*:

	- 
	If the current number is even, you have to divide it by `2`.

	

	- 
	If the current number is odd, you have to add `1` to it.

	

It is guaranteed that you can always reach one for all test cases.

 

Example 1:**

```

**Input:** s = "1101"
**Output:** 6
**Explanation:** "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

```

Example 2:**

```

**Input:** s = "10"
**Output:** 1
**Explanation:** "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

```

Example 3:**

```

**Input:** s = "1"
**Output:** 0

```

 

**Constraints:**

	- `1 <= s.length <= 500`

	- `s` consists of characters '0' or '1'

	- `s[0] == '1'`

## 🧠 Solution Explanation

**Intuition**
The solution works by simulating the process of reducing the binary number to 1 by iteratively applying the given rules. It keeps track of the number of steps taken and the carry value, which represents the result of the previous operation.

**Approach**
1. Initialize variables `steps` to count the number of steps and `carry` to store the carry value.
2. Iterate over the binary string from right to left (from least significant bit to most significant bit).
3. For each bit, check if the current bit and the carry value are different. If they are different, it means the current number is odd, so add 1 to the carry value and increment the steps by 2.
4. If the current bit and the carry value are the same, it means the current number is even, so increment the steps by 1.
5. After iterating over all bits, add the final carry value to the steps.

**Time Complexity**
O(n), where n is the length of the binary string. This is because we are iterating over the string once.

**Space Complexity**
O(1), since we are using a constant amount of space to store the steps and carry values.

**Key Insight**
The key insight is that when the current number is odd, we need to add 1 to it, which effectively increments the steps by 2 (1 for the addition and 1 for the next operation). This is why we increment the steps by 2 when the current bit and the carry value are different.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.1 MB (Beats 87.96%) |
| 📅 Solved | 2026-02-26 |
| 💻 Language | Python |