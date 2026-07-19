---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1184.Distance%20Between%20Bus%20Stops/README_EN.md
rating: 1234
source: Weekly Contest 153 Q1
tags:
    - Array
---

<!-- problem:start -->

# [1184. Distance Between Bus Stops](https://leetcode.com/problems/distance-between-bus-stops)

## Description

<!-- description:start -->

<p>A bus&nbsp;has <code>n</code> stops numbered from <code>0</code> to <code>n - 1</code> that form&nbsp;a circle. We know the distance between all pairs of neighboring stops where <code>distance[i]</code> is the distance between the stops number&nbsp;<code>i</code> and <code>(i + 1) % n</code>.</p>

<p>The bus goes along both directions&nbsp;i.e. clockwise and counterclockwise.</p>

<p>Return the shortest distance between the given&nbsp;<code>start</code>&nbsp;and <code>destination</code>&nbsp;stops.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1184.Distance%20Between%20Bus%20Stops/images/untitled-diagram-1.jpg" style="width: 388px; height: 240px;" /></p>

<pre>

<strong>Input:</strong> distance = [1,2,3,4], start = 0, destination = 1

<strong>Output:</strong> 1

<strong>Explanation:</strong> Distance between 0 and 1 is 1 or 9, minimum is 1.</pre>

<p>&nbsp;</p>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1184.Distance%20Between%20Bus%20Stops/images/untitled-diagram-1-1.jpg" style="width: 388px; height: 240px;" /></p>

<pre>

<strong>Input:</strong> distance = [1,2,3,4], start = 0, destination = 2

<strong>Output:</strong> 3

<strong>Explanation:</strong> Distance between 0 and 2 is 3 or 7, minimum is 3.

</pre>

<p>&nbsp;</p>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1184.Distance%20Between%20Bus%20Stops/images/untitled-diagram-1-2.jpg" style="width: 388px; height: 240px;" /></p>

<pre>

<strong>Input:</strong> distance = [1,2,3,4], start = 0, destination = 3

<strong>Output:</strong> 4

<strong>Explanation:</strong> Distance between 0 and 3 is 6 or 4, minimum is 4.

</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>1 &lt;= n&nbsp;&lt;= 10^4</code></li>

    <li><code>distance.length == n</code></li>

    <li><code>0 &lt;= start, destination &lt; n</code></li>

    <li><code>0 &lt;= distance[i] &lt;= 10^4</code></li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We can first calculate the total distance $s$ that the bus travels, then simulate the bus's journey. Starting from the departure point, we move one stop to the right each time until we reach the destination, recording the travel distance $t$ during this process. Finally, we return the minimum value between $t$ and $s - t$.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{distance}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        s = sum(distance)
        t, n = 0, len(distance)
        while start != destination:
            t += distance[start]
            start = (start + 1) % n
        return min(t, s - t)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
