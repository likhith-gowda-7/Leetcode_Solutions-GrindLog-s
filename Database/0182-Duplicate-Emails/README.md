# 182. Duplicate Emails


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/duplicate-emails/)


## 📝 Problem Description

Table: `Person`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

```

 

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
**Output:** 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
**Explanation:** a@b.com is repeated two times.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a common technique in SQL called "Common Table Expressions" (CTEs) to break down the problem into a more manageable part. By grouping the emails and counting their occurrences, we can easily identify the duplicate emails.

**Approach**
1. Create a CTE named `emails` that selects the `email` column from the `Person` table and counts the occurrences of each email using the `count(*)` function.
2. Group the emails by their values using the `group by` clause.
3. In the main query, select the `email` column from the `emails` CTE where the `email_count` is greater than 1.

**Time Complexity**
O(n), where n is the number of rows in the `Person` table. This is because we are scanning the table once to group the emails and count their occurrences.

**Space Complexity**
O(n), where n is the number of rows in the `Person` table. This is because we are storing the intermediate results in the `emails` CTE.

**Key Insight**
The key insight here is that by using a CTE to group the emails and count their occurrences, we can easily identify the duplicate emails without having to scan the table multiple times. This approach is efficient and scalable, making it suitable for large datasets.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 349 ms (Beats 93.65%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-05-17 |
| 💻 Language | MySQL |