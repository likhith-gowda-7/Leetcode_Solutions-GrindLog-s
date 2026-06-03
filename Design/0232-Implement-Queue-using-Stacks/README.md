> 📌 **Cross-listed:** Primary location is [Stack/0232-Implement-Queue-using-Stacks](../../Stack/0232-Implement-Queue-using-Stacks). This problem also appears under: **Stack**, **Design**, **Queue**

# 232. Implement Queue using Stacks


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Stack](https://img.shields.io/badge/Stack-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Queue](https://img.shields.io/badge/Queue-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)


## 📝 Problem Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

	- `void push(int x)` Pushes element x to the back of the queue.

	- `int pop()` Removes the element from the front of the queue and returns it.

	- `int peek()` Returns the element at the front of the queue.

	- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

	- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.

	- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

 

Example 1:**

```

**Input**
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
**Output**
[null, null, null, 1, 1, false]

**Explanation**
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

```

 

**Constraints:**

	- `1 <= x <= 9`

	- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.

	- All the calls to `pop` and `peek` are valid.

 

**Follow-up:** Can you implement the queue such that each operation is **[amortized](https://en.wikipedia.org/wiki/Amortized_analysis)** `O(1)` time complexity? In other words, performing `n` operations will take overall `O(n)` time even if one of those operations may take longer.

## 🧠 Solution Explanation

**Intuition**
The solution uses a list to simulate a queue, where `push` adds elements to the end of the list, `pop` removes elements from the beginning of the list, `peek` returns the first element without removing it, and `empty` checks if the list is empty. This approach leverages the built-in functionality of lists in Python to implement a queue.

**Approach**
1. Initialize an empty list `Q` in the `MyQueue` class to simulate the queue.
2. In the `push` method, add the element `x` to the end of the list `Q` using the `append` method.
3. In the `pop` method, remove and return the first element from the list `Q` using the `pop(0)` method.
4. In the `peek` method, return the first element from the list `Q` without removing it using indexing `Q[0]`.
5. In the `empty` method, check if the list `Q` is empty by checking its length using `len(Q) == 0`.

**Time Complexity**
- `push`: O(1) because appending to the end of a list is a constant-time operation.
- `pop`: O(n) because removing the first element from a list in Python involves shifting all other elements, resulting in linear time complexity.
- `peek`: O(1) because accessing the first element of a list is a constant-time operation.
- `empty`: O(1) because checking the length of a list is a constant-time operation.

**Space Complexity**
O(n) because the list `Q` stores all elements added to the queue, resulting in linear space complexity.

**Key Insight**
The key insight is that using a list to simulate a queue allows for efficient `push` and `peek` operations, but the `pop` operation has linear time complexity due to the shifting of elements. This trade-off is acceptable for this implementation, as the `pop` operation is not expected to be performed frequently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-11-21 |
| 💻 Language | Python |