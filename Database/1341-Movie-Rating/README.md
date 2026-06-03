# 1341. Movie Rating


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/movie-rating/)


## 📝 Problem Description

Table: `Movies`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
Each movie has a unique title.
```

Table: `Users`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
The column 'name' has unique values.

```

Table: `MovieRating`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date. 

```

 

Write a solution to:

	- Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.

	- Find the movie name with the **highest average** rating in `February 2020`. In case of a tie, return the lexicographically smaller movie name.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  | 
| 2           | 2            | 2            | 2020-02-01  | 
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  | 
| 3           | 2            | 4            | 2020-02-25  | 
+-------------+--------------+--------------+-------------+
**Output:** 
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
**Explanation:** 
Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.

```

## 🧠 Solution Explanation

**Intuition**
This SQL query is designed to find the user with the most ratings and the movie with the highest average rating within a specific date range. The query uses a combination of joins, group by, and order by clauses to achieve this.

**Approach**
1. First, the query selects the user with the most ratings by joining the `Users` and `MovieRating` tables, grouping by `user_id` and `name`, ordering by the count of ratings in descending order, and limiting the result to 1.
2. Then, it selects the movie with the highest average rating within the specified date range by joining the `Movies` and `MovieRating` tables, filtering by the date range, grouping by `movie_id` and `title`, ordering by the average rating in descending order, and limiting the result to 1.
3. The two results are combined using the `UNION ALL` operator.

**Time Complexity**
O(n log n) due to the use of order by clauses, where n is the number of rows in the `MovieRating` table.

**Space Complexity**
O(n) for the temporary result sets created during the execution of the query.

**Key Insight**
The key insight here is the use of the `UNION ALL` operator to combine the results of two separate queries, each of which finds a single row with the most ratings or highest average rating. This allows the query to return both the user with the most ratings and the movie with the highest average rating within the specified date range.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1174 ms (Beats 95.62%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-02-10 |
| 💻 Language | MySQL |