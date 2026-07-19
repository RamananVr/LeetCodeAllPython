---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0964.Least%20Operators%20to%20Express%20Number/README_EN.md
tags:
    - Memoization
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [964. Least Operators to Express Number](https://leetcode.com/problems/least-operators-to-express-number)

## Description

<!-- description:start -->

<p>Given a single positive integer <code>x</code>, we will write an expression of the form <code>x (op1) x (op2) x (op3) x ...</code> where each operator <code>op1</code>, <code>op2</code>, etc. is either addition, subtraction, multiplication, or division (<code>+</code>, <code>-</code>, <code>*</code>, or <code>/)</code>. For example, with <code>x = 3</code>, we might write <code>3 * 3 / 3 + 3 - 3</code> which is a value of <font face="monospace">3</font>.</p>

<p>When writing such an expression, we adhere to the following conventions:</p>

<ul>
	<li>The division operator (<code>/</code>) returns rational numbers.</li>
	<li>There are no parentheses placed anywhere.</li>
	<li>We use the usual order of operations: multiplication and division happen before addition and subtraction.</li>
	<li>It is not allowed to use the unary negation operator (<code>-</code>). For example, &quot;<code>x - x</code>&quot; is a valid expression as it only uses subtraction, but &quot;<code>-x + x</code>&quot; is not because it uses negation.</li>
</ul>

<p>We would like to write an expression with the least number of operators such that the expression equals the given <code>target</code>. Return the least number of operators used.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 3, target = 19
<strong>Output:</strong> 5
<strong>Explanation:</strong> 3 * 3 + 3 * 3 + 3 / 3.
The expression contains 5 operations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 5, target = 501
<strong>Output:</strong> 8
<strong>Explanation:</strong> 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
The expression contains 8 operations.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 100, target = 100000000
<strong>Output:</strong> 3
<strong>Explanation:</strong> 100 * 100 * 100 * 100.
The expression contains 3 operations.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= x &lt;= 100</code></li>
	<li><code>1 &lt;= target &lt;= 2 * 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

We define a function $dfs(v)$, which represents the minimum number of operators needed to compose the number $v$ using $x$. Then the answer is $dfs(target)$.

The execution logic of function $dfs(v)$ is as follows:

If $x \geq v$, then we can obtain $v$ by adding $v$ instances of $x / x$, with the number of operators being $v \times 2 - 1$; or we can obtain $v$ by subtracting $(x - v)$ instances of $x / x$ from $x$, with the number of operators being $(x - v) \times 2$. We take the minimum of the two.

Otherwise, we enumerate $x^k$ starting from $k=2$ to find the first $k$ where $x^k \geq v$:

- If $x^k - v \geq v$ at this point, then we can only first obtain $x^{k-1}$, then recursively calculate $dfs(v - x^{k-1})$. The number of operators in this case is $k - 1 + dfs(v - x^{k-1})$;
- If $x^k - v < v$ at this point, then we can obtain $v$ in the above manner, with the number of operators being $k - 1 + dfs(v - x^{k-1})$; or we can first obtain $x^k$, then recursively calculate $dfs(x^k - v)$, with the number of operators being $k + dfs(x^k - v)$. We take the minimum of the two.

To avoid redundant calculations, we implement the $dfs$ function using memoization search.

The time complexity is $O(\log_{x}{target})$ and the space complexity is $O(\log_{x}{target})$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @cache
        def dfs(v: int) -> int:
            if x >= v:
                return min(v * 2 - 1, 2 * (x - v))
            k = 2
            while x**k < v:
                k += 1
            if x**k - v < v:
                return min(k + dfs(x**k - v), k - 1 + dfs(v - x ** (k - 1)))
            return k - 1 + dfs(v - x ** (k - 1))

        return dfs(target)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
