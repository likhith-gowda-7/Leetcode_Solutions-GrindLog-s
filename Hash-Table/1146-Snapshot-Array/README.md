> 📌 **Cross-listed:** Primary location is [Array/1146-Snapshot-Array](../../Array/1146-Snapshot-Array). This problem also appears under: **Array**, **Hash Table**, **Binary Search**, **Design**

# 1146. Snapshot Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/snapshot-array/)


## 📝 Problem Description

Implement a SnapshotArray that supports the following interface:

	- `SnapshotArray(int length)` initializes an array-like data structure with the given length. **Initially, each element equals 0**.

	- `void set(index, val)` sets the element at the given `index` to be equal to `val`.

	- `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`.

	- `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`

 

Example 1:**

```

**Input:** ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
**Output:** [null,null,0,null,5]
**Explanation: **
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```

 

**Constraints:**

	- `1 <= length <= 5 * 10^4`

	- `0 <= index < length`

	- `0 <= val <= 10^9`

	- `0 <= snap_id < `(the total number of times we call `snap()`)

	- At most `5 * 10^4` calls will be made to `set`, `snap`, and `get`.

## 🧠 Solution Explanation

**Intuition**
The SnapshotArray solution uses a combination of a hash table and binary search to efficiently store and retrieve array values at specific snapshots. The key insight is to store the history of updates for each index in the hash table, allowing for fast retrieval of values at specific snapshots.

**Approach**
1. Initialize a hash table `arr` to store the history of updates for each index, where each key is an index and the value is a list of tuples containing the snapshot ID and the updated value.
2. Initialize a counter `call` to keep track of the number of snapshots taken.
3. In the `set` method, check if the latest update for the given index is from the current snapshot. If not, append a new tuple to the list of updates for that index.
4. In the `snap` method, increment the `call` counter and return the current snapshot ID minus 1.
5. In the `get` method, use binary search to find the latest update for the given index that is from a snapshot with an ID less than or equal to the given `snap_id`. Return the value associated with that update.

**Time Complexity**
- `set`: O(1) amortized, since we only append to the list of updates for an index if the latest update is not from the current snapshot.
- `snap`: O(1), since we simply increment the `call` counter.
- `get`: O(log n), where n is the number of updates for the given index, since we use binary search to find the latest update from a snapshot with an ID less than or equal to the given `snap_id`.

**Space Complexity**
- O(n), where n is the total number of updates across all indices, since we store the history of updates for each index in the hash table.

**Key Insight**
The key insight is to use a hash table to store the history of updates for each index, allowing for fast retrieval of values at specific snapshots. This approach enables efficient implementation of the SnapshotArray interface.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 180 ms (Beats 52.76%) |
| 💾 Memory | 44.1 MB (Beats 99.8%) |
| 📅 Solved | 2025-02-28 |
| 💻 Language | Python |