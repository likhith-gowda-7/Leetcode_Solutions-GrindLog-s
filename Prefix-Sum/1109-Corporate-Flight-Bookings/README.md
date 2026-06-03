> 📌 **Cross-listed:** Primary location is [Array/1109-Corporate-Flight-Bookings](../../Array/1109-Corporate-Flight-Bookings). This problem also appears under: **Array**, **Prefix Sum**

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

## 🧠 Solution Explanation

**Intuition**
The solution uses a technique called "prefix sum" to efficiently calculate the total number of seats reserved for each flight. By maintaining a running sum of the seats reserved for each flight, we can easily calculate the total seats reserved for any given flight.

**Approach**
1. Initialize an array `seats` of size `n+1` with all elements set to 0. This array will store the total number of seats reserved for each flight.
2. Iterate through each booking in the `bookings` array. For each booking, add the number of seats reserved to the `seats` array at the index corresponding to the first flight in the booking, and subtract the number of seats reserved from the `seats` array at the index corresponding to the last flight in the booking.
3. Iterate through the `seats` array, starting from the second element. For each element, add the value of the previous element to it. This effectively calculates the running sum of the seats reserved for each flight.
4. Return all elements of the `seats` array except the last one, which represents the total number of seats reserved for the `n+1`-th flight (which is out of bounds).

**Time Complexity**
O(n + m), where n is the number of flights and m is the number of bookings. The first loop iterates through each booking, and the second loop iterates through the `seats` array, which has a size of n+1.

**Space Complexity**
O(n), where n is the number of flights. The `seats` array has a size of n+1, which is the dominant space complexity term.

**Key Insight**
The key insight behind this solution is that by maintaining a running sum of the seats reserved for each flight, we can efficiently calculate the total seats reserved for any given flight. This is achieved by adding and subtracting the number of seats reserved for each booking from the corresponding indices in the `seats` array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 22 ms (Beats 81.57%) |
| 💾 Memory | 28.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-13 |
| 💻 Language | Python |