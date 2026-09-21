---
comments: true
difficulty: Hard
rating: 2288
source: Weekly Contest 499 Q4
tags:
    - Segment Tree
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [3915. Maximum Sum of Alternating Subsequence With Distance at Least K](https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>Pick a <strong><span data-keyword="subsequence-sequence">subsequence</span></strong> with indices <code>0 &lt;= i<sub>1</sub> &lt; i<sub>2</sub> &lt; ... &lt; i<sub>m</sub> &lt; n</code> such that:</p>

<ul>
	<li>For every <code>1 &lt;= t &lt; m</code>, <code>i<sub>t+1</sub> - i<sub>t</sub> &gt;= k</code>.</li>
	<li>The selected values form a <strong>strictly alternating</strong> sequence. In other words, either:
	<ul>
		<li><code>nums[i<sub>1</sub>] &lt; nums[i<sub>2</sub>] &gt; nums[i<sub>3</sub>] &lt; ...</code>, or</li>
		<li><code>nums[i<sub>1</sub>] &gt; nums[i<sub>2</sub>] &lt; nums[i<sub>3</sub>] &gt; ...</code></li>
	</ul>
	</li>
</ul>

<p>A <strong>subsequence</strong> of length 1 is also considered <strong>strictly</strong> alternating. The score of a <strong>valid</strong> subsequence is the <strong>sum</strong> of its selected values.</p>

<p>Return an integer denoting the <strong>maximum</strong> possible <strong>score</strong> of a valid subsequence.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>An optimal choice is indices <code>[0, 2]</code>, which gives values <code>[5, 2]</code>.</p>

<ul>
	<li>The distance condition holds because <code>2 - 0 = 2 &gt;= k</code>.</li>
	<li>The values are strictly alternating because <code>5 &gt; 2</code>.</li>
</ul>

<p>The score is <code>5 + 2 = 7</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,5,4,2,4], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<p>An optimal choice is indices <code>[0, 1, 3, 4]</code>, which gives values <code>[3, 5, 2, 4]</code>.</p>

<ul>
	<li>The distance condition holds because each pair of consecutive chosen indices differs by at least <code>k = 1</code>.</li>
	<li>The values are strictly alternating since <code>3 &lt; 5 &gt; 2 &lt; 4</code>.</li>
</ul>

<p>The score is <code>3 + 5 + 2 + 4 = 14</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The only valid subsequence is <code>[5]</code>. A subsequence with 1 element is always strictly alternating, so the score is 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming + Binary Indexed Tree

<!-- thinking:start -->

> **Thinking**
>
> A subsequence DP that enumerates every predecessor at least $k$ away is $O(n^2)$ and fails for $n\le 10^5$. Transfers also require the predecessor to be larger or smaller.
>
> Let $f[i][0]$ be the best alternating subsequence ending at $i$ as a valley, and $f[i][1]$ as a peak. A valley may follow only a larger peak, a peak only a smaller valley, and the indices must differ by at least $k$.
>
> Two Fenwick trees store prefix maxima of $f[\cdot][0]$ and suffix maxima of $f[\cdot][1]$ over the discretized value domain. At index $i$ we first insert the state at $i-k$, then query; every predecessor used in a transition is then at least $k$ away.

<!-- thinking:end -->

**State Definition**

Let $f[i][0]$ denote the maximum sum of a valid subsequence ending at index $i$ where the last element is a **valley** (the next element must be larger to maintain alternation), and $f[i][1]$ denote the maximum sum where the last element is a **peak** (the next element must be smaller).

**Transitions**

When transitioning, we enumerate a predecessor index $j$ satisfying $j \leq i - k$:

- State $f[i][0]$ (valley): transitions from $f[j][1]$, requiring $\text{nums}[j] > \text{nums}[i]$, i.e., query the maximum $f[\cdot][1]$ over the value range $(\text{nums}[i],\ +\infty)$:

$$f[i][0] = \text{nums}[i] + \max\!\left(0,\ \max_{\substack{j \leq i-k \\ \text{nums}[j] > \text{nums}[i]}} f[j][1]\right)$$

- State $f[i][1]$ (peak): transitions from $f[j][0]$, requiring $\text{nums}[j] < \text{nums}[i]$, i.e., query the maximum $f[\cdot][0]$ over the value range $[1,\ \text{nums}[i]-1]$:

$$f[i][1] = \text{nums}[i] + \max\!\left(0,\ \max_{\substack{j \leq i-k \\ \text{nums}[j] < \text{nums}[i]}} f[j][0]\right)$$

The final answer is $\max_{0 \leq i < n}\max(f[i][0],\ f[i][1])$.

**Optimization**

The transitions involve dynamic prefix/suffix maximum queries over a value domain, which can be maintained efficiently with two **Binary Indexed Trees (BITs)**:

- BIT $\text{bit}_0$: indexed by value, maintains the prefix maximum of $f[\cdot][0]$, used to query cases where $\text{nums}[j] < \text{nums}[i]$.
- BIT $\text{bit}_1$: indexed by $m + 1 - \textit{rank}$ (reversed, where $m$ is the number of distinct values), maintains the prefix maximum of $f[\cdot][1]$, equivalent to a suffix maximum over the value domain, used to query cases where $\text{nums}[j] > \text{nums}[i]$.

To ensure only indices $j \leq i - k$ participate in transitions, when processing index $i$, we first insert the state of index $i - k$ into the BITs, then query.

The time complexity is $O(n \log m)$ and the space complexity is $O(n + m)$, where $n$ is the length of the array and $m$ is the number of distinct values.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, val: int) -> None:
        while x <= self.n:
            self.c[x] = max(self.c[x], val)
            x += x & -x

    def query(self, x: int) -> int:
        ans = 0
        while x > 0:
            ans = max(ans, self.c[x])
            x -= x & -x
        return ans

class Solution:
    def maxAlternatingSum(self, nums: List[int], k: int) -> int:
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}
        bit0 = BinaryIndexedTree(m)
        bit1 = BinaryIndexedTree(m)
        n = len(nums)
        f = [[0, 0] for _ in range(n)]
        ans = 0
        for i, x in enumerate(nums):
            if i >= k:
                r = rank[nums[i - k]]
                bit0.update(r, f[i - k][0])
                bit1.update(m + 1 - r, f[i - k][1])
            r = rank[x]
            f[i][0] = x + bit1.query(m - r)
            f[i][1] = x + bit0.query(r - 1)
            ans = max(ans, f[i][0], f[i][1])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
