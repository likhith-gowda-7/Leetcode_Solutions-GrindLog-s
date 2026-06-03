> 📌 **Cross-listed:** Primary location is [Array/0679-24-Game](../../Array/0679-24-Game). This problem also appears under: **Array**, **Math**, **Backtracking**

# 679. 24 Game


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/24-game/)


## 📝 Problem Description

You are given an integer array `cards` of length `4`. You have four cards, each containing a number in the range `[1, 9]`. You should arrange the numbers on these cards in a mathematical expression using the operators `['+', '-', '*', '/']` and the parentheses `'('` and `')'` to get the value 24.

You are restricted with the following rules:

	- The division operator `'/'` represents real division, not integer division.

	
		- For example, `4 / (1 - 2 / 3) = 4 / (1 / 3) = 12`.

	
	

	- Every operation done is between two numbers. In particular, we cannot use `'-'` as a unary operator.
	
		- For example, if `cards = [1, 1, 1, 1]`, the expression `"-1 - 1 - 1 - 1"` is **not allowed**.

	
	

	- You cannot concatenate numbers together
	
		- For example, if `cards = [1, 2, 1, 2]`, the expression `"12 + 12"` is not valid.

	
	

Return `true` if you can get such expression that evaluates to `24`, and `false` otherwise.

 

Example 1:**

```

**Input:** cards = [4,1,8,7]
**Output:** true
**Explanation:** (8-4) * (7-1) = 24

```

Example 2:**

```

**Input:** cards = [1,2,1,2]
**Output:** false

```

 

**Constraints:**

	- `cards.length == 4`

	- `1 <= cards[i] <= 9`

## 🧠 Solution Explanation

**Intuition**
This solution uses a backtracking approach to generate all possible mathematical expressions using the given cards and operators. It recursively tries all possible combinations of operations between the cards, and checks if any of them evaluate to 24.

**Approach**
1. Define a list of operators (`ops`) that can be used to combine the numbers.
2. Define a recursive function (`dfs`) that takes a list of numbers as input.
3. If the list contains only one number, check if it is equal to 24 (with some tolerance for floating-point errors).
4. Otherwise, iterate over all pairs of numbers in the list, and for each pair:
   a. Create a new list containing the remaining numbers.
   b. For each operator, apply it to the current pair of numbers, and recursively call `dfs` on the new list.
   c. If the recursive call returns `True`, return `True`.
5. If no combination of operations evaluates to 24, return `False`.

**Time Complexity**
O(4^n * n!), where n is the number of cards. This is because there are 4 possible operations for each pair of numbers, and there are n choose 2 possible pairs of numbers.

**Space Complexity**
O(n), for the recursive call stack.

**Key Insight**
The key insight here is that the problem can be solved using a backtracking approach, where we recursively try all possible combinations of operations between the cards. This allows us to explore the entire search space and find a solution if one exists. The use of a recursive function also makes the code concise and easy to understand.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 73 ms (Beats 32.75%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-08-18 |
| 💻 Language | Python |