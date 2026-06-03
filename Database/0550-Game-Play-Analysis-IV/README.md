# 550. Game Play Analysis IV


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/game-play-analysis-iv/)


## 📝 Problem Description

Table: `Activity`

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

```

 

Write a solution to report the **fraction** of players that logged in again on the day after the day they first logged in, **rounded to 2 decimal places**. In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
**Output:** 
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
**Explanation:** 
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a common technique in SQL known as a "Common Table Expression" (CTE) to first identify the first login date for each player. Then, it joins this CTE with the original table to find the number of players who logged in again the day after their first login.

**Approach**
1. Create a CTE `User_logins` that groups the `Activity` table by `player_id` and selects the minimum `event_date` for each player, which represents their first login date.
2. Join the `User_logins` CTE with the `Activity` table on `player_id` and `event_date` (with a 1-day interval) to find the players who logged in again the day after their first login.
3. Count the number of players who logged in again and divide it by the total number of players to get the fraction.
4. Round the fraction to 2 decimal places using the `round` function.

**Time Complexity**
O(n log n) due to the grouping operation in the CTE, where n is the number of rows in the `Activity` table. However, this can be optimized to O(n) by using a single pass through the table.

**Space Complexity**
O(n) for storing the intermediate results in the CTE.

**Key Insight**
The key insight is to use a CTE to efficiently identify the first login date for each player, which allows us to join the original table and find the players who logged in again the day after their first login. This approach avoids the need for a self-join or a subquery, making it more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 534 ms (Beats 85.48%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-24 |
| 💻 Language | MySQL |