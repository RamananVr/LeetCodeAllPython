---
comments: true
difficulty: Easy
rating: 1167
source: Weekly Contest 169 Q1
tags:
    - Array
    - Math
---

<!-- problem:start -->

# [1304. Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <strong>any</strong> array containing <code>n</code> <strong>unique</strong> integers such that they add up to <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> [-7,-1,1,3,4]
<strong>Explanation:</strong> These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [-1,0,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Construction

<!-- thinking:start -->

> **Thinking**
>
> We need $n$ distinct integers that sum to $0$. Picking numbers at random and then adjusting them easily breaks uniqueness. A pair of opposite numbers already sums to $0$, so we emit $1,-1,\ldots,k,-k$. When $n$ is odd we append $0$, which preserves both the sum and distinctness.

<!-- thinking:end -->

We can start from $1$ and alternately add positive and negative numbers to the result array. We repeat this process $\frac{n}{2}$ times. If $n$ is odd, we add $0$ to the result array at the end.

The time complexity is $O(n)$, where $n$ is the given integer. Ignoring the space used for the answer, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(n >> 1):
            ans.append(i + 1)
            ans.append(-(i + 1))
        if n & 1:
            ans.append(0)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Construction + Mathematics

<!-- thinking:start -->

> **Thinking**
>
> Pairing must treat odd and even $n$ separately. Placing $1$ through $n-1$ and appending the negation of their sum forces the total to $0$, and that last value cannot equal any of those positive integers. The construction is shorter and still distinct.

<!-- thinking:end -->

We can also add all integers from $1$ to $n-1$ to the result array, and finally add the opposite of the sum of the first $n-1$ integers, which is $-\frac{n(n-1)}{2}$, to the result array.

The time complexity is $O(n)$, where $n$ is the given integer. Ignoring the space used for the answer, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = list(range(1, n))
        ans.append(-sum(ans))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
