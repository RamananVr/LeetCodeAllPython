---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2519.Count%20the%20Number%20of%20K-Big%20Indices/README_EN.md
tags:
    - Binary Indexed Tree
    - Segment Tree
    - Array
    - Binary Search
    - Divide and Conquer
    - Ordered Set
    - Merge Sort
---

<!-- problem:start -->

# [2519. Count the Number of K-Big Indices 🔒](https://leetcode.com/problems/count-the-number-of-k-big-indices)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and a positive integer <code>k</code>.</p>

<p>We call an index <code>i</code> <strong>k-big</strong> if the following conditions are satisfied:</p>

<ul>
	<li>There exist at least <code>k</code> different indices <code>idx1</code> such that <code>idx1 &lt; i</code> and <code>nums[idx1] &lt; nums[i]</code>.</li>
	<li>There exist at least <code>k</code> different indices <code>idx2</code> such that <code>idx2 &gt; i</code> and <code>nums[idx2] &lt; nums[i]</code>.</li>
</ul>

<p>Return <em>the number of k-big indices</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,6,5,2,3], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are only two 2-big indices in nums:
- i = 2 --&gt; There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.
- i = 3 --&gt; There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1], k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no 3-big indices in nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], k &lt;= nums.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Indexed Tree

We maintain two binary indexed trees, one records the number of elements smaller than the current position on the left, and the other records the number of elements smaller than the current position on the right.

We traverse the array, and for the current position, if the number of elements smaller than the current position on the left is greater than or equal to $k$, and the number of elements smaller than the current position on the right is greater than or equal to $k$, then the current position is a `k-big`, and we increment the answer by one.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x):
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tree1 = BinaryIndexedTree(n)
        tree2 = BinaryIndexedTree(n)
        for v in nums:
            tree2.update(v, 1)
        ans = 0
        for v in nums:
            tree2.update(v, -1)
            ans += tree1.query(v - 1) >= k and tree2.query(v - 1) >= k
            tree1.update(v, 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
