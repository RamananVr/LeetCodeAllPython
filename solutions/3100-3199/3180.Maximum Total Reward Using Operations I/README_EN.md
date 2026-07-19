---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3180.Maximum%20Total%20Reward%20Using%20Operations%20I/README_EN.md
rating: 1848
source: Weekly Contest 401 Q3
tags:
    - Bit Manipulation
    - Array
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [3180. Maximum Total Reward Using Operations I](https://leetcode.com/problems/maximum-total-reward-using-operations-i)

## Description

<!-- description:start -->

<p>You are given an integer array <code>rewardValues</code> of length <code>n</code>, representing the values of rewards.</p>

<p>Initially, your total reward <code>x</code> is 0, and all indices are <strong>unmarked</strong>. You are allowed to perform the following operation <strong>any</strong> number of times:</p>

<ul>
	<li>Choose an <strong>unmarked</strong> index <code>i</code> from the range <code>[0, n - 1]</code>.</li>
	<li>If <code>rewardValues[i]</code> is <strong>greater</strong> than your current total reward <code>x</code>, then add <code>rewardValues[i]</code> to <code>x</code> (i.e., <code>x = x + rewardValues[i]</code>), and <strong>mark</strong> the index <code>i</code>.</li>
</ul>

<p>Return an integer denoting the <strong>maximum </strong><em>total reward</em> you can collect by performing the operations optimally.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">rewardValues = [1,1,3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">rewardValues = [1,6,4,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<p>Mark the indices 0, 2, and 1 in order. The total reward will then be 11, which is the maximum.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= rewardValues.length &lt;= 2000</code></li>
	<li><code>1 &lt;= rewardValues[i] &lt;= 2000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Memoization + Binary Search

We can sort the `rewardValues` array and then use memoization to solve for the maximum total reward.

We define a function $\textit{dfs}(x)$, representing the maximum total reward that can be obtained when the current total reward is $x$. Thus, the answer is $\textit{dfs}(0)$.

The execution process of the function $\textit{dfs}(x)$ is as follows:

1. Perform a binary search in the `rewardValues` array for the index $i$ of the first element greater than $x$;
2. Iterate over the elements in the `rewardValues` array starting from index $i$, and for each element $v$, calculate the maximum value of $v + \textit{dfs}(x + v)$.
3. Return the result.

To avoid repeated calculations, we use a memoization array `f` to record the results that have already been computed.

The time complexity is $O(n \times (\log n + M))$, and the space complexity is $O(M)$. Where $n$ is the length of the `rewardValues` array, and $M$ is twice the maximum value in the `rewardValues` array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        @cache
        def dfs(x: int) -> int:
            i = bisect_right(rewardValues, x)
            ans = 0
            for v in rewardValues[i:]:
                ans = max(ans, v + dfs(x + v))
            return ans

        rewardValues.sort()
        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We define $f[i][j]$ as whether it is possible to obtain a total reward of $j$ using the first $i$ reward values. Initially, $f[0][0] = \textit{True}$, and all other values are $\textit{False}$.

We consider the $i$-th reward value $v$. If we do not choose it, then $f[i][j] = f[i - 1][j]$. If we choose it, then $f[i][j] = f[i - 1][j - v]$, where $0 \leq j - v < v$. Thus, the state transition equation is:

$$
f[i][j] = f[i - 1][j] \vee f[i - 1][j - v]
$$

The final answer is $\max\{j \mid f[n][j] = \textit{True}\}$.

Since $f[i][j]$ only depends on $f[i - 1][j]$ and $f[i - 1][j - v]$, we can optimize away the first dimension and use only a one-dimensional array for state transitions.

The time complexity is $O(n \times M)$, and the space complexity is $O(M)$. Where $n$ is the length of the `rewardValues` array, and $M$ is twice the maximum value in the `rewardValues` array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        nums = sorted(set(rewardValues))
        m = nums[-1] << 1
        f = [False] * m
        f[0] = True
        for v in nums:
            for j in range(m):
                if 0 <= j - v < v:
                    f[j] |= f[j - v]
        ans = m - 1
        while not f[ans]:
            ans -= 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Dynamic Programming + Bit Manipulation

We can optimize Solution 2 by defining a binary number $f$ to save the current state, where the $i$-th bit of $f$ being $1$ indicates that a total reward of $i$ is reachable.

Observing the state transition equation from Solution 2, $f[j] = f[j] \vee f[j - v]$, this is equivalent to taking the lower $v$ bits of $f$, shifting them left by $v$ bits, and then performing an OR operation with the original $f$.

Thus, the answer is the position of the highest bit in $f$.

The time complexity is $O(n \times M / w)$, and the space complexity is $O(n + M / w)$. Where $n$ is the length of the `rewardValues` array, $M$ is twice the maximum value in the `rewardValues` array, and the integer $w = 32$ or $64$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        nums = sorted(set(rewardValues))
        f = 1
        for v in nums:
            f |= (f & ((1 << v) - 1)) << v
        return f.bit_length() - 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
