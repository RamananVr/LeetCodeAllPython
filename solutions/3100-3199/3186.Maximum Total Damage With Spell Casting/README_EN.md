---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3186.Maximum%20Total%20Damage%20With%20Spell%20Casting/README_EN.md
rating: 1840
source: Weekly Contest 402 Q3
tags:
    - Array
    - Hash Table
    - Two Pointers
    - Binary Search
    - Dynamic Programming
    - Counting
    - Sorting
---

<!-- problem:start -->

# [3186. Maximum Total Damage With Spell Casting](https://leetcode.com/problems/maximum-total-damage-with-spell-casting)

## Description

<!-- description:start -->

<p>A magician has various spells.</p>

<p>You are given an array <code>power</code>, where each element represents the damage of a spell. Multiple spells can have the same damage value.</p>

<p>It is a known fact that if a magician decides to cast a spell with a damage of <code>power[i]</code>, they <strong>cannot</strong> cast any spell with a damage of <code>power[i] - 2</code>, <code>power[i] - 1</code>, <code>power[i] + 1</code>, or <code>power[i] + 2</code>.</p>

<p>Each spell can be cast <strong>only once</strong>.</p>

<p>Return the <strong>maximum</strong> possible <em>total damage</em> that a magician can cast.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">power = [1,1,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">power = [7,1,6,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= power.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= power[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search + Memoization

We can first sort the array $\textit{power}$, use a hash table $\textit{cnt}$ to record the occurrence count of each damage value, and then iterate through the array $\textit{power}$. For each damage value $x$, we can determine the index of the next damage value that can be used when using a spell with damage value $x$, which is the index of the first damage value greater than $x + 2$. We can use binary search to find this index and record it in the array $\textit{nxt}$.

Next, we define a function $\textit{dfs}$ to calculate the maximum damage value that can be obtained starting from the $i$-th damage value.

In the $\textit{dfs}$ function, we can choose to skip the current damage value, so we can skip all the same damage values of the current one and directly jump to $i + \textit{cnt}[x]$, obtaining a damage value of $\textit{dfs}(i + \textit{cnt}[x])$; or we can choose to use the current damage value, so we can use all the same damage values of the current one and then jump to the index of the next damage value, obtaining a damage value of $x \times \textit{cnt}[x] + \textit{dfs}(\textit{nxt}[i])$, where $\textit{nxt}[i]$ represents the index of the first damage value greater than $x + 2$. We take the maximum of these two cases as the return value of the function.

To avoid repeated calculations, we can use memoization, storing the results that have already been calculated in an array $\textit{f}$. Thus, when calculating $\textit{dfs}(i)$, if $\textit{f}[i]$ is not $0$, we directly return $\textit{f}[i]$.

The answer is $\textit{dfs}(0)$.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{power}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            a = dfs(i + cnt[power[i]])
            b = power[i] * cnt[power[i]] + dfs(nxt[i])
            return max(a, b)

        n = len(power)
        cnt = Counter(power)
        power.sort()
        nxt = [bisect_right(power, x + 2, lo=i + 1) for i, x in enumerate(power)]
        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
