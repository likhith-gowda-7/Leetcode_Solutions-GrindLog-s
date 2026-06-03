# 2879. Display the First Three Rows


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-pythondata-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/display-the-first-three-rows/)


## 📝 Problem Description

```

DataFrame: `employees`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+

```

Write a solution to display the **first `3` **rows** **of this DataFrame.

 

Example 1:**

```

**Input:
**DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
**Output:**
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
**Explanation:** 
Only the first 3 rows are displayed.
```

## 🧠 Solution Explanation

**Intuition**
The `head()` function in pandas is used to select the first `n` rows of a DataFrame. In this case, we want to display the first 3 rows, so we pass `3` as an argument to `head()`.

**Approach**
1. Import the pandas library to work with DataFrames.
2. Define a function `selectFirstRows()` that takes a DataFrame `employees` as input and returns a new DataFrame.
3. Use the `head()` function to select the first 3 rows of the `employees` DataFrame.
4. Return the resulting DataFrame.

**Time Complexity**
O(1) - The `head()` function operates in constant time, as it simply returns a slice of the existing DataFrame without modifying it.

**Space Complexity**
O(n) - The `head()` function creates a new DataFrame containing the first 3 rows, which requires additional memory proportional to the number of rows in the original DataFrame.

**Key Insight**
The key insight here is that the `head()` function is a convenient and efficient way to select a subset of rows from a DataFrame, making it a useful tool for data analysis and manipulation.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 267 ms (Beats 71.85%) |
| 💾 Memory | 66.9 MB (Beats 11.25%) |
| 📅 Solved | 2025-06-10 |
| 💻 Language | pythondata |