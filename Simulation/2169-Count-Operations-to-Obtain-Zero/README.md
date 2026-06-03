> 📌 **Cross-listed:** Primary location is [Math/2169-Count-Operations-to-Obtain-Zero](../../Math/2169-Count-Operations-to-Obtain-Zero). This problem also appears under: **Math**, **Simulation**

# 2169. Count Operations to Obtain Zero


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-operations-to-obtain-zero/)


## 📝 Problem Description

You are given two **non-negative** integers `num1` and `num2`.

In one **operation**, if `num1 >= num2`, you must subtract `num2` from `num1`, otherwise subtract `num1` from `num2`.

	- For example, if `num1 = 5` and `num2 = 4`, subtract `num2` from `num1`, thus obtaining `num1 = 1` and `num2 = 4`. However, if `num1 = 4` and `num2 = 5`, after one operation, `num1 = 4` and `num2 = 1`.

Return *the **number of operations** required to make either* `num1 = 0` *or* `num2 = 0`.

 

Example 1:**

```

**Input:** num1 = 2, num2 = 3
**Output:** 3
**Explanation:** 
- Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.

```

Example 2:**

```

**Input:** num1 = 10, num2 = 10
**Output:** 1
**Explanation:** 
- Operation 1: num1 = 10, num2 = 10. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0.
Now num1 = 0 and num2 = 10. Since num1 == 0, we are done.
So the total number of operations required is 1.

```

 

**Constraints:**

	- `0 <= num1, num2 <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the fact that the problem allows us to choose which number to subtract from the other in each operation. By always subtracting the smaller number from the larger one, we can ensure that the difference between the two numbers decreases by at least 1 in each operation. This approach is similar to a "gcd" (greatest common divisor) calculation, where we repeatedly subtract the smaller number from the larger one until we reach 0.

**Approach**
1. Initialize a counter variable `count` to keep track of the number of operations.
2. While both `num1` and `num2` are non-zero:
   1. If `num1` is greater than `num2`, subtract `num2` from `num1`.
   2. Otherwise, subtract `num1` from `num2`.
   3. Increment the `count` variable by 1.
3. Return the `count` variable if either `num1` or `num2` is 0, indicating that we have reached the target state.

**Time Complexity**
The time complexity of this solution is O(log min(num1, num2)), where `log` is the logarithm to the base 2. This is because the number of operations required to reach 0 is proportional to the number of bits in the smaller number. In each operation, we are effectively dividing the larger number by 2, which is a constant-time operation.

**Space Complexity**
The space complexity of this solution is O(1), as we only use a constant amount of space to store the `count` variable and the input numbers `num1` and `num2`.

**Key Insight**
The key insight behind this solution is that by always subtracting the smaller number from the larger one, we can ensure that the difference between the two numbers decreases by at least 1 in each operation. This approach allows us to reach the target state (either `num1` or `num2` being 0) in a minimum number of operations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 35 ms (Beats 68.7%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-11-09 |
| 💻 Language | Python |