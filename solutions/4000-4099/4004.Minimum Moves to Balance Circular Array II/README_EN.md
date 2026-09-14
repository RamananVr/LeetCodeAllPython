---
comments: true
difficulty: Hard
tags:
    - Graph
    - Array
    - Math
    - Min-Cost Flow
---

<!-- problem:start -->

# [4004. Minimum Moves to Balance Circular Array II 🔒](https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii)

## Description

<!-- description:start -->

<p>You are given a <span data-keyword="circular-array">circular array</span> <code>balance</code> of length <code>n</code>, where <code>balance[i]</code> is the net balance of person <code>i</code>.</p>

<p>In one move, a person can transfer <strong>exactly</strong> 1 unit of balance to either their left or right neighbor.</p>

<p>Return the <strong>minimum</strong> number of moves required so that every person has a <strong>non-negative</strong> balance. If it is impossible, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">balance = [-1,2,-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal sequence of moves is:</p>

<ul>
	<li>Move 1 unit from <code>i = 1</code> to <code>i = 0</code>, resulting in <code>balance = [0, 1, -1]</code></li>
	<li>Move 1 unit from <code>i = 1</code> to <code>i = 2</code>, resulting in <code>balance = [0, 0, 0]</code></li>
</ul>

<p>Thus, the minimum number of moves required is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">balance = [4,-1,-2]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal sequence of moves is:</p>

<ul>
	<li>Move 1 unit from <code>i = 0</code> to <code>i = 1</code>, resulting in <code>balance = [3, 0, -2]</code></li>
	<li>Move 1 unit from <code>i = 0</code> to <code>i = 2</code>, resulting in <code>balance = [2, 0, -1]</code></li>
	<li>Move 1 unit from <code>i = 0</code> to <code>i = 2</code>, resulting in <code>balance = [1, 0, 0]</code></li>
</ul>

<p>Thus, the minimum number of moves required is 3.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">balance = [-3,-3,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>It is impossible to make all balances non-negative for <code>balance = [-3, -3, 5]</code>, so the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == balance.length &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup> &lt;= balance[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Minimum Cost Maximum Flow

<!-- thinking:start -->

> **Thinking**
>
> Each move ships one unit to a neighbor on a cycle, with $n\le 1000$. Searching sequences of moves does not scale.
>
> Surplus cells must send units to deficit cells, and the number of steps a unit walks is the operation count. That is min-cost flow with surplus as sources, deficits as sinks, and infinite-capacity cycle edges of cost $1$; the required flow equals the total deficit. A negative total balance is impossible.
>
> The cycle is bidirectional and unit-cost, so successive SPFA augmentations suffice. For this $n$ the worst-case $O(n^3)$ bound is acceptable.

<!-- thinking:end -->

Let $n$ be the length of $\textit{balance}$. If the sum of all balances is negative, it is impossible to make everyone's balance non-negative, so we return $-1$ directly.

Otherwise, we model the problem as a **minimum cost flow** problem:

- Create a source $s$ and a sink $t$;
- For each person $i$ with $\textit{balance}[i] > 0$ (a surplus), add an edge from $s$ to $i$ with capacity $\textit{balance}[i]$ and unit cost $0$;
- For each person $i$ with $\textit{balance}[i] < 0$ (a deficit), add an edge from $i$ to $t$ with capacity $-\textit{balance}[i]$ and unit cost $0$;
- For each $i$, add an edge from $i$ to each of its two neighbors with infinite capacity and unit cost $1$, representing that transferring $1$ unit of balance to a neighbor takes $1$ move.

Let $\textit{totalDeficit} = \sum_{\textit{balance}[i] < 0} (-\textit{balance}[i])$ be the total deficit. The answer is the minimum cost of sending $\textit{totalDeficit}$ units of flow from $s$ to $t$. Since the circular edges connect everyone in both directions, all the required flow can always be delivered as long as the total balance is non-negative. We use SPFA-based successive shortest path augmentation to solve the minimum cost flow problem.

Note that each augmentation pushes the entire bottleneck flow along a shortest path instead of just $1$ unit: the bottleneck edge is either an edge connected to the source or the sink (which then gets saturated), or a reverse circular edge (which reroutes all the existing flow on the corresponding forward edge). Hence the number of augmentations does not depend on the magnitudes of the balances and stays on the order of $O(n)$ for the constraints of this problem. Each augmentation uses SPFA to find a shortest augmenting path, which takes $O(VE)$ time in the worst case, where $V = n + 2$ and $E = O(n)$.

The time complexity is $O(n^3)$ in the worst case, and the space complexity is $O(n)$. Note that $O(n^3)$ is a very conservative bound: on the one hand, there are only $O(n)$ augmentations in practice; on the other hand, the graph in this problem is a unit-cost cycle, on which SPFA behaves almost like BFS — each node is dequeued only a constant number of times on average, so one augmentation actually costs about $O(n)$. The total amount of work is therefore about $O(n^2)$ in practice, roughly $10^7$ simple operations when $n = 1000$, which is fast enough to pass. For a strictly provable bound, SPFA can be replaced by Dijkstra's algorithm with Johnson's potentials, giving $O(n^2 \log n)$ time.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        total_balance = sum(balance)
        if total_balance < 0:
            return -1

        n = len(balance)
        total_deficit = sum(-x for x in balance if x < 0)
        if total_deficit == 0:
            return 0

        source = n
        sink = n + 1
        num_nodes = n + 2

        graph = [[] for _ in range(num_nodes)]

        def add_edge(u, v, cap, cost):
            graph[u].append([v, cap, cost, len(graph[v])])
            graph[v].append([u, 0, -cost, len(graph[u]) - 1])

        for i in range(n):
            if balance[i] > 0:
                add_edge(source, i, balance[i], 0)
            elif balance[i] < 0:
                add_edge(i, sink, -balance[i], 0)

            add_edge(i, (i + 1) % n, inf, 1)
            add_edge(i, (i - 1 + n) % n, inf, 1)

        total_cost = 0
        current_flow = 0

        while current_flow < total_deficit:
            dist = [inf] * num_nodes
            parent_node = [-1] * num_nodes
            parent_edge = [-1] * num_nodes
            in_queue = [False] * num_nodes

            queue = deque([source])
            dist[source] = 0
            in_queue[source] = True

            while queue:
                u = queue.popleft()
                in_queue[u] = False

                for idx, (v, cap, cost, _) in enumerate(graph[u]):
                    if cap > 0 and dist[v] > dist[u] + cost:
                        dist[v] = dist[u] + cost
                        parent_node[v] = u
                        parent_edge[v] = idx
                        if not in_queue[v]:
                            queue.append(v)
                            in_queue[v] = True

            if dist[sink] == inf:
                break

            push_flow = total_deficit - current_flow
            curr = sink
            while curr != source:
                p = parent_node[curr]
                idx = parent_edge[curr]
                push_flow = min(push_flow, graph[p][idx][1])
                curr = p

            curr = sink
            while curr != source:
                p = parent_node[curr]
                idx = parent_edge[curr]
                rev_idx = graph[p][idx][3]
                graph[p][idx][1] -= push_flow
                graph[curr][rev_idx][1] += push_flow
                curr = p

            current_flow += push_flow
            total_cost += push_flow * dist[sink]

        return total_cost if current_flow == total_deficit else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
