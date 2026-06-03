> 📌 **Cross-listed:** Primary location is [Array/1488-Avoid-Flood-in-The-City](../../Array/1488-Avoid-Flood-in-The-City). This problem also appears under: **Array**, **Hash Table**, **Binary Search**, **Greedy**, **Heap (Priority Queue)**

# 1488. Avoid Flood in The City


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/avoid-flood-in-the-city/)


## 📝 Problem Description

Your country has 10^9 lakes. Initially, all the lakes are empty, but when it rains over the `n^th` lake, the `n^th` lake becomes full of water. If it rains over a lake that is **full of water**, there will be a **flood**. Your goal is to avoid floods in any lake.

Given an integer array `rains` where:

	- `rains[i] > 0` means there will be rains over the `rains[i]` lake.

	- `rains[i] == 0` means there are no rains this day and you **must** choose **one lake** this day and **dry it**.

Return *an array `ans`* where:

	- `ans.length == rains.length`

	- `ans[i] == -1` if `rains[i] > 0`.

	- `ans[i]` is the lake you choose to dry in the `ith` day if `rains[i] == 0`.

If there are multiple valid answers return **any** of them. If it is impossible to avoid flood return **an empty array**.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

 

Example 1:**

```

**Input:** rains = [1,2,3,4]
**Output:** [-1,-1,-1,-1]
**Explanation:** After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

```

Example 2:**

```

**Input:** rains = [1,2,0,0,2,1]
**Output:** [-1,-1,2,1,-1,-1]
**Explanation:** After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

```

Example 3:**

```

**Input:** rains = [1,2,0,1,2]
**Output:** []
**Explanation:** After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

```

 

**Constraints:**

	- `1 <= rains.length <= 10^5`

	- `0 <= rains[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of a hash table, a set, and a min heap to efficiently track the lakes that are full of water and the lakes that are scheduled to rain. By maintaining a min heap of the next lake that will flood, the solution can choose a lake to dry on a given day to avoid a flood.

**Approach**
1. Create a hash table `lakes_to_day` to store the lakes that are scheduled to rain on each day.
2. Initialize a set `full_lakes` to track the lakes that are currently full of water.
3. Initialize a min heap `min_heap` to store the next lake that will flood.
4. Iterate through each day, checking if it's a raining day or a dry day.
   - If it's a raining day, check if the lake is already full. If it is, return an empty array because a flood is unavoidable.
   - If it's a dry day, check if the min heap is not empty. If it's not empty, pop the next lake from the heap and remove it from the `full_lakes` set. Otherwise, choose lake 1 to dry.
5. Return the array `res` which contains the lake to dry on each dry day.

**Time Complexity**
O(n log n) due to the use of a min heap. The heap operations (push and pop) take O(log n) time, and we perform these operations n times.

**Space Complexity**
O(n) for the hash table `lakes_to_day` and the set `full_lakes`. The min heap takes O(n) space in the worst case.

**Key Insight**
The key insight is to use a min heap to efficiently track the next lake that will flood, allowing us to choose a lake to dry on a given day to avoid a flood. This approach ensures that we can avoid floods in any lake.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 187 ms (Beats 96.02%) |
| 💾 Memory | 40.2 MB (Beats 15.91%) |
| 📅 Solved | 2025-10-09 |
| 💻 Language | Python |