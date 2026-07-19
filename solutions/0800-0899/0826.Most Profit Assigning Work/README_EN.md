---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0826.Most%20Profit%20Assigning%20Work/README_EN.md
tags:
    - Greedy
    - Array
    - Two Pointers
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [826. Most Profit Assigning Work](https://leetcode.com/problems/most-profit-assigning-work)

## Description

<!-- description:start -->

<p>You have <code>n</code> jobs and <code>m</code> workers. You are given three arrays: <code>difficulty</code>, <code>profit</code>, and <code>worker</code> where:</p>

<ul>
	<li><code>difficulty[i]</code> and <code>profit[i]</code> are the difficulty and the profit of the <code>i<sup>th</sup></code> job, and</li>
	<li><code>worker[j]</code> is the ability of <code>j<sup>th</sup></code> worker (i.e., the <code>j<sup>th</sup></code> worker can only complete a job with difficulty at most <code>worker[j]</code>).</li>
</ul>

<p>Every worker can be assigned <strong>at most one job</strong>, but one job can be <strong>completed multiple times</strong>.</p>

<ul>
	<li>For example, if three workers attempt the same job that pays <code>$1</code>, then the total profit will be <code>$3</code>. If a worker cannot complete any job, their profit is <code>$0</code>.</li>
</ul>

<p>Return the maximum profit we can achieve after assigning the workers to the jobs.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
<strong>Output:</strong> 100
<strong>Explanation:</strong> Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == difficulty.length</code></li>
	<li><code>n == profit.length</code></li>
	<li><code>m == worker.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= difficulty[i], profit[i], worker[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Two Pointers

We can sort the jobs in ascending order of ability, and then sort the jobs in ascending order of difficulty.

Then we traverse the workers. For each worker, we find the job with the maximum profit that he can complete, and then add this profit to the answer.

The time complexity is $O(n \times \log n + m \times \log m)$, and the space complexity is $O(n)$. Where $n$ and $m$ are the lengths of the arrays `profit` and `worker` respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        worker.sort()
        jobs = sorted(zip(difficulty, profit))
        ans = mx = i = 0
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                mx = max(mx, jobs[i][1])
                i += 1
            ans += mx
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

Let's denote $m = \max(\textit{difficulty})$ and define an array $f$ of length $m + 1$, where $f[i]$ represents the maximum profit among jobs with difficulty less than or equal to $i$, initially $f[i] = 0$.

Then, we iterate over the jobs, and for each job $(d, p)$, if $d \leq m$, we update $f[d] = \max(f[d], p)$.

Next, we iterate from $1$ to $m$, and for each $i$, we update $f[i] = \max(f[i], f[i - 1])$.

Finally, we iterate over the workers, and for each worker $w$, we add $f[w]$ to the answer.

The time complexity is $O(n + M)$, and the space complexity is $O(M)$. Here, $n$ is the length of the `profit` array, and $M$ is the maximum value in the `difficulty` array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        m = max(difficulty)
        f = [0] * (m + 1)
        for d, p in zip(difficulty, profit):
            f[d] = max(f[d], p)
        for i in range(1, m + 1):
            f[i] = max(f[i], f[i - 1])
        return sum(f[min(w, m)] for w in worker)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
