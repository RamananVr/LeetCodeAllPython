---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1257.Smallest%20Common%20Region/README_EN.md
rating: 1654
source: Biweekly Contest 13 Q2
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Array
    - Hash Table
    - String
---

<!-- problem:start -->

# [1257. Smallest Common Region 🔒](https://leetcode.com/problems/smallest-common-region)

## Description

<!-- description:start -->

<p>You are given some lists of <code>regions</code> where the first region of each list <strong>directly</strong> contains all other regions in that list.</p>

<p>If a region <code>x</code> contains a region <code>y</code> <em>directly</em>, and region <code>y</code> contains region <code>z</code> <em>directly</em>, then region <code>x</code> is said to contain region <code>z</code> <strong>indirectly</strong>. Note that region <code>x</code> also <strong>indirectly</strong> contains all regions <strong>indirectly</strong> containd in <code>y</code>.</p>

<p>Naturally, if a region <code>x</code> contains (either <em>directly</em> or <em>indirectly</em>) another region <code>y</code>, then <code>x</code> is bigger than or equal to <code>y</code> in size. Also, by definition, a region <code>x</code> contains itself.</p>

<p>Given two regions: <code>region1</code> and <code>region2</code>, return <em>the smallest region that contains both of them</em>.</p>

<p>It is guaranteed the smallest region exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:
</strong>regions = [[&quot;Earth&quot;,&quot;North America&quot;,&quot;South America&quot;],
[&quot;North America&quot;,&quot;United States&quot;,&quot;Canada&quot;],
[&quot;United States&quot;,&quot;New York&quot;,&quot;Boston&quot;],
[&quot;Canada&quot;,&quot;Ontario&quot;,&quot;Quebec&quot;],
[&quot;South America&quot;,&quot;Brazil&quot;]],
region1 = &quot;Quebec&quot;,
region2 = &quot;New York&quot;
<strong>Output:</strong> &quot;North America&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> regions = [[&quot;Earth&quot;, &quot;North America&quot;, &quot;South America&quot;],[&quot;North America&quot;, &quot;United States&quot;, &quot;Canada&quot;],[&quot;United States&quot;, &quot;New York&quot;, &quot;Boston&quot;],[&quot;Canada&quot;, &quot;Ontario&quot;, &quot;Quebec&quot;],[&quot;South America&quot;, &quot;Brazil&quot;]], region1 = &quot;Canada&quot;, region2 = &quot;South America&quot;
<strong>Output:</strong> &quot;Earth&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= regions.length &lt;= 10<sup>4</sup></code></li>
	<li><code>2 &lt;= regions[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= regions[i][j].length, region1.length, region2.length &lt;= 20</code></li>
	<li><code>region1 != region2</code></li>
	<li><code>regions[i][j]</code>, <code>region1</code>, and <code>region2</code> consist of English letters.</li>
	<li>The input is generated such that there exists a region which contains all the other regions, either directly or indirectly.</li>
	<li>A region cannot be directly contained in more than one region.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We can use a hash table $\textit{g}$ to store the parent region of each region. Then, starting from $\textit{region1}$, we keep moving upwards to find all its parent regions until the root region, and store these regions in the set $\textit{s}$. Next, starting from $\textit{region2}$, we keep moving upwards to find the first region that is in the set $\textit{s}$, which is the smallest common region.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the region list $\textit{regions}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        g = {}
        for r in regions:
            x = r[0]
            for y in r[1:]:
                g[y] = x
        s = set()
        x = region1
        while x in g:
            s.add(x)
            x = g[x]
        x = region2
        while x in g and x not in s:
            x = g[x]
        return x
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
