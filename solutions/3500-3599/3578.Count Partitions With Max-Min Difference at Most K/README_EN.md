---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3578.Count%20Partitions%20With%20Max-Min%20Difference%20at%20Most%20K/README_EN.md
rating: 2032
source: Weekly Contest 453 Q3
tags:
    - Queue
    - Array
    - Dynamic Programming
    - Prefix Sum
    - Sliding Window
    - Monotonic Queue
---

<!-- problem:start -->

# [3578. Count Partitions With Max-Min Difference at Most K](https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. Your task is to partition <code>nums</code> into one or more <strong>non-empty</strong> contiguous segments such that in each segment, the difference between its <strong>maximum</strong> and <strong>minimum</strong> elements is <strong>at most</strong> <code>k</code>.</p>

<p>Return the total number of ways to partition <code>nums</code> under this condition.</p>

<p>Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [9,4,1,3,7], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most <code>k = 4</code>:</p>

<ul>
	<li><code>[[9], [4], [1], [3], [7]]</code></li>
	<li><code>[[9], [4], [1], [3, 7]]</code></li>
	<li><code>[[9], [4], [1, 3], [7]]</code></li>
	<li><code>[[9], [4, 1], [3], [7]]</code></li>
	<li><code>[[9], [4, 1], [3, 7]]</code></li>
	<li><code>[[9], [4, 1, 3], [7]]</code></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,3,4], k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>There are 2 valid partitions that satisfy the given conditions:</p>

<ul>
	<li><code>[[3], [3], [4]]</code></li>
	<li><code>[[3, 3], [4]]</code></li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming + Two Pointers + Ordered Set

We define $f[i]$ as the number of ways to partition the first $i$ elements. If an array satisfies that the difference between its maximum and minimum values does not exceed $k$, then any of its subarrays also satisfies this condition. Therefore, we can use two pointers to maintain a sliding window representing the current subarray.

When we reach the $r$-th element, we need to find the left pointer $l$ such that the subarray from $l$ to $r$ satisfies that the difference between the maximum and minimum values does not exceed $k$. We can use an ordered set to maintain the elements in the current window, so that we can quickly get the maximum and minimum values.

Each time we add a new element, we insert it into the ordered set and check the difference between the maximum and minimum values in the current window. If it exceeds $k$, we move the left pointer $l$ until the condition is satisfied. The number of partition ways ending at the $r$-th element is $f[l - 1] + f[l] + \ldots + f[r - 1]$. We can use a prefix sum array to quickly calculate this value.

The answer is $f[n]$, where $n$ is the length of the array.

The time complexity is $O(n \times \log n)$ and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        sl = SortedList()
        n = len(nums)
        f = [1] + [0] * n
        g = [1] + [0] * n
        l = 1
        for r, x in enumerate(nums, 1):
            sl.add(x)
            while sl[-1] - sl[0] > k:
                sl.remove(nums[l - 1])
                l += 1
            f[r] = (g[r - 1] - (g[l - 2] if l >= 2 else 0) + mod) % mod
            g[r] = (g[r - 1] + f[r]) % mod
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
