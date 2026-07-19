---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1751.Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended%20II/README_EN.md
rating: 2040
source: Biweekly Contest 45 Q4
tags:
    - Array
    - Binary Search
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [1751. Maximum Number of Events That Can Be Attended II](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii)

## Description

<!-- description:start -->

<p>You are given an array of <code>events</code> where <code>events[i] = [startDay<sub>i</sub>, endDay<sub>i</sub>, value<sub>i</sub>]</code>. The <code>i<sup>th</sup></code> event starts at <code>startDay<sub>i</sub></code><sub> </sub>and ends at <code>endDay<sub>i</sub></code>, and if you attend this event, you will receive a value of <code>value<sub>i</sub></code>. You are also given an integer <code>k</code> which represents the maximum number of events you can attend.</p>

<p>You can only attend one event at a time. If you choose to attend an event, you must attend the <strong>entire</strong> event. Note that the end day is <strong>inclusive</strong>: that is, you cannot attend two events where one of them starts and the other ends on the same day.</p>

<p>Return <em>the <strong>maximum sum</strong> of values that you can receive by attending events.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1700-1799/1751.Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended%20II/images/screenshot-2021-01-11-at-60048-pm.png" style="width: 400px; height: 103px;" /></p>

<pre>
<strong>Input:</strong> events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
<strong>Output:</strong> 7
<strong>Explanation: </strong>Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1700-1799/1751.Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended%20II/images/screenshot-2021-01-11-at-60150-pm.png" style="width: 400px; height: 103px;" /></p>

<pre>
<strong>Input:</strong> events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
<strong>Output:</strong> 10
<strong>Explanation:</strong> Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do <strong>not</strong> have to attend k events.</pre>

<p><strong class="example">Example 3:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1700-1799/1751.Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended%20II/images/screenshot-2021-01-11-at-60703-pm.png" style="width: 400px; height: 126px;" /></strong></p>

<pre>
<strong>Input:</strong> events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
<strong>Output:</strong> 9
<strong>Explanation:</strong> Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= events.length</code></li>
	<li><code>1 &lt;= k * events.length &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= startDay<sub>i</sub> &lt;= endDay<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= value<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization + Binary Search

First, we sort the events by their start time in ascending order. Then, we define a function $\text{dfs}(i, k)$, which represents the maximum total value achievable by attending at most $k$ events starting from the $i$-th event. The answer is $\text{dfs}(0, k)$.

The calculation process of the function $\text{dfs}(i, k)$ is as follows:

If we do not attend the $i$-th event, the maximum value is $\text{dfs}(i + 1, k)$. If we attend the $i$-th event, we can use binary search to find the first event whose start time is greater than the end time of the $i$-th event, denoted as $j$. Then, the maximum value is $\text{dfs}(j, k - 1) + \text{value}[i]$. We take the maximum of the two options:

$$
\text{dfs}(i, k) = \max(\text{dfs}(i + 1, k), \text{dfs}(j, k - 1) + \text{value}[i])
$$

Here, $j$ is the index of the first event whose start time is greater than the end time of the $i$-th event, which can be found using binary search.

Since the calculation of $\text{dfs}(i, k)$ involves calls to $\text{dfs}(i + 1, k)$ and $\text{dfs}(j, k - 1)$, we can use memoization to store the computed values and avoid redundant calculations.

The time complexity is $O(n \times \log n + n \times k)$, and the space complexity is $O(n \times k)$, where $n$ is the number of events.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @cache
        def dfs(i: int, k: int) -> int:
            if i >= len(events):
                return 0
            _, ed, val = events[i]
            ans = dfs(i + 1, k)
            if k:
                j = bisect_right(events, ed, lo=i + 1, key=lambda x: x[0])
                ans = max(ans, dfs(j, k - 1) + val)
            return ans

        events.sort()
        return dfs(0, k)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming + Binary Search

We can convert the memoization approach in Solution 1 to dynamic programming.

First, sort the events, this time by end time in ascending order. Then define $f[i][j]$ as the maximum total value by attending at most $j$ events among the first $i$ events. The answer is $f[n][k]$.

For the $i$-th event, we can choose to attend it or not. If we do not attend, the maximum value is $f[i][j]$. If we attend, we can use binary search to find the last event whose end time is less than the start time of the $i$-th event, denoted as $h$. Then the maximum value is $f[h + 1][j - 1] + \text{value}[i]$. We take the maximum of the two options:

$$
f[i + 1][j] = \max(f[i][j], f[h + 1][j - 1] + \text{value}[i])
$$

Here, $h$ is the last event whose end time is less than the start time of the $i$-th event, which can be found by binary search.

The time complexity is $O(n \times \log n + n \times k)$, and the space complexity is $O(n \times k)$, where $n$ is the number of events.

Related problems:

- [1235. Maximum Profit in Job Scheduling](https://github.com/doocs/leetcode/blob/main/solution/1200-1299/1235.Maximum%20Profit%20in%20Job%20Scheduling/README_EN.md)
- [2008. Maximum Earnings From Taxi](https://github.com/doocs/leetcode/blob/main/solution/2000-2099/2008.Maximum%20Earnings%20From%20Taxi/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i, (st, _, val) in enumerate(events, 1):
            p = bisect_left(events, st, hi=i - 1, key=lambda x: x[1])
            for j in range(1, k + 1):
                f[i][j] = max(f[i - 1][j], f[p][j - 1] + val)
        return f[n][k]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
