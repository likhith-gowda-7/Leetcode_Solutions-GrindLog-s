# 1211. Queries Quality and Percentage


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/queries-quality-and-percentage/)


## 📝 Problem Description

Table: `Queries`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The `position` column has a value from **1** to **500**.
The `rating` column has a value from **1** to **5**. Query with `rating` less than 3 is a poor query.

```

 

We define query `quality` as:

The average of the ratio between query rating and its position.

We also define `poor query percentage` as:

The percentage of all queries with rating less than 3.

Write a solution to find each `query_name`, the `quality` and `poor_query_percentage`.

Both `quality` and `poor_query_percentage` should be **rounded to 2 decimal places**.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+
**Output:** 
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+
**Explanation:** 
Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33

```

## 🧠 Solution Explanation

**Intuition**
The solution calculates the query quality and poor query percentage for each query name by grouping the queries and applying the defined formulas. The quality is the average of the ratio between the query rating and its position, while the poor query percentage is the percentage of queries with a rating less than 3.

**Approach**
1. The solution starts by selecting the required columns: `query_name`, `quality`, and `poor_query_percentage`.
2. It then calculates the quality for each query by taking the average of the ratio between the `rating` and `position` columns, rounded to 2 decimal places.
3. The poor query percentage is calculated by summing the number of queries with a rating less than 3 and dividing it by the total number of queries, then multiplying by 100 and rounding to 2 decimal places.
4. The solution groups the queries by `query_name` to ensure that the calculations are performed separately for each query.

**Time Complexity**
O(n), where n is the number of queries. This is because the solution iterates over the queries once to calculate the quality and poor query percentage for each query.

**Space Complexity**
O(n), where n is the number of queries. This is because the solution requires temporary storage to store the intermediate results of the calculations.

**Key Insight**
The key insight is that the solution can be simplified by using the `avg` and `sum` aggregation functions to calculate the quality and poor query percentage, respectively. This avoids the need for explicit loops or subqueries, making the solution more efficient and concise.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 333 ms (Beats 95.89%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-24 |
| 💻 Language | MySQL |