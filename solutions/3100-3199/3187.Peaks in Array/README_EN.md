---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3187.Peaks%20in%20Array/README_EN.md
rating: 2154
source: Weekly Contest 402 Q4
tags:
    - Binary Indexed Tree
    - Segment Tree
    - Array
---

<!-- problem:start -->

# [3187. Peaks in Array](https://leetcode.com/problems/peaks-in-array)

## Description

<!-- description:start -->

<p>A <strong>peak</strong> in an array <code>arr</code> is an element that is <strong>greater</strong> than its previous and next element in <code>arr</code>.</p>

<p>You are given an integer array <code>nums</code> and a 2D integer array <code>queries</code>.</p>

<p>You have to process queries of two types:</p>

<ul>
	<li><code>queries[i] = [1, l<sub>i</sub>, r<sub>i</sub>]</code>, determine the count of <strong>peak</strong> elements in the <span data-keyword="subarray">subarray</span> <code>nums[l<sub>i</sub>..r<sub>i</sub>]</code>.<!-- notionvc: 73b20b7c-e1ab-4dac-86d0-13761094a9ae --></li>
	<li><code>queries[i] = [2, index<sub>i</sub>, val<sub>i</sub>]</code>, change <code>nums[index<sub>i</sub>]</code> to <code><font face="monospace">val<sub>i</sub></font></code>.</li>
</ul>

<p>Return an array <code>answer</code> containing the results of the queries of the first type in order.<!-- notionvc: a9ccef22-4061-4b5a-b4cc-a2b2a0e12f30 --></p>

<p><strong>Notes:</strong></p>

<ul>
	<li>The <strong>first</strong> and the <strong>last</strong> element of an array or a subarray<!-- notionvc: fcffef72-deb5-47cb-8719-3a3790102f73 --> <strong>cannot</strong> be a peak.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0]</span></p>

<p><strong>Explanation:</strong></p>

<p>First query: We change <code>nums[3]</code> to 4 and <code>nums</code> becomes <code>[3,1,4,4,5]</code>.</p>

<p>Second query: The number of peaks in the <code>[3,1,4,4,5]</code> is 0.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>First query: <code>nums[2]</code> should become 4, but it is already set to 4.</p>

<p>Second query: The number of peaks in the <code>[4,1,4]</code> is 0.</p>

<p>Third query: The second 4 is a peak in the <code>[4,1,4,2,1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i][0] == 1</code> or <code>queries[i][0] == 2</code></li>
	<li>For all <code>i</code> that:
	<ul>
		<li><code>queries[i][0] == 1</code>: <code>0 &lt;= queries[i][1] &lt;= queries[i][2] &lt;= nums.length - 1</code></li>
		<li><code>queries[i][0] == 2</code>: <code>0 &lt;= queries[i][1] &lt;= nums.length - 1</code>, <code>1 &lt;= queries[i][2] &lt;= 10<sup>5</sup></code></li>
	</ul>
	</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Indexed Tree

According to the problem description, for $0 < i < n - 1$, if it satisfies $nums[i - 1] < nums[i]$ and $nums[i] > nums[i + 1]$, we can consider $nums[i]$ as $1$, otherwise as $0$. Thus, for operation $1$, i.e., querying the number of peak elements in the subarray $nums[l..r]$, it is equivalent to querying the number of $1$s in the interval $[l + 1, r - 1]$. We can use a binary indexed tree to maintain the number of $1$s in the interval $[1, n - 1]$.

For operation $1$, i.e., updating $nums[idx]$ to $val$, it will only affect the values at positions $idx - 1$, $idx$, and $idx + 1$, so we only need to update these three positions. Specifically, we can first remove the peak elements at these three positions, then update the value of $nums[idx]$, and finally add back the peak elements at these three positions.

The time complexity is $O((n + q) \times \log n)$, and the space complexity is $O(n)$. Here, $n$ and $q$ are the lengths of the array `nums` and the query array `queries`, respectively.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    __slots__ = "n", "c"

    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def update(i: int, val: int):
            if i <= 0 or i >= n - 1:
                return
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                tree.update(i, val)

        n = len(nums)
        tree = BinaryIndexedTree(n - 1)
        for i in range(1, n - 1):
            update(i, 1)
        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1] + 1, q[2] - 1
                ans.append(0 if l > r else tree.query(r) - tree.query(l - 1))
            else:
                idx, val = q[1:]
                for i in range(idx - 1, idx + 2):
                    update(i, -1)
                nums[idx] = val
                for i in range(idx - 1, idx + 2):
                    update(i, 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
