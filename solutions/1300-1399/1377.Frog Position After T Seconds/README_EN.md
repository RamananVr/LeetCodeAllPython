---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1377.Frog%20Position%20After%20T%20Seconds/README_EN.md
rating: 1823
source: Weekly Contest 179 Q4
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Graph
---

<!-- problem:start -->

# [1377. Frog Position After T Seconds](https://leetcode.com/problems/frog-position-after-t-seconds)

## Description

<!-- description:start -->

<p>Given an undirected tree consisting of <code>n</code> vertices numbered from <code>1</code> to <code>n</code>. A frog starts jumping from <strong>vertex 1</strong>. In one second, the frog jumps from its current vertex to another <strong>unvisited</strong> vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.</p>

<p>The edges of the undirected tree are given in the array <code>edges</code>, where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> means that exists an edge connecting the vertices <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>.</p>

<p><em>Return the probability that after <code>t</code> seconds the frog is on the vertex <code>target</code>. </em>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1377.Frog%20Position%20After%20T%20Seconds/images/frog1.jpg" style="width: 338px; height: 304px;" />
<pre>
<strong>Input:</strong> n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
<strong>Output:</strong> 0.16666666666666666 
<strong>Explanation:</strong> The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after <strong>second 1</strong> and then jumping with 1/2 probability to vertex 4 after <strong>second 2</strong>. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1377.Frog%20Position%20After%20T%20Seconds/images/frog2.jpg" style="width: 304px; height: 304px;" /></strong>

<pre>
<strong>Input:</strong> n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
<strong>Output:</strong> 0.3333333333333333
<strong>Explanation: </strong>The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after <strong>second 1</strong>. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
	<li><code>1 &lt;= t &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

First, based on the undirected tree edges given in the problem, we construct an adjacency list $g$, where $g[u]$ represents all adjacent vertices of vertex $u$.

Then, we define the following data structures:

- Queue $q$, used to store the vertices and their probabilities for each round of search. Initially, $q = [(1, 1.0)]$, indicating that the probability of the frog being at vertex $1$ is $1.0$;
- Array $vis$, used to record whether each vertex has been visited. Initially, $vis[1] = true$, and all other elements are $false$.

Next, we start the breadth-first search.

In each round of search, we take out the head element $(u, p)$ of the queue, where $u$ and $p$ represent the current vertex and its probability, respectively. The number of unvisited adjacent vertices of the current vertex $u$ is denoted as $cnt$.

- If $u = target$, it means that the frog has reached the target vertex. At this time, we judge whether the frog reaches the target vertex in $t$ seconds, or it reaches the target vertex in less than $t$ seconds but cannot jump to other vertices (i.e., $t=0$ or $cnt=0$). If so, return $p$, otherwise return $0$.
- If $u \neq target$, we evenly distribute the probability $p$ to all unvisited adjacent vertices of $u$, then add these vertices to the queue $q$, and mark these vertices as visited.

At the end of a round of search, we decrease $t$ by $1$, and then continue the next round of search until the queue is empty or $t \lt 0$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        q = deque([(1, 1.0)])
        vis = [False] * (n + 1)
        vis[1] = True
        while q and t >= 0:
            for _ in range(len(q)):
                u, p = q.popleft()
                cnt = len(g[u]) - int(u != 1)
                if u == target:
                    return p if cnt * t == 0 else 0
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        q.append((v, p / cnt))
            t -= 1
        return 0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
