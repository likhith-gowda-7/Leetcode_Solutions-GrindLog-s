# 175. Combine Two Tables


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/combine-two-tables/)


## 📝 Problem Description

Table: `Person`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.

```

 

Table: `Address`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.

```

 

Write a solution to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
**Output:** 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
**Explanation:** 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.

```

## 🧠 Solution Explanation

**Intuition**
The problem requires combining data from two tables, `Person` and `Address`, based on a common column `personId`. The goal is to retrieve the first name, last name, city, and state for each person. A left join is used to include all rows from the `Person` table, even if there is no matching row in the `Address` table.

**Approach**
1. Select the desired columns from the `Person` table (`p.firstName`, `p.lastName`) and the `Address` table (`a.city`, `a.state`).
2. Use a left join to combine the two tables based on the `personId` column.
3. The left join ensures that all rows from the `Person` table are included, even if there is no matching row in the `Address` table.

**Time Complexity**
O(n + m), where n is the number of rows in the `Person` table and m is the number of rows in the `Address` table. This is because the left join needs to iterate over all rows in both tables to perform the join.

**Space Complexity**
O(n + m), as the result set will contain at most n + m rows, assuming that each row in the `Person` table has a matching row in the `Address` table.

**Key Insight**
The key insight is to use a left join to ensure that all rows from the `Person` table are included, even if there is no matching row in the `Address` table. This allows for a more comprehensive result set that includes all persons, regardless of whether they have an associated address.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 386 ms (Beats 89.86%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |