# 176. Second Highest Salary


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/second-highest-salary/)


## 📝 Problem Description

Table: `Employee`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

```

 

Write a solution to find the second highest **distinct** salary from the `Employee` table. If there is no second highest salary, return `null (return None in Pandas)`.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
**Output:** 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

```

Example 2:**

```

**Input:** 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
**Output:** 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a common technique in SQL to rank rows based on a specific column, in this case, the `salary` column. The `dense_rank()` function assigns a unique rank to each distinct salary, allowing us to easily identify the second highest salary.

**Approach**
1. Create a temporary result set `details` that contains the `salary` column and a new column `salary_rank` using the `dense_rank()` function.
2. Order the `salary` column in descending order to prioritize higher salaries.
3. Select the maximum `salary` from the `details` result set where the `salary_rank` is equal to 2.

**Time Complexity**
O(n), where n is the number of rows in the `Employee` table. This is because the `dense_rank()` function needs to process each row once to assign the ranks.

**Space Complexity**
O(n), where n is the number of rows in the `Employee` table. This is because the temporary result set `details` needs to store all the rows from the `Employee` table.

**Key Insight**
The key insight is to use the `dense_rank()` function to assign a unique rank to each distinct salary, allowing us to easily identify the second highest salary. This approach is more efficient than sorting the salaries and then selecting the second highest one, as it avoids the need for explicit sorting.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 368 ms (Beats 61.06%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-05-03 |
| 💻 Language | mssql |