# 584. Find Customer Referee


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-customer-referee/)


## 📝 Problem Description

Table: `Customer`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

```

 

Find the names of the customer that are either:

	- **referred by** any customer with `id != 2`.

	- **not referred by** any customer.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
**Output:** 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+

```

## 🧠 Solution Explanation

**Intuition**
This solution works by filtering the customers based on their referee_id. If the referee_id is null, it means the customer was not referred by anyone. If the referee_id is not equal to 2, it means the customer was referred by someone other than the customer with id 2.

**Approach**
1. The query selects the name column from the Customer table.
2. It applies a WHERE clause with two conditions:
   - `referee_id is Null`: This condition checks for customers who were not referred by anyone.
   - `referee_id != 2`: This condition checks for customers who were referred by someone other than the customer with id 2.
3. The OR operator is used to combine these two conditions, ensuring that customers who meet either condition are included in the result.

**Time Complexity**
O(n), where n is the number of rows in the Customer table. This is because the query needs to scan each row in the table to apply the conditions.

**Space Complexity**
O(1), which means the space complexity is constant. This is because the query only requires a small amount of memory to store the result, regardless of the size of the input table.

**Key Insight**
The key insight here is that we can use a simple WHERE clause with two conditions to filter the customers based on their referee_id. By combining these conditions with an OR operator, we can efficiently identify the customers who meet the specified criteria.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 499 ms (Beats 51.63%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | mssql |