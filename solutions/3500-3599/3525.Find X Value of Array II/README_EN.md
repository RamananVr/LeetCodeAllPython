---
comments: true
difficulty: Hard
rating: 2644
source: Weekly Contest 446 Q4
tags:
    - Segment Tree
    - Array
    - Math
---

<!-- problem:start -->

# [3525. Find X Value of Array II](https://leetcode.com/problems/find-x-value-of-array-ii)

## Description

<!-- description:start -->

<p>You are given an array of <strong>positive</strong> integers <code>nums</code> and a <strong>positive</strong> integer <code>k</code>. You are also given a 2D array <code>queries</code>, where <code>queries[i] = [index<sub>i</sub>, value<sub>i</sub>, start<sub>i</sub>, x<sub>i</sub>]</code>.</p>

<p>You are allowed to perform an operation <strong>once</strong> on <code>nums</code>, where you can remove any <strong>suffix</strong> from <code>nums</code> such that <code>nums</code> remains <strong>non-empty</strong>.</p>

<p>The <strong>x-value</strong> of <code>nums</code> <strong>for a given</strong> <code>x</code> is defined as the number of ways to perform this operation so that the <strong>product</strong> of the remaining elements leaves a <em>remainder</em> of <code>x</code> <strong>modulo</strong> <code>k</code>.</p>

<p>For each query in <code>queries</code> you need to determine the <strong>x-value</strong> of <code>nums</code> for <code>x<sub>i</sub></code> after performing the following actions:</p>

<ul>
	<li>Update <code>nums[index<sub>i</sub>]</code> to <code>value<sub>i</sub></code>. Only this step persists for the rest of the queries.</li>
	<li><strong>Remove</strong> the prefix <code>nums[0..(start<sub>i</sub> - 1)]</code> (where <code>nums[0..(-1)]</code> will be used to represent the <strong>empty</strong> prefix).</li>
</ul>

<p>Return an array <code>result</code> of size <code>queries.length</code> where <code>result[i]</code> is the answer for the <code>i<sup>th</sup></code> query.</p>

<p>A <strong>prefix</strong> of an array is a <span data-keyword="subarray">subarray</span> that starts from the beginning of the array and extends to any point within it.</p>

<p>A <strong>suffix</strong> of an array is a <span data-keyword="subarray">subarray</span> that starts at any point within the array and extends to the end of the array.</p>

<p><strong>Note</strong> that the prefix and suffix to be chosen for the operation can be <strong>empty</strong>.</p>

<p><strong>Note</strong> that x-value has a <em>different</em> definition in this version.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For query 0, <code>nums</code> becomes <code>[1, 2, 2, 4, 5]</code>, and the empty prefix <strong>must</strong> be removed. The possible operations are:

    <ul>
    	<li>Remove the suffix <code>[2, 4, 5]</code>. <code>nums</code> becomes <code>[1, 2]</code>.</li>
    	<li>Remove the empty suffix. <code>nums</code> becomes <code>[1, 2, 2, 4, 5]</code> with a product 80, which gives remainder 2 when divided by 3.</li>
    </ul>
    </li>
    <li>For query 1, <code>nums</code> becomes <code>[1, 2, 2, 3, 5]</code>, and the prefix <code>[1, 2, 2]</code> <strong>must</strong> be removed. The possible operations are:
    <ul>
    	<li>Remove the empty suffix. <code>nums</code> becomes <code>[3, 5]</code>.</li>
    	<li>Remove the suffix <code>[5]</code>. <code>nums</code> becomes <code>[3]</code>.</li>
    </ul>
    </li>
    <li>For query 2, <code>nums</code> becomes <code>[1, 2, 2, 3, 5]</code>, and the empty prefix <strong>must</strong> be removed. The possible operations are:
    <ul>
    	<li>Remove the suffix <code>[2, 2, 3, 5]</code>. <code>nums</code> becomes <code>[1]</code>.</li>
    	<li>Remove the suffix <code>[3, 5]</code>. <code>nums</code> becomes <code>[1, 2, 2]</code>.</li>
    </ul>
    </li>

</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For query 0, <code>nums</code> becomes <code>[2, 2, 4, 8, 16, 32]</code>. The only possible operation is:

    <ul>
    	<li>Remove the suffix <code>[2, 4, 8, 16, 32]</code>.</li>
    </ul>
    </li>
    <li>For query 1, <code>nums</code> becomes <code>[2, 2, 4, 8, 16, 32]</code>. There is no possible way to perform the operation.</li>

</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[5]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 5</code></li>
	<li><code>1 &lt;= queries.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>queries[i] == [index<sub>i</sub>, value<sub>i</sub>, start<sub>i</sub>, x<sub>i</sub>]</code></li>
	<li><code>0 &lt;= index<sub>i</sub> &lt;= nums.length - 1</code></li>
	<li><code>1 &lt;= value<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= nums.length - 1</code></li>
	<li><code>0 &lt;= x<sub>i</sub> &lt;= k - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Segment Tree

<!-- thinking:start -->

> **Thinking**
>
> The static count from the previous problem does not survive point updates and a forced prefix deletion. $k \le 5$, so a segment only needs its product modulo $k$ and the number of ways each remainder arises after dropping a suffix.
>
> Store that payload in a segment tree and define a merge. After each update, query the target remainder on $[start, n)$.

<!-- thinking:end -->

Each query first sets $nums[\textit{index}]$ to $\textit{value}$ (the update persists), then drops the prefix $nums[0..start-1]$. After that we may only drop a suffix, so the remainder is a non-empty prefix of $nums[start..n-1]$. The query therefore counts how many prefixes of $[start, n)$ have product congruent to $x$ modulo $k$.

Since $k \le 5$, each segment-tree node stores:

- $\textit{prod}$: the product of the whole segment modulo $k$
- $\textit{cnt}[r]$: how many prefixes of this segment have product $r$ modulo $k$

A leaf with $a = nums[i] \bmod k$ has $\textit{prod} = a$ and $\textit{cnt}[a] = 1$.

Merging left and right children $L$ and $R$:

$$
P.\textit{prod} = (L.\textit{prod} \times R.\textit{prod}) \bmod k
$$

Prefixes lying entirely in $L$ copy $L.\textit{cnt}$. Prefixes that take all of $L$ and then a prefix of $R$ contribute $R.\textit{cnt}[r]$ to remainder $(L.\textit{prod} \times r) \bmod k$.

After a point update, query $\textit{cnt}[x]$ on $[start+1, n]$ (1-indexed). Merges during a query must combine left then right.

The time complexity is $O((n + q) \times k \times \log n)$ and the space complexity is $O(n \times k)$, where $n$ is the array length and $q$ is the number of queries.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = "l", "r", "prod", "cnt"

    def __init__(self, l: int, r: int, k: int):
        self.l = l
        self.r = r
        self.prod = 1
        self.cnt = [0] * k

class SegmentTree:
    __slots__ = "k", "tr"

    def __init__(self, nums: list[int], k: int):
        self.k = k
        n = len(nums)
        self.tr = [None] * (n << 2)
        self.build(1, 1, n, nums)

    def merge(self, a: Node, b: Node) -> tuple[int, list[int]]:
        k = self.k
        prod = a.prod * b.prod % k
        cnt = a.cnt[:]
        for r, c in enumerate(b.cnt):
            cnt[a.prod * r % k] += c
        return prod, cnt

    def pushup(self, u: int):
        prod, cnt = self.merge(self.tr[u << 1], self.tr[u << 1 | 1])
        self.tr[u].prod = prod
        self.tr[u].cnt = cnt

    def build(self, u: int, l: int, r: int, nums: list[int]):
        self.tr[u] = Node(l, r, self.k)
        if l == r:
            v = nums[l - 1] % self.k
            self.tr[u].prod = v
            self.tr[u].cnt[v] = 1
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid, nums)
        self.build(u << 1 | 1, mid + 1, r, nums)
        self.pushup(u)

    def modify(self, u: int, x: int, v: int):
        if self.tr[u].l == self.tr[u].r:
            v %= self.k
            self.tr[u].prod = v
            self.tr[u].cnt = [0] * self.k
            self.tr[u].cnt[v] = 1
            return
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if x <= mid:
            self.modify(u << 1, x, v)
        else:
            self.modify(u << 1 | 1, x, v)
        self.pushup(u)

    def query(self, u: int, l: int, r: int) -> Node:
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u]
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if r <= mid:
            return self.query(u << 1, l, r)
        if l > mid:
            return self.query(u << 1 | 1, l, r)
        left = self.query(u << 1, l, r)
        right = self.query(u << 1 | 1, l, r)
        prod, cnt = self.merge(left, right)
        res = Node(0, 0, self.k)
        res.prod = prod
        res.cnt = cnt
        return res

class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []
        for idx, val, start, x in queries:
            tree.modify(1, idx + 1, val)
            ans.append(tree.query(1, start + 1, n).cnt[x])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
