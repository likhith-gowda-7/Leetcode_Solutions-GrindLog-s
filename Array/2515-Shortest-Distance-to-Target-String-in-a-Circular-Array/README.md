# 2515. Shortest Distance to Target String in a Circular Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/)


## 📝 Problem Description

You are given a **0-indexed** **circular** string array `words` and a string `target`. A **circular array** means that the array's end connects to the array's beginning.

	- Formally, the next element of `words[i]` is `words[(i + 1) % n]` and the previous element of `words[i]` is `words[(i - 1 + n) % n]`, where `n` is the length of `words`.

Starting from `startIndex`, you can move to either the next word or the previous word with `1` step at a time.

Return *the **shortest** distance needed to reach the string* `target`. If the string `target` does not exist in `words`, return `-1`.

 

Example 1:**

```

**Input:** words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
**Output:** 1
**Explanation:** We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.

```

Example 2:**

```

**Input:** words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
**Output:** 1
**Explanation:** We start from index 0 and can reach "leetcode" by
- moving 2 units to the right to reach index 2.
- moving 1 unit to the left to reach index 2.
The shortest distance to reach "leetcode" is 1.
```

Example 3:**

```

**Input:** words = ["i","eat","leetcode"], target = "ate", startIndex = 0
**Output:** -1
**Explanation:** Since "ate" does not exist in `words`, we return -1.

```

 

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 100`

	- `words[i]` and `target` consist of only lowercase English letters.

	- `0 <= startIndex < words.length`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a two-pointer approach to traverse the circular array from both the start and end directions simultaneously. This allows for efficient exploration of the array, taking advantage of the circular nature of the problem.

**Approach**
1. First, check if the target string exists in the array. If not, return -1.
2. Initialize two pointers, `back` and `front`, to the start index. `back` moves in the reverse direction, while `front` moves in the forward direction.
3. Initialize a counter `c` to keep track of the number of steps taken.
4. Continue moving `back` and `front` until either of them reaches the target string.
5. Return the total number of steps taken, which represents the shortest distance to the target string.

**Time Complexity**
O(n), where n is the length of the array. This is because in the worst case, we might need to traverse the entire array to find the target string.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointers and the counter.

**Key Insight**
The key insight here is that by using two pointers moving in opposite directions, we can efficiently explore the circular array and find the shortest distance to the target string. This approach takes advantage of the fact that the array is circular, allowing us to cover the entire array in a single pass.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 98.7%) |
| 📅 Solved | 2026-04-16 |
| 💻 Language | Python |