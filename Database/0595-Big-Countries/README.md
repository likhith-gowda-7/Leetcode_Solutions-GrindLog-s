# 595. Big Countries


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/big-countries/)


## 📝 Problem Description

Table: `World`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

```

 

A country is **big** if:

	- it has an area of at least three million (i.e., `3000000 km^2`), or

	- it has a population of at least twenty-five million (i.e., `25000000`).

Write a solution to find the name, population, and area of the **big countries**.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
**Output:** 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+

```

## 🧠 Solution Explanation

**Intuition**
The problem asks us to identify "big countries" based on their area or population. We can solve this by filtering the `World` table to include only rows where the area is at least 3 million or the population is at least 25 million.

**Approach**
1. We start by selecting the columns we're interested in: `name`, `population`, and `area`.
2. We then use the `where` clause to filter the table based on the conditions specified in the problem.
3. We use the `or` operator to combine the two conditions: `area >= 3000000` or `population >= 25000000`.
4. The resulting table will contain only the rows that satisfy either of these conditions.

**Time Complexity**
O(n), where n is the number of rows in the `World` table. This is because we're scanning the entire table once to filter out the rows that don't meet the conditions.

**Space Complexity**
O(n), where n is the number of rows in the resulting table. This is because we're creating a new table with the filtered rows.

**Key Insight**
The key insight here is that we can use a simple `where` clause with an `or` operator to filter the table based on multiple conditions. This is a common technique in SQL, and it allows us to solve the problem efficiently without needing to use complex joins or subqueries.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 557 ms (Beats 64.95%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-15 |
| 💻 Language | mssql |