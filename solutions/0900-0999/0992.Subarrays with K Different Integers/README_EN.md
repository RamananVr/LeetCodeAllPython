---
comments: true
difficulty: Hard
tags:
    - Array
    - Hash Table
    - Counting
    - Sliding Window
---

<!-- problem:start -->

# [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the number of <strong>good subarrays</strong> of </em><code>nums</code>.</p>

<p>A <strong>good array</strong> is an array where the number of different integers in that array is exactly <code>k</code>.</p>

<ul>
	<li>For example, <code>[1,2,3,1,2]</code> has <code>3</code> different integers: <code>1</code>, <code>2</code>, and <code>3</code>.</li>
</ul>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,2,3], k = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,3,4], k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= nums.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Count subarrays with exactly $k$ distinct values. $n\le 2\times 10^4$, so enumeration is too slow. The number of distinct values is monotone in the window, so “at most $k$” is a sliding window. Exactly $k$ equals the leftmost index for “at most $k$” minus that for “at most $k-1$”, summed over every right end.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(k):
            pos = [0] * len(nums)
            cnt = Counter()
            j = 0
            for i, x in enumerate(nums):
                cnt[x] += 1
                while len(cnt) > k:
                    cnt[nums[j]] -= 1
                    if cnt[nums[j]] == 0:
                        cnt.pop(nums[j])
                    j += 1
                pos[i] = j
            return pos

        return sum(a - b for a, b in zip(f(k - 1), f(k)))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
