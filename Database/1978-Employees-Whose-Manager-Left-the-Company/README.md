# 1978. Employees Whose Manager Left the Company


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/employees-whose-manager-left-the-company/)


## 📝 Problem Description

Table: `Employees`

```

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
In SQL, employee_id is the primary key for this table.
This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null). 

```

 

Find the IDs of the employees whose salary is strictly less than `$30000` and whose manager left the company. When a manager leaves the company, their information is deleted from the `Employees` table, but the reports still have their `manager_id` set to the manager that left.

Return the result table ordered by `employee_id`.

The result format is in the following example.

 

Example 1:**

```

**Input: ** 
Employees table:
+-------------+-----------+------------+--------+
| employee_id | name      | manager_id | salary |
+-------------+-----------+------------+--------+
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
+-------------+-----------+------------+--------+
**Output:** 
+-------------+
| employee_id |
+-------------+
| 11          |
+-------------+

**Explanation:** 
The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
Kalel's manager is employee 11, who is still in the company (Joziah).
Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a self-join to find employees whose manager left the company. By joining the `Employees` table with itself, we can identify employees whose manager's ID no longer exists in the table, indicating that the manager has left.

**Approach**
1. Perform a self-join on the `Employees` table, joining `e1` with `e2` on `e1.manager_id = e2.employee_id`. This allows us to compare each employee with their manager.
2. Filter the results to include only employees with a salary less than $30000 (`e1.salary < 30000`).
3. Filter the results to include only employees whose manager ID is not null (`e1.manager_id IS NOT NULL`), as employees without a manager will not have a valid manager ID.
4. Filter the results to include only employees whose manager's ID is null in the joined table (`e2.employee_id IS NULL`), indicating that the manager has left the company.
5. Order the results by `employee_id` to ensure the output is sorted correctly.

**Time Complexity**
O(n^2) due to the self-join operation, where n is the number of employees in the table. This is because each employee is compared with every other employee to find their manager.

**Space Complexity**
O(n) for storing the joined result set, where n is the number of employees in the table.

**Key Insight**
The key insight is that by joining the `Employees` table with itself, we can identify employees whose manager's ID no longer exists in the table, indicating that the manager has left. This allows us to find the IDs of employees whose manager left the company, even if their manager's information has been deleted from the table.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 405 ms (Beats 48.84%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-31 |
| 💻 Language | mssql |