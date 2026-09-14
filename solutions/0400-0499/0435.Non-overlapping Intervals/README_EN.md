---
comments: true
difficulty: Medium
tags:
    - Greedy
    - Array
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals)

## Description

<!-- description:start -->

<p>Given an array of intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</em>.</p>

<p><strong>Note</strong> that intervals which only touch at a point are <strong>non-overlapping</strong>. For example, <code>[1, 2]</code> and <code>[2, 3]</code> are non-overlapping.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> [1,3] can be removed and the rest of the intervals are non-overlapping.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[1,2],[1,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need to remove two [1,2] to make the rest of the intervals non-overlapping.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Greedy

<!-- thinking:start -->

> **Thinking**
>
> Removing the fewest intervals so the rest are disjoint is the same as keeping the largest set of non-overlapping intervals. Subset search is too large.
>
> Sort by right endpoint and keep an interval when it starts at or after the last kept end. The earliest finish leaves the most room, which is why we sort by the right end.
>
> The answer starts at $n$ and decreases once per kept interval: total minus the size of a maximum compatible set.

<!-- thinking:end -->

We first sort the intervals in ascending order by their right boundary. We use a variable $\textit{pre}$ to record the right boundary of the previous interval and a variable $\textit{ans}$ to record the number of intervals that need to be removed. Initially, $\textit{ans} = \textit{intervals.length}$.

Then we iterate through the intervals. For each interval:

- If the left boundary of the current interval is greater than or equal to $\textit{pre}$, it means that this interval does not need to be removed. We directly update $\textit{pre}$ to the right boundary of the current interval and decrement $\textit{ans}$ by one;
- Otherwise, it means that this interval needs to be removed, and we do not need to update $\textit{pre}$ and $\textit{ans}$.

Finally, we return $\textit{ans}$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(\log n)$, where $n$ is the number of intervals.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = len(intervals)
        pre = -inf
        for l, r in intervals:
            if pre <= l:
                ans -= 1
                pre = r
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
