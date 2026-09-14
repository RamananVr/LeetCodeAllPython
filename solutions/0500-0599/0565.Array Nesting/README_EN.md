---
comments: true
difficulty: Medium
tags:
    - Depth-First Search
    - Array
---

<!-- problem:start -->

# [565. Array Nesting](https://leetcode.com/problems/array-nesting)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> where <code>nums</code> is a permutation of the numbers in the range <code>[0, n - 1]</code>.</p>

<p>You should build a set <code>s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... }</code> subjected to the following rule:</p>

<ul>
	<li>The first element in <code>s[k]</code> starts with the selection of the element <code>nums[k]</code> of <code>index = k</code>.</li>
	<li>The next element in <code>s[k]</code> should be <code>nums[nums[k]]</code>, and then <code>nums[nums[nums[k]]]</code>, and so on.</li>
	<li>We stop adding right before a duplicate element occurs in <code>s[k]</code>.</li>
</ul>

<p>Return <em>the longest length of a set</em> <code>s[k]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,0,3,1,6,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,2]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt; nums.length</code></li>
	<li>All the values of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> $A[i]$ points to $A[A[i]]$, partitioning the array into disjoint cycles. A nest is a cycle. Walking from every index would revisit the same cycle.
>
> A visited array marks seen indices; start a walk only from an unseen index and count the cycle. Disjointness visits each index once. The longest cycle is the answer.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        vis = [False] * n
        res = 0
        for i in range(n):
            if vis[i]:
                continue
            cur, m = nums[i], 1
            vis[cur] = True
            while nums[cur] != nums[i]:
                cur = nums[cur]
                m += 1
                vis[cur] = True
            res = max(res, m)
        return res
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 uses an $O(n)$ visited array. Values already lie in $[0,n-1]$, so the sentinel $n$ can mark a visited cell in place.
>
> Walk the cycle, write $n$ into each cell, and count. A stored $n$ means this index was already processed. Extra space becomes constant; the cycles are the same.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            cnt = 0
            while nums[i] != n:
                j = nums[i]
                nums[i] = n
                i = j
                cnt += 1
            ans = max(ans, cnt)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
