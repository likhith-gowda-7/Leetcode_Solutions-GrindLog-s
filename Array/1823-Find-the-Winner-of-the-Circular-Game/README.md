# 1823. Find the Winner of the Circular Game


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple) ![Queue](https://img.shields.io/badge/Queue-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-winner-of-the-circular-game/)


## 📝 Problem Description

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the `i^th` friend brings you to the `(i+1)^th` friend for `1 <= i < n`, and moving clockwise from the `n^th` friend brings you to the `1^st` friend.

The rules of the game are as follows:

	- **Start** at the `1^st` friend.

	- Count the next `k` friends in the clockwise direction **including** the friend you started at. The counting wraps around the circle and may count some friends more than once.

	- The last friend you counted leaves the circle and loses the game.

	- If there is still more than one friend in the circle, go back to step `2` **starting** from the friend **immediately clockwise** of the friend who just lost and repeat.

	- Else, the last friend in the circle wins the game.

Given the number of friends, `n`, and an integer `k`, return *the winner of the game*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/25/ic234-q2-ex11.png)
```

**Input:** n = 5, k = 2
**Output:** 3
**Explanation:** Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
```

Example 2:**

```

**Input:** n = 6, k = 5
**Output:** 1
**Explanation:** The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

```

 

**Constraints:**

	- `1 <= k <= n <= 500`

 

**Follow up:**

Could you solve this problem in linear time with constant space?

## 🧠 Solution Explanation

**Intuition**
The solution simulates the circular game by maintaining a list of friends in the circle and removing friends based on the given rules. The key insight is to use modular arithmetic to efficiently handle the circular nature of the game.

**Approach**
1. Initialize an empty list `circle` to represent the friends in the circle.
2. Populate the list with friends numbered from 1 to `n` in clockwise order.
3. Initialize a variable `ele` to keep track of the current friend being considered for removal.
4. Subtract 1 from `k` to make the counting start from 0 (for easier modular arithmetic).
5. While there is more than one friend in the circle:
   1. Calculate the index of the friend to be removed using modular arithmetic: `ele = (ele + k) % len(circle)`.
   2. Remove the friend at the calculated index from the circle.
6. Return the index of the last friend remaining in the circle.

**Time Complexity**
O(n) - The while loop iterates at most `n` times, where `n` is the number of friends in the circle.

**Space Complexity**
O(n) - The space complexity is linear due to the use of a list to represent the friends in the circle.

**Key Insight**
The key insight is to use modular arithmetic to efficiently handle the circular nature of the game. By using `(ele + k) % len(circle)`, we can calculate the index of the friend to be removed without worrying about the circular boundary. This allows us to simplify the problem and avoid explicit handling of the circular boundary.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-28 |
| 💻 Language | Python |