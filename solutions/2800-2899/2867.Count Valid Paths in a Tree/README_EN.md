---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2867.Count%20Valid%20Paths%20in%20a%20Tree/README_EN.md
rating: 2428
source: Weekly Contest 364 Q4
tags:
    - Tree
    - Depth-First Search
    - Math
    - Dynamic Programming
    - Number Theory
---

<!-- problem:start -->

# [2867. Count Valid Paths in a Tree](https://leetcode.com/problems/count-valid-paths-in-a-tree)

## Description

<!-- description:start -->

<p>There is an undirected tree with <code>n</code> nodes labeled from <code>1</code> to <code>n</code>. You are given the integer <code>n</code> and a 2D integer array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates that there is an edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> in the tree.</p>

<p>Return <em>the <strong>number of valid paths</strong> in the tree</em>.</p>

<p>A path <code>(a, b)</code> is <strong>valid</strong> if there exists <strong>exactly one</strong> prime number among the node labels in the path from <code>a</code> to <code>b</code>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>The path <code>(a, b)</code> is a sequence of <strong>distinct</strong> nodes starting with node <code>a</code> and ending with node <code>b</code> such that every two adjacent nodes in the sequence share an edge in the tree.</li>
	<li>Path <code>(a, b)</code> and path <code>(b, a)</code> are considered the <strong>same</strong> and counted only <strong>once</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2867.Count%20Valid%20Paths%20in%20a%20Tree/images/example1.png" style="width: 440px; height: 357px;" />
<pre>
<strong>Input:</strong> n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2. 
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (2, 4) since the path from 2 to 4 contains prime number 2.
It can be shown that there are only 4 valid paths.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2867.Count%20Valid%20Paths%20in%20a%20Tree/images/example2.png" style="width: 488px; height: 384px;" />
<pre>
<strong>Input:</strong> n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2.
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (1, 6) since the path from 1 to 6 contains prime number 3.
- (2, 4) since the path from 2 to 4 contains prime number 2.
- (3, 6) since the path from 3 to 6 contains prime number 3.
It can be shown that there are only 6 valid paths.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li>The input is generated such that <code>edges</code> represent a valid tree.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Union-Find + Enumeration

We can preprocess to get all the prime numbers in $[1, n]$, where $prime[i]$ indicates whether $i$ is a prime number.

Next, we build a graph $g$ based on the two-dimensional integer array, where $g[i]$ represents all the neighbor nodes of node $i$. If both nodes of an edge are not prime numbers, we merge these two nodes into the same connected component.

Then, we enumerate all prime numbers $i$ in the range of $[1, n]$, considering all paths that include $i$.

Since $i$ is already a prime number, if $i$ is an endpoint of the path, we only need to accumulate the sizes of all connected components adjacent to node $i$. If $i$ is a middle point on the path, we need to accumulate the product of the sizes of any two adjacent connected components.

The time complexity is $O(n \times \alpha(n))$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes, and $\alpha$ is the inverse function of the Ackermann function.

<!-- tabs:start -->

#### Python3

```python
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
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

mx = 10**5 + 10
prime = [True] * (mx + 1)
prime[0] = prime[1] = False
for i in range(2, mx + 1):
    if prime[i]:
        for j in range(i * i, mx + 1, i):
            prime[j] = False

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        uf = UnionFind(n + 1)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            if prime[u] + prime[v] == 0:
                uf.union(u, v)

        ans = 0
        for i in range(1, n + 1):
            if prime[i]:
                t = 0
                for j in g[i]:
                    if not prime[j]:
                        cnt = uf.size[uf.find(j)]
                        ans += cnt
                        ans += t * cnt
                        t += cnt
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        def mul(x, y):
            return x * y

        def dfs(x, f, con, prime, r):
            v = [1 - prime[x], prime[x]]
            for y in con[x]:
                if y == f:
                    continue
                p = dfs(y, x, con, prime, r)
                r[0] += mul(p[0], v[1]) + mul(p[1], v[0])
                if prime[x]:
                    v[1] += p[0]
                else:
                    v[0] += p[0]
                    v[1] += p[1]
            return v

        prime = [True] * (n + 1)
        prime[1] = False

        all_primes = []
        for i in range(2, n + 1):
            if prime[i]:
                all_primes.append(i)
            for x in all_primes:
                temp = i * x
                if temp > n:
                    break
                prime[temp] = False
                if i % x == 0:
                    break

        con = [[] for _ in range(n + 1)]
        for e in edges:
            con[e[0]].append(e[1])
            con[e[1]].append(e[0])

        r = [0]
        dfs(1, 0, con, prime, r)
        return r[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
