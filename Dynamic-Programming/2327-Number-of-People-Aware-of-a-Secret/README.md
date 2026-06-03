# 2327. Number of People Aware of a Secret


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-people-aware-of-a-secret/)


## 📝 Problem Description

On day `1`, one person discovers a secret.

You are given an integer `delay`, which means that each person will **share** the secret with a new person **every day**, starting from `delay` days after discovering the secret. You are also given an integer `forget`, which means that each person will **forget** the secret `forget` days after discovering it. A person **cannot** share the secret on the same day they forgot it, or on any day afterwards.

Given an integer `n`, return* the number of people who know the secret at the end of day *`n`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

 

Example 1:**

```

**Input:** n = 6, delay = 2, forget = 4
**Output:** 5
**Explanation:**
Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)

```

Example 2:**

```

**Input:** n = 4, delay = 1, forget = 3
**Output:** 6
**Explanation:**
Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)

```

 

**Constraints:**

	- `2 <= n <= 1000`

	- `1 <= delay < forget <= n`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved by simulating the process of people discovering and forgetting the secret. We maintain a dynamic programming array `dp` where `dp[i]` represents the number of people who know the secret at the end of day `i`. We also keep track of the number of active sharers, which is the number of people who know the secret and can share it on the current day.

**Approach**
1. Initialize a dynamic programming array `dp` of size `n+1` with all elements set to 0, except `dp[1]` which is set to 1 (since one person discovers the secret on day 1).
2. Initialize `active_sharers` to 0, which represents the number of people who know the secret and can share it on the current day.
3. Iterate from day 2 to `n` (inclusive):
   1. If `day - delay` is greater than 0, add the number of people who knew the secret `delay` days ago to `active_sharers` (since they can share it now).
   2. If `day - forget` is greater than 0, subtract the number of people who forgot the secret `forget` days ago from `active_sharers` (since they cannot share it now).
   3. Update `dp[day]` with the current value of `active_sharers`.
4. Calculate the total number of people who know the secret at the end of day `n` by summing up the values of `dp` from `(n-forget)+1` to `n` (inclusive) and taking the result modulo `10^9 + 7`.

**Time Complexity**
O(n), where n is the number of days. This is because we iterate from day 2 to `n` (inclusive) once.

**Space Complexity**
O(n), where n is the number of days. This is because we use a dynamic programming array of size `n+1` to store the number of people who know the secret at the end of each day.

**Key Insight**
The key insight is to maintain the number of active sharers, which is the number of people who know the secret and can share it on the current day. By simulating the process of people discovering and forgetting the secret, we can efficiently calculate the total number of people who know the secret at the end of day `n`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 89.22%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-09-09 |
| 💻 Language | Python |