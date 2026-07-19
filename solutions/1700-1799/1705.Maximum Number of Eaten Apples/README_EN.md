---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1705.Maximum%20Number%20of%20Eaten%20Apples/README_EN.md
rating: 1929
source: Weekly Contest 221 Q2
tags:
    - Greedy
    - Array
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1705. Maximum Number of Eaten Apples](https://leetcode.com/problems/maximum-number-of-eaten-apples)

## Description

<!-- description:start -->

<p>There is a special kind of apple tree that grows apples every day for <code>n</code> days. On the <code>i<sup>th</sup></code> day, the tree grows <code>apples[i]</code> apples that will rot after <code>days[i]</code> days, that is on day <code>i + days[i]</code> the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by <code>apples[i] == 0</code> and <code>days[i] == 0</code>.</p>

<p>You decided to eat <strong>at most</strong> one apple a day (to keep the doctors away). Note that you can keep eating after the first <code>n</code> days.</p>

<p>Given two integer arrays <code>days</code> and <code>apples</code> of length <code>n</code>, return <em>the maximum number of apples you can eat.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> apples = [1,2,3,5,2], days = [3,2,1,4,2]
<strong>Output:</strong> 7
<strong>Explanation:</strong> You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can eat 5 apples:
- On the first to the third day you eat apples that grew on the first day.
- Do nothing on the fouth and fifth days.
- On the sixth and seventh days you eat apples that grew on the sixth day.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == apples.length == days.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= apples[i], days[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>days[i] = 0</code> if and only if <code>apples[i] = 0</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Priority Queue

We can greedily choose the apples that are closest to rotting among the unrotten apples, so that we can eat as many apples as possible.

Therefore, we can use a priority queue (min-heap) to store the rotting time of the apples and the corresponding number of apples. Each time, we take out the apples with the smallest rotting time from the priority queue, then decrement their quantity by one. If the quantity is not zero after decrementing, we put them back into the priority queue. If the apples have already rotted, we remove them from the priority queue.

The time complexity is $O(n \times \log n + M)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{days}$, and $M = \max(\textit{days})$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(days)
        i = ans = 0
        q = []
        while i < n or q:
            if i < n and apples[i]:
                heappush(q, (i + days[i] - 1, apples[i]))
            while q and q[0][0] < i:
                heappop(q)
            if q:
                t, v = heappop(q)
                v -= 1
                ans += 1
                if v and t > i:
                    heappush(q, (t, v))
            i += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
