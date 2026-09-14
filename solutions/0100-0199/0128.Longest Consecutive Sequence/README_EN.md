---
comments: true
difficulty: Medium
tags:
    - Union Find
    - Array
    - Hash Table
---

<!-- problem:start -->

# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)

## Description

<!-- description:start -->

<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,2]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

<!-- thinking:start -->

> **Thinking**
>
> Sorting and scanning runs is $O(n\log n)$; the problem asks for $O(n)$. $n \le 10^5$. Put the values in a hash set. From each $x$ still in the set, walk right until the run breaks, store that length at the start, and let earlier starts concatenate. Each number enters and leaves the set once.

<!-- thinking:end -->

We can use a hash table $\textit{s}$ to store all the elements in the array, a variable $\textit{ans}$ to record the length of the longest consecutive sequence, and a hash table $\textit{d}$ to record the length of the consecutive sequence each element $x$ belongs to.

Next, we iterate through each element $x$ in the array, using a temporary variable $y$ to record the maximum value of the current consecutive sequence, initially $y = x$. Then, we continuously try to match $y+1, y+2, y+3, \dots$ until we can no longer match. During this process, we remove the matched elements from the hash table $\textit{s}$. The length of the consecutive sequence that the current element $x$ belongs to is $d[x] = d[y] + y - x$, and then we update the answer $\textit{ans} = \max(\textit{ans}, d[x])$.

After the iteration, we return the answer $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        d = defaultdict(int)
        for x in nums:
            y = x
            while y in s:
                s.remove(y)
                y += 1
            d[x] = d[y] + y - x
            ans = max(ans, d[x])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Hash Table (Optimization)

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 stores each run's length so later starts can concatenate. If we only grow a run when $x-1$ is absent, $x$ is already a start, so the extra map $d$ is unnecessary. The code is shorter and still touches each number a constant number of times.

<!-- thinking:end -->

Similar to Solution 1, we use a hash table $\textit{s}$ to store all the elements in the array and a variable $\textit{ans}$ to record the length of the longest consecutive sequence. However, we no longer use a hash table $\textit{d}$ to record the length of the consecutive sequence each element $x$ belongs to. During the iteration, we skip elements where $x-1$ is also in the hash table $\textit{s}$. If $x-1$ is in the hash table $\textit{s}$, then $x$ is definitely not the start of a consecutive sequence, so we can directly skip $x$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for x in s:
            if x - 1 not in s:
                y = x + 1
                while y in s:
                    y += 1
                ans = max(ans, y - x)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
