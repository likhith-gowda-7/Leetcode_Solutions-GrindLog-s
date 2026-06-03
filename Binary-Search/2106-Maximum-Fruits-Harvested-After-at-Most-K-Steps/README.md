> 📌 **Cross-listed:** Primary location is [Array/2106-Maximum-Fruits-Harvested-After-at-Most-K-Steps](../../Array/2106-Maximum-Fruits-Harvested-After-at-Most-K-Steps). This problem also appears under: **Array**, **Binary Search**, **Sliding Window**, **Prefix Sum**

# 2106. Maximum Fruits Harvested After at Most K Steps


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/)


## 📝 Problem Description

Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array `fruits` where `fruits[i] = [position_i, amount_i]` depicts `amount_i` fruits at the position `position_i`. `fruits` is already **sorted** by `position_i` in **ascending order**, and each `position_i` is **unique**.

You are also given an integer `startPos` and an integer `k`. Initially, you are at the position `startPos`. From any position, you can either walk to the **left or right**. It takes **one step** to move **one unit** on the x-axis, and you can walk **at most** `k` steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.

Return *the **maximum total number** of fruits you can harvest*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/11/21/1.png)
```

**Input:** fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
**Output:** 9
**Explanation:** 
The optimal way is to:
- Move right to position 6 and harvest 3 fruits
- Move right to position 8 and harvest 6 fruits
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/11/21/2.png)
```

**Input:** fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
**Output:** 14
**Explanation:** 
You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
The optimal way is to:
- Harvest the 7 fruits at the starting position 5
- Move left to position 4 and harvest 1 fruit
- Move right to position 6 and harvest 2 fruits
- Move right to position 7 and harvest 4 fruits
You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/11/21/3.png)
```

**Input:** fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
**Output:** 0
**Explanation:**
You can move at most k = 2 steps and cannot reach any position with fruits.

```

 

**Constraints:**

	- `1 <= fruits.length <= 10^5`

	- `fruits[i].length == 2`

	- `0 <= startPos, position_i <= 2 * 10^5`

	- `position_i-1 < position_i` for any `i > 0` (**0-indexed**)

	- `1 <= amount_i <= 10^4`

	- `0 <= k <= 2 * 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with a twist. It maintains a window of fruits that can be harvested within the given steps `k`. The window is expanded to the right and shrunk from the left based on the minimum steps required to reach the rightmost fruit in the window from the start position.

**Approach**
1. Initialize variables to keep track of the current total fruits, left and right pointers, and the maximum count of fruits harvested.
2. Iterate over the fruits array from left to right.
3. For each right pointer, calculate the total fruits in the current window by adding the fruits at the right position and subtracting the fruits that are out of the window.
4. While the left pointer is within the window, calculate the minimum steps required to reach the rightmost fruit from the start position.
5. If the minimum steps are within the given steps `k`, break the loop; otherwise, shrink the window by moving the left pointer to the right.
6. Update the maximum count of fruits harvested if the current total fruits is greater.
7. Return the maximum count of fruits harvested.

**Time Complexity**
O(n * log n), where n is the number of fruits. The while loop inside the for loop has a time complexity of O(log n) due to the binary search-like behavior of the minimum steps calculation.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the variables.

**Key Insight**
The key insight is to maintain a window of fruits that can be harvested within the given steps `k`. By expanding the window to the right and shrinking it from the left, we can efficiently calculate the maximum total number of fruits that can be harvested. The minimum steps calculation is the crucial part that allows us to determine when to expand or shrink the window.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 136 ms (Beats 37.5%) |
| 💾 Memory | 52.4 MB (Beats 100%) |
| 📅 Solved | 2025-08-03 |
| 💻 Language | Python |