# 2878. Get the Size of a DataFrame


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-pythondata-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/get-the-size-of-a-dataframe/)


## 📝 Problem Description

```

DataFrame `players:`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+

```

Write a solution to calculate and display the **number of rows and columns** of `players`.

Return the result as an array:

`[number of rows, number of columns]`

The result format is in the following example.

 

Example 1:**

```

**Input:
**+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+**
Output:
**[10, 5]
**Explanation:**
This DataFrame contains 10 rows and 5 columns.

```

## 🧠 Solution Explanation

**Intuition**
The solution leverages the built-in `shape` attribute of pandas DataFrames, which returns a tuple containing the number of rows and columns in the DataFrame. This attribute is specifically designed to provide the size of a DataFrame, making it an efficient and straightforward approach.

**Approach**
1. Import the necessary pandas library to work with DataFrames.
2. Define a function `getDataframeSize` that takes a DataFrame `players` as input.
3. Use the `shape` attribute of the DataFrame to retrieve the number of rows and columns as a tuple.
4. Unpack the tuple into two separate variables `rows` and `column`.
5. Return the size of the DataFrame as a list containing the number of rows and columns.

**Time Complexity**
O(1) - The `shape` attribute directly returns the size of the DataFrame without requiring any additional operations or iterations, making it a constant-time operation.

**Space Complexity**
O(1) - The solution only requires a constant amount of space to store the result, which is a list containing two integers.

**Key Insight**
The key insight is recognizing the `shape` attribute as a built-in property of pandas DataFrames, which provides a direct and efficient way to retrieve the size of a DataFrame. This attribute eliminates the need for manual counting or iteration, making the solution concise and scalable.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 273 ms (Beats 61.12%) |
| 💾 Memory | 66.6 MB (Beats 12.92%) |
| 📅 Solved | 2025-06-10 |
| 💻 Language | pythondata |