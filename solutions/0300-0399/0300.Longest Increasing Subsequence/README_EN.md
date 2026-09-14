---
comments: true
difficulty: Medium
tags:
    - Array
    - Binary Search
    - Dynamic Programming
    - Longest Increasing Subsequence
---

<!-- problem:start -->

# [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return <em>the length of the longest <strong>strictly increasing </strong></em><span data-keyword="subsequence-array"><em><strong>subsequence</strong></em></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2500</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b>&nbsp;Can you come up with an algorithm that runs in&nbsp;<code>O(n log(n))</code> time complexity?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> A subsequence must keep relative order and increase strictly. Enumerating all subsequences explodes with $n$; $n \le 2500$ still allows an $O(n^2)$ transfer by ending index.
>
> The LIS ending at $nums[i]$ depends only on smaller values to its left. Define $f[i]$ as that length, and for each $j < i$ with $nums[j] < nums[i]$ take $\max(f[j]+1)$. A singleton has length $1$, and the answer is $\max f$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Method 1 scans the left side linearly for the best $f[j]$ below $x$, which costs $O(n^2)$. After discretizing values, that query is a prefix maximum on ranks, which a Fenwick tree maintains in $O(\log n)$.
>
> Scan each $x$ in original order: query the prefix max strictly below $x$, then write $x$. Only left-hand information is used, so the recurrence matches Method 1 in $O(n \log n)$ time.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] = max(self.c[x], v)
            x += x & -x

    def query(self, x: int) -> int:
        mx = 0
        while x:
            mx = max(mx, self.c[x])
            x -= x & -x
        return mx

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        m = len(s)
        tree = BinaryIndexedTree(m)
        for x in nums:
            x = bisect_left(s, x) + 1
            t = tree.query(x - 1) + 1
            tree.update(x, t)
        return tree.query(m)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
