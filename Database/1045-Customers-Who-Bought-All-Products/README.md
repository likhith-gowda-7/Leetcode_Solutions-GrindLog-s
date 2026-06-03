# 1045. Customers Who Bought All Products


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/customers-who-bought-all-products/)


## 📝 Problem Description

Table: `Customer`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
This table may contain duplicates rows. 
`customer_id` is not NULL`.`
product_key is a foreign key (reference column) to `Product` table.

```

 

Table: `Product`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key (column with unique values) for this table.

```

 

Write a solution to report the customer ids from the `Customer` table that bought all the products in the `Product` table.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
**Output:** 
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
**Explanation:** 
The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.

```

## 🧠 Solution Explanation

**Intuition**
The solution works by grouping customers by their IDs and checking if each group has a count of distinct products equal to the total number of products in the `Product` table. This implies that the customer in each group has bought all the products.

**Approach**
1. The query selects the `customer_id` column from the `Customer` table.
2. It groups the results by `customer_id` using the `GROUP BY` clause.
3. The `HAVING` clause is used to filter the groups where the count of distinct `product_key` values is equal to the total number of products in the `Product` table. This is achieved by comparing the count of distinct `product_key` values in each group to the result of a subquery that counts the total number of products in the `Product` table.

**Time Complexity**
O(n log n) due to the grouping operation, where n is the number of rows in the `Customer` table. The subquery in the `HAVING` clause is executed only once, so it doesn't affect the overall time complexity.

**Space Complexity**
O(n) for storing the intermediate results of the grouping operation, where n is the number of rows in the `Customer` table.

**Key Insight**
The key insight is to use the `HAVING` clause to filter the groups based on the count of distinct products, rather than trying to join the `Customer` table with the `Product` table. This approach is more efficient and scalable, especially for large datasets.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 532 ms (Beats 90.96%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |