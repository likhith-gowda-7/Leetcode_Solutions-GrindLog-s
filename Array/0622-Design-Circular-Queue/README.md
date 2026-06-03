# 622. Design Circular Queue


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Queue](https://img.shields.io/badge/Queue-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/design-circular-queue/)


## 📝 Problem Description

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the `MyCircularQueue` class:

	- `MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`.

	- `int Front()` Gets the front item from the queue. If the queue is empty, return `-1`.

	- `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`.

	- `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful.

	- `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful.

	- `boolean isEmpty()` Checks whether the circular queue is empty or not.

	- `boolean isFull()` Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:**

```

**Input**
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
**Output**
[null, true, true, true, false, 3, true, true, true, 4]

**Explanation**
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

```

 

**Constraints:**

	- `1 <= k <= 1000`

	- `0 <= value <= 1000`

	- At most `3000` calls will be made to `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.

## 🧠 Solution Explanation

**Intuition**
The circular queue is a data structure that uses a fixed-size array to store elements in a circular manner, allowing for efficient insertion and deletion of elements from both ends. The key insight is to use modular arithmetic to handle the circular nature of the queue, ensuring that the front and rear indices wrap around to the beginning of the array when necessary.

**Approach**
1. Initialize the queue with a fixed size `k` and an empty array of size `k`.
2. Use two indices, `front` and `rear`, to keep track of the front and rear of the queue.
3. In `enQueue(value)`, check if the queue is full. If not, increment `rear` modulo `k` and store the value at the new `rear` index.
4. In `deQueue()`, check if the queue is empty. If not, increment `front` modulo `k` and update `rear` if necessary.
5. In `Front()` and `Rear()`, return the value at the `front` and `rear` indices, respectively, or -1 if the queue is empty.
6. In `isEmpty()` and `isFull()`, check if the queue is empty or full based on the values of `rear` and `front`.

**Time Complexity**
- `enQueue(value)`: O(1) because we only perform a constant number of operations (incrementing `rear` and storing the value).
- `deQueue()`: O(1) because we only perform a constant number of operations (incrementing `front` and updating `rear` if necessary).
- `Front()`, `Rear()`, `isEmpty()`, and `isFull()`: O(1) because we only access or update a constant number of indices.

**Space Complexity**
O(k) because we need to store the queue elements in an array of size `k`.

**Key Insight**
The key insight is to use modular arithmetic to handle the circular nature of the queue, ensuring that the front and rear indices wrap around to the beginning of the array when necessary. This allows us to efficiently insert and delete elements from both ends of the queue.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 76.2%) |
| 💾 Memory | 18.6 MB (Beats 100%) |
| 📅 Solved | 2025-03-24 |
| 💻 Language | Python |