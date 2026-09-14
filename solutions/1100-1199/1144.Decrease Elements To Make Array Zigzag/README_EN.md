---
comments: true
difficulty: Medium
rating: 1558
source: Weekly Contest 148 Q1
tags:
    - Greedy
    - Array
---

<!-- problem:start -->

# [1144. Decrease Elements To Make Array Zigzag](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag)

## Description

<!-- description:start -->

<p>Given an array <code>nums</code> of integers, a <em>move</em>&nbsp;consists of choosing any element and <strong>decreasing it by 1</strong>.</p>

<p>An array <code>A</code> is a&nbsp;<em>zigzag array</em>&nbsp;if either:</p>

<ul>
	<li>Every even-indexed element is greater than adjacent elements, ie.&nbsp;<code>A[0] &gt; A[1] &lt; A[2] &gt; A[3] &lt; A[4] &gt; ...</code></li>
	<li>OR, every odd-indexed element is greater than adjacent elements, ie.&nbsp;<code>A[0] &lt; A[1] &gt; A[2] &lt; A[3] &gt; A[4] &lt; ...</code></li>
</ul>

<p>Return the minimum number of moves to transform the given array <code>nums</code> into a zigzag array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can decrease 2 to 0 or 3 to 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,6,1,6,2]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration + Greedy

<!-- thinking:start -->

> **Thinking**
>
> We may only decrease values. A zigzag is either “even indices smaller” or “odd indices smaller”; compute both and keep the cheaper. For an index that must become smaller, the needed decrease is determined by its two neighbors, and those positions do not interfere.

<!-- thinking:end -->

We can separately enumerate the even and odd positions as the elements "smaller than adjacent elements", and then calculate the required number of operations. The minimum of the two is taken.

The time complexity is $O(n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        ans = [0, 0]
        n = len(nums)
        for i in range(2):
            for j in range(i, n, 2):
                d = 0
                if j:
                    d = max(d, nums[j] - nums[j - 1] + 1)
                if j < n - 1:
                    d = max(d, nums[j] - nums[j + 1] + 1)
                ans[i] += d
        return min(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
