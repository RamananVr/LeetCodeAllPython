---
comments: true
difficulty: Hard
rating: 2381
source: Biweekly Contest 82 Q4
tags:
    - Stack
    - Union Find
    - Array
    - Monotonic Stack
---

<!-- problem:start -->

# [2334. Subarray With Elements Greater Than Varying Threshold](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and an integer <code>threshold</code>.</p>

<p>Find any subarray of <code>nums</code> of length <code>k</code> such that <strong>every</strong> element in the subarray is <strong>greater</strong> than <code>threshold / k</code>.</p>

<p>Return<em> the <strong>size</strong> of <strong>any</strong> such subarray</em>. If there is no such subarray, return <code>-1</code>.</p>

<p>A <strong>subarray</strong> is a contiguous non-empty sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,4,3,1], threshold = 6
<strong>Output:</strong> 3
<strong>Explanation:</strong> The subarray [3,4,3] has a size of 3, and every element is greater than 6 / 3 = 2.
Note that this is the only valid subarray.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,6,5,8], threshold = 7
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [8] has a size of 1, and 8 &gt; 7 / 1 = 7. So 1 is returned.
Note that the subarray [6,5] has a size of 2, and every element is greater than 7 / 2 = 3.5. 
Similarly, the subarrays [6,5,6], [6,5,6,5], [6,5,6,5,8] also satisfy the given conditions.
Therefore, 2, 3, 4, or 5 may also be returned.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], threshold &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> We need a subarray of length $k$ whose minimum exceeds $\textit{threshold}/k$. $n \le 10^5$, so scanning ranges is too slow. The longest span where a value is the minimum is bounded by nearer smaller elements.
>
> Insert values from large to small and union already-present neighbors. Then $v$ is the minimum of its component; if $v > \textit{threshold}/sz$ we are done.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def merge(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            p[pa] = pb
            size[pb] += size[pa]

        n = len(nums)
        p = list(range(n))
        size = [1] * n
        arr = sorted(zip(nums, range(n)), reverse=True)
        vis = [False] * n
        for v, i in arr:
            if i and vis[i - 1]:
                merge(i, i - 1)
            if i < n - 1 and vis[i + 1]:
                merge(i, i + 1)
            if v > threshold // size[find(i)]:
                return size[find(i)]
            vis[i] = True
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Union-find needs a sort and a log factor. A monotonic stack finds each index’s range as a minimum in linear time, yielding $k$ and the same inequality without merging by value.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stk = []
        for i, v in enumerate(nums):
            while stk and nums[stk[-1]] >= v:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        for i, v in enumerate(nums):
            k = right[i] - left[i] - 1
            if v > threshold // k:
                return k
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
