---
comments: true
difficulty: Hard
tags:
    - Stack
    - Array
    - Two Pointers
    - Dynamic Programming
    - Monotonic Stack
---

<!-- problem:start -->

# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)

## Description

<!-- description:start -->

<p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0042.Trapping%20Rain%20Water/images/rainwatertrap.png" style="width: 412px; height: 161px;" />
<pre>
<strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> The first idea is, for each $i$, scan left and right for the tallest bars; water is $\min(\textit{leftMax}, \textit{rightMax}) - \textit{height}[i]$. Correct, but $O(n^2)$. $n \le 2 \times 10^4$ can time out.
>
> The bottleneck is recomputing left/right maxima at every $i$. Those maxima only depend on one side and can be precomputed in linear time.
>
> Store, at each index, the highest bar to the left (inclusive) and to the right (inclusive), then sum. The water level is the shorter of the two walls — that is the DP state.

<!-- thinking:end -->

We define $left[i]$ as the height of the highest bar to the left of and including the position at index $i$, and $right[i]$ as the height of the highest bar to the right of and including the position at index $i$. Therefore, the amount of rainwater that can be trapped at index $i$ is $min(left[i], right[i]) - height[i]$. We traverse the array to calculate $left[i]$ and $right[i]$, and the final answer is $\sum_{i=0}^{n-1} \min(left[i], right[i]) - height[i]$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [height[0]] * n
        right = [height[-1]] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            right[n - i - 1] = max(right[n - i], height[n - i - 1])
        return sum(min(l, r) - h for l, r, h in zip(left, right, height))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
