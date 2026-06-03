# 197. Rising Temperature


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rising-temperature/)


## 📝 Problem Description

Table: `Weather`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.

```

 

Write a solution to find all dates' `id` with higher temperatures compared to its previous dates (yesterday).

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
**Output:** 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
**Explanation:** 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a self-join to compare each row with its previous row, checking if the temperature is higher. This approach works because the `datediff` function can be used to find the difference between two dates, allowing us to identify the previous row.

**Approach**
1. Perform a self-join on the `Weather` table, joining each row with itself.
2. Use the `datediff` function to find the difference between the `recordDate` of the two joined rows.
3. Filter the results to include only rows where the date difference is 1 (i.e., the current row is the next day).
4. Select the `id` column from the current row (`w1`) where the temperature is higher than the temperature of the previous row (`w2`).

**Time Complexity**
O(n^2) due to the self-join, where n is the number of rows in the `Weather` table. This is because for each row, we are joining it with every other row.

**Space Complexity**
O(n) for the temporary result set created by the join operation.

**Key Insight**
The key insight is recognizing that a self-join can be used to compare each row with its previous row, allowing us to efficiently identify dates with higher temperatures. This approach is particularly useful when dealing with time-series data like the `Weather` table.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 453 ms (Beats 74.12%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-16 |
| 💻 Language | MySQL |