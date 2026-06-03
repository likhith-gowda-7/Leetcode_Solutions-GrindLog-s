> 📌 **Cross-listed:** Primary location is [Stack/0901-Online-Stock-Span](../../Stack/0901-Online-Stock-Span). This problem also appears under: **Stack**, **Design**, **Monotonic Stack**, **Data Stream**

# 901. Online Stock Span


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Stack](https://img.shields.io/badge/Stack-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple) ![Data Stream](https://img.shields.io/badge/Data%20Stream-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/online-stock-span/)


## 📝 Problem Description

Design an algorithm that collects daily price quotes for some stock and returns **the span** of that stock's price for the current day.

The **span** of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

	- For example, if the prices of the stock in the last four days is `[7,2,1,2]` and the price of the stock today is `2`, then the span of today is `4` because starting from today, the price of the stock was less than or equal `2` for `4` consecutive days.

	- Also, if the prices of the stock in the last four days is `[7,34,1,2]` and the price of the stock today is `8`, then the span of today is `3` because starting from today, the price of the stock was less than or equal `8` for `3` consecutive days.

Implement the `StockSpanner` class:

	- `StockSpanner()` Initializes the object of the class.

	- `int next(int price)` Returns the **span** of the stock's price given that today's price is `price`.

 

Example 1:**

```

**Input**
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
**Output**
[null, 1, 1, 1, 2, 1, 4, 6]

**Explanation**
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6

```

 

**Constraints:**

	- `1 <= price <= 10^5`

	- At most `10^4` calls will be made to `next`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the stock prices and their corresponding spans. When a new price is encountered, it checks the stack to find the maximum span by popping elements that are less than or equal to the current price and adding their spans to the current span. This approach takes advantage of the monotonic stack property, where the stack is always sorted in ascending order of prices.

**Approach**
1. Initialize an empty stack to store the stock prices and their corresponding spans.
2. When a new price is encountered, initialize the current span to 1.
3. While the stack is not empty and the top element of the stack has a price less than or equal to the current price, pop the top element and add its span to the current span.
4. Push the current price and span onto the stack.
5. Return the current span.

**Time Complexity**
O(n), where n is the number of days. This is because each day, we may need to pop all elements from the stack that are less than or equal to the current price, resulting in a maximum of n operations.

**Space Complexity**
O(n), where n is the number of days. This is because in the worst-case scenario, the stack may store all days' prices and spans.

**Key Insight**
The key insight is to use a monotonic stack to efficiently calculate the span of each day's price. By popping elements that are less than or equal to the current price, we can find the maximum span in O(1) time, resulting in a linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 63 ms (Beats 55.36%) |
| 💾 Memory | 22.2 MB (Beats 100%) |
| 📅 Solved | 2025-01-30 |
| 💻 Language | Python |