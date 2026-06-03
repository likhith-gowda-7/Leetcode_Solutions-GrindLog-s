# 1581. Customer Who Visited but Did Not Make Any Transactions


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)


## 📝 Problem Description

Table: `Visits`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.

```

 

Table: `Transactions`

```

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.

```

 

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
**Output:** 
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+
**Explanation:** 
Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
Customer with id = 30 visited the mall once and did not make any transactions.
Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
Customer with id = 96 visited the mall once and did not make any transactions.
As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.

```

## 🧠 Solution Explanation

**Intuition**
The solution works by identifying customers who have a visit but no corresponding transaction. This is achieved by performing a left join between the `Visits` and `Transactions` tables, and then filtering for rows where there is no matching transaction.

**Approach**
1. Perform a left join between the `Visits` and `Transactions` tables on the `visit_id` column.
2. Filter the result to include only rows where the `visit_id` in the `Transactions` table is `NULL`, indicating that there is no matching transaction.
3. Group the remaining rows by `customer_id` to count the number of visits without transactions for each customer.

**Time Complexity**
The time complexity of this solution is O(n), where n is the total number of rows in the `Visits` and `Transactions` tables combined. This is because we are performing a single pass through both tables.

**Space Complexity**
The space complexity of this solution is O(n), where n is the total number of rows in the `Visits` and `Transactions` tables combined. This is because we are storing the result of the join in memory.

**Key Insight**
The key insight here is that a left join allows us to include all rows from the `Visits` table, even if there is no matching row in the `Transactions` table. By filtering for `NULL` values in the `Transactions` table, we can identify the customers who have visited but made no transactions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1130 ms (Beats 86.86%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-15 |
| 💻 Language | mssql |