> 📌 **Cross-listed:** Primary location is [Stack/0155-Min-Stack](../../Stack/0155-Min-Stack). This problem also appears under: **Stack**, **Design**

# 155. Min Stack


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Stack](https://img.shields.io/badge/Stack-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/min-stack/)


## 📝 Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

	- `MinStack()` initializes the stack object.

	- `void push(int val)` pushes the element `val` onto the stack.

	- `void pop()` removes the element on the top of the stack.

	- `int top()` gets the top element of the stack.

	- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

 

Example 1:**

```

**Input**
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

**Output**
[null,null,null,null,-3,null,0,-2]

**Explanation**
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

```

 

**Constraints:**

	- `-2^31 <= val <= 2^31 - 1`

	- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.

	- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## 🧠 Solution Explanation

**Intuition**
The solution uses two stacks to achieve O(1) time complexity for each operation. The main stack stores the actual elements, while the auxiliary stack stores the minimum elements encountered so far.

**Approach**
1. Initialize two empty stacks: `self.stack` for storing actual elements and `self.min_stack` for storing minimum elements.
2. In the `push` method:
   - Append the new element to `self.stack`.
   - If `self.min_stack` is empty or the new element is less than or equal to the top element of `self.min_stack`, append the new element to `self.min_stack`.
3. In the `pop` method:
   - Remove the top element from `self.stack`.
   - If the removed element is equal to the top element of `self.min_stack`, remove it from `self.min_stack` as well.
4. In the `top` method:
   - Return the top element of `self.stack`.
5. In the `getMin` method:
   - Return the top element of `self.min_stack` if it's not empty; otherwise, return None.

**Time Complexity**
- `push` and `pop` operations: O(1), as we're performing constant-time operations on the stacks.
- `top` operation: O(1), as we're simply returning the top element of `self.stack`.
- `getMin` operation: O(1), as we're returning the top element of `self.min_stack`.

**Space Complexity**
- O(n), where n is the number of elements in the stack, as we're using two stacks to store elements.

**Key Insight**
The key to this solution is maintaining two stacks: one for actual elements and another for minimum elements. By updating the auxiliary stack when a new minimum element is encountered, we can efficiently retrieve the minimum element in constant time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 67.39%) |
| 💾 Memory | 21.3 MB (Beats 100%) |
| 📅 Solved | 2025-08-22 |
| 💻 Language | Python |