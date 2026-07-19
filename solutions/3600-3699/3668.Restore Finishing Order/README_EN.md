---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3600-3699/3668.Restore%20Finishing%20Order/README_EN.md
rating: 1255
source: Weekly Contest 465 Q1
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [3668. Restore Finishing Order](https://leetcode.com/problems/restore-finishing-order)

## Description

<!-- description:start -->

<p>You are given an integer array <code>order</code> of length <code>n</code> and an integer array <code>friends</code>.</p>

<ul>
	<li><code>order</code> contains every integer from 1 to <code>n</code> <strong>exactly once</strong>, representing the IDs of the participants of a race in their <strong>finishing</strong> order.</li>
	<li><code>friends</code> contains the IDs of your friends in the race <strong>sorted</strong> in strictly increasing order. Each ID in friends is guaranteed to appear in the <code>order</code> array.</li>
</ul>

<p>Return an array containing your friends&#39; IDs in their <strong>finishing</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">order = [3,1,2,5,4], friends = [1,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,1,4]</span></p>

<p><strong>Explanation:</strong></p>

<p>The finishing order is <code>[<u><strong>3</strong></u>, <u><strong>1</strong></u>, 2, 5, <u><strong>4</strong></u>]</code>. Therefore, the finishing order of your friends is <code>[3, 1, 4]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">order = [1,4,5,3,2], friends = [2,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[5,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The finishing order is <code>[1, 4, <u><strong>5</strong></u>, 3, <u><strong>2</strong></u>]</code>. Therefore, the finishing order of your friends is <code>[5, 2]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == order.length &lt;= 100</code></li>
	<li><code>order</code> contains every integer from 1 to <code>n</code> exactly once</li>
	<li><code>1 &lt;= friends.length &lt;= min(8, n)</code></li>
	<li><code>1 &lt;= friends[i] &lt;= n</code></li>
	<li><code>friends</code> is strictly increasing</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Custom Sorting

First, we build a mapping from the order array to record the finishing position of each ID. Then, we sort the friends array based on the finishing order of these IDs in the order array.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the order array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        d = {x: i for i, x in enumerate(order)}
        return sorted(friends, key=lambda x: d[x])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
