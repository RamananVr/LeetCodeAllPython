---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0040.Combination%20Sum%20II/README_EN.md
tags:
    - Array
    - Backtracking
---

<!-- problem:start -->

# [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii)

## Description

<!-- description:start -->

<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sum to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong>&nbsp;The solution set must not contain duplicate combinations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Pruning + Backtracking

We can first sort the array to facilitate pruning and skipping duplicate numbers.

Next, we design a function $dfs(i, s)$, which means starting the search from index $i$ with a remaining target value of $s$. Here, $i$ and $s$ are both non-negative integers, the current search path is $t$, and the answer is $ans$.

In the function $dfs(i, s)$, we first check whether $s$ is $0$. If it is, we add the current search path $t$ to the answer $ans$, and then return. If $i \geq n$ or $s \lt candidates[i]$, the path is invalid, so we return directly. Otherwise, we start the search from index $i$, and the search index range is $j \in [i, n)$, where $n$ is the length of the array $candidates$. During the search, if $j \gt i$ and $candidates[j] = candidates[j - 1]$, it means that the current number is the same as the previous number, we can skip the current number because the previous number has been searched. Otherwise, we add the current number to the search path $t$, recursively call the function $dfs(j + 1, s - candidates[j])$, and after the recursion ends, we remove the current number from the search path $t$.

We can also change the implementation logic of the function $dfs(i, s)$ to another form. If we choose the current number, we add the current number to the search path $t$, then recursively call the function $dfs(i + 1, s - candidates[i])$, and after the recursion ends, we remove the current number from the search path $t$. If we do not choose the current number, we can skip all numbers that are the same as the current number, then recursively call the function $dfs(j, s)$, where $j$ is the index of the first number that is different from the current number.

In the main function, we just need to call the function $dfs(0, target)$ to get the answer.

The time complexity is $O(2^n \times n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $candidates$. Due to pruning, the actual time complexity is much less than $O(2^n \times n)$.

Similar problems:

- [39. Combination Sum](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0039.Combination%20Sum/README_EN.md)
- [77. Combinations](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0077.Combinations/README_EN.md)
- [216. Combination Sum III](https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0216.Combination%20Sum%20III/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, s: int):
            if s == 0:
                ans.append(t[:])
                return
            if i >= len(candidates) or s < candidates[i]:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                t.append(candidates[j])
                dfs(j + 1, s - candidates[j])
                t.pop()

        candidates.sort()
        ans = []
        t = []
        dfs(0, target)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Sorting + Pruning + Backtracking(Another Form)

We can also change the implementation logic of the function $dfs(i, s)$ to another form. If we choose the current number, we add the current number to the search path $t$, then recursively call the function $dfs(i + 1, s - candidates[i])$, and after the recursion ends, we remove the current number from the search path $t$. If we do not choose the current number, we can skip all numbers that are the same as the current number, then recursively call the function $dfs(j, s)$, where $j$ is the index of the first number that is different from the current number.

The time complexity is $O(2^n \times n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $candidates$. Due to pruning, the actual time complexity is much less than $O(2^n \times n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, s: int):
            if s == 0:
                ans.append(t[:])
                return
            if i >= len(candidates) or s < candidates[i]:
                return
            x = candidates[i]
            t.append(x)
            dfs(i + 1, s - x)
            t.pop()
            while i < len(candidates) and candidates[i] == x:
                i += 1
            dfs(i, s)

        candidates.sort()
        ans = []
        t = []
        dfs(0, target)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
