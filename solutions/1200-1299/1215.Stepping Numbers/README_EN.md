---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1215.Stepping%20Numbers/README_EN.md
rating: 1674
source: Biweekly Contest 10 Q3
tags:
    - Breadth-First Search
    - Math
    - Backtracking
---

<!-- problem:start -->

# [1215. Stepping Numbers 🔒](https://leetcode.com/problems/stepping-numbers)

## Description

<!-- description:start -->

<p>A <strong>stepping number</strong> is an integer such that all of its adjacent digits have an absolute difference of exactly <code>1</code>.</p>

<ul>
	<li>For example, <code>321</code> is a <strong>stepping number</strong> while <code>421</code> is not.</li>
</ul>

<p>Given two integers <code>low</code> and <code>high</code>, return <em>a sorted list of all the <strong>stepping numbers</strong> in the inclusive range</em> <code>[low, high]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> low = 0, high = 21
<strong>Output:</strong> [0,1,2,3,4,5,6,7,8,9,10,12,21]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> low = 10, high = 15
<strong>Output:</strong> [10,12]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= low &lt;= high &lt;= 2 * 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

First, if $low$ is $0$, we need to add $0$ to the answer.

Next, we create a queue $q$ and add $1 \sim 9$ to the queue. Then, we repeatedly take out elements from the queue. Let the current element be $v$. If $v$ is greater than $high$, we stop searching. If $v$ is in the range $[low, high]$, we add $v$ to the answer. Then, we need to record the last digit of $v$ as $x$. If $x \gt 0$, we add $v \times 10 + x - 1$ to the queue. If $x \lt 9$, we add $v \times 10 + x + 1$ to the queue. Repeat the above steps until the queue is empty.

The time complexity is $O(10 \times 2^{\log M})$, and the space complexity is $O(2^{\log M})$, where $M$ is the number of digits in $high$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        ans = []
        if low == 0:
            ans.append(0)
        q = deque(range(1, 10))
        while q:
            v = q.popleft()
            if v > high:
                break
            if v >= low:
                ans.append(v)
            x = v % 10
            if x:
                q.append(v * 10 + x - 1)
            if x < 9:
                q.append(v * 10 + x + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
