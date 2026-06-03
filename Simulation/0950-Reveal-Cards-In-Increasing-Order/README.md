> 📌 **Cross-listed:** Primary location is [Array/0950-Reveal-Cards-In-Increasing-Order](../../Array/0950-Reveal-Cards-In-Increasing-Order). This problem also appears under: **Array**, **Queue**, **Sorting**, **Simulation**

# 950. Reveal Cards In Increasing Order


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reveal-cards-in-increasing-order/)


## 📝 Problem Description

You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The integer on the `i^th` card is `deck[i]`.

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

	- Take the top card of the deck, reveal it, and take it out of the deck.

	- If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.

	- If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Return *an ordering of the deck that would reveal the cards in increasing order*.

**Note** that the first entry in the answer is considered to be the top of the deck.

 

Example 1:**

```

**Input:** deck = [17,13,11,2,3,5,7]
**Output:** [2,13,3,11,5,17,7]
**Explanation:** 
We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.

```

Example 2:**

```

**Input:** deck = [1,1000]
**Output:** [1,1000]

```

 

**Constraints:**

	- `1 <= deck.length <= 1000`

	- `1 <= deck[i] <= 10^6`

	- All the values of `deck` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The problem requires us to simulate the process of revealing cards in increasing order. We can achieve this by maintaining a queue of indices and popping elements from the queue to place them in the result array in the correct order. The key insight is to use a deque to efficiently remove and insert elements at the front and back of the queue.

**Approach**
1. Sort the deck in ascending order.
2. Initialize a queue `dq` with indices from 0 to `n-1`, where `n` is the length of the deck.
3. Initialize a result array `q` of size `n` with all elements set to 0.
4. Iterate through the sorted deck. For each card value `val`:
   1. Dequeue an index `i` from the front of `dq`.
   2. Place the card value `val` at the index `i` in the result array `q`.
   3. If there are still elements in `dq`, dequeue another index and append it to the back of `dq` to maintain the correct order.

**Time Complexity**
The time complexity is O(n log n) due to the sorting operation, where n is the length of the deck. The subsequent deque operations take O(n) time, but this is dominated by the sorting time.

**Space Complexity**
The space complexity is O(n) for the result array `q` and the deque `dq`, both of which require additional space proportional to the length of the deck.

**Key Insight**
The key insight is to use a deque to maintain the correct order of indices, allowing us to efficiently remove and insert elements at the front and back of the queue. This approach enables us to simulate the process of revealing cards in increasing order in a efficient and elegant manner.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-25 |
| 💻 Language | Python |