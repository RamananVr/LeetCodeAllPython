---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1900-1999/1959.Minimum%20Total%20Space%20Wasted%20With%20K%20Resizing%20Operations/README_EN.md
rating: 2310
source: Biweekly Contest 58 Q3
tags:
    - Array
    - Dynamic Programming
    - Prefix Sum
---

<!-- problem:start -->

# [1959. Minimum Total Space Wasted With K Resizing Operations](https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations)

## Description

<!-- description:start -->

<p>You are currently designing a dynamic array. You are given a <strong>0-indexed</strong> integer array <code>nums</code>, where <code>nums[i]</code> is the number of elements that will be in the array at time <code>i</code>. In addition, you are given an integer <code>k</code>, the <strong>maximum</strong> number of times you can <strong>resize</strong> the array (to<strong> any</strong> size).</p>

<p>The size of the array at time <code>t</code>, <code>size<sub>t</sub></code>, must be at least <code>nums[t]</code> because there needs to be enough space in the array to hold all the elements. The <strong>space wasted</strong> at&nbsp;time <code>t</code> is defined as <code>size<sub>t</sub> - nums[t]</code>, and the <strong>total</strong> space wasted is the <strong>sum</strong> of the space wasted across every time <code>t</code> where <code>0 &lt;= t &lt; nums.length</code>.</p>

<p>Return <em>the <strong>minimum</strong> <strong>total space wasted</strong> if you can resize the array at most</em> <code>k</code> <em>times</em>.</p>

<p><strong>Note:</strong> The array can have <strong>any size</strong> at the start and does<strong> not </strong>count towards the number of resizing operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,20], k = 0
<strong>Output:</strong> 10
<strong>Explanation:</strong> size = [20,20].
We can set the initial size to be 20.
The total wasted space is (20 - 10) + (20 - 20) = 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,20,30], k = 1
<strong>Output:</strong> 10
<strong>Explanation:</strong> size = [20,20,30].
We can set the initial size to be 20 and resize to 30 at time 2. 
The total wasted space is (20 - 10) + (20 - 20) + (30 - 30) = 10.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,20,15,30,20], k = 2
<strong>Output:</strong> 15
<strong>Explanation:</strong> size = [10,20,20,30,30].
We can set the initial size to 10, resize to 20 at time 1, and resize to 30 at time 3.
The total wasted space is (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

The problem is equivalent to dividing the array $\textit{nums}$ into $k + 1$ segments. The wasted space for each segment is the maximum value of that segment multiplied by the length of the segment minus the sum of the elements in that segment. By summing the wasted space of each segment, we get the total wasted space. By adding 1 to $k$, we are effectively dividing the array into $k$ segments.

Therefore, we define an array $\textit{g}[i][j]$ to represent the wasted space for the segment $\textit{nums}[i..j]$, which is the maximum value of $\textit{nums}[i..j]$ multiplied by the length of $\textit{nums}[i..j]$ minus the sum of the elements in $\textit{nums}[i..j]$. We iterate over $i$ in the range $[0, n)$ and $j$ in the range $[i, n)$, using a variable $s$ to maintain the sum of the elements in $\textit{nums}[i..j]$ and a variable $\textit{mx}$ to maintain the maximum value of $\textit{nums}[i..j]$. Then we can get:

$$ \textit{g}[i][j] = \textit{mx} \times (j - i + 1) - s $$

Next, we define $\textit{f}[i][j]$ to represent the minimum wasted space for dividing the first $i$ elements into $j$ segments. We initialize $\textit{f}[0][0] = 0$ and the other positions to infinity. We iterate over $i$ in the range $[1, n]$ and $j$ in the range $[1, k]$, then we iterate over the last element $h$ of the previous $j - 1$ segments. Then we have:

$$ \textit{f}[i][j] = \min(\textit{f}[i][j], \textit{f}[h][j - 1] + \textit{g}[h][i - 1]) $$

The final answer is $\textit{f}[n][k]$.

The time complexity is $O(n^2 \times k)$, and the space complexity is $O(n \times (n + k))$. Where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        k += 1
        n = len(nums)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            s = mx = 0
            for j in range(i, n):
                s += nums[j]
                mx = max(mx, nums[j])
                g[i][j] = mx * (j - i + 1) - s
        f = [[inf] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for h in range(i):
                    f[i][j] = min(f[i][j], f[h][j - 1] + g[h][i - 1])
        return f[-1][-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
