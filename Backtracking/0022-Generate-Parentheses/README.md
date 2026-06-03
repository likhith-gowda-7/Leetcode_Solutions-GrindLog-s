> 📌 **Cross-listed:** Primary location is [String/0022-Generate-Parentheses](../../String/0022-Generate-Parentheses). This problem also appears under: **String**, **Dynamic Programming**, **Backtracking**

# 22. Generate Parentheses


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/generate-parentheses/)


## 📝 Problem Description

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

 

Example 1:**

```
**Input:** n = 3
**Output:** ["((()))","(()())","(())()","()(())","()()()"]

```
Example 2:**

```
**Input:** n = 1
**Output:** ["()"]

```

 

**Constraints:**

	- `1 <= n <= 8`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using a backtracking approach, where we recursively add opening and closing parentheses to the current combination, ensuring that the number of opening parentheses does not exceed the number of closing parentheses at any point.

**Approach**
1. Initialize an empty list `res` to store the final result and an empty list `sol` to store the current combination.
2. Define a recursive function `backtrack(op, cl)` that takes the number of opening and closing parentheses as arguments.
3. If the number of opening and closing parentheses are both equal to `n`, it means we have a valid combination, so append it to the result list `res`.
4. If the number of opening parentheses is less than `n`, add an opening parenthesis to the current combination `sol` and recursively call `backtrack(op+1, cl)`.
5. If the number of opening parentheses is greater than the number of closing parentheses, add a closing parenthesis to the current combination `sol` and recursively call `backtrack(op, cl+1)`.
6. After each recursive call, remove the last added parenthesis from the current combination `sol` to backtrack.
7. Call the `backtrack(0, 0)` function to start the backtracking process.

**Time Complexity**
O(4^n / n^(3/2)) due to the Catalan number sequence, which represents the number of valid combinations.

**Space Complexity**
O(n) for the recursive call stack and the current combination `sol`.

**Key Insight**
The key to this solution is the use of backtracking to explore all possible combinations of parentheses, ensuring that the number of opening parentheses does not exceed the number of closing parentheses at any point. This approach allows us to efficiently generate all valid combinations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 35.1%) |
| 📅 Solved | 2026-05-16 |
| 💻 Language | Python |