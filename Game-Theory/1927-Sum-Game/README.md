> 📌 **Cross-listed:** Primary location is [Math/1927-Sum-Game](../../Math/1927-Sum-Game). This problem also appears under: **Math**, **String**, **Greedy**, **Game Theory**

# 1927. Sum Game


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Game Theory](https://img.shields.io/badge/Game%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-game/)


## 📝 Problem Description

Alice and Bob take turns playing a game, with **Alice**** starting first**.

You are given a string `num` of **even length** consisting of digits and `'?'` characters. On each turn, a player will do the following if there is still at least one `'?'` in `num`:

	- Choose an index `i` where `num[i] == '?'`.

	- Replace `num[i]` with any digit between `'0'` and `'9'`.

The game ends when there are no more `'?'` characters in `num`.

For Bob to win, the sum of the digits in the first half of `num` must be **equal** to the sum of the digits in the second half. For Alice to win, the sums must **not be equal**.

	- For example, if the game ended with `num = "243801"`, then Bob wins because `2+4+3 = 8+0+1`. If the game ended with `num = "243803"`, then Alice wins because `2+4+3 != 8+0+3`.

Assuming Alice and Bob play **optimally**, return `true` *if Alice will win and *`false` *if Bob will win*.

 

Example 1:**

```

**Input:** num = "5023"
**Output:** false
**Explanation:** There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.

```

Example 2:**

```

**Input:** num = "25??"
**Output:** true
**Explanation: **Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.

```

Example 3:**

```

**Input:** num = "?3295???"
**Output:** false
**Explanation:** It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first '?' with '9'. num = "93295???".
- Bob replaces one of the '?' in the right half with '9'. num = "932959??".
- Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
- Bob replaces the last '?' in the right half with '7'. num = "93295927".
Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.

```

 

**Constraints:**

	- `2 <= num.length <= 10^5`

	- `num.length` is **even**.

	- `num` consists of only digits and `'?'`.

## 🧠 Solution Explanation

**Intuition**  
The game is a two‑player zero‑sum game where each move only changes the sum of one half. If the total number of blanks is odd, Alice can always force a win by making the two halves unequal. When the blanks are even, the outcome depends on the difference between the current sums and how many blanks remain on each side.

**Approach**  
1. Scan the string once, computing  
   - `sumL`, `sumR`: sums of known digits in the left/right halves.  
   - `qL`, `qR`: counts of `'?'` in each half.  
2. If no blanks (`qL+qR==0`), Bob wins iff the sums differ.  
3. If the total blanks is odd, Alice can always win → return `True`.  
4. If blanks are even:  
   - If `qL == qR`, the game is symmetric; Bob wins iff the current sums differ.  
   - Otherwise, let `d = sumL - sumR` and `k = qR - qL`.  
     Each pair of moves can change `d` by at most 9 (placing 9 on the side with fewer blanks).  
     Bob can force equality iff `2*d == 9*k`; otherwise Alice wins.  
5. Return the result of the last condition.

**Time Complexity**  
`O(n)` – a single pass over the string of length `n`.

**Space Complexity**  
`O(1)` – only a few integer counters are used.

**Key Insight**  
When the number of blanks is even, the game reduces to whether the current sum difference can be balanced by the remaining blanks. The critical equation `2*(sumL - sumR) == 9*(qR - qL)` captures exactly when Bob can force equality; otherwise Alice can always keep the sums unequal.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 78 ms (Beats 18.24%) |
| 💾 Memory | 19.8 MB (Beats 65.29%) |
| 📅 Solved | 2026-08-23 |
| 💻 Language | Python |