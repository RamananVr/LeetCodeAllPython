---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0043.Multiply%20Strings/README_EN.md
tags:
    - Math
    - String
    - Simulation
---

<!-- problem:start -->

# [43. Multiply Strings](https://leetcode.com/problems/multiply-strings)

## Description

<!-- description:start -->

<p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as strings, return the product of <code>num1</code> and <code>num2</code>, also represented as a string.</p>

<p><strong>Note:</strong>&nbsp;You must not use any built-in BigInteger library or convert the inputs to integer directly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num1 = "2", num2 = "3"
<strong>Output:</strong> "6"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num1 = "123", num2 = "456"
<strong>Output:</strong> "56088"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1.length, num2.length &lt;= 200</code></li>
	<li><code>num1</code> and <code>num2</code> consist of digits only.</li>
	<li>Both <code>num1</code> and <code>num2</code>&nbsp;do not contain any leading zero, except the number <code>0</code> itself.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulating Mathematical Multiplication

Assume the lengths of $num1$ and $num2$ are $m$ and $n$ respectively, then the length of their product can be at most $m + n$.

The proof is as follows:

- If $num1$ and $num2$ both take the minimum value, then their product is ${10}^{m - 1} \times {10}^{n - 1} = {10}^{m + n - 2}$, with a length of $m + n - 1$.
- If $num1$ and $num2$ both take the maximum value, then their product is $({10}^m - 1) \times ({10}^n - 1) = {10}^{m + n} - {10}^m - {10}^n + 1$, with a length of $m + n$.

Therefore, we can apply for an array of length $m + n$ to store each digit of the product.

From the least significant digit to the most significant digit, we calculate each digit of the product in turn, and finally convert the array into a string.

Note to check whether the most significant digit is $0$, if it is, remove it.

The time complexity is $O(m \times n)$, and the space complexity is $O(m + n)$. Here, $m$ and $n$ are the lengths of $num1$ and $num2$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        arr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            a = int(num1[i])
            for j in range(n - 1, -1, -1):
                b = int(num2[j])
                arr[i + j + 1] += a * b
        for i in range(m + n - 1, 0, -1):
            arr[i - 1] += arr[i] // 10
            arr[i] %= 10
        i = 0 if arr[0] else 1
        return "".join(str(x) for x in arr[i:])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
