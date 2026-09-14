---
comments: true
difficulty: Medium
tags:
    - Array
    - Two Pointers
---

<!-- problem:start -->

# [795. Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> and two integers <code>left</code> and <code>right</code>, return <em>the number of contiguous non-empty <strong>subarrays</strong> such that the value of the maximum array element in that subarray is in the range </em><code>[left, right]</code>.</p>

<p>The test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,4,3], left = 2, right = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three subarrays that meet the requirements: [2], [2, 1], [3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,9,2,5,6], left = 2, right = 8
<strong>Output:</strong> 7
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= left &lt;= right &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Count subarrays whose maximum lies in $[left,right]$. $n\le 10^5$. That is (max $\le right$) minus (max $\le left-1$).
>
> $f(x)$ walks once: grow a valid suffix while $v\le x$ and add its length, else reset.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def f(x):
            cnt = t = 0
            for v in nums:
                t = 0 if v > x else t + 1
                cnt += t
            return cnt

        return f(right) - f(left - 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> The difference of $f$ hides who the maximum is. A monotonic stack finds the nearest stricter left greater and non-stricter right greater; the span $(i-l)(r-i)$ counts if $nums[i]$ is in range.
>
> Asymmetric bounds assign a unique maximum when values tie.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        l, r = [-1] * n, [n] * n
        stk = []
        for i, v in enumerate(nums):
            while stk and nums[stk[-1]] <= v:
                stk.pop()
            if stk:
                l[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
            if stk:
                r[i] = stk[-1]
            stk.append(i)
        return sum(
            (i - l[i]) * (r[i] - i) for i, v in enumerate(nums) if left <= v <= right
        )
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
