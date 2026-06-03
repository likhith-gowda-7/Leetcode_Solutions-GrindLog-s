# 1757. Recyclable and Low Fat Products


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/recyclable-and-low-fat-products/)


## 📝 Problem Description

Table: `Products`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
```

 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
**Output:** 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
**Explanation:** Only products 1 and 3 are both low fat and recyclable.

```

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the product IDs that satisfy two conditions: being low fat and recyclable. We can achieve this by filtering the products table based on these conditions.

**Approach**
1. We select the `product_id` column from the `Products` table.
2. We apply a filter to include only rows where `low_fats` is 'Y' (indicating low fat) and `recyclable` is 'Y' (indicating recyclable).

**Time Complexity**
O(n), where n is the number of rows in the `Products` table. This is because we are scanning the entire table to apply the filter.

**Space Complexity**
O(1), as we are not using any additional space that scales with the input size. We are simply returning a subset of the original table.

**Key Insight**
The key insight here is that we can use a simple filter to achieve the desired result. By applying the conditions directly to the `low_fats` and `recyclable` columns, we can efficiently identify the product IDs that meet both criteria.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 419 ms (Beats 65.57%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-15 |
| 💻 Language | mssql |