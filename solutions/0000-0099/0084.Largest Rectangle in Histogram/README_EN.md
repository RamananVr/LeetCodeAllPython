---
comments: true
difficulty: Hard
tags:
    - Stack
    - Array
    - Monotonic Stack
    - Range Query
---

<!-- problem:start -->

# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram)

## Description

<!-- description:start -->

<p>Given an array of integers <code>heights</code> representing the histogram&#39;s bar height where the width of each bar is <code>1</code>, return <em>the area of the largest rectangle in the histogram</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0084.Largest%20Rectangle%20in%20Histogram/images/histogram.jpg" style="width: 522px; height: 242px;" />
<pre>
<strong>Input:</strong> heights = [2,1,5,6,2,3]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0084.Largest%20Rectangle%20in%20Histogram/images/histogram-1.jpg" style="width: 202px; height: 362px;" />
<pre>
<strong>Input:</strong> heights = [2,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= heights[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack

<!-- thinking:start -->

> **Thinking**
>
> The first idea is enumerate every interval $[l, r]$, take the min height, area $(r - l + 1) \times \min$. Correct, but $O(n^2)$. $n \le 10^5$ will time out.
>
> The bottleneck is recomputing the min over every range. Flip the enumeration: let bar $i$ be the shortest bar of the rectangle; the width is the span to the nearest strictly shorter bars on both sides.
>
> “Nearest smaller on left/right” is the monotonic-stack model. Indices in the stack have increasing heights; a shorter bar pops others and becomes their right bound, while the new top is the left bound. Each bar enters and leaves once, so one linear pass.

<!-- thinking:end -->

We can enumerate the height $h$ of each bar as the height of the rectangle. Using a monotonic stack, we find the index $left_i$, $right_i$ of the first bar with a height less than $h$ to the left and right. The area of the rectangle at this time is $h \times (right_i-left_i-1)$. We can find the maximum value.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ represents the length of $heights$.

Common model of monotonic stack: Find the **nearest** number to the left/right of each number that is **larger/smaller** than it. Template:

```python
stk = []
for i in range(n):
    while stk and check(stk[-1], i):
        stk.pop()
    stk.append(i)
```

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        left = [-1] * n
        right = [n] * n
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
