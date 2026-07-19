---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1228.Missing%20Number%20In%20Arithmetic%20Progression/README_EN.md
rating: 1244
source: Biweekly Contest 11 Q1
tags:
    - Array
    - Math
---

<!-- problem:start -->

# [1228. Missing Number In Arithmetic Progression 🔒](https://leetcode.com/problems/missing-number-in-arithmetic-progression)

## Description

<!-- description:start -->

<p>In some array <code>arr</code>, the values were in arithmetic progression: the values <code>arr[i + 1] - arr[i]</code> are all equal for every <code>0 &lt;= i &lt; arr.length - 1</code>.</p>

<p>A value from <code>arr</code> was removed that <strong>was not the first or last value in the array</strong>.</p>

<p>Given <code>arr</code>, return <em>the removed value</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [5,7,11,13]
<strong>Output:</strong> 9
<strong>Explanation:</strong> The previous array was [5,7,<strong>9</strong>,11,13].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [15,13,12]
<strong>Output:</strong> 14
<strong>Explanation:</strong> The previous array was [15,<strong>14</strong>,13,12].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
	<li>The given array is <strong>guaranteed</strong> to be a valid array.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Arithmetic Series Sum Formula

The sum formula for an arithmetic series is $\frac{(a_1 + a_n)n}{2}$, where $n$ is the number of terms in the arithmetic series, the first term is $a_1$, and the last term is $a_n$.

Since the array given in the problem is an arithmetic series with one missing number, the number of terms in the array is $n + 1$, the first term is $a_1$, and the last term is $a_n$. Therefore, the sum of the array is $\frac{(a_1 + a_n)(n + 1)}{2}$.

Thus, the missing number is $\frac{(a_1 + a_n)(n + 1)}{2} - \sum_{i = 0}^n a_i$.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Find Common Difference + Traverse

Since the array given in the problem is an arithmetic series with one missing number, the first term is $a_1$, and the last term is $a_n$. The common difference $d$ is $\frac{a_n - a_1}{n}$.

Traverse the array, and if $a_i \neq a_{i - 1} + d$, then return $a_{i - 1} + d$.

If the traversal completes without finding the missing number, it means all numbers in the array are equal. In this case, directly return the first number of the array.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        d = (arr[-1] - arr[0]) // n
        for i in range(1, n):
            if arr[i] != arr[i - 1] + d:
                return arr[i - 1] + d
        return arr[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
