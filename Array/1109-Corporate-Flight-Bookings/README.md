# 1109. Corporate Flight Bookings


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/corporate-flight-bookings/)


## 📝 Problem Description

There are `n` flights that are labeled from `1` to `n`.

You are given an array of flight bookings `bookings`, where `bookings[i] = [first_i, last_i, seats_i]` represents a booking for flights `first_i` through `last_i` (**inclusive**) with `seats_i` seats reserved for **each flight** in the range.

Return *an array *`answer`* of length *`n`*, where *`answer[i]`* is the total number of seats reserved for flight *`i`.

 

Example 1:**

```

**Input:** bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
**Output:** [10,55,45,25,25]
**Explanation:**
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

```

Example 2:**

```

**Input:** bookings = [[1,2,10],[2,2,15]], n = 2
**Output:** [10,25]
**Explanation:**
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]

```

 

**Constraints:**

	- `1 <= n <= 2 * 10^4`

	- `1 <= bookings.length <= 2 * 10^4`

	- `bookings[i].length == 3`

	- `1 <= first_i <= last_i <= n`

	- `1 <= seats_i <= 10^4`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 22 ms (Beats 81.5%) |
| 💾 Memory | 28.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-13 |
| 💻 Language | Python |