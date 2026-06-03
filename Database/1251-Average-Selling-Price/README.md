# 1251. Average Selling Price


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/average-selling-price/)


## 📝 Problem Description

Table: `Prices`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.

```

 

Table: `UnitsSold`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold. 

```

 

Write a solution to find the average selling price for each product. `average_price` should be **rounded to 2 decimal places**. If a product does not have any sold units, its average selling price is assumed to be 0.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
**Output:** 
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+
**Explanation:** 
Average selling price = Total Price of Product / Number of products sold.
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96

```

## 🧠 Solution Explanation

**Intuition**
The solution joins the `Prices` and `UnitsSold` tables based on the product ID and date range, then calculates the average price for each product by dividing the total revenue (price * units) by the total units sold.

**Approach**
1. Perform a LEFT JOIN between the `Prices` and `UnitsSold` tables on the product ID and date range.
2. For each joined row, multiply the price by the units sold to get the total revenue.
3. Calculate the total units sold by summing the units column.
4. Divide the total revenue by the total units sold to get the average price.
5. Round the average price to two decimal places using the `ROUND` function.
6. Group the results by product ID using the `GROUP BY` clause.

**Time Complexity**
O(n), where n is the total number of rows in the `Prices` and `UnitsSold` tables. This is because we perform a single pass through the joined tables to calculate the average price for each product.

**Space Complexity**
O(n), where n is the total number of rows in the `Prices` and `UnitsSold` tables. This is because we need to store the intermediate results in memory before grouping and calculating the average price.

**Key Insight**
The key insight here is to use a LEFT JOIN to include all products from the `Prices` table, even if there are no matching rows in the `UnitsSold` table. This allows us to calculate the average price for each product, even if there are no sales data available.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 716 ms (Beats 97.59%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-23 |
| 💻 Language | MySQL |