> 📌 **Cross-listed:** Primary location is [Array/2029-Stone-Game-IX](../../Array/2029-Stone-Game-IX). This problem also appears under: **Array**, **Math**, **Greedy**, **Minimax**, **Counting**, **Game Theory**, **Nim Game**, **Zero-Sum Game**

# 2029. Stone Game IX


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Minimax](https://img.shields.io/badge/Minimax-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/stone-game-ix/)


## 📝 Problem Description

Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array `stones`, where `stones[i]` is the **value** of the `i^th` stone.

Alice and Bob take turns, with **Alice** starting first. On each turn, the player may remove any stone from `stones`. The player who removes a stone **loses** if the **sum** of the values of **all removed stones** is divisible by `3`. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play **optimally**, return `true` *if Alice wins and* `false` *if Bob wins*.

 

Example 1:**

```

**Input:** stones = [2,1]
**Output:** true
**Explanation:** The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.

```

Example 2:**

```

**Input:** stones = [2]
**Output:** false
**Explanation:** Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.

```

Example 3:**

```

**Input:** stones = [5,1,2,4,3]
**Output:** false
**Explanation:** Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.

```

 

**Constraints:**

	- `1 <= stones.length <= 10^5`

	- `1 <= stones[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**  
Only the residue of each stone modulo 3 matters.  
Removing a stone that is 0 (mod 3) never changes the total sum modulo 3, so its only effect is to flip the parity of the number of such stones.  
Stones that are 1 (mod 3) and 2 (mod 3) can cancel each other out; the game boils down to how many of each type remain.

**Approach**  
1. Count how many stones give remainder 0, 1, 2 when divided by 3 → `f[0]`, `f[1]`, `f[2]`.  
2. If the number of 0‑mod 3 stones is **even** (Alice can avoid losing immediately), Alice wins iff there is at least one stone of each of the other two types: `min(f[1], f[2]) ≥ 1`.  
3. If the number of 0‑mod 3 stones is **odd**, Alice must rely on the imbalance between 1‑mod 3 and 2‑mod 3 stones. She wins iff the absolute difference `|f[1] – f[2]|` is at least 3.  
4. Return the corresponding boolean.

**Time Complexity**  
`O(n)` – one pass over the array to count residues.

**Space Complexity**  
`O(1)` – only three integer counters are stored.

**Key Insight**  
The game reduces to the parity of 0‑mod 3 stones and the difference between counts of 1‑mod 3 and 2‑mod 3 stones; once these are known, optimal play is determined by the simple rules above.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 53 ms (Beats 49.63%) |
| 💾 Memory | 30.6 MB (Beats 43.7%) |
| 📅 Solved | 2026-08-16 |
| 💻 Language | Python |