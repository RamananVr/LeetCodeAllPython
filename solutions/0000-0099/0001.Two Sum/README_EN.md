---
comments: true
difficulty: Easy
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [1. Two Sum](https://leetcode.com/problems/two-sum)

## Description

<!-- description:start -->

<p>You are given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

<!-- thinking:start -->

> **Thinking**
>
> The first idea is a nested loop: pick $x$, then scan for $target-x$. Correct, but $O(n^2)$. $n \le 10^4$ might pass, yet the follow-up asks for faster.
>
> The bottleneck is repeatedly searching for the complement among numbers already seen. A hash table makes that lookup expected $O(1)$. Walk once, storing value $\to$ index: when we see $x$, ask whether $target-x$ already appeared; if yes, return the two indices; if not, store $x$.
>
> Look up before inserting. Insert-then-lookup would reuse the same index on $[3,3]$, $target=6$. Lookup-first guarantees the match is an earlier index.

<!-- thinking:end -->

We can use a hash table $\textit{d}$ to store each element and its corresponding index.

Traverse the array $\textit{nums}$, for the current element $\textit{nums}[i]$, we first check if $\textit{target} - \textit{nums}[i]$ is in the hash table $\textit{d}$. If it is in $\textit{d}$, it means the $\textit{target}$ value has been found, and we return the indices of $\textit{target} - \textit{nums}[i]$ and $i$.

Time complexity is $O(n)$, and space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            if (y := target - x) in d:
                return [d[y], i]
            d[x] = i
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
