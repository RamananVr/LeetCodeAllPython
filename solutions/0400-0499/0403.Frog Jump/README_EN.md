---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0403.Frog%20Jump/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [403. Frog Jump](https://leetcode.com/problems/frog-jump)

## Description

<!-- description:start -->

<p>A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.</p>

<p>Given a list of <code>stones</code>&nbsp;positions (in units) in sorted <strong>ascending order</strong>, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be <code>1</code> unit.</p>

<p>If the frog&#39;s last jump was <code>k</code> units, its next jump must be either <code>k - 1</code>, <code>k</code>, or <code>k + 1</code> units. The frog can only jump in the forward direction.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stones = [0,1,3,5,6,8,12,17]
<strong>Output:</strong> true
<strong>Explanation:</strong> The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stones = [0,1,2,3,4,8,9,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= stones.length &lt;= 2000</code></li>
	<li><code>0 &lt;= stones[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>stones[0] == 0</code></li>
	<li><code>stones</code>&nbsp;is sorted in a strictly increasing order.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Memoization

We use a hash table $pos$ to record the index of each stone. Next, we design a function $dfs(i, k)$, which means that the frog jumps from the $i$-th stone and the last jump distance is $k$. If the frog can reach the end, the function returns `true`, otherwise it returns `false`.

The calculation process of function $dfs(i, k)$ is as follows:

If $i$ is the index of the last stone, the frog has reached the end, and return `true`;

Otherwise, we need to enumerate the frog's next jump distance $j$, where $j \in [k-1, k, k+1]$. If $j$ is a positive integer and the hash table $pos$ exists the position $stones[i] + j$, then the frog can choose to jump $j$ units on the $i$-th stone, if $dfs(pos[stones[i] + j], j)$ returns `true`, the frog can successfully jump to the end from the $i$-th stone, and we can return `true`.

The enumeration is over, indicating that the frog cannot choose the appropriate jump distance on the $i$-th stone to jump to the end, so we return `false`.

In order to prevent repeated calculations in the function $dfs(i, k)$, we can use memoization, record the result of $dfs(i, k)$ in an array $f$, and assign $f[i][k]$ each time the function $dfs(i, k)$ returns result, and return $f[i][k]$ directly when encountering $dfs(i, k)$ next time.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Where $n$ is the number of stones.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dfs(i, k):
            if i == n - 1:
                return True
            for j in range(k - 1, k + 2):
                if j > 0 and stones[i] + j in pos and dfs(pos[stones[i] + j], j):
                    return True
            return False

        n = len(stones)
        pos = {s: i for i, s in enumerate(stones)}
        return dfs(0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We define $f[i][k]$ to be true if and only if it is possible to reach stone $i$ with last jump of size $k$. Initially $f[0][0] = true$, and all other elements of $f$ are false.

We can determine the value of $f[i][k]$ for all $i$ and $k$ using a double loop. For each possible jump size $k$, we look at the stones we could have jumped from: $i-k$, $i-k+1$, $i-k+2$. If any of these stones exist and if we can reach them with a last jump of size $k-1$, $k$, or $k+1$, then we can reach stone $i$ with a last jump of size $k$.

If we can reach the last stone, the answer is true. Otherwise, the answer is false.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Where $n$ is the number of stones.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        f = [[False] * n for _ in range(n)]
        f[0][0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k - 1 > j:
                    break
                f[i][k] = f[j][k - 1] or f[j][k] or f[j][k + 1]
                if i == n - 1 and f[i][k]:
                    return True
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
