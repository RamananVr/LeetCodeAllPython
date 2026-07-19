---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1655.Distribute%20Repeating%20Integers/README_EN.md
rating: 2307
source: Biweekly Contest 39 Q4
tags:
    - Bit Manipulation
    - Array
    - Hash Table
    - Dynamic Programming
    - Backtracking
    - Bitmask
    - Counting
---

<!-- problem:start -->

# [1655. Distribute Repeating Integers](https://leetcode.com/problems/distribute-repeating-integers)

## Description

<!-- description:start -->

<p>You are given an array of <code>n</code> integers, <code>nums</code>, where there are at most <code>50</code> unique values in the array. You are also given an array of <code>m</code> customer order quantities, <code>quantity</code>, where <code>quantity[i]</code> is the amount of integers the <code>i<sup>th</sup></code> customer ordered. Determine if it is possible to distribute <code>nums</code> such that:</p>

<ul>
	<li>The <code>i<sup>th</sup></code> customer gets <strong>exactly</strong> <code>quantity[i]</code> integers,</li>
	<li>The integers the <code>i<sup>th</sup></code> customer gets are <strong>all equal</strong>, and</li>
	<li>Every customer is satisfied.</li>
</ul>

<p>Return <code>true</code><em> if it is possible to distribute </em><code>nums</code><em> according to the above conditions</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4], quantity = [2]
<strong>Output:</strong> false
<strong>Explanation:</strong> The 0<sup>th</sup> customer cannot be given two different integers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,3], quantity = [2]
<strong>Output:</strong> true
<strong>Explanation:</strong> The 0<sup>th</sup> customer is given [3,3]. The integers [1,2] are not used.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2,2], quantity = [2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> The 0<sup>th</sup> customer is given [1,1], and the 1st customer is given [2,2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>m == quantity.length</code></li>
	<li><code>1 &lt;= m &lt;= 10</code></li>
	<li><code>1 &lt;= quantity[i] &lt;= 10<sup>5</sup></code></li>
	<li>There are at most <code>50</code> unique values in <code>nums</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: State Compression Dynamic Programming + Subset Enumeration

First, we count the occurrence of each number in the array `nums`, and record it in the hash table `cnt`. Then we store the values in the hash table into the array `arr`. We denote the length of the array `arr` as `n`.

Note that the length of the array `quantity` does not exceed 10, so we can use a binary number to represent a subset of `quantity`. That is, the number `j` represents a subset of `quantity`, where the `i`-th bit of the binary representation of `j` is `1` means the `i`-th number in `quantity` is selected, and `0` means the `i`-th number is not selected.

We can preprocess an array `s`, where `s[j]` represents the sum of all numbers in the subset `j` of `quantity`.

Next, we define `f[i][j]` to represent whether the numbers in `arr[0,..i-1]` can be successfully allocated to the subset `j` of `quantity`, where `i` ranges from `[0,..n-1]`, and `j` ranges from `[0,2^m-1]`, where `m` is the length of `quantity`.

Considering `f[i][j]`, if there exists a subset `k` in `j` such that `s[k] <= arr[i]`, and `f[i-1][j XOR k]` is true, then `f[i][j]` is true, otherwise `f[i][j]` is false.

The answer is `f[n-1][2^m-1]`.

The time complexity is `O(n * 3^m)`, and the space complexity is `O(n * 2^m)`. Here, `n` is the number of different integers in the array `nums`, and `m` is the length of the array `quantity`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        m = len(quantity)
        s = [0] * (1 << m)
        for i in range(1, 1 << m):
            for j in range(m):
                if i >> j & 1:
                    s[i] = s[i ^ (1 << j)] + quantity[j]
                    break
        cnt = Counter(nums)
        arr = list(cnt.values())
        n = len(arr)
        f = [[False] * (1 << m) for _ in range(n)]
        for i in range(n):
            f[i][0] = True
        for i, x in enumerate(arr):
            for j in range(1, 1 << m):
                if i and f[i - 1][j]:
                    f[i][j] = True
                    continue
                k = j
                while k:
                    ok1 = j == k if i == 0 else f[i - 1][j ^ k]
                    ok2 = s[k] <= x
                    if ok1 and ok2:
                        f[i][j] = True
                        break
                    k = (k - 1) & j
        return f[-1][-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
