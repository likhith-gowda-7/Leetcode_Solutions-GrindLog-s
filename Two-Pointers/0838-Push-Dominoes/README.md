# 838. Push Dominoes


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/push-dominoes/)


## 📝 Problem Description

There are `n` dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string `dominoes` representing the initial state where:

	- `dominoes[i] = 'L'`, if the `i^th` domino has been pushed to the left,

	- `dominoes[i] = 'R'`, if the `i^th` domino has been pushed to the right, and

	- `dominoes[i] = '.'`, if the `i^th` domino has not been pushed.

Return *a string representing the final state*.

 

Example 1:**

```

**Input:** dominoes = "RR.L"
**Output:** "RR.L"
**Explanation:** The first domino expends no additional force on the second domino.

```

Example 2:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png)
```

**Input:** dominoes = ".L.R...LR..L.."
**Output:** "LL.RR.LLRRLL.."

```

 

**Constraints:**

	- `n == dominoes.length`

	- `1 <= n <= 10^5`

	- `dominoes[i]` is either `'L'`, `'R'`, or `'.'`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a queue to simulate the domino effect, where each domino's state (L, R, or .) is updated based on the adjacent dominoes. The key insight is that a domino will stay still if it has dominoes falling on it from both sides, so we only need to consider the dominoes that are not yet balanced.

**Approach**
1. Convert the input string into a list of characters and create a queue to store the dominoes that need to be updated.
2. Iterate through the list and add the dominoes that are not yet balanced (i.e., L, R) to the queue along with their indices.
3. While the queue is not empty, pop the next domino from the queue and check its adjacent dominoes.
4. If the current domino is falling to the right (R) and the next domino is still standing (.), update the next domino to R and add it to the queue.
5. If the current domino is falling to the left (L) and the previous domino is still standing (.), update the previous domino to L and add it to the queue.
6. Repeat steps 3-5 until the queue is empty.
7. Join the updated list of dominoes back into a string and return the result.

**Time Complexity**
O(n), where n is the length of the input string. This is because we iterate through the list of dominoes once and perform a constant amount of work for each domino.

**Space Complexity**
O(n), where n is the length of the input string. This is because we store the dominoes that need to be updated in a queue, which can grow up to the size of the input string in the worst case.

**Key Insight**
The key insight is that we only need to consider the dominoes that are not yet balanced, and we can update their states based on the adjacent dominoes. This allows us to avoid considering all possible combinations of dominoes and reduces the time complexity to O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 163 ms (Beats 59.35%) |
| 💾 Memory | 25.7 MB (Beats 39.63%) |
| 📅 Solved | 2025-05-02 |
| 💻 Language | Python |