---
comments: true
difficulty: Hard
rating: 2538
source: Weekly Contest 443 Q4
tags:
    - Array
    - Hash Table
    - Math
    - Dynamic Programming
    - Sliding Window
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3505. Minimum Operations to Make Elements Within K Subarrays Equal](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and two integers, <code>x</code> and <code>k</code>. You can perform the following operation any number of times (<strong>including zero</strong>):</p>

<ul>
	<li>Increase or decrease any element of <code>nums</code> by 1.</li>
</ul>

<p>Return the <strong>minimum</strong> number of operations needed to have <strong>at least</strong> <code>k</code> <em>non-overlapping <span data-keyword="subarray-nonempty">subarrays</span></em> of size <strong>exactly</strong> <code>x</code> in <code>nums</code>, where all elements within each subarray are equal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Use 3 operations to add 3 to <code>nums[1]</code> and use 2 operations to subtract 2 from <code>nums[3]</code>. The resulting array is <code>[5, 1, 1, 1, 7, 3, 6, 4, -1]</code>.</li>
	<li>Use 1 operation to add 1 to <code>nums[5]</code> and use 2 operations to subtract 2 from <code>nums[6]</code>. The resulting array is <code>[5, 1, 1, 1, 7, 4, 4, 4, -1]</code>.</li>
	<li>Now, all elements within each subarray <code>[1, 1, 1]</code> (from indices 1 to 3) and <code>[4, 4, 4]</code> (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [9,-2,-2,-2,1,5], x = 2, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Use 3 operations to subtract 3 from <code>nums[4]</code>. The resulting array is <code>[9, -2, -2, -2, -2, 5]</code>.</li>
	<li>Now, all elements within each subarray <code>[-2, -2]</code> (from indices 1 to 2) and <code>[-2, -2]</code> (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>2 &lt;= x &lt;= nums.length</code></li>
	<li><code>1 &lt;= k &lt;= 15</code></li>
	<li><code>2 &lt;= k * x &lt;= nums.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Ordered Set + Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> $n \le 10^5$ and $k \le 15$, so we cannot brute-force sort every window of length $x$ and then search combinations. The minimum operations to make a subarray all equal is the sum of distances to its median. By maintaining two ordered sets $l$ and $r$ for the lower and upper halves of the sliding window along with their sums, we can update the window in $O(\log x)$ time and query its minimum cost in $O(1)$ time.
>
> Choosing $k$ non-overlapping windows can be solved with dynamic programming: let $f[i][j]$ be the minimum cost to choose $j$ subarrays of length $x$ from the first $i$ elements. At step $i$, we either skip ending a subarray at $i$ (cost $f[i - 1][j]$) or place the $j$-th subarray at $[i - x, i - 1]$ (cost $f[i - x][j - 1] + w$). Since $k$ is small, the total time complexity $O(n(\log x + k))$ easily passes.

<!-- thinking:end -->

To make all elements in a subarray of length $x$ equal, the minimum number of operations is achieved by changing every element to the median of the subarray. To efficiently compute this minimum cost for every sliding window of length $x$, we design a helper structure $\textit{MedianCost}$ that maintains two ordered multisets $l$ and $r$ along with their element sums $\textit{s1}$ and $\textit{s2}$:

- Multiset $l$ stores the smaller half of the elements in the window and $r$ stores the larger half. The $\textit{adjust}$ method keeps $0 \le |l| - |r| \le 1$, so the largest element in $l$ is always the median $\textit{mid}$ of the window.
- $\textit{add}(v)$: inserts $v$ into $r$ and adds $v$ to $\textit{s2}$, then moves the smallest element of $r$ into $l$ (updating $\textit{s2}$ and $\textit{s1}$), and calls $\textit{adjust}$ to rebalance the sizes.
- $\textit{remove}(v)$: if $v \in l$, removes $v$ from $l$ and subtracts $v$ from $\textit{s1}$; otherwise removes $v$ from $r$ and subtracts $v$ from $\textit{s2}$, and then calls $\textit{adjust}$ to rebalance.
- $\textit{query}()$: letting $\textit{mid}$ be the largest element in $l$, the number of operations to make all elements in the window equal to $\textit{mid}$ is $|l| \times \textit{mid} - \textit{s1} + \textit{s2} - |r| \times \textit{mid}$.

We then use dynamic programming. Define $f[i][j]$ as the minimum number of operations to choose $j$ non-overlapping subarrays of length $x$ from the first $i$ elements of $\textit{nums}$ such that all elements within each subarray are equal. Initially, $f[0][0] = 0$ and all other states are set to $+\infty$.

We iterate $i$ from $1$ to $n$, adding $\textit{nums}[i - 1]$ to $\textit{mc}$ and querying the current window cost $w = \textit{mc}.\textit{query}()$. For each $j \in [0, k]$:

- If we do not end a subarray at the $i$-th element, $f[i][j] = f[i - 1][j]$;
- If $j > 0$ and $i \ge x$, we can choose the subarray $\textit{nums}[i - x .. i - 1]$ as the $j$-th subarray, giving the transition:

$$
f[i][j] = \min(f[i - 1][j], f[i - x][j - 1] + w)
$$

When $i \ge x$, we remove the outgoing element $\textit{nums}[i - x]$ from $\textit{mc}$ before moving to the next index. After the loop, $f[n][k]$ is the answer.

The time complexity is $O(n(\log x + k))$, and the space complexity is $O(nk)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class MedianCost:
    def __init__(self):
        self.l = SortedList()
        self.r = SortedList()
        self.s1 = 0
        self.s2 = 0

    def add(self, x: int):
        self.r.add(x)
        self.s2 += x

        y = self.r.pop(0)
        self.s2 -= y
        self.l.add(y)
        self.s1 += y
        self.adjust()

    def adjust(self):
        while len(self.l) - len(self.r) > 1:
            x = self.l.pop()
            self.s1 -= x
            self.r.add(x)
            self.s2 += x
        while len(self.r) > len(self.l):
            x = self.r.pop(0)
            self.s2 -= x
            self.l.add(x)
            self.s1 += x

    def remove(self, x: int):
        if x in self.l:
            self.l.remove(x)
            self.s1 -= x
        else:
            self.r.remove(x)
            self.s2 -= x
        self.adjust()

    def query(self) -> int:
        mid = self.l[-1]
        return len(self.l) * mid - self.s1 + self.s2 - len(self.r) * mid

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        f = [[inf] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        mc = MedianCost()
        for i, v in enumerate(nums, 1):
            mc.add(v)
            w = mc.query()
            for j in range(k + 1):
                f[i][j] = min(f[i][j], f[i - 1][j])
                if j > 0 and i >= x:
                    f[i][j] = min(f[i][j], f[i - x][j - 1] + w)
            if i >= x:
                mc.remove(nums[i - x])
        return f[n][k]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
