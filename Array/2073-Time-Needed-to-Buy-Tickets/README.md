# 2073. Time Needed to Buy Tickets


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/time-needed-to-buy-tickets/)


## 📝 Problem Description

There are `n` people in a line queuing to buy tickets, where the `0^th` person is at the **front** of the line and the `(n - 1)^th` person is at the **back** of the line.

You are given a **0-indexed** integer array `tickets` of length `n` where the number of tickets that the `i^th` person would like to buy is `tickets[i]`.

Each person takes **exactly 1 second** to buy a ticket. A person can only buy **1 ticket at a time** and has to go back to **the end** of the line (which happens **instantaneously**) in order to buy more tickets. If a person does not have any tickets left to buy, the person will **leave **the line.

Return the **time taken** for the person **initially** at position **k**** **(0-indexed) to finish buying tickets.

 

Example 1:**

**Input:** tickets = [2,3,2], k = 2

**Output:** 6

**Explanation:**

	- The queue starts as [2,3,2], where the kth person is underlined.

	- After the person at the front has bought a ticket, the queue becomes [3,2,1] at 1 second.

	- Continuing this process, the queue becomes [2,1,2] at 2 seconds.

	- Continuing this process, the queue becomes [1,2,1] at 3 seconds.

	- Continuing this process, the queue becomes [2,1] at 4 seconds. Note: the person at the front left the queue.

	- Continuing this process, the queue becomes [1,1] at 5 seconds.

	- Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

Example 2:**

**Input:** tickets = [5,1,1,1], k = 0

**Output:** 8

**Explanation:**

	- The queue starts as [5,1,1,1], where the kth person is underlined.

	- After the person at the front has bought a ticket, the queue becomes [1,1,1,4] at 1 second.

	- Continuing this process for 3 seconds, the queue becomes [4] at 4 seconds.

	- Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8.

 

**Constraints:**

	- `n == tickets.length`

	- `1 <= n <= 100`

	- `1 <= tickets[i] <= 100`

	- `0 <= k < n`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved by simulating the process of people buying tickets. We use a queue to represent the line of people, and we keep track of the time taken for each person to buy their tickets. The key insight is that we only need to consider the person at position `k` and the people behind them, as they are the ones who will eventually buy tickets.

**Approach**
1. Initialize a queue with the tickets array and a variable `time_taken` to keep track of the time taken.
2. While the queue is not empty, pop the front person from the queue and increment the `time_taken` by 1.
3. If the person has more than one ticket left, decrement their ticket count and push them back to the end of the queue.
4. If the person has one ticket left and it's the person at position `k`, break the loop as they will finish buying tickets.
5. If the person has no tickets left and it's not the person at position `k`, update the position `k` to be the last person in the queue.
6. Return the `time_taken`.

**Time Complexity**
O(n), where n is the number of people in the line. This is because we make a single pass through the queue, and each operation (popping, pushing, and updating `k`) takes constant time.

**Space Complexity**
O(n), where n is the number of people in the line. This is because we use a queue to store the people in the line, which takes up to n space.

**Key Insight**
The key insight is that we only need to consider the person at position `k` and the people behind them, as they are the ones who will eventually buy tickets. This allows us to simplify the problem and avoid considering the people in front of `k`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 52.37%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-11-21 |
| 💻 Language | Python |