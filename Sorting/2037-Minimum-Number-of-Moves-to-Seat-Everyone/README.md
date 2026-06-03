> 📌 **Cross-listed:** Primary location is [Array/2037-Minimum-Number-of-Moves-to-Seat-Everyone](../../Array/2037-Minimum-Number-of-Moves-to-Seat-Everyone). This problem also appears under: **Array**, **Greedy**, **Sorting**, **Counting Sort**

# 2037. Minimum Number of Moves to Seat Everyone


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Counting Sort](https://img.shields.io/badge/Counting%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/)


## 📝 Problem Description

There are `n` **availabe **seats and `n` students **standing** in a room. You are given an array `seats` of length `n`, where `seats[i]` is the position of the `i^th` seat. You are also given the array `students` of length `n`, where `students[j]` is the position of the `j^th` student.

You may perform the following move any number of times:

	- Increase or decrease the position of the `i^th` student by `1` (i.e., moving the `i^th` student from position `x` to `x + 1` or `x - 1`)

Return *the **minimum number of moves** required to move each student to a seat** such that no two students are in the same seat.*

Note that there may be **multiple** seats or students in the **same **position at the beginning.

 

Example 1:**

```

**Input:** seats = [3,1,5], students = [2,7,4]
**Output:** 4
**Explanation:** The students are moved as follows:
- The first student is moved from position 2 to position 1 using 1 move.
- The second student is moved from position 7 to position 5 using 2 moves.
- The third student is moved from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.

```

Example 2:**

```

**Input:** seats = [4,1,5,9], students = [1,3,2,6]
**Output:** 7
**Explanation:** The students are moved as follows:
- The first student is not moved.
- The second student is moved from position 3 to position 4 using 1 move.
- The third student is moved from position 2 to position 5 using 3 moves.
- The fourth student is moved from position 6 to position 9 using 3 moves.
In total, 0 + 1 + 3 + 3 = 7 moves were used.

```

Example 3:**

```

**Input:** seats = [2,2,6,6], students = [1,3,2,6]
**Output:** 4
**Explanation:** Note that there are two seats at position 2 and two seats at position 6.
The students are moved as follows:
- The first student is moved from position 1 to position 2 using 1 move.
- The second student is moved from position 3 to position 6 using 3 moves.
- The third student is not moved.
- The fourth student is not moved.
In total, 1 + 3 + 0 + 0 = 4 moves were used.

```

 

**Constraints:**

	- `n == seats.length == students.length`

	- `1 <= n <= 100`

	- `1 <= seats[i], students[j] <= 100`

## 🧠 Solution Explanation

**Intuition**
The approach to this problem is to pair each seat with the closest student, minimizing the total number of moves required. This is a classic greedy algorithm problem, where the optimal solution can be found by making the locally optimal choice at each step.

**Approach**
1. Sort the `seats` array in ascending order.
2. Sort the `students` array in ascending order.
3. Initialize a variable `mini` to store the total number of moves.
4. Iterate through the sorted `seats` and `students` arrays simultaneously using a for loop.
5. For each pair of seat and student, calculate the absolute difference between their positions using the `abs` function.
6. Add the absolute difference to the `mini` variable.
7. Return the total number of moves stored in `mini`.

**Time Complexity**
O(n log n) due to the sorting of the `seats` and `students` arrays, where n is the number of seats or students.

**Space Complexity**
O(1) excluding the input arrays, as only a constant amount of space is used to store the `mini` variable and the loop indices.

**Key Insight**
The key insight to this problem is that by pairing each seat with the closest student, we are effectively minimizing the total number of moves required. This is because the absolute difference between the positions of each pair represents the minimum number of moves needed to seat the student. By sorting the arrays and iterating through them simultaneously, we can find the optimal solution efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-15 |
| 💻 Language | Python |