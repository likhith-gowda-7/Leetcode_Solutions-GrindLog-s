# 1729. Find Followers Count


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-followers-count/)


## 📝 Problem Description

Table: `Followers`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
This table contains the IDs of a user and a follower in a social media app where the follower follows the user.
```

 

Write a solution that will, for each user, return the number of followers.

Return the result table ordered by `user_id` in ascending order.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Followers table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+
**Output:** 
+---------+----------------+
| user_id | followers_count|
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+
**Explanation:** 
The followers of 0 are {1}
The followers of 1 are {0}
The followers of 2 are {0,1}

```

## 🧠 Solution Explanation

**Intuition**
This solution works by grouping the followers table by the user_id column, then counting the number of rows in each group. This effectively gives us the number of followers for each user.

**Approach**
1. The SQL query selects the user_id column and uses the count(*) function to count the number of rows in each group.
2. The group by clause is used to group the rows by the user_id column.
3. The order by clause is used to sort the result table by user_id in ascending order.

**Time Complexity**
O(n), where n is the number of rows in the Followers table. This is because the query needs to iterate over each row in the table to count the number of followers for each user.

**Space Complexity**
O(n), where n is the number of unique user_id values in the Followers table. This is because the query needs to store the count of followers for each user in the result table.

**Key Insight**
The key insight here is that grouping by the user_id column allows us to count the number of rows in each group, which corresponds to the number of followers for each user. This is a simple yet effective approach to solving the problem, and it takes advantage of the fact that the table is already grouped by the user_id column.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 505 ms (Beats 94.32%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-25 |
| 💻 Language | MySQL |