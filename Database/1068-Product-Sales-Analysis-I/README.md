# 1068. Product Sales Analysis I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/product-sales-analysis-i/)


## 📝 Problem Description

Table: `Sales`

```

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to `Product` table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.

```

 

Table: `Product`

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.

```

 

Write a solution to report the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.

Return the resulting table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
**Output:** 
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
**Explanation:** 
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.

```

## 🧠 Solution Explanation

**Intuition**
The given SQL query is designed to retrieve the product name, year of sale, and price for each sale in the `Sales` table, joining it with the `Product` table based on the product ID.

**Approach**
1. The query uses an implicit join between the `Sales` and `Product` tables, which is equivalent to an inner join. This is done by specifying both tables in the `FROM` clause and the join condition in the `WHERE` clause.
2. The `SELECT` statement retrieves the desired columns: `product_name` from the `Product` table, `year` and `price` from the `Sales` table.
3. The `WHERE` clause filters the results to include only rows where the `product_id` in the `Sales` table matches the `product_id` in the `Product` table.

**Time Complexity**
O(n), where n is the number of rows in the `Sales` table. This is because the query scans each row in the `Sales` table once to perform the join.

**Space Complexity**
O(n), where n is the number of rows in the `Sales` table. This is because the query returns a result set with one row for each matching row in the `Sales` table.

**Key Insight**
The key insight here is that implicit joins can be less readable and more prone to errors than explicit joins, but they can also be more concise and efficient. However, in modern SQL, explicit joins are generally preferred for their clarity and maintainability.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2500 ms (Beats 99.84%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-15 |
| 💻 Language | mssql |