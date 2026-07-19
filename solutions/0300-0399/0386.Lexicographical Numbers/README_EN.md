---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0386.Lexicographical%20Numbers/README_EN.md
tags:
    - Depth-First Search
    - Trie
---

<!-- problem:start -->

# [386. Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return all the numbers in the range <code>[1, n]</code> sorted in lexicographical order.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and uses <code>O(1)</code> extra space.&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 13
<strong>Output:</strong> [1,10,11,12,13,2,3,4,5,6,7,8,9]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> [1,2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Iteration

We first define a variable $v$, initially $v = 1$. Then we start iterating from $1$, adding $v$ to the answer array each time. Then, if $v \times 10 \leq n$, we update $v$ to $v \times 10$; otherwise, if $v \bmod 10 = 9$ or $v + 1 > n$, we loop to divide $v$ by $10$. After the loop ends, we increment $v$. Continue iterating until we have added $n$ numbers to the answer array.

The time complexity is $O(n)$, where $n$ is the given integer $n$. Ignoring the space consumption of the answer array, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        v = 1
        for _ in range(n):
            ans.append(v)
            if v * 10 <= n:
                v *= 10
            else:
                while v % 10 == 9 or v + 1 > n:
                    v //= 10
                v += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
