---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1500-1599/1588.Sum%20of%20All%20Odd%20Length%20Subarrays/README_EN.md
rating: 1408
source: Biweekly Contest 35 Q1
tags:
    - Array
    - Math
    - Prefix Sum
---

<!-- problem:start -->

# [1588. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays)

## Description

<!-- description:start -->

<p>Given an array of positive integers <code>arr</code>, return <em>the sum of all possible <strong>odd-length subarrays</strong> of </em><code>arr</code>.</p>

<p>A <strong>subarray</strong> is a contiguous subsequence of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,4,2,5,3]
<strong>Output:</strong> 58
<strong>Explanation: </strong>The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2]
<strong>Output:</strong> 3
<b>Explanation: </b>There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [10,11,12]
<strong>Output:</strong> 66
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<p>Could you solve this problem in O(n) time complexity?</p>

<!-- description:end -->

## Solutions

### Solution 1: Dynamic Programming

We define two arrays $f$ and $g$ of length $n$, where $f[i]$ represents the sum of subarrays ending at $\textit{arr}[i]$ with odd lengths, and $g[i]$ represents the sum of subarrays ending at $\textit{arr}[i]$ with even lengths. Initially, $f[0] = \textit{arr}[0]$, and $g[0] = 0$. The answer is $\sum_{i=0}^{n-1} f[i]$.

When $i > 0$, consider how $f[i]$ and $g[i]$ transition:

For the state $f[i]$, the element $\textit{arr}[i]$ can form an odd-length subarray with the previous $g[i-1]$. The number of such subarrays is $(i / 2) + 1$, so $f[i] = g[i-1] + \textit{arr}[i] \times ((i / 2) + 1)$.

For the state $g[i]$, when $i = 0$, there are no even-length subarrays, so $g[0] = 0$. When $i > 0$, the element $\textit{arr}[i]$ can form an even-length subarray with the previous $f[i-1]$. The number of such subarrays is $(i + 1) / 2$, so $g[i] = f[i-1] + \textit{arr}[i] \times ((i + 1) / 2)$.

The final answer is $\sum_{i=0}^{n-1} f[i]$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{arr}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        f = [0] * n
        g = [0] * n
        ans = f[0] = arr[0]
        for i in range(1, n):
            f[i] = g[i - 1] + arr[i] * (i // 2 + 1)
            g[i] = f[i - 1] + arr[i] * ((i + 1) // 2)
            ans += f[i]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming (Space Optimization)

We notice that the values of $f[i]$ and $g[i]$ only depend on $f[i - 1]$ and $g[i - 1]$. Therefore, we can use two variables $f$ and $g$ to record the values of $f[i - 1]$ and $g[i - 1]$, respectively, thus optimizing the space complexity.

The time complexity is $O(n)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans, f, g = arr[0], arr[0], 0
        for i in range(1, len(arr)):
            ff = g + arr[i] * (i // 2 + 1)
            gg = f + arr[i] * ((i + 1) // 2)
            f, g = ff, gg
            ans += f
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
