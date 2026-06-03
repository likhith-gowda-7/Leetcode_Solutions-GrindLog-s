# 1174. Immediate Food Delivery II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/immediate-food-delivery-ii/)


## 📝 Problem Description

Table: `Delivery`

```

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).

```

 

If the customer's preferred delivery date is the same as the order date, then the order is called **immediate;** otherwise, it is called **scheduled**.

The **first order** of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, **rounded to 2 decimal places**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+
**Output:** 
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
**Explanation:** 
The customer id 1 has a first order with delivery id 1 and it is scheduled.
The customer id 2 has a first order with delivery id 2 and it is immediate.
The customer id 3 has a first order with delivery id 5 and it is scheduled.
The customer id 4 has a first order with delivery id 7 and it is immediate.
Hence, half the customers have immediate first orders.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a Common Table Expression (CTE) to find the minimum order date for each customer, and then calculates the percentage of immediate orders by dividing the count of immediate orders by the total count of orders for each customer.

**Approach**
1. Create a CTE `Customer_min_orderDate` that selects the minimum `order_date` for each `customer_id` from the `Delivery` table.
2. Use a subquery to select the `customer_id` and `order_date` pairs from `Customer_min_orderDate`.
3. In the main query, calculate the percentage of immediate orders by summing the count of orders where `order_date` equals `customer_pref_delivery_date` and dividing by the total count of orders for each customer.
4. Use the `round` function to format the result to two decimal places.

**Time Complexity**
O(n log n) due to the grouping operation in the CTE, where n is the number of rows in the `Delivery` table.

**Space Complexity**
O(n) for storing the intermediate results of the CTE.

**Key Insight**
The key insight is to use a CTE to find the minimum order date for each customer, which allows us to efficiently calculate the percentage of immediate orders for each customer by filtering the orders based on the minimum order date. This approach avoids the need to join the `Delivery` table with itself, which would increase the time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 599 ms (Beats 85.29%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-24 |
| 💻 Language | MySQL |