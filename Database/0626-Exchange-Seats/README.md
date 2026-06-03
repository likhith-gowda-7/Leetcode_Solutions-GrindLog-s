# 626. Exchange Seats


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/exchange-seats/)


## 📝 Problem Description

Table: `Seat`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.

```

 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by `id` **in ascending order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
**Output:** 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
**Explanation:** 
Note that if the number of students is odd, there is no need to change the last one's seat.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of mathematical operations and SQL features to swap the seat IDs of every two consecutive students. The key insight is to use the modulo operator to identify even and odd IDs, and then adjust the ID accordingly.

**Approach**
1. The `mod(id, 2) = 0` condition checks if the ID is even, and if so, subtracts 1 from it to swap the ID with the previous one.
2. The `id = count(*) over ()` condition checks if the ID is the last one, and if so, leaves it unchanged since the last student's ID is not swapped.
3. The `else id + 1` condition checks if the ID is odd, and if so, adds 1 to it to swap the ID with the next one.
4. The `from Seat` clause selects the data from the `Seat` table.
5. The `order by id` clause sorts the result by the adjusted ID in ascending order.

**Time Complexity**
O(n), where n is the number of students, since we are scanning the table once.

**Space Complexity**
O(1), since we are not using any additional space that scales with the input size.

**Key Insight**
The key insight is to use the modulo operator to identify even and odd IDs, and then adjust the ID accordingly. This approach allows us to swap the IDs of every two consecutive students in a single pass through the table.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 371 ms (Beats 33.42%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-02-09 |
| 💻 Language | MySQL |