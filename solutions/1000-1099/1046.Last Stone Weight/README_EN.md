---
comments: true
difficulty: Easy
rating: 1172
source: Weekly Contest 137 Q1
tags:
    - Array
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight)

## Description

<!-- description:start -->

<p>You are given an array of integers <code>stones</code> where <code>stones[i]</code> is the weight of the <code>i<sup>th</sup></code> stone.</p>

<p>We are playing a game with the stones. On each turn, we choose the <strong>heaviest two stones</strong> and smash them together. Suppose the heaviest two stones have weights <code>x</code> and <code>y</code> with <code>x &lt;= y</code>. The result of this smash is:</p>

<ul>
	<li>If <code>x == y</code>, both stones are destroyed, and</li>
	<li>If <code>x != y</code>, the stone of weight <code>x</code> is destroyed, and the stone of weight <code>y</code> has new weight <code>y - x</code>.</li>
</ul>

<p>At the end of the game, there is <strong>at most one</strong> stone left.</p>

<p>Return <em>the weight of the last remaining stone</em>. If there are no stones left, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stones = [2,7,4,1,8,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that&#39;s the value of the last stone.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stones = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Each smash uses the two heaviest stones. Scanning for the maximum every time repeats comparisons; a heap extracts them in logarithmic time.
>
> Negating the weights turns a min-heap into a max-heap. Pop $y\ge x$ and push $y-x$ when they differ, until fewer than two stones remain.
>
> An empty heap is $0$; otherwise the answer is the negated top.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapify(h)
        while len(h) > 1:
            y, x = -heappop(h), -heappop(h)
            if x != y:
                heappush(h, x - y)
        return 0 if not h else -h[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
