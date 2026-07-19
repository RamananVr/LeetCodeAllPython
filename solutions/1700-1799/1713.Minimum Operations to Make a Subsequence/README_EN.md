---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1713.Minimum%20Operations%20to%20Make%20a%20Subsequence/README_EN.md
rating: 2350
source: Weekly Contest 222 Q4
tags:
    - Greedy
    - Array
    - Hash Table
    - Binary Search
---

<!-- problem:start -->

# [1713. Minimum Operations to Make a Subsequence](https://leetcode.com/problems/minimum-operations-to-make-a-subsequence)

## Description

<!-- description:start -->

<p>You are given an array <code>target</code> that consists of <strong>distinct</strong> integers and another integer array <code>arr</code> that <strong>can</strong> have duplicates.</p>

<p>In one operation, you can insert any integer at any position in <code>arr</code>. For example, if <code>arr = [1,4,1,2]</code>, you can add <code>3</code> in the middle and make it <code>[1,4,<u>3</u>,1,2]</code>. Note that you can insert the integer at the very beginning or end of the array.</p>

<p>Return <em>the <strong>minimum</strong> number of operations needed to make </em><code>target</code><em> a <strong>subsequence</strong> of </em><code>arr</code><em>.</em></p>

<p>A <strong>subsequence</strong> of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements&#39; relative order. For example, <code>[2,7,4]</code> is a subsequence of <code>[4,<u>2</u>,3,<u>7</u>,2,1,<u>4</u>]</code> (the underlined elements), while <code>[2,4,2]</code> is not.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = [5,1,3], <code>arr</code> = [9,4,2,3,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can add 5 and 1 in such a way that makes <code>arr</code> = [<u>5</u>,9,4,<u>1</u>,2,3,4], then target will be a subsequence of <code>arr</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = [6,4,8,1,3,2], <code>arr</code> = [4,7,6,2,3,8,6,1]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length, arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= target[i], arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>target</code> contains no duplicates.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Longest Increasing Subsequence + Binary Indexed Tree

According to the problem statement, the longer the common subsequence between `target` and `arr`, the fewer elements need to be added. Therefore, the minimum number of elements to be added equals the length of `target` minus the length of the longest common subsequence between `target` and `arr`.

However, the time complexity of [finding the longest common subsequence](https://github.com/doocs/leetcode/blob/main/solution/1100-1199/1143.Longest%20Common%20Subsequence/README.md) is $O(m \times n)$, which cannot pass this problem. We need to change our approach.

We can use a hash table to record the index of each element in the `target` array, then iterate through the `arr` array. For each element in the `arr` array, if the hash table contains that element, we add the index of that element to an array. This gives us a new array `nums`, which represents the indices in the `target` array of elements from `arr` (excluding elements not in `target`). The length of the longest increasing subsequence of this array `nums` is the length of the longest common subsequence between `target` and `arr`.

Therefore, the problem is transformed into finding the length of the longest increasing subsequence of the `nums` array. Refer to [300. Longest Increasing Subsequence](https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0300.Longest%20Increasing%20Subsequence/README.md).

The time complexity is $O(n \times \log m)$, and the space complexity is $O(m)$. Here, $m$ and $n$ are the lengths of `target` and `arr`, respectively.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    __slots__ = "n", "c"

    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] = max(self.c[x], v)
            x += x & -x

    def query(self, x: int) -> int:
        res = 0
        while x:
            res = max(res, self.c[x])
            x -= x & -x
        return res

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d = {x: i for i, x in enumerate(target, 1)}
        nums = [d[x] for x in arr if x in d]
        m = len(target)
        tree = BinaryIndexedTree(m)
        ans = 0
        for x in nums:
            v = tree.query(x - 1) + 1
            ans = max(ans, v)
            tree.update(x, v)
        return len(target) - ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
