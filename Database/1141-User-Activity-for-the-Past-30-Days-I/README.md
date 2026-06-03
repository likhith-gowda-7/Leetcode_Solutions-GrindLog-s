# 1141. User Activity for the Past 30 Days I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/)


## 📝 Problem Description

Table: `Activity`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
This table may have duplicate rows.
The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website. 
Note that each session belongs to exactly one user.

```

 

Write a solution to find the daily active user count for a period of `30` days ending `2019-07-27` inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in **any order**.

The result format is in the following example.

Note: **Any** activity from (`'open_session'`, `'end_session'`, `'scroll_down'`, `'send_message'`) will be considered valid activity for a user to be considered active on a day.

 

Example 1:**

```

**Input:** 
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+
**Output:** 
+------------+--------------+ 
| day        | active_users |
+------------+--------------+ 
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+ 
**Explanation:** Note that we do not care about days with zero active users.

```

## 🧠 Solution Explanation

**Intuition**
The solution works by grouping the activities by date and counting the distinct users for each day. This approach is effective because it directly addresses the problem's requirement of finding the daily active user count.

**Approach**
1. The query selects the `activity_date` as the day and counts the distinct `user_id` for each day.
2. The `group by` clause groups the activities by date.
3. The `having` clause filters the results to include only the days between '2019-06-28' and '2019-07-28'.

**Time Complexity**
O(n), where n is the number of activities. This is because the query needs to iterate over all activities to group them by date and count the distinct users.

**Space Complexity**
O(n), where n is the number of unique days. This is because the query needs to store the count of distinct users for each day in the result set.

**Key Insight**
The key insight here is that we can directly count the distinct users for each day by grouping the activities by date. This approach avoids the need to iterate over all users and dates, making it efficient for large datasets.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 444 ms (Beats 97.78%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |