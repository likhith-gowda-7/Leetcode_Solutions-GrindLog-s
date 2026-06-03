# 1789. Primary Department for Each Employee


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/primary-department-for-each-employee/)


## 📝 Problem Description

Table: `Employee`

```

+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
(employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
employee_id is the id of the employee.
department_id is the id of the department to which the employee belongs.
primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.

```

 

Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is `'N'`.

Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Employee table:
+-------------+---------------+--------------+
| employee_id | department_id | primary_flag |
+-------------+---------------+--------------+
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |
+-------------+---------------+--------------+
**Output:** 
+-------------+---------------+
| employee_id | department_id |
+-------------+---------------+
| 1           | 1             |
| 2           | 1             |
| 3           | 3             |
| 4           | 3             |
+-------------+---------------+
**Explanation:** 
- The Primary department for employee 1 is 1.
- The Primary department for employee 2 is 1.
- The Primary department for employee 3 is 3.
- The Primary department for employee 4 is 3.

```

## 🧠 Solution Explanation

**Intuition**
This solution uses a Common Table Expression (CTE) to count the number of departments each employee belongs to, then joins this result with the original table to identify the primary department for each employee.

**Approach**
1. Create a CTE `cust_details` that groups the `Employee` table by `employee_id` and counts the number of departments each employee belongs to.
2. Join the `Employee` table with the `cust_details` CTE on `employee_id`.
3. In the joined table, select rows where the employee has only one department (`cnt = 1`) or has multiple departments and the current department is marked as primary (`cnt > 1` and `primary_flag = 'Y'`).

**Time Complexity**
O(n log n) due to the grouping operation in the CTE, where n is the number of employees.

**Space Complexity**
O(n) for storing the intermediate result of the CTE.

**Key Insight**
The key insight here is to use a CTE to count the number of departments each employee belongs to, which allows us to efficiently identify the primary department for each employee. This approach avoids the need for self-joins or complex subqueries, making it more scalable and efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 499 ms (Beats 97.27%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |