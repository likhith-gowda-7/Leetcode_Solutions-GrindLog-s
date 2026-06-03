# 1148. Article Views I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/article-views-i/)


## 📝 Problem Description

Table: `Views`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.

```

 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by `id` in ascending order.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
**Output:** 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+

```

## 🧠 Solution Explanation

**Intuition**
The solution works by identifying rows in the `Views` table where the `author_id` matches the `viewer_id`, indicating that the author viewed their own article. This is a simple filtering operation that can be performed efficiently using a SQL query.

**Approach**
1. Select the `author_id` column from the `Views` table.
2. Apply a filter to include only rows where `author_id` equals `viewer_id`.
3. Use the `distinct` keyword to remove duplicate `author_id` values.
4. Order the result by `id` in ascending order.

**Time Complexity**
O(n), where n is the number of rows in the `Views` table. This is because we need to scan the entire table to find the matching rows.

**Space Complexity**
O(n), where n is the number of rows in the `Views` table. This is because we need to store the filtered results in memory.

**Key Insight**
The key insight here is that we can use a simple equality filter to identify the authors who viewed their own articles. This is a common pattern in database queries, where we use a condition to narrow down the data to the desired subset. In this case, the condition is `author_id = viewer_id`, which is a straightforward and efficient way to solve the problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 861 ms (Beats 42.3%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-15 |
| 💻 Language | mssql |