# 1327. List the Products Ordered in a Period


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/list-the-products-ordered-in-a-period/)


## 📝 Problem Description

Table: `Products`

```

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.

```

 

Table: `Orders`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.

```

 

Write a solution to get the names of products that have at least `100` units ordered in **February 2020** and their amount.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Products table:
+-------------+-----------------------+------------------+
| product_id  | product_name          | product_category |
+-------------+-----------------------+------------------+
| 1           | Leetcode Solutions    | Book             |
| 2           | Jewels of Stringology | Book             |
| 3           | HP                    | Laptop           |
| 4           | Lenovo                | Laptop           |
| 5           | Leetcode Kit          | T-shirt          |
+-------------+-----------------------+------------------+
Orders table:
+--------------+--------------+----------+
| product_id   | order_date   | unit     |
+--------------+--------------+----------+
| 1            | 2020-02-05   | 60       |
| 1            | 2020-02-10   | 70       |
| 2            | 2020-01-18   | 30       |
| 2            | 2020-02-11   | 80       |
| 3            | 2020-02-17   | 2        |
| 3            | 2020-02-24   | 3        |
| 4            | 2020-03-01   | 20       |
| 4            | 2020-03-04   | 30       |
| 4            | 2020-03-04   | 60       |
| 5            | 2020-02-25   | 50       |
| 5            | 2020-02-27   | 50       |
| 5            | 2020-03-01   | 50       |
+--------------+--------------+----------+
**Output:** 
+--------------------+---------+
| product_name       | unit    |
+--------------------+---------+
| Leetcode Solutions | 130     |
| Leetcode Kit       | 100     |
+--------------------+---------+
**Explanation:** 
Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
Products with product_id = 2 is ordered in February a total of 80.
Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
Products with product_id = 4 was not ordered in February 2020.
Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.

```

## 🧠 Solution Explanation

**Intuition**
The solution works by joining the `Products` and `Orders` tables based on the `product_id` column, then filtering the results to only include orders from February 2020. The `group by` clause groups the results by `product_id`, and the `having` clause filters the results to only include products with a total unit count of 100 or more.

**Approach**

1. Join the `Products` and `Orders` tables on the `product_id` column to link each product with its corresponding orders.
2. Filter the joined table to only include orders from February 2020 using the `month` and `year` functions.
3. Group the filtered table by `product_id` to calculate the total unit count for each product.
4. Use the `having` clause to filter the grouped table to only include products with a total unit count of 100 or more.

**Time Complexity**
O(n), where n is the number of orders in the `Orders` table. This is because the solution involves a single join operation, followed by filtering and grouping, all of which can be performed in a single pass through the data.

**Space Complexity**
O(n), where n is the number of orders in the `Orders` table. This is because the solution requires storing the joined and filtered data in memory.

**Key Insight**
The key insight here is that the `having` clause allows us to filter the results after grouping, which is more efficient than trying to filter the data before grouping. This is because the `having` clause can take advantage of the grouping already performed, making the solution more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 639 ms (Beats 98.97%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |