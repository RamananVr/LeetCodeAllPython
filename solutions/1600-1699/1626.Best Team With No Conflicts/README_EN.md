---
comments: true
difficulty: Medium
rating: 2027
source: Weekly Contest 211 Q3
tags:
    - Array
    - Dynamic Programming
    - Sorting
    - Longest Increasing Subsequence
---

<!-- problem:start -->

# [1626. Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts)

## Description

<!-- description:start -->

<p>You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the <strong>sum</strong> of scores of all the players in the team.</p>

<p>However, the basketball team is not allowed to have <strong>conflicts</strong>. A <strong>conflict</strong> exists if a younger player has a <strong>strictly higher</strong> score than an older player. A conflict does <strong>not</strong> occur between players of the same age.</p>

<p>Given two lists, <code>scores</code> and <code>ages</code>, where each <code>scores[i]</code> and <code>ages[i]</code> represents the score and age of the <code>i<sup>th</sup></code> player, respectively, return <em>the highest overall score of all possible basketball teams</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> scores = [1,3,5,10,15], ages = [1,2,3,4,5]
<strong>Output:</strong> 34
<strong>Explanation:</strong>&nbsp;You can choose all the players.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> scores = [4,5,6,5], ages = [2,1,2,1]
<strong>Output:</strong> 16
<strong>Explanation:</strong>&nbsp;It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> scores = [1,2,3,5], ages = [8,9,10,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong>&nbsp;It is best to choose the first 3 players. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= scores.length, ages.length &lt;= 1000</code></li>
	<li><code>scores.length == ages.length</code></li>
	<li><code>1 &lt;= scores[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= ages[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> A conflict is an older player with a strictly lower score. Sorting by score, then age, reduces the constraint to a nondecreasing age subsequence.
>
> With $n \le 1000$, the best score ending at a player is an $O(n^2)$ LIS-style DP: take the best $f[j]$ among earlier players who are no older, then add the current score.
>
> The answer is the maximum $f[i]$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = sorted(zip(scores, ages))
        n = len(arr)
        f = [0] * n
        for i, (score, age) in enumerate(arr):
            for j in range(i):
                if age >= arr[j][1]:
                    f[i] = max(f[i], f[j])
            f[i] += score
        return max(f)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 scans every predecessor in $O(n^2)$. After the same sort we only need the best score among ages up to the current one — a prefix maximum.
>
> A Fenwick tree stores those maxima: query $[1,\textit{age}]$, add $\textit{score}$, and update that age, for $O(n\log m)$ time.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x, val):
        while x <= self.n:
            self.c[x] = max(self.c[x], val)
            x += x & -x

    def query(self, x):
        s = 0
        while x:
            s = max(s, self.c[x])
            x -= x & -x
        return s

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        m = max(ages)
        tree = BinaryIndexedTree(m)
        for score, age in sorted(zip(scores, ages)):
            tree.update(age, score + tree.query(age))
        return tree.query(m)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
