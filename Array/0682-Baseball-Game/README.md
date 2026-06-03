# 682. Baseball Game


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/baseball-game/)


## 📝 Problem Description

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings `operations`, where `operations[i]` is the `i^th` operation you must apply to the record and is one of the following:

	- An integer `x`.

	
		- Record a new score of `x`.

	
	

	- `'+'`.
	
		- Record a new score that is the sum of the previous two scores.

	
	

	- `'D'`.
	
		- Record a new score that is the double of the previous score.

	
	

	- `'C'`.
	
		- Invalidate the previous score, removing it from the record.

	
	

Return *the sum of all the scores on the record after applying all the operations*.

The test cases are generated such that the answer and all intermediate calculations fit in a **32-bit** integer and that all operations are valid.

 

Example 1:**

```

**Input:** ops = ["5","2","C","D","+"]
**Output:** 30
**Explanation:**
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

```

Example 2:**

```

**Input:** ops = ["5","-2","4","C","D","9","+","+"]
**Output:** 27
**Explanation:**
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

```

Example 3:**

```

**Input:** ops = ["1","C"]
**Output:** 0
**Explanation:**
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.

```

 

**Constraints:**

	- `1 <= operations.length <= 1000`

	- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range `[-3 * 10^4, 3 * 10^4]`.

	- For operation `"+"`, there will always be at least two previous scores on the record.

	- For operations `"C"` and `"D"`, there will always be at least one previous score on the record.

## 🧠 Solution Explanation

**Intuition**
This solution works by simulating the baseball game operations on a stack data structure, where each score is a stack element. The key insight is to use the stack's append and pop operations to efficiently manage the scores, taking advantage of the problem's constraints to avoid unnecessary computations.

**Approach**
1. Initialize an empty list `res` to store the scores.
2. Iterate over each operation `op` in the `operations` list.
3. If `op` is "+", append the sum of the last two scores to `res`.
4. If `op` is "D", append twice the last score to `res`.
5. If `op` is "C", remove the last score from `res` (if it exists).
6. If `op` is an integer, append it to `res` as a score.
7. After iterating over all operations, return the sum of all scores in `res`.

**Time Complexity**
O(n), where n is the number of operations. This is because we iterate over the operations list once, performing a constant-time operation for each element.

**Space Complexity**
O(n), where n is the number of operations. This is because in the worst case, we store all operations as scores in the `res` list.

**Key Insight**
The key insight is to use the stack's append and pop operations to efficiently manage the scores, taking advantage of the problem's constraints to avoid unnecessary computations. This approach allows us to simulate the baseball game operations in a straightforward and efficient manner.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-01-23 |
| 💻 Language | Python |