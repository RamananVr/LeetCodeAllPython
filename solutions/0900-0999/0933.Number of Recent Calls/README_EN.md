---
comments: true
difficulty: Easy
tags:
    - Design
    - Queue
    - Data Stream
---

<!-- problem:start -->

# [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls)

## Description

<!-- description:start -->

<p>You have a <code>RecentCounter</code> class which counts the number of recent requests within a certain time frame.</p>

<p>Implement the <code>RecentCounter</code> class:</p>

<ul>
	<li><code>RecentCounter()</code> Initializes the counter with zero recent requests.</li>
	<li><code>int ping(int t)</code> Adds a new request at time <code>t</code>, where <code>t</code> represents some time in milliseconds, and returns the number of requests that has happened in the past <code>3000</code> milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range <code>[t - 3000, t]</code>.</li>
</ul>

<p>It is <strong>guaranteed</strong> that every call to <code>ping</code> uses a strictly larger value of <code>t</code> than the previous call.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;RecentCounter&quot;, &quot;ping&quot;, &quot;ping&quot;, &quot;ping&quot;, &quot;ping&quot;]
[[], [1], [100], [3001], [3002]]
<strong>Output</strong>
[null, 1, 2, 3, 3]

<strong>Explanation</strong>
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [<u>1</u>], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [<u>1</u>, <u>100</u>], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [<u>1</u>, <u>100</u>, <u>3001</u>], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, <u>100</u>, <u>3001</u>, <u>3002</u>], range is [2,3002], return 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= t &lt;= 10<sup>9</sup></code></li>
	<li>Each test case will call <code>ping</code> with <strong>strictly increasing</strong> values of <code>t</code>.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>ping</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> $t$ is strictly increasing, so a request older than $t-3000$ never returns. Store times in a queue and pop from the front while expired; the queue size is the answer.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> The queue is amortized linear. Because times are sorted, we may keep them in an array and binary-search the first index $\ge t-3000$; the suffix length is the count. Extra space stays linear, and each query pays a logarithm.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class RecentCounter:
    def __init__(self):
        self.s = []

    def ping(self, t: int) -> int:
        self.s.append(t)
        return len(self.s) - bisect_left(self.s, t - 3000)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
