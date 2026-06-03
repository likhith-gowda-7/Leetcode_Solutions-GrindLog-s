# 1204. Last Person to Fit in the Bus


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/last-person-to-fit-in-the-bus/)


## 📝 Problem Description

Table: `Queue`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id column contains unique values.
This table has the information about all people waiting for a bus.
The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
weight is the weight of the person in kilograms.

```

 

There is a queue of people waiting to board a bus. However, the bus has a weight limit of `1000`** kilograms**, so there may be some people who cannot board.

Write a solution to find the `person_name` of the **last person** that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.

**Note** that *only one* person can board the bus at any given turn.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Queue table:
+-----------+-------------+--------+------+
| person_id | person_name | weight | turn |
+-----------+-------------+--------+------+
| 5         | Alice       | 250    | 1    |
| 4         | Bob         | 175    | 5    |
| 3         | Alex        | 350    | 2    |
| 6         | John Cena   | 400    | 3    |
| 1         | Winston     | 500    | 6    |
| 2         | Marie       | 200    | 4    |
+-----------+-------------+--------+------+
**Output:** 
+-------------+
| person_name |
+-------------+
| John Cena   |
+-------------+
**Explanation:** The folowing table is ordered by the turn for simplicity.
+------+----+-----------+--------+--------------+
| Turn | ID | Name      | Weight | Total Weight |
+------+----+-----------+--------+--------------+
| 1    | 5  | Alice     | 250    | 250          |
| 2    | 3  | Alex      | 350    | 600          |
| 3    | 6  | John Cena | 400    | 1000         | (last person to board)
| 4    | 2  | Marie     | 200    | 1200         | (cannot board)
| 5    | 4  | Bob       | 175    | ___          |
| 6    | 1  | Winston   | 500    | ___          |
+------+----+-----------+--------+--------------+

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a common technique in SQL, known as window functions, to calculate the cumulative sum of weights for each person as they board the bus. This allows us to determine which person is the last one to fit on the bus without exceeding the weight limit.

**Approach**
1. Create a temporary result set `person_sum` that contains the person's name and the cumulative sum of weights as they board the bus, ordered by turn.
2. Use the `sum` window function with the `order by` clause to calculate the cumulative sum.
3. Select the person's name from `person_sum` where the cumulative sum is less than or equal to the weight limit (1000 kg).
4. Order the results by the cumulative sum in descending order and limit the output to the first row.

**Time Complexity**
O(n), where n is the number of rows in the table. This is because we are scanning the table once to calculate the cumulative sum.

**Space Complexity**
O(n), where n is the number of rows in the table. This is because we are creating a temporary result set `person_sum` that contains all the rows from the original table.

**Key Insight**
The key insight here is that we can use window functions to efficiently calculate the cumulative sum of weights, which allows us to determine which person is the last one to fit on the bus without having to iterate through all possible combinations of people. This makes the solution much more efficient than a brute-force approach.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 737 ms (Beats 93.29%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-30 |
| 💻 Language | MySQL |