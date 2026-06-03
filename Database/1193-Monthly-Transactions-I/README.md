# 1193. Monthly Transactions I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/monthly-transactions-i/)


## 📝 Problem Description

Table: `Transactions`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].

```

 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in **any order**.

The query result format is in the following example.

 

Example 1:**

```

**Input:** 
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
**Output:** 
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+

```

## 🧠 Solution Explanation

**Intuition**
The solution works by extracting the month from the `trans_date` column, grouping the transactions by month and country, and then calculating the required metrics (transaction count, total amount, approved transaction count, and approved total amount) for each group.

**Approach**
1. Extract the month from the `trans_date` column using the `SUBSTRING` function, which returns the first 7 characters (i.e., the month and year).
2. Group the transactions by the extracted month and country using the `GROUP BY` clause.
3. For each group, calculate the transaction count using the `COUNT(*)` function.
4. Calculate the total amount for each group using the `SUM` function.
5. Calculate the approved transaction count and approved total amount for each group using conditional `SUM` functions with `CASE` statements.

**Time Complexity**
O(n), where n is the number of transactions. This is because we are scanning the transactions table once to extract the month and group the transactions.

**Space Complexity**
O(n), where n is the number of groups (i.e., the number of unique month-country combinations). This is because we are storing the intermediate results for each group in the result table.

**Key Insight**
The key insight is to extract the month from the `trans_date` column and group the transactions by month and country, which allows us to calculate the required metrics for each group efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 545 ms (Beats 94.04%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |