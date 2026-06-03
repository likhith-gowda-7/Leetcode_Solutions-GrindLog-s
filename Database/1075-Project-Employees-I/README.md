# 1075. Project Employees I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/project-employees-i/)


## 📝 Problem Description

Table: `Project`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to `Employee` table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.

```

 

Table: `Employee`

```

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.

```

 

Write an SQL query that reports the **average** experience years of all the employees for each project, **rounded to 2 digits**.

Return the result table in **any order**.

The query result format is in the following example.

 

Example 1:**

```

**Input:** 
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
**Output:** 
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
**Explanation:** The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50

```

## 🧠 Solution Explanation

**Intuition**
The solution joins the `Project` and `Employee` tables based on the `employee_id` column, then calculates the average experience years for each project by grouping the results.

**Approach**
1. Join the `Project` and `Employee` tables on the `employee_id` column to create a combined table with project information and employee experience years.
2. Group the combined table by `project_id` to calculate the average experience years for each project.
3. Use the `round` function to round the average experience years to two decimal places.

**Time Complexity**
O(n), where n is the number of rows in the combined table. This is because we are performing a single pass through the data to join the tables and calculate the average experience years.

**Space Complexity**
O(n), where n is the number of rows in the combined table. This is because we are creating a new table with the combined data, which requires additional storage space.

**Key Insight**
The key insight here is that we can use a simple join and grouping operation to calculate the average experience years for each project, without needing to use any complex aggregation functions or subqueries. This is a great example of how a well-designed join can simplify complex queries.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 480 ms (Beats 92.34%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-23 |
| 💻 Language | MySQL |