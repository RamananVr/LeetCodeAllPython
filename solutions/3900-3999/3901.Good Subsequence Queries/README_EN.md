---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3900-3999/3901.Good%20Subsequence%20Queries/README_EN.md
rating: 2544
source: Weekly Contest 497 Q4
tags:
    - Segment Tree
    - Array
    - Math
    - Number Theory
---

<!-- problem:start -->

# [3901. Good Subsequence Queries](https://leetcode.com/problems/good-subsequence-queries)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>p</code>.</p>

<p>A <strong>non-empty <span data-keyword="subsequence-sequence">subsequence</span></strong> of <code>nums</code> is called <strong>good</strong> if:</p>

<ul>
	<li>Its length is <strong>strictly less</strong> than <code>n</code>.</li>
	<li>The <strong>greatest common divisor (GCD)</strong> of its elements is <strong>exactly</strong> <code>p</code>.</li>
</ul>

<p>You are also given a 2D integer array <code>queries</code> of length <code>q</code>, where each <code>queries[i] = [ind<sub>i</sub>, val<sub>i</sub>]</code> indicates that you should update <code>nums[ind<sub>i</sub>]</code> to <code>val<sub>i</sub></code>.</p>

<p>After each query, determine whether there exists <strong>any good subsequence</strong> in the current array.</p>

<p>Return the <strong>number</strong> of queries for which a <strong>good subsequence</strong> exists.</p>
The term <code>gcd(a, b)</code> denotes the <strong>greatest common divisor</strong> of <code>a</code> and <code>b</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;"><code>[ind<sub>i</sub>, val<sub>i</sub>]</code></th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated <code>nums</code></th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>[0, 3]</code></td>
			<td style="border: 1px solid black;">Update <code>nums[0]</code> to <code>3</code></td>
			<td style="border: 1px solid black;"><code>[3, 8, 12, 16]</code></td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly <code>p = 2</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>[2, 6]</code></td>
			<td style="border: 1px solid black;">Update <code>nums[2]</code> to <code>6</code></td>
			<td style="border: 1px solid black;"><code>[3, 8, 6, 16]</code></td>
			<td style="border: 1px solid black;">Yes, subsequence <code>[8, 6]</code> has GCD exactly <code>p = 2</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the answer is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;"><code>[ind<sub>i</sub>, val<sub>i</sub>]</code></th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated <code>nums</code></th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>[0, 6]</code></td>
			<td style="border: 1px solid black;">Update <code>nums[0]</code> to <code>6</code></td>
			<td style="border: 1px solid black;"><code>[6, 5, 7, 8]</code></td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly <code>p = 3</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>[1, 9]</code></td>
			<td style="border: 1px solid black;">Update <code>nums[1]</code> to <code>9</code></td>
			<td style="border: 1px solid black;"><code>[6, 9, 7, 8]</code></td>
			<td style="border: 1px solid black;">Yes, subsequence <code>[6, 9]</code> has GCD exactly <code>p = 3</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>[2, 3]</code></td>
			<td style="border: 1px solid black;">Update <code>nums[2]</code> to <code>3</code></td>
			<td style="border: 1px solid black;"><code>[6, 9, 3, 8]</code></td>
			<td style="border: 1px solid black;">Yes, subsequence <code>[6, 9, 3]</code> has GCD exactly <code>p = 3</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the answer is 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,7,9], p = 2, queries = [[1,4],[2,8]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;"><code>[ind<sub>i</sub>, val<sub>i</sub>]</code></th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Updated <code>nums</code></th>
			<th style="border: 1px solid black;">Any good Subsequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>[1, 4]</code></td>
			<td style="border: 1px solid black;">Update <code>nums[1]</code> to <code>4</code></td>
			<td style="border: 1px solid black;"><code>[5, 4, 9]</code></td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly <code>p = 2</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>[2, 8]</code></td>
			<td style="border: 1px solid black;">Update <code>nums[2]</code> to <code>8</code></td>
			<td style="border: 1px solid black;"><code>[5, 4, 8]</code></td>
			<td style="border: 1px solid black;">No, as no subsequence has GCD exactly <code>p = 2</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>queries[i] = [ind<sub>i</sub>, val<sub>i</sub>]</code></li>
	<li><code>1 &lt;= val<sub>i</sub>, p &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ind<sub>i</sub> &lt;= n - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Segment Tree + GCD

We only care about numbers that are multiples of $p$, because if a number is not divisible by $p$, it can never belong to a subsequence whose GCD is exactly $p$.

Therefore, we can treat positions whose values are not divisible by $p$ as $0$, and only maintain the following value for each position in the segment tree:

- If $\textit{nums}[i]$ is divisible by $p$, store its actual value in the segment tree.
- Otherwise, store $0$.

In this way, the whole segment tree maintains the GCD of all current multiples of $p$. Denote it by $g$:

- If $g \ne p$, then no matter how we choose, the GCD of all candidate elements cannot be exactly $p$, so the answer is definitely false.
- If $g = p$, then all multiples of $p$ together already have GCD equal to $p$.

Next, we still need the subsequence length to be strictly smaller than $n$.

- If not all elements are divisible by $p$, that is, the number of valid elements satisfies $\textit{cnt} < n$, then we can directly take all multiples of $p$, and this is already a good subsequence of length less than $n$.
- If $\textit{cnt} = n$, then every element is divisible by $p$, so we must delete at least one element and check whether the GCD of the remaining elements is still $p$.

Here we use the following fact: if $n > 6$, all elements are divisible by $p$, and the overall GCD is already $p$, then we can always delete one element and still keep the GCD equal to $p$. So we only need to brute-force the deleted position when $n \le 6$ and all elements are divisible by $p$. In that case, we query the GCD of the left part and the right part with the segment tree, and then merge them.

The segment tree supports two operations:

- Point update: change one position to the new value or to $0$.
- Range query: get the GCD of a given interval.

After each query update, we just apply the rules above to determine whether a good subsequence exists.

The time complexity is $O((n + q) \times \log n)$. In the worst case, when $n \le 6$, we additionally enumerate the deleted position for each query, but that is only a constant factor. So the total complexity remains $O((n + q) \times \log n)$. The space complexity is $O(n)$, where $n$ is the length of $\textit{nums}$ and $q$ is the number of queries.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = "l", "r", "g"

    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.g = 0

class SegmentTree:
    __slots__ = "tr"

    def __init__(self, n: int):
        self.tr: list[Node | None] = [None] * (n << 2)
        self.build(1, 1, n)

    def build(self, u: int, l: int, r: int):
        self.tr[u] = Node(l, r)
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def pushup(self, u: int):
        self.tr[u].g = gcd(self.tr[u << 1].g, self.tr[u << 1 | 1].g)

    def modify(self, u: int, x: int, v: int):
        if self.tr[u].l == self.tr[u].r:
            self.tr[u].g = v
            return
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if x <= mid:
            self.modify(u << 1, x, v)
        else:
            self.modify(u << 1 | 1, x, v)
        self.pushup(u)

    def query(self, u: int, l: int, r: int) -> int:
        if l > r:
            return 0
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].g
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if r <= mid:
            return self.query(u << 1, l, r)
        if l > mid:
            return self.query(u << 1 | 1, l, r)
        return gcd(self.query(u << 1, l, mid), self.query(u << 1 | 1, mid + 1, r))

class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        n = len(nums)
        tree = SegmentTree(n)
        cnt = 0

        for i, x in enumerate(nums, 1):
            if x % p == 0:
                tree.modify(1, i, x)
                cnt += 1

        ans = 0
        for idx, val in queries:
            if nums[idx] % p == 0:
                tree.modify(1, idx + 1, 0)
                cnt -= 1
            if val % p == 0:
                tree.modify(1, idx + 1, val)
                cnt += 1
            nums[idx] = val

            if tree.tr[1].g != p:
                continue

            if cnt < n or n > 6:
                ans += 1
                continue

            for i in range(1, n + 1):
                left_g = tree.query(1, 1, i - 1)
                right_g = tree.query(1, i + 1, n)
                if gcd(left_g, right_g) == p:
                    ans += 1
                    break

        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
