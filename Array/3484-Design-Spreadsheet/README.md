# 3484. Design Spreadsheet


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/design-spreadsheet/)


## 📝 Problem Description

A spreadsheet is a grid with 26 columns (labeled from `'A'` to `'Z'`) and a given number of `rows`. Each cell in the spreadsheet can hold an integer value between 0 and 10^5.

Implement the `Spreadsheet` class:

	- `Spreadsheet(int rows)` Initializes a spreadsheet with 26 columns (labeled `'A'` to `'Z'`) and the specified number of rows. All cells are initially set to 0.

	- `void setCell(String cell, int value)` Sets the value of the specified `cell`. The cell reference is provided in the format `"AX"` (e.g., `"A1"`, `"B10"`), where the letter represents the column (from `'A'` to `'Z'`) and the number represents a **1-indexed** row.

	- `void resetCell(String cell)` Resets the specified cell to 0.

	- `int getValue(String formula)` Evaluates a formula of the form `"=X+Y"`, where `X` and `Y` are **either** cell references or non-negative integers, and returns the computed sum.

**Note:** If `getValue` references a cell that has not been explicitly set using `setCell`, its value is considered 0.

 

Example 1:**

**Input:**

["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]

[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

**Output:**

[null, 12, null, 16, null, 25, null, 15] 

**Explanation**

Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns
spreadsheet.getValue("=5+7"); // returns 12 (5+7)
spreadsheet.setCell("A1", 10); // sets A1 to 10
spreadsheet.getValue("=A1+6"); // returns 16 (10+6)
spreadsheet.setCell("B2", 15); // sets B2 to 15
spreadsheet.getValue("=A1+B2"); // returns 25 (10+15)
spreadsheet.resetCell("A1"); // resets A1 to 0
spreadsheet.getValue("=A1+B2"); // returns 15 (0+15)

 

**Constraints:**

	- `1 <= rows <= 10^3`

	- `0 <= value <= 10^5`

	- The formula is always in the format `"=X+Y"`, where `X` and `Y` are either valid cell references or **non-negative** integers with values less than or equal to `10^5`.

	- Each cell reference consists of a capital letter from `'A'` to `'Z'` followed by a row number between `1` and `rows`.

	- At most `10^4` calls will be made in **total** to `setCell`, `resetCell`, and `getValue`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table (dictionary in Python) to store the spreadsheet data, where each key is a cell reference and the value is the cell's integer value. The `getValue` method parses the formula, extracts the cell references, and evaluates the expression using the stored values.

**Approach**
1. Initialize the spreadsheet with a hash table and a set of column letters.
2. In the `setCell` method, store the cell value in the hash table.
3. In the `resetCell` method, reset the cell value to 0 in the hash table.
4. In the `getValue` method:
   1. Remove the leading "=" from the formula.
   2. Find the "+" operator in the formula.
   3. Extract the two cell references on either side of the "+" operator.
   4. If a cell reference is a letter (column), retrieve the stored value from the hash table.
   5. Evaluate the expression by adding the two values and return the result.

**Time Complexity**
The time complexity is O(n), where n is the length of the formula. This is because we iterate through the formula to find the "+" operator and extract the cell references.

**Space Complexity**
The space complexity is O(m), where m is the number of cells in the spreadsheet. This is because we store the cell values in a hash table.

**Key Insight**
The key insight is to use a hash table to store the cell values, allowing for efficient lookup and update of cell values. This enables the `getValue` method to quickly retrieve the values of the cell references in the formula and evaluate the expression.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 78 ms (Beats 79.15%) |
| 💾 Memory | 23.5 MB (Beats 100%) |
| 📅 Solved | 2025-09-19 |
| 💻 Language | Python |