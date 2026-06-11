# 177. Nth Highest Salary


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/nth-highest-salary/)


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

 

Write a solution to find the `n^th` highest **distinct** salary from the `Employee` table. If there are less than `n` distinct salaries, return `null`.

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
n = 2
**Output:** 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

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
n = 2
**Output:** 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a MySQL function to find the nth highest distinct salary from the Employee table. It achieves this by ranking the salaries in descending order and then selecting the nth rank.

**Approach**
1. A subquery is used to rank the salaries in descending order using the `dense_rank()` function.
2. The outer query selects the distinct salaries where the rank matches the input `N`.
3. If there are less than `N` distinct salaries, the query will return `null`.

**Time Complexity**
O(log N) due to the use of the `dense_rank()` function, which has a time complexity of O(log N) for ranking the rows.

**Space Complexity**
O(N) for storing the temporary result of the subquery.

**Key Insight**
The key insight here is the use of `dense_rank()` function, which allows us to efficiently rank the rows in descending order. This is particularly useful when dealing with large datasets, as it avoids the need for a self-join or a subquery with a correlated subquery.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 473 ms (Beats 36.76%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-06-11 |
| 💻 Language | MySQL |