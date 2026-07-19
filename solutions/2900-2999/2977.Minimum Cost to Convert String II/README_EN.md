---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2977.Minimum%20Cost%20to%20Convert%20String%20II/README_EN.md
rating: 2695
source: Weekly Contest 377 Q4
tags:
    - Graph
    - Trie
    - Array
    - String
    - Dynamic Programming
    - Shortest Path
---

<!-- problem:start -->

# [2977. Minimum Cost to Convert String II](https://leetcode.com/problems/minimum-cost-to-convert-string-ii)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> strings <code>source</code> and <code>target</code>, both of length <code>n</code> and consisting of <strong>lowercase</strong> English characters. You are also given two <strong>0-indexed</strong> string arrays <code>original</code> and <code>changed</code>, and an integer array <code>cost</code>, where <code>cost[i]</code> represents the cost of converting the string <code>original[i]</code> to the string <code>changed[i]</code>.</p>

<p>You start with the string <code>source</code>. In one operation, you can pick a <strong>substring</strong> <code>x</code> from the string, and change it to <code>y</code> at a cost of <code>z</code> <strong>if</strong> there exists <strong>any</strong> index <code>j</code> such that <code>cost[j] == z</code>, <code>original[j] == x</code>, and <code>changed[j] == y</code>. You are allowed to do <strong>any</strong> number of operations, but any pair of operations must satisfy <strong>either</strong> of these two conditions:</p>

<ul>
	<li>The substrings picked in the operations are <code>source[a..b]</code> and <code>source[c..d]</code> with either <code>b &lt; c</code> <strong>or</strong> <code>d &lt; a</code>. In other words, the indices picked in both operations are <strong>disjoint</strong>.</li>
	<li>The substrings picked in the operations are <code>source[a..b]</code> and <code>source[c..d]</code> with <code>a == c</code> <strong>and</strong> <code>b == d</code>. In other words, the indices picked in both operations are <strong>identical</strong>.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> cost to convert the string </em><code>source</code><em> to the string </em><code>target</code><em> using <strong>any</strong> number of operations</em>. <em>If it is impossible to convert</em> <code>source</code> <em>to</em> <code>target</code>,<em> return</em> <code>-1</code>.</p>

<p><strong>Note</strong> that there may exist indices <code>i</code>, <code>j</code> such that <code>original[j] == original[i]</code> and <code>changed[j] == changed[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcd&quot;, target = &quot;acbe&quot;, original = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;e&quot;,&quot;d&quot;], changed = [&quot;b&quot;,&quot;c&quot;,&quot;b&quot;,&quot;e&quot;,&quot;b&quot;,&quot;e&quot;], cost = [2,5,5,1,2,20]
<strong>Output:</strong> 28
<strong>Explanation:</strong> To convert &quot;abcd&quot; to &quot;acbe&quot;, do the following operations:
- Change substring source[1..1] from &quot;b&quot; to &quot;c&quot; at a cost of 5.
- Change substring source[2..2] from &quot;c&quot; to &quot;e&quot; at a cost of 1.
- Change substring source[2..2] from &quot;e&quot; to &quot;b&quot; at a cost of 2.
- Change substring source[3..3] from &quot;d&quot; to &quot;e&quot; at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28. 
It can be shown that this is the minimum possible cost.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcdefgh&quot;, target = &quot;acdeeghh&quot;, original = [&quot;bcd&quot;,&quot;fgh&quot;,&quot;thh&quot;], changed = [&quot;cde&quot;,&quot;thh&quot;,&quot;ghh&quot;], cost = [1,3,5]
<strong>Output:</strong> 9
<strong>Explanation:</strong> To convert &quot;abcdefgh&quot; to &quot;acdeeghh&quot;, do the following operations:
- Change substring source[1..3] from &quot;bcd&quot; to &quot;cde&quot; at a cost of 1.
- Change substring source[5..7] from &quot;fgh&quot; to &quot;thh&quot; at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
- Change substring source[5..7] from &quot;thh&quot; to &quot;ghh&quot; at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
The total cost incurred is 1 + 3 + 5 = 9.
It can be shown that this is the minimum possible cost.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcdefgh&quot;, target = &quot;addddddd&quot;, original = [&quot;bcd&quot;,&quot;defgh&quot;], changed = [&quot;ddd&quot;,&quot;ddddd&quot;], cost = [100,1578]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is impossible to convert &quot;abcdefgh&quot; to &quot;addddddd&quot;.
If you select substring source[1..3] as the first operation to change &quot;abcdefgh&quot; to &quot;adddefgh&quot;, you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
If you select substring source[3..7] as the first operation to change &quot;abcdefgh&quot; to &quot;abcddddd&quot;, you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= source.length == target.length &lt;= 1000</code></li>
	<li><code>source</code>, <code>target</code> consist only of lowercase English characters.</li>
	<li><code>1 &lt;= cost.length == original.length == changed.length &lt;= 100</code></li>
	<li><code>1 &lt;= original[i].length == changed[i].length &lt;= source.length</code></li>
	<li><code>original[i]</code>, <code>changed[i]</code> consist only of lowercase English characters.</li>
	<li><code>original[i] != changed[i]</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Trie + Floyd Algorithm + Memoization Search

According to the problem description, we can consider each string as a node, and the conversion cost between each pair of strings as a directed edge. We first initialize a $26 \times 26$ two-dimensional array $g$, where $g[i][j]$ represents the minimum cost of converting string $i$ to string $j$. Initially, $g[i][j] = \infty$, and if $i = j$, then $g[i][j] = 0$. Here, we can use a trie to store the strings in `original` and `changed` along with their corresponding integer identifiers.

Next, we use the Floyd algorithm to calculate the minimum cost between any two strings.

Then, we define a function $dfs(i)$ to represent the minimum cost of converting the string $source[i..]$ to the string $target[i..]$. The answer is $dfs(0)$.

The calculation process of the function $dfs(i)$ is as follows:

- If $i \geq |source|$, no conversion is needed, return $0$.
- Otherwise, if $source[i] = target[i]$, we can skip directly and recursively calculate $dfs(i + 1)$. We can also enumerate the index $j$ in the range $[i, |source|)$, if $source[i..j]$ and $target[i..j]$ are both in the trie, and their corresponding integer identifiers $x$ and $y$ are both greater than or equal to $0$, then we can add $dfs(j + 1)$ and $g[x][y]$ to get the cost of one conversion scheme, and we take the minimum value among all schemes.

In summary, we can get:

$$
dfs(i) = \begin{cases}
0, & i \geq |source| \\
dfs(i + 1), & source[i] = target[i] \\
\min_{i \leq j < |source|} \{ dfs(j + 1) + g[x][y] \}, & \textit{otherwise}
\end{cases}
$$

Where $x$ and $y$ are the integer identifiers of $source[i..j]$ and $target[i..j]$ in the trie, respectively.

To avoid repeated calculations, we can use memoization search.

The time complexity is $O(m^3 + n^2 + m \times n)$, and the space complexity is $O(m^2 + m \times n + n)$. Where $m$ and $n$ are the lengths of the arrays `original` and `source`, respectively.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = ["children", "v"]

    def __init__(self):
        self.children: List[Node | None] = [None] * 26
        self.v = -1

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        m = len(cost)
        g = [[inf] * (m << 1) for _ in range(m << 1)]
        for i in range(m << 1):
            g[i][i] = 0
        root = Node()
        idx = 0

        def insert(w: str) -> int:
            node = root
            for c in w:
                i = ord(c) - ord("a")
                if node.children[i] is None:
                    node.children[i] = Node()
                node = node.children[i]
            if node.v < 0:
                nonlocal idx
                node.v = idx
                idx += 1
            return node.v

        @cache
        def dfs(i: int) -> int:
            if i >= len(source):
                return 0
            res = dfs(i + 1) if source[i] == target[i] else inf
            p = q = root
            for j in range(i, len(source)):
                p = p.children[ord(source[j]) - ord("a")]
                q = q.children[ord(target[j]) - ord("a")]
                if p is None or q is None:
                    break
                if p.v < 0 or q.v < 0:
                    continue
                res = min(res, dfs(j + 1) + g[p.v][q.v])
            return res

        for x, y, z in zip(original, changed, cost):
            x = insert(x)
            y = insert(y)
            g[x][y] = min(g[x][y], z)
        for k in range(idx):
            for i in range(idx):
                if g[i][k] >= inf:
                    continue
                for j in range(idx):
                    # g[i][j] = min(g[i][j], g[i][k] + g[k][j])
                    if g[i][k] + g[k][j] < g[i][j]:
                        g[i][j] = g[i][k] + g[k][j]

        ans = dfs(0)
        return -1 if ans >= inf else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
