# 1070. Product Sales Analysis III


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/product-sales-analysis-iii/)


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
Each row records a sale of a product in a given year.
A product may have multiple sales entries in the same year.
Note that the per-unit price.

```

Write a solution to find all sales that occurred in the first year** each product was sold.

	
	For each product_id`, identify the earliest year` it appears in the Sales` table.

	

	
	Return all** sales entries for that product in that year.

	

Return a table with the following columns: **product_id**,** first_year**, **quantity, **and** price**.

Return the result in any order.

 

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

**Output:** 
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a common technique in SQL known as a "Common Table Expression" (CTE) to first identify the earliest year each product was sold, and then joins this result with the original sales table to retrieve all sales entries for that year.

**Approach**

1. Create a CTE named `product_first_year` that groups the sales table by `product_id` and selects the minimum `year` for each group, effectively finding the earliest year each product was sold.
2. Use the `IN` operator to join the sales table with the `product_first_year` CTE, selecting only rows where the product's earliest year matches the year of the sale.
3. Select the desired columns (`product_id`, `year`, `quantity`, and `price`) from the joined table.

**Time Complexity**
O(n log n) due to the grouping operation in the CTE, where n is the number of unique product-year combinations in the sales table. The subsequent join operation is linear, but the grouping operation dominates the time complexity.

**Space Complexity**
O(n) to store the intermediate result of the CTE, where n is the number of unique product-year combinations in the sales table.

**Key Insight**
The key insight is to use a CTE to isolate the earliest year each product was sold, and then join this result with the original sales table to retrieve all sales entries for that year. This approach allows us to efficiently identify the desired sales entries without having to perform complex subqueries or aggregations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 683 ms (Beats 81.67%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-25 |
| 💻 Language | MySQL |