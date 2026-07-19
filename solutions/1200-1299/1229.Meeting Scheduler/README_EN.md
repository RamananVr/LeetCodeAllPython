---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1229.Meeting%20Scheduler/README_EN.md
rating: 1541
source: Biweekly Contest 11 Q2
tags:
    - Array
    - Two Pointers
    - Sorting
---

<!-- problem:start -->

# [1229. Meeting Scheduler 🔒](https://leetcode.com/problems/meeting-scheduler)

## Description

<!-- description:start -->

<p>Given the availability time slots arrays <code>slots1</code> and <code>slots2</code> of two people and a meeting duration <code>duration</code>, return the <strong>earliest time slot</strong> that works for both of them and is of duration <code>duration</code>.</p>

<p>If there is no common time slot that satisfies the requirements, return an <strong>empty array</strong>.</p>

<p>The format of a time slot is an array of two elements <code>[start, end]</code> representing an inclusive time range from <code>start</code> to <code>end</code>.</p>

<p>It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots <code>[start1, end1]</code> and <code>[start2, end2]</code> of the same person, either <code>start1 &gt; end2</code> or <code>start2 &gt; end1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
<strong>Output:</strong> [60,68]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= slots1.length, slots2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>slots1[i].length, slots2[i].length == 2</code></li>
	<li><code>slots1[i][0] &lt; slots1[i][1]</code></li>
	<li><code>slots2[i][0] &lt; slots2[i][1]</code></li>
	<li><code>0 &lt;= slots1[i][j], slots2[i][j] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= duration &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Two Pointers

We can sort the free time intervals of both people, then use two pointers to traverse the two arrays and find the intersection of the free time intervals of both people. If the length of the intersection is greater than or equal to `duration`, return the start time of the intersection and the start time plus `duration`. Otherwise, if the end time of the first person's free time interval is less than the end time of the second person's free time interval, move the first person's pointer; otherwise, move the second person's pointer. Continue traversing until a suitable time interval is found or the traversal ends.

The time complexity is $O(m \times \log m + n \times \log n)$, and the space complexity is $O(\log m + \log n)$. Here, $m$ and $n$ are the lengths of the two arrays, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots1.sort()
        slots2.sort()
        m, n = len(slots1), len(slots2)
        i = j = 0
        while i < m and j < n:
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
