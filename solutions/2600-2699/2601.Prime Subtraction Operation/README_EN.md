---
comments: true
difficulty: Medium
rating: 1779
source: Weekly Contest 338 Q2
tags:
    - Greedy
    - Array
    - Math
    - Binary Search
    - Number Theory
---

<!-- problem:start -->

# [2601. Prime Subtraction Operation](https://leetcode.com/problems/prime-subtraction-operation)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code>.</p>

<p>You can perform the following operation as many times as you want:</p>

<ul>
	<li>Pick an index <code>i</code> that you haven&rsquo;t picked before, and pick a prime <code>p</code> <strong>strictly less than</strong> <code>nums[i]</code>, then subtract <code>p</code> from <code>nums[i]</code>.</li>
</ul>

<p>Return <em>true if you can make <code>nums</code> a strictly increasing array using the above operation and false otherwise.</em></p>

<p>A <strong>strictly increasing array</strong> is an array whose each element is strictly greater than its preceding element.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,9,6,10]
<strong>Output:</strong> true
<strong>Explanation:</strong> In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,8,11,12]
<strong>Output:</strong> true
<strong>Explanation: </strong>Initially nums is sorted in strictly increasing order, so we don&#39;t need to make any operations.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,8,3]
<strong>Output:</strong> false
<strong>Explanation:</strong> It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code><font face="monospace">nums.length == n</font></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing prime numbers + binary search

<!-- thinking:start -->

> **Thinking**
>
> Each index may subtract a prime at most once, and the array must become strictly increasing. Greedy left-to-right may compress a value too far for later positions. Enumerating primes at every index is feasible for $n \le 1000$ and values at most $1000$, but the scan direction still matters.
>
> The rightmost value $nums[n-1]$ is freer when larger, so we process from right to left. When $nums[i] \ge nums[i+1]$, we must subtract a prime strictly larger than $nums[i]-nums[i+1]$ and smaller than $nums[i]$, taking the smallest such prime so the left side keeps as much room as possible.
>
> We therefore sieve primes up to $1000$ into $p$ and binary-search the least prime above that lower bound. If none exists, the array cannot be made strictly increasing.

<!-- thinking:end -->

We first preprocess all the primes within $1000$ and record them in the array $p$.

For each element $nums[i]$ in the array $nums$, we need to find a prime $p[j]$ such that $p[j] \gt nums[i] - nums[i + 1]$ and $p[j]$ is as small as possible. If there is no such prime, it means that it cannot be strictly increased by subtraction operations, return `false`. If there is such a prime, we will subtract $p[j]$ from $nums[i]$ and continue to process the next element.

If all the elements in $nums$ are processed, it means that it can be strictly increased by subtraction operations, return `true`.

The time complexity is $O(n \log n)$ and the space complexity is $O(n)$. where $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        p = []
        for i in range(2, max(nums)):
            for j in p:
                if i % j == 0:
                    break
            else:
                p.append(i)

        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                continue
            j = bisect_right(p, nums[i] - nums[i + 1])
            if j == len(p) or p[j] >= nums[i]:
                return False
            nums[i] -= p[j]
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Preprocessing prime numbers

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 binary-searches the prime table each time. With values at most $1000$, we can index directly: let $p[x]$ be the least prime that is at least $x$. The lower bound $nums[i]-nums[i+1]$ then becomes a single array access, removing the search.
>
> The rest is unchanged: still right-to-left, still subtracting that smallest prime.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
