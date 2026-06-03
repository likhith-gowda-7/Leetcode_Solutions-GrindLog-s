# 570. Managers with at Least 5 Direct Reports


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/)


## 📝 Problem Description

Table: `Employee`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.

```

 

Write a solution to find managers with at least **five direct reports**.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
**Output:** 
+------+
| name |
+------+
| John |
+------+

```

## 🧠 Solution Explanation

**Intuition**
The solution works by joining the `Employee` table with itself on the `managerId` column, effectively creating a table where each row represents a manager and their direct reports. The `GROUP BY` clause then groups these rows by the manager's `id`, and the `HAVING` clause filters the results to only include managers with at least five direct reports.

**Approach**
1. Join the `Employee` table with itself on the `managerId` column, creating a table where each row represents a manager and their direct reports.
2. Group the resulting table by the manager's `id`.
3. Use the `COUNT(*)` function to count the number of direct reports for each manager.
4. Filter the results using the `HAVING` clause to only include managers with at least five direct reports.

**Time Complexity**
O(n log n) due to the `GROUP BY` clause, where n is the number of employees. This is because the `GROUP BY` clause requires sorting the data, which takes O(n log n) time.

**Space Complexity**
O(n) because we need to store the intermediate results of the join and group operations.

**Key Insight**
The key insight here is that by joining the `Employee` table with itself on the `managerId` column, we can effectively create a table where each row represents a manager and their direct reports. This allows us to easily count the number of direct reports for each manager using the `COUNT(*)` function.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 432 ms (Beats 9.41%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-20 |
| 💻 Language | MySQL |