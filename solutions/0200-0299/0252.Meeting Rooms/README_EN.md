---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0252.Meeting%20Rooms/README_EN.md
tags:
    - Array
    - Sorting
---

<!-- problem:start -->

# [252. Meeting Rooms 🔒](https://leetcode.com/problems/meeting-rooms)

## Description

<!-- description:start -->

<p>You are given an array of meeting times&nbsp;<code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>.</p>

<p>A person can attend all meetings if no two meeting intervals overlap. Meetings ending at time <code>t</code> and starting at time <code>t</code> <strong>do not</strong> overlap.</p>

<p>​​​​​​​Return <code>true</code> if a person can attend all meetings. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[0,30],[5,10],[15,20]]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[7,10],[2,4]]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;&nbsp;end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting

We sort the meetings based on their start times, and then iterate through the sorted meetings. If the start time of the current meeting is less than the end time of the previous meeting, it indicates that there is an overlap between the two meetings, and we return `false`. Otherwise, we continue iterating.

If no overlap is found by the end of the iteration, we return `true`.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(\log n)$, where $n$ is the number of meetings.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(a[1] <= b[0] for a, b in pairwise(intervals))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
