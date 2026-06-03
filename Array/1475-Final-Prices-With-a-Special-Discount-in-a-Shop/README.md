# 1475. Final Prices With a Special Discount in a Shop


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)


## 📝 Problem Description

You are given an integer array `prices` where `prices[i]` is the price of the `i^th` item in a shop.

There is a special discount for items in the shop. If you buy the `i^th` item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any discount at all.

Return an integer array `answer` where `answer[i]` is the final price you will pay for the `i^th` item of the shop, considering the special discount.

 

Example 1:**

```

**Input:** prices = [8,4,6,2,3]
**Output:** [4,2,4,2,3]
**Explanation:** 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.

```

Example 2:**

```

**Input:** prices = [1,2,3,4,5]
**Output:** [1,2,3,4,5]
**Explanation:** In this case, for all items, you will not receive any discount at all.

```

Example 3:**

```

**Input:** prices = [10,1,1,6]
**Output:** [9,0,1,6]

```

 

**Constraints:**

	- `1 <= prices.length <= 500`

	- `1 <= prices[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the indices of the prices that have not been discounted yet. It iterates through the prices array, popping elements from the stack if the current price is smaller than the price at the top of the stack, and updating the result array with the discounted price.

**Approach**
1. Initialize an empty stack and a result array of the same length as the input prices array.
2. Iterate through the prices array, keeping track of the current index and price.
3. While the stack is not empty and the price at the top of the stack is greater than or equal to the current price:
   - Pop the top element from the stack, which represents the index and price of an item that has not been discounted yet.
   - Update the result array at the popped index with the discounted price.
4. Push the current index and price onto the stack.
5. After iterating through the entire prices array, pop any remaining elements from the stack and update the result array with their original prices.
6. Return the result array.

**Time Complexity**
O(n), where n is the length of the prices array. This is because each element in the prices array is pushed and popped from the stack at most once.

**Space Complexity**
O(n), where n is the length of the prices array. This is because in the worst case, the stack will store all elements from the prices array.

**Key Insight**
The key insight is to use a stack to keep track of the indices of the prices that have not been discounted yet. By popping elements from the stack when a smaller price is encountered, we can efficiently calculate the discounted price for each item. This approach takes advantage of the fact that the prices array is processed in order, allowing us to use a stack to store the indices of the prices that have not been discounted yet.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-11-14 |
| 💻 Language | Python |