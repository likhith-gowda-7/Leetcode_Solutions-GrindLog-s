# 17. Letter Combinations of a Phone Number


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)


## 📝 Problem Description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)
 

Example 1:**

```

**Input:** digits = "23"
**Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

```

Example 2:**

```

**Input:** digits = "2"
**Output:** ["a","b","c"]

```

 

**Constraints:**

	- `1 <= digits.length <= 4`

	- `digits[i]` is a digit in the range `['2', '9']`.

## 🧠 Solution Explanation

**Intuition**
The problem requires generating all possible letter combinations for a given phone number. The key insight is to use a backtracking approach to explore all possible combinations. We can break down the problem into smaller sub-problems by considering each digit of the input number and generating all possible letters for that digit.

**Approach**
1. Create a dictionary `num_letters` to map each digit to its corresponding letters.
2. Initialize an empty list `res` to store the result.
3. Define a recursive function `backtrack` to explore all possible combinations.
4. In the `backtrack` function:
   1. If the current solution `sol` has reached the length of the input number `n`, add it to the result list `res`.
   2. For each letter `ch` corresponding to the current digit `digits[curr_idx]`, add it to the solution `sol` and recursively call `backtrack` with the next index `curr_idx+1`.
   3. After the recursive call, remove the last added letter from the solution `sol` to backtrack and explore other possibilities.
5. Call the `backtrack` function with the initial index `0` and an empty solution `[]`.

**Time Complexity**
The time complexity of this solution is O(4^n), where n is the length of the input number. This is because each digit can have up to 4 possible letters, and we recursively explore all possible combinations.

**Space Complexity**
The space complexity of this solution is O(4^n), where n is the length of the input number. This is because in the worst case, we need to store all possible combinations in the result list `res`.

**Key Insight**
The key insight is to use a backtracking approach to explore all possible combinations of letters for each digit of the input number. This approach allows us to efficiently generate all possible combinations without generating duplicate solutions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 78%) |
| 📅 Solved | 2026-04-09 |
| 💻 Language | Python |