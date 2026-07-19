---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1354.Construct%20Target%20Array%20With%20Multiple%20Sums/README_EN.md
rating: 2014
source: Weekly Contest 176 Q4
tags:
    - Array
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1354. Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums)

## Description

<!-- description:start -->

<p>You are given an array <code>target</code> of n integers. From a starting array <code>arr</code> consisting of <code>n</code> 1&#39;s, you may perform the following procedure :</p>

<ul>
	<li>let <code>x</code> be the sum of all elements currently in your array.</li>
	<li>choose index <code>i</code>, such that <code>0 &lt;= i &lt; n</code> and set the value of <code>arr</code> at index <code>i</code> to <code>x</code>.</li>
	<li>You may repeat this procedure as many times as needed.</li>
</ul>

<p>Return <code>true</code> <em>if it is possible to construct the</em> <code>target</code> <em>array from</em> <code>arr</code><em>, otherwise, return</em> <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = [9,3,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = [1,1,1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> Impossible to create target array from [1,1,1,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = [8,5]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= target[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Reverse Construction + Priority Queue (Max Heap)

We observe that if we start constructing the target array $\textit{target}$ from the array $\textit{arr}$ in a forward manner, it is difficult to determine which index $i$ to choose each time, making the problem quite complex. However, if we construct in reverse starting from the array $\textit{target}$, each construction step must select the largest element in the current array, which ensures that each construction is unique, making the problem relatively simple.

Therefore, we can use a priority queue (max heap) to store the elements of array $\textit{target}$, and use a variable $s$ to record the sum of all elements in array $\textit{target}$. Each time we extract the maximum element $mx$ from the priority queue and calculate the sum $t$ of all elements in the current array except $mx$. If $t \lt 1$ or $mx - t \lt 1$, it means the target array $\textit{target}$ cannot be constructed, and we return `false`. Otherwise, we calculate $mx \bmod t$. If $mx \bmod t = 0$, we set $x = t$; otherwise, we set $x = mx \bmod t$. We add $x$ to the priority queue and update the value of $s$. We repeat this process until all elements in the priority queue become $1$, at which point we return `true`.

The time complexity is $O(n \log n)$ and the space complexity is $O(n)$, where $n$ is the length of array $\textit{target}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        pq = [-x for x in target]
        heapify(pq)
        while -pq[0] > 1:
            mx = -heappop(pq)
            t = s - mx
            if t == 0 or mx - t < 1:
                return False
            x = (mx % t) or t
            heappush(pq, -x)
            s = s - mx + x
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
