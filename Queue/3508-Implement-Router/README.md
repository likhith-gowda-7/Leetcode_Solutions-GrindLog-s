> 📌 **Cross-listed:** Primary location is [Array/3508-Implement-Router](../../Array/3508-Implement-Router). This problem also appears under: **Array**, **Hash Table**, **Binary Search**, **Design**, **Queue**, **Ordered Set**

# 3508. Implement Router


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/implement-router/)


## 📝 Problem Description

Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

	- `source`: A unique identifier for the machine that generated the packet.

	- `destination`: A unique identifier for the target machine.

	- `timestamp`: The time at which the packet arrived at the router.

Implement the `Router` class:

`Router(int memoryLimit)`: Initializes the Router object with a fixed memory limit.

	- `memoryLimit` is the **maximum** number of packets the router can store at any given time.

	- If adding a new packet would exceed this limit, the **oldest** packet must be removed to free up space.

`bool addPacket(int source, int destination, int timestamp)`: Adds a packet with the given attributes to the router.

	- A packet is considered a duplicate if another packet with the same `source`, `destination`, and `timestamp` already exists in the router.

	- Return `true` if the packet is successfully added (i.e., it is not a duplicate); otherwise return `false`.

`int[] forwardPacket()`: Forwards the next packet in FIFO (First In First Out) order.

	- Remove the packet from storage.

	- Return the packet as an array `[source, destination, timestamp]`.

	- If there are no packets to forward, return an empty array.

`int getCount(int destination, int startTime, int endTime)`:

	- Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range `[startTime, endTime]`.

**Note** that queries for `addPacket` will be made in non-decreasing order of `timestamp`.

 

Example 1:**

**Input:**

["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]

[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]

**Output:**

[null, true, true, false, true, true, [2, 5, 90], true, 1] 

**Explanation**

Router router = new Router(3); // Initialize Router with memoryLimit of 3.

router.addPacket(1, 4, 90); // Packet is added. Return True.

router.addPacket(2, 5, 90); // Packet is added. Return True.

router.addPacket(1, 4, 90); // This is a duplicate packet. Return False.

router.addPacket(3, 5, 95); // Packet is added. Return True

router.addPacket(4, 5, 105); // Packet is added, `[1, 4, 90]` is removed as number of packets exceeds memoryLimit. Return True.

router.forwardPacket(); // Return `[2, 5, 90]` and remove it from router.

router.addPacket(5, 2, 110); // Packet is added. Return True.

router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range `[100, 110]` is `[4, 5, 105]`. Return 1.

Example 2:**

**Input:**

["Router", "addPacket", "forwardPacket", "forwardPacket"]

[[2], [7, 4, 90], [], []]

**Output:**

[null, true, [7, 4, 90], []] 

**Explanation**

Router router = new Router(2); // Initialize `Router` with `memoryLimit` of 2.

router.addPacket(7, 4, 90); // Return True.

router.forwardPacket(); // Return `[7, 4, 90]`.

router.forwardPacket(); // There are no packets left, return `[]`.

 

**Constraints:**

	- `2 <= memoryLimit <= 10^5`

	- `1 <= source, destination <= 2 * 10^5`

	- `1 <= timestamp <= 10^9`

	- `1 <= startTime <= endTime <= 10^9`

	- At most `10^5` calls will be made to `addPacket`, `forwardPacket`, and `getCount` methods altogether.

	- queries for `addPacket` will be made in non-decreasing order of `timestamp`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of data structures to efficiently manage data packets in a network router. It utilizes a queue to store packets, a set to keep track of unique packets, and a dictionary to store packets by destination. This design allows for efficient addition and removal of packets, as well as counting packets by destination within a time range.

**Approach**
1. Initialize the Router object with a fixed memory limit and create an empty queue, set, and dictionary.
2. When adding a packet, check if it already exists in the set. If it does, return False.
3. If the current size equals the maximum size, remove the oldest packet from the queue, set, and dictionary.
4. Add the new packet to the queue, set, and dictionary, and increment the current size.
5. When forwarding a packet, remove it from the queue, set, and dictionary, and decrement the current size.
6. To count packets by destination within a time range, use binary search to find the indices of the start and end times in the sorted list of timestamps for the given destination.

**Time Complexity**
- `addPacket`: O(1) for insertion and deletion operations in the queue and set, O(log n) for binary search in the dictionary. Overall, O(1) amortized time complexity.
- `forwardPacket`: O(1) for removal operations in the queue and set, O(log n) for binary search in the dictionary. Overall, O(1) time complexity.
- `getCount`: O(log n) for binary search in the dictionary.

**Space Complexity**
- The solution uses O(n) space for the queue, set, and dictionary, where n is the maximum number of packets the router can store.

**Key Insight**
The key insight is the use of a combination of data structures to efficiently manage packets. The queue allows for efficient addition and removal of packets, while the set ensures uniqueness of packets. The dictionary enables efficient counting of packets by destination within a time range using binary search. This design allows the solution to achieve O(1) amortized time complexity for adding and forwarding packets, making it efficient for large-scale network routing applications.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 480 ms (Beats 30.5%) |
| 💾 Memory | 88.8 MB (Beats 5.38%) |
| 📅 Solved | 2025-09-20 |
| 💻 Language | Python |