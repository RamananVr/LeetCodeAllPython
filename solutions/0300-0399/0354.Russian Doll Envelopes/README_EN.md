---
comments: true
difficulty: Hard
tags:
    - Array
    - Binary Search
    - Dynamic Programming
    - Sorting
    - Longest Increasing Subsequence
---

<!-- problem:start -->

# [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes)

## Description

<!-- description:start -->

<p>You are given a 2D array of integers <code>envelopes</code> where <code>envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]</code> represents the width and the height of an envelope.</p>

<p>One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope&#39;s width and height.</p>

<p>Return <em>the maximum number of envelopes you can Russian doll (i.e., put one inside the other)</em>.</p>

<p><strong>Note:</strong> You cannot rotate an envelope.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> envelopes = [[5,4],[6,4],[6,7],[2,3]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The maximum number of envelopes you can Russian doll is <code>3</code> ([2,3] =&gt; [5,4] =&gt; [6,7]).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> envelopes = [[1,1],[1,1],[1,1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= envelopes.length &lt;= 10<sup>5</sup></code></li>
	<li><code>envelopes[i].length == 2</code></li>
	<li><code>1 &lt;= w<sub>i</sub>, h<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> An envelope nests only if both width and height increase; we want the longest chain. A 2D $O(n^2)$ LIS fails for $n\le 10^5$. After sorting by width, LIS on height is the answer; equal widths must not nest.
>
> Sort by width ascending and height descending, then greedy LIS on heights: append if larger than the tail, else binary-replace. Descending heights keep at most one envelope per width.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        d = [envelopes[0][1]]
        for _, h in envelopes[1:]:
            if h > d[-1]:
                d.append(h)
            else:
                idx = bisect_left(d, h)
                d[idx] = h
        return len(d)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
