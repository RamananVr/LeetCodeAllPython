---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1235.Maximum%20Profit%20in%20Job%20Scheduling/README_EN.md
rating: 2022
source: Weekly Contest 159 Q4
tags:
    - Array
    - Binary Search
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling)

## Description

<!-- description:start -->

<p>We have <code>n</code> jobs, where every job is scheduled to be done from <code>startTime[i]</code> to <code>endTime[i]</code>, obtaining a profit of <code>profit[i]</code>.</p>

<p>You&#39;re given the <code>startTime</code>, <code>endTime</code> and <code>profit</code> arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.</p>

<p>If you choose a job that ends at time <code>X</code> you will be able to start another job that starts at time <code>X</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1235.Maximum%20Profit%20in%20Job%20Scheduling/images/sample1_1584.png" style="width: 380px; height: 154px;" /></strong></p>

<pre>
<strong>Input:</strong> startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
<strong>Output:</strong> 120
<strong>Explanation:</strong> The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1235.Maximum%20Profit%20in%20Job%20Scheduling/images/sample22_1584.png" style="width: 600px; height: 112px;" /> </strong></p>

<pre>
<strong>Input:</strong> startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
<strong>Output:</strong> 150
<strong>Explanation:</strong> The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1235.Maximum%20Profit%20in%20Job%20Scheduling/images/sample3_1584.png" style="width: 400px; height: 112px;" /></strong></p>

<pre>
<strong>Input:</strong> startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= startTime.length == endTime.length == profit.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= startTime[i] &lt; endTime[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= profit[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search + Binary Search

First, we sort the jobs by start time in ascending order, then design a function $dfs(i)$ to represent the maximum profit that can be obtained starting from the $i$-th job. The answer is $dfs(0)$.

The calculation process of function $dfs(i)$ is as follows:

For the $i$-th job, we can choose to do it or not. If we don't do it, the maximum profit is $dfs(i + 1)$; if we do it, we can use binary search to find the first job that starts after the end time of the $i$-th job, denoted as $j$, then the maximum profit is $profit[i] + dfs(j)$. We take the larger of the two. That is:

$$
dfs(i)=\max(dfs(i+1),profit[i]+dfs(j))
$$

Where $j$ is the smallest index that satisfies $startTime[j] \ge endTime[i]$.

In this process, we can use memoization search to save the answer of each state to avoid repeated calculations.

The time complexity is $O(n \times \log n)$, where $n$ is the number of jobs.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        @cache
        def dfs(i):
            if i >= n:
                return 0
            _, e, p = jobs[i]
            j = bisect_left(jobs, e, lo=i + 1, key=lambda x: x[0])
            return max(dfs(i + 1), p + dfs(j))

        jobs = sorted(zip(startTime, endTime, profit))
        n = len(profit)
        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming + Binary Search

We can also change the memoization search in Solution 1 to dynamic programming.

First, sort the jobs, this time we sort by end time in ascending order, then define $dp[i]$, which represents the maximum profit that can be obtained from the first $i$ jobs. The answer is $dp[n]$. Initialize $dp[0]=0$.

For the $i$-th job, we can choose to do it or not. If we don't do it, the maximum profit is $dp[i]$; if we do it, we can use binary search to find the last job that ends before the start time of the $i$-th job, denoted as $j$, then the maximum profit is $profit[i] + dp[j]$. We take the larger of the two. That is:

$$
dp[i+1] = \max(dp[i], profit[i] + dp[j])
$$

Where $j$ is the largest index that satisfies $endTime[j] \leq startTime[i]$.

The time complexity is $O(n \times \log n)$, where $n$ is the number of jobs.

Similar problems:

- [2008. Maximum Earnings From Taxi](https://github.com/doocs/leetcode/blob/main/solution/2000-2099/2008.Maximum%20Earnings%20From%20Taxi/README.md)
- [1751. Maximum Number of Events That Can Be Attended II](https://github.com/doocs/leetcode/blob/main/solution/1700-1799/1751.Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended%20II/README.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(profit)
        dp = [0] * (n + 1)
        for i, (_, s, p) in enumerate(jobs):
            j = bisect_right(jobs, s, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[j] + p)
        return dp[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
