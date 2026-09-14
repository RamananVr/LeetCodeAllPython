---
comments: true
difficulty: Medium
tags:
    - Bit Manipulation
    - Array
    - Hash Table
    - Backtracking
---

<!-- problem:start -->

# [491. Non-decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return <em>all the different possible non-decreasing subsequences of the given array with at least two elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,6,7,7]
<strong>Output:</strong> [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,4,3,2,1]
<strong>Output:</strong> [[4,4]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 15</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Every non-decreasing subsequence of length at least $2$, without duplicate lists. The array is unsorted, so we cannot sort then pick.
>
> DFS at index $u$: take $nums[u]$ when it is $\ge last$; skip it only when $nums[u]\ne last$. That second guard drops the duplicate of “skip a value then take the same value later”.
>
> $last$ starts at a tiny sentinel so the first number is always eligible. Only sequences longer than $1$ are kept.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(u, last, t):
            if u == len(nums):
                if len(t) > 1:
                    ans.append(t[:])
                return
            if nums[u] >= last:
                t.append(nums[u])
                dfs(u + 1, nums[u], t)
                t.pop()
            if nums[u] != last:
                dfs(u + 1, last, t)

        ans = []
        dfs(0, -1000, [])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
