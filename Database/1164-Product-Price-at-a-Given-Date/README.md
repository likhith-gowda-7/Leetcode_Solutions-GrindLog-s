# 1164. Product Price at a Given Date


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/product-price-at-a-given-date/)


## 📝 Problem Description

Table: `Products`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
```

Initially, all products have price 10.

Write a solution to find the prices of all products on the date `2019-08-16`.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
**Output:** 
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+

```

## 🧠 Solution Explanation

**Intuition**
This solution works by first identifying the latest price change for each product before the target date, and then filling in the products that haven't had a price change.

**Approach**

1. Create a temporary table `details` that includes all price changes for products up to the target date, along with a ranking of the most recent change for each product.
2. Select the product ID and new price from `details` where the ranking is 1, indicating the most recent price change.
3. Use a UNION to include products that haven't had a price change, with a default price of 10.

**Time Complexity**
The time complexity of this solution is O(n log n) due to the use of the `RANK()` function with `ORDER BY` and `PARTITION BY` clauses, which requires a sort operation.

**Space Complexity**
The space complexity of this solution is O(n) for storing the temporary table `details`.

**Key Insight**
The key insight here is the use of the `RANK()` function to identify the most recent price change for each product, allowing us to easily fill in the products that haven't had a price change.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 431 ms (Beats 96.67%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-27 |
| 💻 Language | MySQL |