# 1683. Invalid Tweets


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-mssql-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/invalid-tweets/)


## 📝 Problem Description

Table: `Tweets`

```

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, '!', or ' ' and no other special characters.
This table contains all the tweets in a social media app.

```

 

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is **strictly greater** than `15`.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
**Output:** 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
**Explanation:** 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.

```

## 🧠 Solution Explanation

**Intuition**
The solution works by filtering the tweets table to include only the rows where the length of the content is greater than 15. This effectively identifies the invalid tweets based on the given condition.

**Approach**
1. The `len(content)` function is used to get the length of the content string in each row.
2. The `where` clause is used to filter the rows where the length of the content is greater than 15.
3. The `select` statement is used to retrieve the `tweet_id` column from the filtered rows.

**Time Complexity**
O(n), where n is the number of rows in the tweets table. This is because we are scanning each row once to check the length of the content.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the filtered results. The input table is not modified, and we are not creating any additional data structures that scale with the input size.

**Key Insight**
The key insight here is that we can use a simple filtering condition to identify the invalid tweets. By leveraging the `len` function, we can efficiently scan the table and retrieve the IDs of the invalid tweets. This approach highlights the importance of using the right database functions to simplify complex queries.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 780 ms (Beats 74.2%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-15 |
| 💻 Language | mssql |