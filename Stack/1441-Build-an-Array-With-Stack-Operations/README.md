> 📌 **Cross-listed:** Primary location is [Array/1441-Build-an-Array-With-Stack-Operations](../../Array/1441-Build-an-Array-With-Stack-Operations). This problem also appears under: **Array**, **Stack**, **Simulation**

# 1441. Build an Array With Stack Operations


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/build-an-array-with-stack-operations/)


## 📝 Problem Description

You are given an integer array `target` and an integer `n`.

You have an empty stack with the two following operations:

	- **`"Push"`**: pushes an integer to the top of the stack.

	- **`"Pop"`**: removes the integer on the top of the stack.

You also have a stream of the integers in the range `[1, n]`.

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to `target`. You should follow the following rules:

	- If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.

	- If the stack is not empty, pop the integer at the top of the stack.

	- If, at any moment, the elements in the stack (from the bottom to the top) are equal to `target`, do not read new integers from the stream and do not do more operations on the stack.

Return *the stack operations needed to build *`target` following the mentioned rules. If there are multiple valid answers, return **any of them**.

 

Example 1:**

```

**Input:** target = [1,3], n = 3
**Output:** ["Push","Push","Pop","Push"]
**Explanation:** Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].

```

Example 2:**

```

**Input:** target = [1,2,3], n = 3
**Output:** ["Push","Push","Push"]
**Explanation:** Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].

```

Example 3:**

```

**Input:** target = [1,2], n = 4
**Output:** ["Push","Push"]
**Explanation:** Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.

```

 

**Constraints:**

	- `1 <= target.length <= 100`

	- `1 <= n <= 100`

	- `1 <= target[i] <= n`

	- `target` is strictly increasing.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to simulate the stack operations. It iterates through the range of integers from 1 to `n` and decides whether to push or pop an integer from the stack based on whether it matches the current target integer. This approach ensures that the stack elements match the target array as soon as possible.

**Approach**
1. Initialize an empty list `ops` to store the stack operations and an index `idx` to track the current target integer.
2. Iterate through the range of integers from 1 to `n`.
3. For each integer `i`, append "Push" to `ops` to simulate pushing `i` onto the stack.
4. If `i` does not match the current target integer `target[idx]`, append "Pop" to `ops` to simulate popping the top element from the stack.
5. If `i` matches the current target integer, increment `idx` to move to the next target integer.
6. If the current target integer index `idx` reaches the length of the target array, break the loop.
7. Return the list of stack operations `ops`.

**Time Complexity**
O(n), where n is the length of the range of integers from 1 to `n`. This is because we iterate through the range once.

**Space Complexity**
O(n), where n is the length of the range of integers from 1 to `n`. This is because we store the stack operations in a list of length up to n.

**Key Insight**
The key insight is to use a greedy approach to simulate the stack operations. By always pushing the current integer onto the stack and popping it if it doesn't match the target, we ensure that the stack elements match the target array as soon as possible. This approach avoids unnecessary operations and minimizes the number of stack operations required.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-11-14 |
| 💻 Language | Python |