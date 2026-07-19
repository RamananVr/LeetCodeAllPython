---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3873.Maximum%20Points%20Activated%20with%20One%20Addition/README_EN.md
rating: 2198
source: Weekly Contest 493 Q4
tags:
    - Union Find
    - Array
    - Hash Table
---

<!-- problem:start -->

# [3873. Maximum Points Activated with One Addition](https://leetcode.com/problems/maximum-points-activated-with-one-addition)

## Description

<!-- description:start -->

<p>You are given a 2D integer array <code>points</code>, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the coordinates of the <code>i<sup>th</sup></code> point. All coordinates in <code>points</code> are <strong>distinct</strong>.</p>

<p>If a point is <strong>activated</strong>, then all points that have the <strong>same</strong> x-coordinate <strong>or</strong> y-coordinate become <strong>activated</strong> as well.</p>

<p>Activation continues until no additional points can be activated.</p>

<p>You may add <strong>one additional</strong> point at any integer coordinate <code>(x, y)</code> not already present in <code>points</code>. Activation begins by <strong>activating</strong> this <strong>newly added point</strong>.</p>

<p>Return an integer denoting the <strong>maximum</strong> number of points that can be activated, including the newly added point.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,1],[1,2],[2,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Adding and activating a point such as <code>(1, 3)</code> causes activations:</p>

<ul>
	<li><code>(1, 3)</code> shares <code>x = 1</code> with <code>(1, 1)</code> and <code>(1, 2)</code> -&gt; <code>(1, 1)</code> and <code>(1, 2)</code> become activated.</li>
	<li><code>(1, 2)</code> shares <code>y = 2</code> with <code>(2, 2)</code> -&gt; <code>(2, 2)</code> becomes activated.</li>
</ul>

<p>Thus, the activated points are <code>(1, 3)</code>, <code>(1, 1)</code>, <code>(1, 2)</code>, <code>(2, 2)</code>, so 4 points in total. We can show this is the maximum activated.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[2,2],[1,1],[3,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Adding and activating a point such as <code>(1, 2)</code> causes activations:</p>

<ul>
	<li><code>(1, 2)</code> shares <code>x = 1</code> with <code>(1, 1)</code> -&gt; <code>(1, 1)</code> becomes activated.</li>
	<li><code>(1, 2)</code> shares <code>y = 2</code> with <code>(2, 2)</code> -&gt; <code>(2, 2)</code> becomes activated.</li>
</ul>

<p>Thus, the activated points are <code>(1, 2)</code>, <code>(1, 1)</code>, <code>(2, 2)</code>, so 3 points in total. We can show this is the maximum activated.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[2,3],[2,2],[1,1],[4,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Adding and activating a point such as <code>(2, 1)</code> causes activations:</p>

<ul>
	<li><code>(2, 1)</code> shares <code>x = 2</code> with <code>(2, 3)</code> and <code>(2, 2)</code> -&gt; <code>(2, 3)</code> and <code>(2, 2)</code> become activated.</li>
	<li><code>(2, 1)</code> shares <code>y = 1</code> with <code>(1, 1)</code> -&gt; <code>(1, 1)</code> becomes activated.</li>
</ul>

<p>Thus, the activated points are <code>(2, 1)</code>, <code>(2, 3)</code>, <code>(2, 2)</code>, <code>(1, 1)</code>, so 4 points in total.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code></li>
	<li><code>-10<sup>9</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>points</code> contains all <strong>distinct</strong> coordinates.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Union-Find

We can use a Union-Find data structure to solve this problem.

First, we map the $x$ coordinates and $y$ coordinates of all points into the same Union-Find structure. Specifically, we add a sufficiently large constant $m$ (e.g., $3 \times 10^9$) to each $y$ coordinate to ensure that the $x$ and $y$ coordinates do not conflict.

Next, we iterate over all points and union those that share the same $x$ coordinate or the same $y$ coordinate. This way, points with the same $x$ or $y$ coordinate will be grouped into the same set.

Finally, we count the number of points in each set and find the sizes of the two largest sets. Since we can add one new point to connect these two sets, the final answer is the sum of the sizes of the two largest sets plus $1$.

The time complexity is $O(n \alpha(n))$, where $n$ is the number of points and $\alpha$ is the inverse Ackermann function. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class UnionFind:
    def __init__(self):
        self.p = {}
        self.size = {}

    def find(self, x):
        if x not in self.p:
            self.p[x] = x
            self.size[x] = 1
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        uf = UnionFind()
        m = int(3e9)

        for x, y in points:
            uf.union(x, y + m)

        cnt = Counter()
        for x, _ in points:
            cnt[uf.find(x)] += 1

        mx1 = mx2 = 0
        for x in cnt.values():
            if mx1 < x:
                mx2 = mx1
                mx1 = x
            elif mx2 < x:
                mx2 = x
        return mx1 + mx2 + 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
