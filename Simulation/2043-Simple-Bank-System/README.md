> 📌 **Cross-listed:** Primary location is [Array/2043-Simple-Bank-System](../../Array/2043-Simple-Bank-System). This problem also appears under: **Array**, **Hash Table**, **Design**, **Simulation**

# 2043. Simple Bank System


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/simple-bank-system/)


## 📝 Problem Description

You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has `n` accounts numbered from `1` to `n`. The initial balance of each account is stored in a **0-indexed** integer array `balance`, with the `(i + 1)^th` account having an initial balance of `balance[i]`.

Execute all the **valid** transactions. A transaction is **valid** if:

	- The given account number(s) are between `1` and `n`, and

	- The amount of money withdrawn or transferred from is **less than or equal** to the balance of the account.

Implement the `Bank` class:

	- `Bank(long[] balance)` Initializes the object with the **0-indexed** integer array `balance`.

	- `boolean transfer(int account1, int account2, long money)` Transfers `money` dollars from the account numbered `account1` to the account numbered `account2`. Return `true` if the transaction was successful, `false` otherwise.

	- `boolean deposit(int account, long money)` Deposit `money` dollars into the account numbered `account`. Return `true` if the transaction was successful, `false` otherwise.

	- `boolean withdraw(int account, long money)` Withdraw `money` dollars from the account numbered `account`. Return `true` if the transaction was successful, `false` otherwise.

 

Example 1:**

```

**Input**
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
**Output**
[null, true, true, true, false, false]

**Explanation**
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                         // Account 3 has $20 - $10 = $10.
bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
                         // Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
bank.deposit(5, 20);     // return true, it is valid to deposit $20 to account 5.
                         // Account 5 has $10 + $20 = $30.
bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
                         // so it is invalid to transfer $15 from it.
bank.withdraw(10, 50);   // return false, it is invalid because account 10 does not exist.

```

 

**Constraints:**

	- `n == balance.length`

	- `1 <= n, account, account1, account2 <= 10^5`

	- `0 <= balance[i], money <= 10^12`

	- At most `10^4` calls will be made to **each** function `transfer`, `deposit`, `withdraw`.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a simple array-based data structure to simulate the bank's transactions. By maintaining a balance array, the class can efficiently perform deposit, withdraw, and transfer operations while validating account numbers and balances.

**Approach**
1. Initialize the `Bank` object with the balance array in the constructor.
2. In the `transfer` method:
   - Subtract 1 from the account numbers to convert them to 0-indexed.
   - Check if the account numbers are valid (within the array bounds).
   - Verify if the transfer amount is less than or equal to the balance of the source account.
   - If valid, update the balances of the source and destination accounts.
3. In the `deposit` method:
   - Subtract 1 from the account number to convert it to 0-indexed.
   - Check if the account number is valid (within the array bounds).
   - Update the balance of the account.
4. In the `withdraw` method:
   - Subtract 1 from the account number to convert it to 0-indexed.
   - Check if the account number is valid (within the array bounds).
   - Verify if the withdrawal amount is less than or equal to the balance of the account.
   - If valid, update the balance of the account.

**Time Complexity**
The time complexity of this solution is O(1) for each operation (transfer, deposit, withdraw), as it involves constant-time array accesses and updates.

**Space Complexity**
The space complexity is O(n), where n is the number of accounts, as the balance array is stored in memory.

**Key Insight**
The key insight is to utilize a simple array-based data structure to simulate the bank's transactions, allowing for efficient and constant-time operations. By maintaining a balance array, the class can validate account numbers and balances while updating the account balances accordingly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 23 ms (Beats 83.91%) |
| 💾 Memory | 47.7 MB (Beats 100%) |
| 📅 Solved | 2025-10-26 |
| 💻 Language | Python |