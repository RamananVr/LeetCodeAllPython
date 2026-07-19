---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1395.Count%20Number%20of%20Teams/README_EN.md
rating: 1343
source: Weekly Contest 182 Q2
tags:
    - Binary Indexed Tree
    - Segment Tree
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [1395. Count Number of Teams](https://leetcode.com/problems/count-number-of-teams)

## Description

<!-- description:start -->

<p>There are <code>n</code> soldiers standing in a line. Each soldier is assigned a <strong>unique</strong> <code>rating</code> value.</p>

<p>You have to form a team of 3 soldiers amongst them under the following rules:</p>

<ul>
	<li>Choose 3 soldiers with index (<code>i</code>, <code>j</code>, <code>k</code>) with rating (<code>rating[i]</code>, <code>rating[j]</code>, <code>rating[k]</code>).</li>
	<li>A team is valid if: (<code>rating[i] &lt; rating[j] &lt; rating[k]</code>) or (<code>rating[i] &gt; rating[j] &gt; rating[k]</code>) where (<code>0 &lt;= i &lt; j &lt; k &lt; n</code>).</li>
</ul>

<p>Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> rating = [2,5,3,4,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> rating = [2,1,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> We can&#39;t form any team given the conditions.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> rating = [1,2,3,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == rating.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= rating[i] &lt;= 10<sup>5</sup></code></li>
	<li>All the integers in <code>rating</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumerate Middle Element

We can enumerate each element $rating[i]$ in the array $rating$ as the middle element, then count the number of elements $l$ that are smaller than it on the left, and the number of elements $r$ that are larger than it on the right. The number of combat units with this element as the middle element is $l \times r + (i - l) \times (n - i - 1 - r)$. We can add this to the answer.

The time complexity is $O(n^2)$, and the space complexity is $O(1)$. Where $n$ is the length of the array $rating$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)
        for i, b in enumerate(rating):
            l = sum(a < b for a in rating[:i])
            r = sum(c > b for c in rating[i + 1 :])
            ans += l * r
            ans += (i - l) * (n - i - 1 - r)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Binary Indexed Tree

We can use two binary indexed trees to maintain the number of elements $l$ that are smaller than each element on the left in the array $rating$, and the number of elements $r$ that are larger than it on the right. Then count the number of combat units with this element as the middle element as $l \times r + (i - l) \times (n - i - 1 - r)$, and add this to the answer.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array $rating$.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] += v
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        nums = sorted(set(rating))
        m = len(nums)
        tree1 = BinaryIndexedTree(m)
        tree2 = BinaryIndexedTree(m)
        for v in rating:
            x = bisect_left(nums, v) + 1
            tree2.update(x, 1)
        n = len(rating)
        ans = 0
        for i, v in enumerate(rating):
            x = bisect_left(nums, v) + 1
            tree1.update(x, 1)
            tree2.update(x, -1)
            l = tree1.query(x - 1)
            r = n - i - 1 - tree2.query(x)
            ans += l * r
            ans += (i - l) * (n - i - 1 - r)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Recursion + Memoization

<!-- solution:end -->

<!-- problem:end -->
