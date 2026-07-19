---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0539.Minimum%20Time%20Difference/README_EN.md
tags:
    - Array
    - Math
    - String
    - Sorting
---

<!-- problem:start -->

# [539. Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference)

## Description

<!-- description:start -->

Given a list of 24-hour clock time points in <strong>&quot;HH:MM&quot;</strong> format, return <em>the minimum <b>minutes</b> difference between any two time-points in the list</em>.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> timePoints = ["23:59","00:00"]
<strong>Output:</strong> 1
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> timePoints = ["00:00","23:59","00:00"]
<strong>Output:</strong> 0
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= timePoints.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>timePoints[i]</code> is in the format <strong>&quot;HH:MM&quot;</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting

We notice that there can be at most $24 \times 60 = 1440$ distinct time points. Therefore, if the length of $timePoints$ exceeds $1440$, it implies there are duplicate time points, and we can return $0$ early.

Next, we iterate through the list of time points and convert it into a list of minutes $nums$. For example, for the time point `13:14`, we convert it into $13 \times 60 + 14$.

Then, we sort the list of minutes in ascending order and append the smallest time $nums[0]$ plus $1440$ to the end of the list. This step is to handle the special case of the difference between the maximum and minimum values.

Finally, we iterate through the list of minutes to find the minimum difference between any two adjacent times.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of time points.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        nums = sorted(int(x[:2]) * 60 + int(x[3:]) for x in timePoints)
        nums.append(nums[0] + 1440)
        return min(b - a for a, b in pairwise(nums))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
