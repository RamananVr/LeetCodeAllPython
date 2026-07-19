---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1246.Palindrome%20Removal/README_EN.md
rating: 2203
source: Biweekly Contest 12 Q4
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [1246. Palindrome Removal 🔒](https://leetcode.com/problems/palindrome-removal)

## Description

<!-- description:start -->

<p>You are given an integer array <code>arr</code>.</p>

<p>In one move, you can select a <strong>palindromic</strong> subarray <code>arr[i], arr[i + 1], ..., arr[j]</code> where <code>i &lt;= j</code>, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.</p>

<p>Return <em>the minimum number of moves needed to remove all numbers from the array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,4,1,5]
<strong>Output:</strong> 3
<b>Explanation: </b>Remove [4] then remove [1,3,1] then remove [5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 20</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming (Interval DP)

We define $f[i][j]$ as the minimum number of operations required to delete all numbers in the index range $[i,..j]$. Initially, $f[i][i] = 1$, which means that when there is only one number, one deletion operation is needed.

For $f[i][j]$, if $i + 1 = j$, i.e., there are only two numbers, if $arr[i]=arr[j]$, then $f[i][j] = 1$, otherwise $f[i][j] = 2$.

For the case of more than two numbers, if $arr[i]=arr[j]$, then $f[i][j]$ can be $f[i + 1][j - 1]$, or we can enumerate $k$ in the index range $[i,..j-1]$, take the minimum value of $f[i][k] + f[k + 1][j]$. Assign the minimum value to $f[i][j]$.

The answer is $f[0][n - 1]$.

The time complexity is $O(n^3)$, and the space complexity is $O(n^2)$. Where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if i + 1 == j:
                    f[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    t = f[i + 1][j - 1] if arr[i] == arr[j] else inf
                    for k in range(i, j):
                        t = min(t, f[i][k] + f[k + 1][j])
                    f[i][j] = t
        return f[0][n - 1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
