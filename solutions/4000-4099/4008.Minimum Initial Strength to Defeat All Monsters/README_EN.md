---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/4000-4099/4008.Minimum%20Initial%20Strength%20to%20Defeat%20All%20Monsters/README_EN.md
rating: 1776
source: Biweekly Contest 188 Q3
tags:
    - Greedy
    - Array
    - Binary Search
    - Prefix Sum
---

<!-- problem:start -->

# [4008. Minimum Initial Strength to Defeat All Monsters](https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters)

## Description

<!-- description:start -->

<p>You are given an integer array <code>monsters</code>, where <code>monsters[i]</code> represents the strength of the <code>i<sup>th</sup></code> monster.</p>

<p>You are also given a 2D integer array <code>boosts</code>, where <code>boosts[i] = [l<sub>i</sub>, r<sub>i</sub>, v<sub>i</sub>]</code> indicates that <code>v<sub>i</sub></code> is added to your <strong>temporary bonus</strong> while fighting any monster whose index lies in <code>[l<sub>i</sub>, r<sub>i</sub>]</code>. Boost ranges may overlap, and the values of all applicable boosts are added together.</p>

<p>You start with a <strong>non-negative</strong> initial strength and fight the monsters from left to right.</p>

<p>For each monster at index <code>i</code>:</p>

<ul>
	<li>Let <code>bonus</code> be the <strong>sum</strong> of the values of all boosts that apply to monster <code>i</code>.</li>
	<li>You can defeat the monster only if your current strength plus <code>bonus</code> is <strong>at least</strong> <code>monsters[i]</code>.</li>
	<li>After defeating the monster, only your current strength decreases by <code>monsters[i]</code>. If it becomes <strong>negative</strong>, it is set to 0.</li>
</ul>

<p>Return the <strong>minimum</strong> initial strength required to defeat all monsters.</p>

<p>Note: The temporary bonus is used only to determine whether the current monster can be defeated. It does not otherwise change your current strength.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">monsters = [5,10,15], boosts = [[1,1,10]]</span></p>

<p><strong>Output:</strong> <span class="example-io">30</span></p>

<p><strong>Explanation:</strong></p>

<p>Let&#39;s start with an initial strength of 30.</p>

<ul>
	<li><code>monsters[0] = 5</code>: At index 0, the bonus is 0. Since <code>30 + 0 &gt;= 5</code>, this monster can be defeated. The strength becomes <code>30 - 5 = 25</code>.</li>
	<li><code>monsters[1] = 10</code>: At index 1, the bonus is 10. Since <code>25 + 10 &gt;= 10</code>, this monster can be defeated. The strength becomes <code>25 - 10 = 15</code>.</li>
	<li><code>monsters[2] = 15</code>: At index 2, the bonus is 0. Since <code>15 + 0 &gt;= 15</code>, this monster can be defeated. The strength becomes <code>15 - 15 = 0</code>.</li>
</ul>

<p>Thus, the minimum initial strength required is 30.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">monsters = [5,10,15], boosts = [[1,2,10],[1,2,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>Let&#39;s start with an initial strength of 5.</p>

<ul>
	<li><code>monsters[0] = 5</code>: The bonus is 0. Since <code>5 + 0 &gt;= 5</code>, the monster can be defeated. The strength becomes <code>5 - 5 = 0</code>.</li>
	<li><code>monsters[1] = 10</code>: The two overlapping boosts provide <code>bonus = 10 + 5 = 15</code>. Since <code>0 + 15 &gt;= 10</code>, the monster can be defeated. The strength remains 0.</li>
	<li><code>monsters[2] = 15</code>: The two overlapping boosts again provide <code>bonus = 15</code>. Since <code>0 + 15 &gt;= 15</code>, the monster can be defeated. The strength remains 0.</li>
</ul>

<p>Thus, the minimum initial strength required is 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= monsters.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= monsters[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= boosts.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>boosts[i] == [l<sub>i</sub>, r<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt; monsters.length</code></li>
	<li><code>1 &lt;= v<sub>i</sub> &lt;= 10<sup>9</sup></code>​​​​​​​</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Difference Array + Binary Search

Each boost adds a value to an entire index range $[l, r]$, so we first apply all boosts using a difference array $d$. The $\textit{bonus}$ when fighting the $i$-th monster is then the prefix sum $\sum_{j=0}^{i} d[j]$.

Next, we binary search the initial strength $v$. For a given $v$, we simulate the fights from left to right: maintain the current $\textit{bonus}$ (the prefix sum of the difference array); if $v + \textit{bonus} < \textit{monsters}[i]$, the monster cannot be defeated and $v$ is infeasible; otherwise, we defeat it, decrease $v$ by $\textit{monsters}[i]$, and reset $v$ to $0$ if it becomes negative. If all monsters can be defeated, $v$ is feasible.

A larger initial strength never makes it harder to defeat all monsters, so feasibility is monotonic in $v$, and we can binary search the minimum feasible initial strength. The upper bound of the search is set to $10^{15}$ (the total strength of all monsters is at most $5 \times 10^4 \times 10^9 = 5 \times 10^{13}$).

The time complexity is $O((n + m) \times \log M)$, and the space complexity is $O(n)$, where $n$ is the number of monsters, $m$ is the number of boosts, and $M = 10^{15}$ is the upper bound of the binary search.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        def check(v: int) -> bool:
            bonus = 0
            for a, b in zip(monsters, d):
                bonus += b
                if v + bonus < a:
                    return False
                v -= a
                v = max(v, 0)
            return True

        n = len(monsters)
        d = [0] * (n + 1)
        for l, r, v in boosts:
            d[l] += v
            d[r + 1] -= v

        l, r = 0, 10**15
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
