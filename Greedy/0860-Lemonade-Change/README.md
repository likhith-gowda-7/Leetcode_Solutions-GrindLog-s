> 📌 **Cross-listed:** Primary location is [Array/0860-Lemonade-Change](../../Array/0860-Lemonade-Change). This problem also appears under: **Array**, **Greedy**

# 860. Lemonade Change


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lemonade-change/)


## 📝 Problem Description

At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the `i^th` customer pays, return `true` *if you can provide every customer with the correct change, or* `false` *otherwise*.

 

Example 1:**

```

**Input:** bills = [5,5,5,10,20]
**Output:** true
**Explanation:** 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

```

Example 2:**

```

**Input:** bills = [5,5,10,10,20]
**Output:** false
**Explanation:** 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

```

 

**Constraints:**

	- `1 <= bills.length <= 10^5`

	- `bills[i]` is either `5`, `10`, or `20`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to manage the available bills. It keeps track of the number of $5 and $10 bills to determine if it can provide the correct change for each customer. The key insight is that we can always make change for a $10 bill with a $5 bill, and we can make change for a $20 bill with a $10 bill and a $5 bill, or three $5 bills.

**Approach**
1. Initialize counters for $5 and $10 bills.
2. Iterate through each bill in the input array.
3. If the bill is $5, increment the $5 counter.
4. If the bill is $10 and there are available $5 bills, decrement the $5 counter and increment the $10 counter.
5. If the bill is $20, check if there are available $10 and $5 bills. If so, decrement both counters. Otherwise, check if there are at least three $5 bills available. If not, return False.
6. If the bill is not $5, $10, or $20, return False.
7. After iterating through all bills, return True if all customers can be served.

**Time Complexity**
O(n), where n is the number of bills. We iterate through each bill once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the counters.

**Key Insight**
The solution relies on the fact that we can always make change for a $10 bill with a $5 bill, and we can make change for a $20 bill with a $10 bill and a $5 bill, or three $5 bills. This allows us to use a greedy approach to manage the available bills.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 76.07%) |
| 💾 Memory | 21.9 MB (Beats 99.97%) |
| 📅 Solved | 2025-02-13 |
| 💻 Language | Python |