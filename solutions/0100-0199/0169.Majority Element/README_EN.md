---
comments: true
difficulty: Easy
tags:
    - Array
    - Hash Table
    - Divide and Conquer
    - Counting
    - Sorting
    - Boyer-Moore Voting
---

<!-- problem:start -->

# [169. Majority Element](https://leetcode.com/problems/majority-element)

## Description

<!-- description:start -->

<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The input is generated such that a majority element will exist in the array.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Moore Voting Algorithm

<!-- thinking:start -->

> **Thinking**
>
> The majority value appears more than $\lfloor n/2\rfloor$ times and is guaranteed. Counting or sorting works; the follow-up wants $O(n)$ time and $O(1)$ space. $n\le 5\times 10^4$.
>
> Boyer–Moore cancels distinct values in pairs. When the counter hits zero we change candidate. The majority cannot be fully cancelled, so the candidate after one pass is the answer; a second pass is unnecessary.

<!-- thinking:end -->

The basic steps of the Moore voting algorithm are as follows:

Initialize the element $m$ and initialize the counter $cnt = 0$. Then, for each element $x$ in the input list:

1. If $cnt = 0$, then $m = x$ and $cnt = 1$;
1. Otherwise, if $m = x$, then $cnt = cnt + 1$, otherwise $cnt = cnt - 1$.

In general, the Moore voting algorithm requires **two passes** over the input list. In the first pass, we generate the candidate value $m$, and if there is a majority, the candidate value is the majority value. In the second pass, we simply compute the frequency of the candidate value to confirm whether it is the majority value. Since this problem has clearly stated that there is a majority value, we can directly return $m$ after the first pass, without the need for a second pass to confirm whether it is the majority value.

The time complexity is $O(n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = m = 0
        for x in nums:
            if cnt == 0:
                m, cnt = x, 1
            else:
                cnt += 1 if m == x else -1
        return m
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
