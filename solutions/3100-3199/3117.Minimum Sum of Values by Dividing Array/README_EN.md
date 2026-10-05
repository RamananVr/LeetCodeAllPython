---
comments: true
difficulty: Hard
rating: 2735
source: Weekly Contest 393 Q4
tags:
    - Bit Manipulation
    - Segment Tree
    - Queue
    - Array
    - Binary Search
    - Dynamic Programming
---

<!-- problem:start -->

# [3117. Minimum Sum of Values by Dividing Array](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array)

## Description

<!-- description:start -->

<p>You are given two arrays <code>nums</code> and <code>andValues</code> of length <code>n</code> and <code>m</code> respectively.</p>

<p>The <strong>value</strong> of an array is equal to the <strong>last</strong> element of that array.</p>

<p>You have to divide <code>nums</code> into <code>m</code> <strong>disjoint contiguous</strong> <span data-keyword="subarray-nonempty">subarrays</span> such that for the <code>i<sup>th</sup></code> subarray <code>[l<sub>i</sub>, r<sub>i</sub>]</code>, the bitwise <code>AND</code> of the subarray elements is equal to <code>andValues[i]</code>, in other words, <code>nums[l<sub>i</sub>] &amp; nums[l<sub>i</sub> + 1] &amp; ... &amp; nums[r<sub>i</sub>] == andValues[i]</code> for all <code>1 &lt;= i &lt;= m</code>, where <code>&amp;</code> represents the bitwise <code>AND</code> operator.</p>

<p>Return <em>the <strong>minimum</strong> possible sum of the <strong>values</strong> of the </em><code>m</code><em> subarrays </em><code>nums</code><em> is divided into</em>. <em>If it is not possible to divide </em><code>nums</code><em> into </em><code>m</code><em> subarrays satisfying these conditions, return</em> <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,3,3,2], andValues = [0,3,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible way to divide <code>nums</code> is:</p>

<ol>
	<li><code>[1,4]</code> as <code>1 &amp; 4 == 0</code>.</li>
	<li><code>[3]</code> as the bitwise <code>AND</code> of a single element subarray is that element itself.</li>
	<li><code>[3]</code> as the bitwise <code>AND</code> of a single element subarray is that element itself.</li>
	<li><code>[2]</code> as the bitwise <code>AND</code> of a single element subarray is that element itself.</li>
</ol>

<p>The sum of the values for these subarrays is <code>4 + 3 + 3 + 2 = 12</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,5,7,7,7,5], andValues = [0,7,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">17</span></p>

<p><strong>Explanation:</strong></p>

<p>There are three ways to divide <code>nums</code>:</p>

<ol>
	<li><code>[[2,3,5],[7,7,7],[5]]</code> with the sum of the values <code>5 + 7 + 5 == 17</code>.</li>
	<li><code>[[2,3,5,7],[7,7],[5]]</code> with the sum of the values <code>7 + 7 + 5 == 19</code>.</li>
	<li><code>[[2,3,5,7,7],[7],[5]]</code> with the sum of the values <code>7 + 7 + 5 == 19</code>.</li>
</ol>

<p>The minimum possible sum of the values is <code>17</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4], andValues = [2]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>The bitwise <code>AND</code> of the entire array <code>nums</code> is <code>0</code>. As there is no possible way to divide <code>nums</code> into a single subarray to have the bitwise <code>AND</code> of elements <code>2</code>, return <code>-1</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m == andValues.length &lt;= min(n, 10)</code></li>
	<li><code>1 &lt;= nums[i] &lt; 10<sup>5</sup></code></li>
	<li><code>0 &lt;= andValues[j] &lt; 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

<!-- thinking:start -->

> **Thinking**
>
> The array must be split into $m$ segments whose AND equals $\textit{andValues}[j]$, minimizing the sum of segment endpoints. Enumerating every cut is exponential.
>
> AND only loses bits, so a segment can be abandoned once it drops below the target. The state (index, finished segments, running AND) is unique, and distinct AND values are $O(\log M)$.
>
> Memoize $dfs(i,j,a)$: AND in $nums[i]$, then either extend the segment or, when the AND matches the target, cut and add $nums[i]$. Return infinity when too few elements remain or the AND undershoots.

<!-- thinking:end -->

We design a function $dfs(i, j, a)$, which represents the possible minimum sum of subarray values that can be obtained starting from the $i$-th element, with $j$ subarrays already divided, and the bitwise AND result of the current subarray to be divided is $a$. The answer is $dfs(0, 0, -1)$.

The execution process of the function $dfs(i, j, a)$ is as follows:

- If $n - i < m - j$, it means that the remaining elements are not enough to divide into $m - j$ subarrays, return $+\infty$.
- If $j = m$, it means that $m$ subarrays have been divided. At this time, check whether $i = n$ holds. If it holds, return $0$, otherwise return $+\infty$.
- Otherwise, we perform a bitwise AND operation on $a$ and $nums[i]$ to get a new $a$. If $a < andValues[j]$, it means that the bitwise AND result of the current subarray to be divided does not meet the requirements, return $+\infty$. Otherwise, we have two choices:
    - Do not divide the current element, i.e., $dfs(i + 1, j, a)$.
    - Divide the current element, i.e., $dfs(i + 1, j + 1, -1) + nums[i]$.
- Return the minimum of the above two choices.

To avoid repeated calculations, we use the method of memoization search and store the result of $dfs(i, j, a)$ in a hash table.

The time complexity is $O(n \times m \times \log M)$, and the space complexity is $O(n \times m \times \log M)$. Where $n$ and $m$ are the lengths of the arrays $nums$ and $andValues$ respectively; and $M$ is the maximum value in the array $nums$, in this problem $M \leq 10^5$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        @cache
        def dfs(i: int, j: int, a: int) -> int:
            if n - i < m - j:
                return inf
            if j == m:
                return 0 if i == n else inf
            a &= nums[i]
            if a < andValues[j]:
                return inf
            ans = dfs(i + 1, j, a)
            if a == andValues[j]:
                ans = min(ans, dfs(i + 1, j + 1, -1) + nums[i])
            return ans

        n, m = len(nums), len(andValues)
        ans = dfs(0, 0, -1)
        return ans if ans < inf else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Split the array into $m$ segments whose AND equals $\textit{andValues}[j]$, and minimize the sum of the segment endpoints. $n$ can be $10^4$, so enumerating every cut is exponential.
>
> The state is the index, the number of finished segments, and the running AND. Extending the current segment is always the first call, so the chain from index $0$ to $n$ has length $n$. Python raises RecursionError at $n=2000$, Java overflows at $n=10^4$, and Node overflows at $n=8000$.
>
> AND only drops bits. Subarrays that end at the same index have $O(\log M)$ distinct AND values, and the best future cost depends only on the segment index and that AND.
>
> Walk left to right and keep one map from $(j,a)$ to the minimum cost of reaching it. $a=-1$ means the new segment has no element yet. After absorbing $nums[i]$, stay in segment $j$, or, when the AND matches the target, close the segment, add $nums[i]$, and open the next one. The last segment can close only at the end of the array.

<!-- thinking:end -->

Scan the array from left to right and keep only the current layer. State $(j, a)$ means $j$ segments are finished and the AND of the open segment, before absorbing the next element, is $a$. Its value is the minimum sum of segment endpoints used to reach it. $a = -1$ means the open segment is empty. The only initial state is $(0, -1)$ with cost $0$. The answer is the cost of $(m, -1)$ after the whole array has been scanned.

When handling $nums[i]$, consider every state $(j, a)$:

- If $n - i < m - j$, too few elements remain for $m - j$ segments, so drop the state.
- Let $a'$ be the bitwise AND of $a$ and $nums[i]$. The empty value $-1$ AND any number is that number itself. If $a' < \textit{andValues}[j]$, later ANDs can only get smaller and can no longer hit the target, so drop the state.
- Otherwise $nums[i]$ can stay in the current segment. Move to $(j, a')$ with the same cost.
- If $a' = \textit{andValues}[j]$, the current segment can also end at index $i$, adding $nums[i]$ to the cost. When $j + 1 < m$, the new state is $(j + 1, -1)$. When $j + 1 = m$, the division covers the array only if $i = n - 1$, and that state is $(m, -1)$.

Keep the smaller cost for the same state. If $(m, -1)$ is absent, return $-1$.

The time complexity is $O(n \times m \times \log M)$, and the space complexity is $O(m \times \log M)$. Here $n$ and $m$ are the lengths of $nums$ and $andValues$, and $M$ is the maximum value in $nums$, with $M \leq 10^5$ in this problem. Subarray ANDs that share a right endpoint change at most $O(\log M)$ times, so each layer has $O(m \times \log M)$ states.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)
        f = {(0, -1): 0}
        for i, x in enumerate(nums):
            g = {}
            for (j, a), cost in f.items():
                if n - i < m - j:
                    continue
                na = a & x
                if na < andValues[j]:
                    continue
                g[j, na] = min(g.get((j, na), inf), cost)
                if na == andValues[j]:
                    t = cost + x
                    if j + 1 == m:
                        if i == n - 1:
                            g[m, -1] = min(g.get((m, -1), inf), t)
                    else:
                        g[j + 1, -1] = min(g.get((j + 1, -1), inf), t)
            f = g
        ans = f.get((m, -1), inf)
        return ans if ans < inf else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
