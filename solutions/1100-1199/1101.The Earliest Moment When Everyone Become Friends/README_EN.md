---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1101.The%20Earliest%20Moment%20When%20Everyone%20Become%20Friends/README_EN.md
rating: 1558
source: Biweekly Contest 3 Q3
tags:
    - Union Find
    - Array
    - Sorting
---

<!-- problem:start -->

# [1101. The Earliest Moment When Everyone Become Friends 🔒](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends)

## Description

<!-- description:start -->

<p>There are n people in a social group labeled from <code>0</code> to <code>n - 1</code>. You are given an array <code>logs</code> where <code>logs[i] = [timestamp<sub>i</sub>, x<sub>i</sub>, y<sub>i</sub>]</code> indicates that <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> will be friends at the time <code>timestamp<sub>i</sub></code>.</p>

<p>Friendship is <strong>symmetric</strong>. That means if <code>a</code> is friends with <code>b</code>, then <code>b</code> is friends with <code>a</code>. Also, person <code>a</code> is acquainted with a person <code>b</code> if <code>a</code> is friends with <code>b</code>, or <code>a</code> is a friend of someone acquainted with <code>b</code>.</p>

<p>Return <em>the earliest time for which every person became acquainted with every other person</em>. If there is no such earliest time, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
<strong>Output:</strong> 20190301
<strong>Explanation:</strong> 
The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>logs[i].length == 3</code></li>
	<li><code>0 &lt;= timestamp<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>x<sub>i</sub> != y<sub>i</sub></code></li>
	<li>All the values <code>timestamp<sub>i</sub></code> are <strong>unique</strong>.</li>
	<li>All the pairs <code>(x<sub>i</sub>, y<sub>i</sub>)</code> occur at most one time in the input.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Union-Find

We sort all the logs in ascending order by timestamp, then traverse the sorted logs. Using a union-find set, we check whether the two people in the current log are already friends. If they are not friends, we merge them into one friend circle, until everyone is in one friend circle, then return the timestamp of the current log.

If we have traversed all the logs and not everyone is in one friend circle, then return $-1$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the number of logs.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        for t, x, y in sorted(logs):
            if find(x) == find(y):
                continue
            p[find(x)] = find(y)
            n -= 1
            if n == 1:
                return t
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class UnionFind:
    __slots__ = ('p', 'size')

    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int) -> bool:
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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        for t, x, y in sorted(logs):
            if uf.union(x, y):
                n -= 1
                if n == 1:
                    return t
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
