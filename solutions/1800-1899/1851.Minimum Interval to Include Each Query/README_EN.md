---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1851.Minimum%20Interval%20to%20Include%20Each%20Query/README_EN.md
rating: 2286
source: Weekly Contest 239 Q4
tags:
    - Array
    - Binary Search
    - Sorting
    - Sweep Line
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query)

## Description

<!-- description:start -->

<p>You are given a 2D integer array <code>intervals</code>, where <code>intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]</code> describes the <code>i<sup>th</sup></code> interval starting at <code>left<sub>i</sub></code> and ending at <code>right<sub>i</sub></code> <strong>(inclusive)</strong>. The <strong>size</strong> of an interval is defined as the number of integers it contains, or more formally <code>right<sub>i</sub> - left<sub>i</sub> + 1</code>.</p>

<p>You are also given an integer array <code>queries</code>. The answer to the <code>j<sup>th</sup></code> query is the <strong>size of the smallest interval</strong> <code>i</code> such that <code>left<sub>i</sub> &lt;= queries[j] &lt;= right<sub>i</sub></code>. If no such interval exists, the answer is <code>-1</code>.</p>

<p>Return <em>an array containing the answers to the queries</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
<strong>Output:</strong> [3,3,1,4]
<strong>Explanation:</strong> The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
<strong>Output:</strong> [2,-1,4,6]
<strong>Explanation:</strong> The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>1 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt;= 10<sup>7</sup></code></li>
	<li><code>1 &lt;= queries[j] &lt;= 10<sup>7</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Offline Query + Priority Queue (Min Heap)

We notice that the order of queries does not affect the answer, and the intervals involved do not change. Therefore, we consider sorting all queries in ascending order, and sorting all intervals in ascending order of the left endpoint.

We use a priority queue (min heap) $pq$ to maintain all current intervals. Each element in the queue is a pair $(v, r)$, representing an interval with length $v$ and right endpoint $r$. Initially, the priority queue is empty. In addition, we define a pointer $i$ that points to the current interval being traversed, and initially $i=0$.

We traverse each query $(x, j)$ in ascending order and perform the following operations:

- If the pointer $i$ has not traversed all intervals, and the left endpoint of the current interval $[a, b]$ is less than or equal to $x$, then we add this interval to the priority queue and move the pointer $i$ one step forward. Repeat this process.
- If the priority queue is not empty, and the right endpoint of the heap top element is less than $x$, then we pop the heap top element. Repeat this process.
- At this point, if the priority queue is not empty, then the heap top element is the smallest interval containing $x$. We add its length $v$ to the answer array $ans$.

After the above process is over, we return the answer array $ans$.

The time complexity is $O(n \times \log n + m \times \log m)$, and the space complexity is $O(n + m)$. Where $n$ and $m$ are the lengths of the arrays `intervals` and `queries` respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(intervals), len(queries)
        intervals.sort()
        queries = sorted((x, i) for i, x in enumerate(queries))
        ans = [-1] * m
        pq = []
        i = 0
        for x, j in queries:
            while i < n and intervals[i][0] <= x:
                a, b = intervals[i]
                heappush(pq, (b - a + 1, b))
                i += 1
            while pq and pq[0][1] < x:
                heappop(pq)
            if pq:
                ans[j] = pq[0][0]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
