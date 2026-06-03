# 620. Not Boring Movies


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/not-boring-movies/)


## 📝 Problem Description

Table: `Cinema`

```

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]

```

 

Write a solution to report the movies with an odd-numbered ID and a description that is not `"boring"`.

Return the result table ordered by `rating` **in descending order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Cinema table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+
**Output:** 
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+
**Explanation:** 
We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a simple SQL query to filter the `Cinema` table based on two conditions: the movie ID is odd and the description is not "boring". The result is then sorted in descending order by rating.

**Approach**
1. The query starts by selecting all columns (`id`, `movie`, `description`, `rating`) from the `Cinema` table.
2. The `where` clause filters the rows based on two conditions:
   - `id%2<>0` checks if the ID is odd by using the modulo operator (`%`). If the remainder of the division of the ID by 2 is not 0, the ID is odd.
   - `description <> 'boring'` checks if the description is not equal to "boring".
3. The `order by` clause sorts the result in descending order by rating.

**Time Complexity**
The time complexity of this solution is O(n), where n is the number of rows in the `Cinema` table. This is because the query needs to scan all rows to apply the filters and sort the result.

**Space Complexity**
The space complexity of this solution is O(1), which means the space required does not grow with the size of the input. This is because the query only requires a constant amount of space to store the result.

**Key Insight**
The key insight here is the use of the modulo operator (`%`) to check if the ID is odd, which is a simple and efficient way to filter the rows. Additionally, the use of the `<>` operator to check for inequality is a common pattern in SQL queries.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 242 ms (Beats 95.57%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |