# 1378. Replace Employee ID With The Unique Identifier


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)


## 📝 Problem Description

Table: `Employees`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.

```

 

Table: `EmployeeUNI`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.

```

 

Write a solution to show the **unique ID **of each user, If a user does not have a unique ID replace just show `null`.

Return the result table in **any** order.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
**Output:** 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
**Explanation:** 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.

```

## 🧠 Solution Explanation

**Intuition**
The solution involves joining two tables, `Employees` and `EmployeeUNI`, based on the `id` column. The `left join` operation ensures that all employees from the `Employees` table are included in the result, even if there is no matching unique ID in the `EmployeeUNI` table.

**Approach**
1. The `select` statement specifies the columns to be included in the result: `b.unique_id` and `a.name`.
2. The `from` clause specifies the first table to be joined, `Employees`, which is aliased as `a`.
3. The `left join` clause specifies the second table to be joined, `EmployeeUNI`, which is aliased as `b`, and the join condition: `b.id = a.id`.
4. The `on` clause specifies the condition for joining the two tables.

**Time Complexity**
O(n), where n is the number of rows in the `Employees` table. This is because the join operation is performed once, and the result is returned in a single pass.

**Space Complexity**
O(n), where n is the number of rows in the `Employees` table. This is because the result set contains all employees from the `Employees` table, plus the unique ID from the `EmployeeUNI` table.

**Key Insight**
The key insight is that the `left join` operation allows us to include all employees from the `Employees` table, even if there is no matching unique ID in the `EmployeeUNI` table. This is achieved by specifying the join condition `b.id = a.id`, which ensures that only rows with matching IDs are joined.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1072 ms (Beats 96%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-15 |
| 💻 Language | MySQL |