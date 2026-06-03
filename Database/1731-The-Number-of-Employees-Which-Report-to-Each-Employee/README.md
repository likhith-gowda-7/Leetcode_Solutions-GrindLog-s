# 1731. The Number of Employees Which Report to Each Employee


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/)


## 📝 Problem Description

Table: `Employees`

```

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null). 

```

 

For this problem, we will consider a **manager** an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all **managers**, the number of employees who report **directly** to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by `employee_id`.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+
**Output:** 
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
**Explanation:** Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.

```

Example 2:**

```

**Input:** 
Employees table:
+-------------+---------+------------+-----+ 
| employee_id | name    | reports_to | age |
|-------------|---------|------------|-----|
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
+-------------+---------+------------+-----+ 
**Output:** 
+-------------+---------+---------------+-------------+
| employee_id | name    | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |
+-------------+---------+---------------+-------------+

```

## 🧠 Solution Explanation

**Intuition**
The solution works by joining the `Employees` table with itself on the `reports_to` column, which represents the manager-employee relationship. This allows us to group employees by their manager and calculate the desired statistics.

**Approach**
1. Perform an inner join on the `Employees` table with itself, matching rows based on the `reports_to` column.
2. Group the resulting table by the `employee_id` of the manager (i.e., the `reports_to` column).
3. For each group, calculate the count of employees reporting directly to the manager using `count(a.employee_id)`.
4. Calculate the average age of the reports by summing the `age` column and dividing by the count of employees, then rounding to the nearest integer using `round(sum(a.age)/count(*),0)`.
5. Order the result table by the `employee_id` of the manager.

**Time Complexity**
O(n), where n is the number of employees. This is because the join and grouping operations are performed in a single pass through the data.

**Space Complexity**
O(n), as the join operation creates a temporary table that can grow up to the size of the original table.

**Key Insight**
The key insight is that by joining the table with itself, we can establish the manager-employee relationship and perform the necessary calculations in a single query. This approach avoids the need for recursive queries or subqueries, making it efficient and scalable.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 597 ms (Beats 90.65%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |