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

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 267 ms (Beats 71.85%) |
| 💾 Memory | 66.9 MB (Beats 11.25%) |
| 📅 Solved | 2025-06-10 |
| 💻 Language | pythondata |