# 1934. Confirmation Rate


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/confirmation-rate/)


## 📝 Problem Description

Table: `Signups`

```

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the column of unique values for this table.
Each row contains information about the signup time for the user with ID user_id.

```

 

Table: `Confirmations`

```

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
user_id is a foreign key (reference column) to the Signups table.
action is an ENUM (category) of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').

```

 

The **confirmation rate** of a user is the number of `'confirmed'` messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is `0`. Round the confirmation rate to **two decimal** places.

Write a solution to find the **confirmation rate** of each user.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Signups table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
Confirmations table:
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+
**Output:** 
+---------+-------------------+
| user_id | confirmation_rate |
+---------+-------------------+
| 6       | 0.00              |
| 3       | 0.00              |
| 7       | 1.00              |
| 2       | 0.50              |
+---------+-------------------+
**Explanation:** 
User 6 did not request any confirmation messages. The confirmation rate is 0.
User 3 made 2 requests and both timed out. The confirmation rate is 0.
User 7 made 3 requests and all were confirmed. The confirmation rate is 1.
User 2 made 2 requests where one was confirmed and the other timed out. The confirmation rate is 1 / 2 = 0.5.

```

## 🧠 Solution Explanation

**Intuition**
The solution calculates the confirmation rate for each user by averaging the number of confirmed actions over the total number of actions. This is done by joining the `Signups` and `Confirmations` tables on the `user_id` column and then grouping the results by user.

**Approach**

1. Perform a LEFT JOIN between the `Signups` and `Confirmations` tables on the `user_id` column to match each signup with its corresponding confirmations.
2. Use the `IFNULL` function to handle cases where a user has no confirmations, in which case the `AVG` function would return `NULL`.
3. Calculate the average number of confirmed actions using the `AVG` function with a conditional expression `c.action = 'confirmed'`.
4. Round the result to 2 decimal places using the `ROUND` function.
5. Group the results by user ID using the `GROUP BY` clause.

**Time Complexity**
The time complexity of this solution is O(n), where n is the total number of rows in the `Signups` and `Confirmations` tables. This is because we are performing a single pass through the data to join the tables and calculate the confirmation rate.

**Space Complexity**
The space complexity of this solution is O(n), where n is the total number of unique user IDs in the `Signups` table. This is because we are storing the results in a temporary table or result set.

**Key Insight**
The key insight here is to use a LEFT JOIN to match each signup with its corresponding confirmations, and then use the `IFNULL` function to handle cases where a user has no confirmations. This allows us to calculate the confirmation rate accurately even for users with no confirmations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 633 ms (Beats 85.32%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-23 |
| 💻 Language | MySQL |