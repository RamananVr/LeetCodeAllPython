---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3897.Maximum%20Value%20of%20Concatenated%20Binary%20Segments/README_EN.md
rating: 1998
source: Biweekly Contest 180 Q4
tags:
    - Greedy
    - Array
    - Sorting
---

<!-- problem:start -->

# [3897. Maximum Value of Concatenated Binary Segments](https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments)

## Description

<!-- description:start -->

<p>You are given two integer arrays <code>nums1</code> and <code>nums0</code>, each of size <code>n</code>.</p>

<ul>
	<li><code>nums1[i]</code> represents the number of <code>&#39;1&#39;</code>s in the <code>i<sup>th</sup></code> segment.</li>
	<li><code>nums0[i]</code> represents the number of <code>&#39;0&#39;</code>s in the <code>i<sup>th</sup></code> segment.</li>
</ul>

<p>For each index <code>i</code>, construct a binary segment consisting of:</p>

<ul>
	<li><code>nums1[i]</code> occurrences of <code>&#39;1&#39;</code> followed by</li>
	<li><code>nums0[i]</code> occurrences of <code>&#39;0&#39;</code>.</li>
</ul>

<p>You may <strong>rearrange</strong> the order of these <strong>segments</strong> in any way. After rearranging, <strong>concatenate</strong> all segments to form a single binary string.</p>

<p>Return the <strong>maximum</strong> possible integer value of the concatenated binary string.</p>

<p>Since the result can be very large, return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [1,2], nums0 = [1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>At index 0, <code>nums1[0] = 1</code> and <code>nums0[0] = 1</code>, so the segment formed is <code>&quot;10&quot;</code>.</li>
	<li>At index 1, <code>nums1[1] = 2</code> and <code>nums0[1] = 0</code>, so the segment formed is <code>&quot;11&quot;</code>.</li>
	<li>Reordering the segments as <code>&quot;11&quot;</code> followed by <code>&quot;10&quot;</code> produces the binary string <code>&quot;1110&quot;</code>.</li>
	<li>The binary number <code>&quot;1110&quot;</code> has value 14 which is the maximum possible value.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [3,1], nums0 = [0,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">120</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>At index 0, <code>nums1[0] = 3</code> and <code>nums0[0] = 0</code>, so the segment formed is <code>&quot;111&quot;</code>.</li>
	<li>At index 1, <code>nums1[1] = 1</code> and <code>nums0[1] = 3</code>, so the segment formed is <code>&quot;1000&quot;</code>.</li>
	<li>Reordering the segments as <code>&quot;111&quot;</code> followed by <code>&quot;1000&quot;</code> produces the binary string <code>&quot;1111000&quot;</code>.</li>
	<li>The binary number <code>&quot;1111000&quot;</code> has value 120 which is the maximum possible value.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums1.length == nums0.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums0[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums1[i] + nums0[i] &gt; 0</code></li>
	<li>The total sum of all elements in <code>nums1</code> and <code>nums0</code> does not exceed 2 * 10<sup>5</sup>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Greedy

Let the binary string corresponding to the $i$-th segment be $1^{x_i}0^{y_i}$, where $x_i = \textit{nums1}[i]$ and $y_i = \textit{nums0}[i]$.

The problem allows us to rearrange these segments arbitrarily, and the goal is to maximize the integer value represented by the final concatenated binary string. Since comparing binary strings by value is essentially equivalent to comparing them lexicographically, we want as many `1`s as possible to appear earlier.

Consider the relative order of two segments $A = 1^a0^b$ and $B = 1^c0^d$. If we concatenate them as $AB$ or $BA$, we should clearly choose the one with the larger lexicographical order.

Based on this rule, we can derive the following sorting strategy:

- If a segment satisfies $y = 0$, it consists only of some `1`s. Such segments should be placed as early as possible because they do not introduce any `0` prematurely. Among these segments, the one with more `1`s should come first.
- If two segments both satisfy $x > 0$ and $y > 0$, then the segment with more leading `1`s should come first, so we sort by $x$ in descending order. If $x$ is the same, then the segment with fewer `0`s should come first, so we sort by $y$ in ascending order.
- If a segment satisfies $x = 0$, it consists only of some `0`s. Such segments should be placed at the end.

After sorting in this way, the concatenated binary string is maximized.

Next, we do not need to actually construct the whole binary string. Let the total length of all concatenated segments be $m$. We preprocess $2^0, 2^1, \dots, 2^{m-1}$ modulo $10^9 + 7$. Then we traverse the segments in sorted order:

- When we encounter a `1`, we add the weight of the current highest bit to the answer.
- When we encounter a `0`, we only need to move the current position backward.

Finally, we obtain the answer.

The time complexity is $O(n \log n + m)$, and the space complexity is $O(n + m)$. Here, $n$ is the number of segments, and $m = \sum \textit{nums1}[i] + \sum \textit{nums0}[i]$. The problem guarantees that $m \le 2 \times 10^5$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        MOD = 10**9 + 7
        pairs = list(zip(nums1, nums0))
        b = sum(x + y for x, y in pairs)

        def key(p: tuple[int, int]) -> tuple[int, int, int]:
            x, y = p
            if y == 0:
                return (0, -x, 0)
            if x > 0:
                return (1, -x, y)
            return (2, y, 0)

        pairs.sort(key=key)

        ans = 0
        p = [1] * b
        for i in range(1, b):
            p[i] = p[i - 1] * 2 % MOD

        b -= 1
        for cnt1, cnt0 in pairs:
            while cnt1:
                ans = (ans + p[b]) % MOD
                b -= 1
                cnt1 -= 1
            b -= cnt0
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
