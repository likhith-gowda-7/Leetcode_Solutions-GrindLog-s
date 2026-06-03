# 577. Employee Bonus


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/employee-bonus/)


## 📝 Problem Description

Table: `Employee`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.

```

 

Table: `Bonus`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.

```

 

Write a solution to report the name and bonus amount of each employee who satisfies either of the following:

	- The employee has a bonus **less than** `1000`.

	- The employee did not get any bonus.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
**Output:** 
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+

```

## 🧠 Solution Explanation

**Intuition**
The solution joins the `Employee` and `Bonus` tables based on the `empId` column and selects employees who either have no bonus or a bonus less than $1000.

**Approach**
1. The solution starts by selecting the `name` column from the `Employee` table (`e`) and the `bonus` column from the `Bonus` table (`b`).
2. It then performs a left join on the `Employee` and `Bonus` tables based on the `empId` column. This ensures that all employees are included in the result, even if they don't have a bonus.
3. The `where` clause filters the result to include only employees with no bonus (`b.bonus is null`) or a bonus less than $1000 (`b.bonus < 1000`).

**Time Complexity**
O(n + m), where n is the number of employees and m is the number of bonuses. This is because the solution performs a single pass through both tables.

**Space Complexity**
O(n + m), where n is the number of employees and m is the number of bonuses. This is because the solution needs to store the result of the join, which can be up to the size of both tables.

**Key Insight**
The key insight here is that the left join allows us to include all employees in the result, even if they don't have a bonus. By filtering the result based on the bonus amount, we can easily identify employees who meet the condition. This approach is efficient because it avoids the need for subqueries or complex filtering logic.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1021 ms (Beats 40.88%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-16 |
| 💻 Language | MySQL |