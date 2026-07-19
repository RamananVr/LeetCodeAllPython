---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3300-3399/3310.Remove%20Methods%20From%20Project/README_EN.md
rating: 1710
source: Weekly Contest 418 Q2
tags:
    - Depth-First Search
    - Breadth-First Search
    - Graph
---

<!-- problem:start -->

# [3310. Remove Methods From Project](https://leetcode.com/problems/remove-methods-from-project)

## Description

<!-- description:start -->

<p>You are maintaining a project that has <code>n</code> methods numbered from <code>0</code> to <code>n - 1</code>.</p>

<p>You are given two integers <code>n</code> and <code>k</code>, and a 2D integer array <code>invocations</code>, where <code>invocations[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that method <code>a<sub>i</sub></code> invokes method <code>b<sub>i</sub></code>.</p>

<p>There is a known bug in method <code>k</code>. Method <code>k</code>, along with any method invoked by it, either <strong>directly</strong> or <strong>indirectly</strong>, are considered <strong>suspicious</strong> and we aim to remove them.</p>

<p>A group of methods can only be removed if no method <strong>outside</strong> the group invokes any methods <strong>within</strong> it.</p>

<p>Return an array containing all the remaining methods after removing all the <strong>suspicious</strong> methods. You may return the answer in <em>any order</em>. If it is not possible to remove <strong>all</strong> the suspicious methods, <strong>none</strong> should be removed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,2,3]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3300-3399/3310.Remove%20Methods%20From%20Project/images/graph-2.png" style="width: 200px; height: 200px;" /></p>

<p>Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,4]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3300-3399/3310.Remove%20Methods%20From%20Project/images/graph-3.png" style="width: 200px; height: 200px;" /></p>

<p>Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3300-3399/3310.Remove%20Methods%20From%20Project/images/graph.png" style="width: 200px; height: 200px;" /></p>

<p>All methods are suspicious. We can remove them.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= n - 1</code></li>
	<li><code>0 &lt;= invocations.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>invocations[i] == [a<sub>i</sub>, b<sub>i</sub>]</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>invocations[i] != invocations[j]</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two DFS

We can start from $k$ and find all suspicious methods, recording them in the array $\textit{suspicious}$. Then, we traverse from $0$ to $n-1$, starting from all non-suspicious methods, and mark all reachable methods as non-suspicious. Finally, we return all non-suspicious methods.

The time complexity is $O(n + m)$, and the space complexity is $O(n + m)$. Here, $n$ and $m$ represent the number of methods and the number of call relationships, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        def dfs(i: int):
            suspicious[i] = True
            for j in g[i]:
                if not suspicious[j]:
                    dfs(j)

        def dfs2(i: int):
            vis[i] = True
            for j in f[i]:
                if not vis[j]:
                    suspicious[j] = False
                    dfs2(j)

        f = [[] for _ in range(n)]
        g = [[] for _ in range(n)]
        for a, b in invocations:
            f[a].append(b)
            f[b].append(a)
            g[a].append(b)
        suspicious = [False] * n
        dfs(k)

        vis = [False] * n
        ans = []
        for i in range(n):
            if not suspicious[i] and not vis[i]:
                dfs2(i)
        return [i for i in range(n) if not suspicious[i]]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
