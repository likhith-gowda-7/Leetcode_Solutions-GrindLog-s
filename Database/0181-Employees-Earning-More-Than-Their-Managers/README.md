# 181. Employees Earning More Than Their Managers


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/employees-earning-more-than-their-managers/)


## 📝 Problem Description

Table: `Employee`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

```

 

Write a solution to find the employees who earn more than their managers.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
**Output:** 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
**Explanation:** Joe is the only employee who earns more than his manager.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a self-join to compare the salaries of employees with their managers. By joining the `Employee` table with itself, we can create a relationship between each employee and their manager, allowing us to compare their salaries.

**Approach**
1. We join the `Employee` table with itself on the `managerId` column, creating a relationship between each employee and their manager.
2. We select the `name` column from the first instance of the table (`a`) and alias it as `Employee`.
3. We filter the results to include only employees whose salary is greater than their manager's salary.

**Time Complexity**
O(n^2) where n is the number of employees. This is because the self-join operation has a time complexity of O(n^2), and the filtering operation does not affect the overall time complexity.

**Space Complexity**
O(n) where n is the number of employees. This is because we are creating a temporary result set that contains all employees who earn more than their managers.

**Key Insight**
The key insight here is that we can use a self-join to create a relationship between each employee and their manager, allowing us to compare their salaries. This is a common technique in SQL when working with hierarchical or relational data.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 362 ms (Beats 87.77%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |