---
comments: true
difficulty: Medium
rating: 1850
source: Biweekly Contest 28 Q3
tags:
    - Array
    - Hash Table
    - Binary Search
    - Dynamic Programming
    - Sliding Window
---

<!-- problem:start -->

# [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum)

## Description

<!-- description:start -->

<p>You are given an array of integers <code>arr</code> and an integer <code>target</code>.</p>

<p>You have to find <strong>two non-overlapping sub-arrays</strong> of <code>arr</code> each with a sum equal <code>target</code>. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is <strong>minimum</strong>.</p>

<p>Return <em>the minimum sum of the lengths</em> of the two required sub-arrays, or return <code>-1</code> if you cannot find such two sub-arrays.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,2,2,4,3], target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [7,3,4,7], target = 7
<strong>Output:</strong> 2
<strong>Explanation:</strong> Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,3,2,6,2,3,4], target = 6
<strong>Output:</strong> -1
<strong>Explanation:</strong> We have only one sub-array of sum = 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Prefix Sum + Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> The straightforward approach is to enumerate every subarray that sums to $target$ and pair them while checking overlap. With $n \le 10^5$, the number of subarrays is quadratic, so this does not fit.
>
> Once the right segment is fixed, the left one must lie entirely in the prefix before it, and only the shortest valid subarray in that prefix matters. We therefore need a running answer to "the shortest valid segment in the prefix so far".
>
> All values are positive, so prefix sums are strictly increasing and unique. A hash map from prefix sum to index then finds, in constant time, the unique segment $[j+1,i]$ that ends at the current position and sums to $target$.
>
> We scan left to right while maintaining $f[i]$, the shortest such subarray among the first $i$ elements. When $[j+1,i]$ appears, add $f[j]$ to the current length to update the answer, then set $f[i]=\min(f[i-1], i-j)$. The left piece always comes from before the current segment, so the two never overlap.

<!-- thinking:end -->

We use a hash table $d$ to record the index of each prefix sum, initially $d[0]=0$.

Define $f[i]$ as the minimum length of a subarray with sum equal to $target$ among the first $i$ elements. Initially, $f[0]=\infty$ and $ans=\infty$. Indices are $1$-based.

Iterate through $\textit{arr}$. For the current position $i$, first set $f[i]=f[i-1]$ and accumulate the prefix sum $s$. If $s-\textit{target}$ exists in the hash table, let $j=d[s-\textit{target}]$. Then the interval $[j+1,i]$ sums to $target$ and has length $i-j$. Update $f[i]=\min(f[i], i-j)$, and update the answer with the best length on the left: $ans=\min(ans, f[j]+i-j)$. Then store $d[s]=i$.

Finally, if $ans$ is greater than the array length, return $-1$; otherwise, return $ans$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of $\textit{arr}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        d = {0: 0}
        s, n = 0, len(arr)
        f = [inf] * (n + 1)
        ans = inf
        for i, v in enumerate(arr, 1):
            s += v
            f[i] = f[i - 1]
            if s - target in d:
                j = d[s - target]
                f[i] = min(f[i], i - j)
                ans = min(ans, f[j] + i - j)
            d[s] = i
        return -1 if ans > n else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
