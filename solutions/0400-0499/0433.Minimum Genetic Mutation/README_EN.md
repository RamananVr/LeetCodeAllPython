---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0433.Minimum%20Genetic%20Mutation/README_EN.md
tags:
    - Breadth-First Search
    - Hash Table
    - String
---

<!-- problem:start -->

# [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation)

## Description

<!-- description:start -->

<p>A gene string can be represented by an 8-character long string, with choices from <code>&#39;A&#39;</code>, <code>&#39;C&#39;</code>, <code>&#39;G&#39;</code>, and <code>&#39;T&#39;</code>.</p>

<p>Suppose we need to investigate a mutation from a gene string <code>startGene</code> to a gene string <code>endGene</code> where one mutation is defined as one single character changed in the gene string.</p>

<ul>
	<li>For example, <code>&quot;AACCGGTT&quot; --&gt; &quot;AACCGGTA&quot;</code> is one mutation.</li>
</ul>

<p>There is also a gene bank <code>bank</code> that records all the valid gene mutations. A gene must be in <code>bank</code> to make it a valid gene string.</p>

<p>Given the two gene strings <code>startGene</code> and <code>endGene</code> and the gene bank <code>bank</code>, return <em>the minimum number of mutations needed to mutate from </em><code>startGene</code><em> to </em><code>endGene</code>. If there is no such a mutation, return <code>-1</code>.</p>

<p>Note that the starting point is assumed to be valid, so it might not be included in the bank.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> startGene = &quot;AACCGGTT&quot;, endGene = &quot;AACCGGTA&quot;, bank = [&quot;AACCGGTA&quot;]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> startGene = &quot;AACCGGTT&quot;, endGene = &quot;AAACGGTA&quot;, bank = [&quot;AACCGGTA&quot;,&quot;AACCGCTA&quot;,&quot;AAACGGTA&quot;]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= bank.length &lt;= 10</code></li>
	<li><code>startGene.length == endGene.length == bank[i].length == 8</code></li>
	<li><code>startGene</code>, <code>endGene</code>, and <code>bank[i]</code> consist of only the characters <code>[&#39;A&#39;, &#39;C&#39;, &#39;G&#39;, &#39;T&#39;]</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

We define a queue `q` to store the current gene sequence and the number of changes, and a set `vis` to store the visited gene sequences. Initially, we add the starting gene sequence `start` to the queue `q` and the set `vis`.

Then, we continuously take out a gene sequence from the queue `q`. If this gene sequence equals the target gene sequence, we return the current number of changes. Otherwise, we iterate through the gene bank `bank`, calculate the difference value between the current gene sequence and the gene sequence in the gene bank. If the difference value is $1$ and the gene sequence in the gene bank has not been visited, we add it to the queue `q` and the set `vis`.

If the queue `q` is empty, it means that the gene change cannot be completed, so we return $-1$.

The time complexity is $O(C \times n \times m)$, and the space complexity is $O(n \times m)$. Where $n$ and $m$ are the lengths of the gene sequence and the gene bank respectively, and $C$ is the size of the character set of the gene sequence. In this problem, $C = 4$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([(startGene, 0)])
        vis = {startGene}
        while q:
            gene, depth = q.popleft()
            if gene == endGene:
                return depth
            for nxt in bank:
                diff = sum(a != b for a, b in zip(gene, nxt))
                if diff == 1 and nxt not in vis:
                    q.append((nxt, depth + 1))
                    vis.add(nxt)
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
