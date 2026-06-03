> 📌 **Cross-listed:** Primary location is [Array/1352-Product-of-the-Last-K-Numbers](../../Array/1352-Product-of-the-Last-K-Numbers). This problem also appears under: **Array**, **Math**, **Design**, **Data Stream**, **Prefix Sum**

# 1352. Product of the Last K Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Data Stream](https://img.shields.io/badge/Data%20Stream-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/product-of-the-last-k-numbers/)


## 📝 Problem Description

Design an algorithm that accepts a stream of integers and retrieves the product of the last `k` integers of the stream.

Implement the `ProductOfNumbers` class:

	- `ProductOfNumbers()` Initializes the object with an empty stream.

	- `void add(int num)` Appends the integer `num` to the stream.

	- `int getProduct(int k)` Returns the product of the last `k` numbers in the current list. You can assume that always the current list has at least `k` numbers.

The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

Example:**

```

**Input**
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

**Output**
[null,null,null,null,null,null,20,40,0,null,32]

**Explanation**
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 

```

 

**Constraints:**

	- `0 <= num <= 100`

	- `1 <= k <= 4 * 10^4`

	- At most `4 * 10^4` calls will be made to `add` and `getProduct`.

	- The product of the stream at any point in time will fit in a **32-bit** integer.

 

**Follow-up: **Can you implement **both** `GetProduct` and `Add` to work in `O(1)` time complexity instead of `O(k)` time complexity?

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a prefix array to efficiently calculate the product of the last `k` numbers in the stream. By maintaining a running product and handling zeros separately, we can achieve a time complexity of O(1) for the `getProduct` method.

**Approach**
1. Initialize a prefix array `prefix` with a single element `1`, and a counter `l` to keep track of the current length of the prefix array.
2. In the `add` method, check if the last element in the prefix array is `0`. If it is, reset the `zero` variable to the current length of the prefix array minus one, and append the new number to the prefix array.
3. If the last element is not `0`, append the product of the last element and the new number to the prefix array.
4. In the `getProduct` method, check if the `zero` variable is greater than or equal to `l-k`. If it is, return `0`, as the product of the last `k` numbers will be zero.
5. If the prefix array element at index `l-k-1` is `0`, return the last element of the prefix array, as the product of the last `k` numbers will be the product of all numbers after the zero.
6. Otherwise, return the last element of the prefix array divided by the prefix array element at index `l-k-1`, which represents the product of the last `k` numbers.

**Time Complexity**
O(1) for both `add` and `getProduct` methods, as we are performing constant-time operations.

**Space Complexity**
O(n), where n is the number of elements in the stream, as we are storing the prefix array with a maximum length of n.

**Key Insight**
The key insight is to handle zeros separately and maintain a running product in the prefix array, allowing us to calculate the product of the last `k` numbers in constant time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 61 ms (Beats 28.79%) |
| 💾 Memory | 32 MB (Beats 100%) |
| 📅 Solved | 2025-02-14 |
| 💻 Language | Python |