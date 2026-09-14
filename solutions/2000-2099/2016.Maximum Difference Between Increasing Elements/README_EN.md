---
comments: true
difficulty: Easy
rating: 1246
source: Weekly Contest 260 Q1
tags:
    - Array
---

<!-- problem:start -->

# [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements)

## Description

<!-- description:start -->

<p>Given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>n</code>, find the <strong>maximum difference</strong> between <code>nums[i]</code> and <code>nums[j]</code> (i.e., <code>nums[j] - nums[i]</code>), such that <code>0 &lt;= i &lt; j &lt; n</code> and <code>nums[i] &lt; nums[j]</code>.</p>

<p>Return <em>the <strong>maximum difference</strong>. </em>If no such <code>i</code> and <code>j</code> exists, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,<strong><u>1</u></strong>,<strong><u>5</u></strong>,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i &gt; j, so it is not valid.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,4,3,2]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There is no i and j such that i &lt; j and nums[i] &lt; nums[j].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [<strong><u>1</u></strong>,5,2,<strong><u>10</u></strong>]
<strong>Output:</strong> 9
<strong>Explanation:</strong>
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Maintaining Prefix Minimum

<!-- thinking:start -->

> **Thinking**
>
> $n \le 1000$ allows a double loop, but we only need the maximum $nums[j]-nums[i]$ with $i<j$. For a fixed right end, the best left is the prefix minimum.
>
> Track $mi$: if $x>mi$ update the difference, otherwise replace $mi$ with $x$. Keep $-1$ when no increasing pair exists.

<!-- thinking:end -->

We use a variable $\textit{mi}$ to represent the minimum value among the elements currently being traversed, and a variable $\textit{ans}$ to represent the maximum difference. Initially, $\textit{mi}$ is set to $+\infty$, and $\textit{ans}$ is set to $-1$.

Traverse the array. For the current element $x$, if $x \gt \textit{mi}$, update $\textit{ans}$ to $\max(\textit{ans}, x - \textit{mi})$. Otherwise, update $\textit{mi}$ to $x$.

After the traversal, return $\textit{ans}$.

Time complexity is $O(n)$, where $n$ is the length of the array. Space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mi = inf
        ans = -1
        for x in nums:
            if x > mi:
                ans = max(ans, x - mi)
            else:
                mi = x
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
