---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0906.Super%20Palindromes/README_EN.md
tags:
    - Math
    - String
    - Enumeration
---

<!-- problem:start -->

# [906. Super Palindromes](https://leetcode.com/problems/super-palindromes)

## Description

<!-- description:start -->

<p>Let&#39;s say a positive integer is a <strong>super-palindrome</strong> if it is a palindrome, and it is also the square of a palindrome.</p>

<p>Given two positive integers <code>left</code> and <code>right</code> represented as strings, return <em>the number of <strong>super-palindromes</strong> integers in the inclusive range</em> <code>[left, right]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> left = &quot;4&quot;, right = &quot;1000&quot;
<strong>Output:</strong> 4
<strong>Explanation</strong>: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> left = &quot;1&quot;, right = &quot;2&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= left.length, right.length &lt;= 18</code></li>
	<li><code>left</code> and <code>right</code> consist of only digits.</li>
	<li><code>left</code> and <code>right</code> cannot have leading zeros.</li>
	<li><code>left</code> and <code>right</code> represent integers in the range <code>[1, 10<sup>18</sup> - 1]</code>.</li>
	<li><code>left</code> is less than or equal to <code>right</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Enumeration

According to the problem description, we assume that the super palindrome number $x = p^2 \in [1, 10^{18})$, where $p$ is a palindrome number, so $p \in [1, 10^9)$. We can enumerate the first half of the palindrome number $p$, then reverse it, and concatenate it to get all palindrome numbers, which are recorded in the array $ps$.

Next, we traverse the array $ps$. For each $p$, we calculate $p^2$, check whether it is in the interval $[L, R]$, and also check whether $p^2$ is a palindrome number. If it is, the answer is incremented by one.

After the traversal, return the answer.

The time complexity is $O(M^{\frac{1}{4}} \times \log M)$, and the space complexity is $O(M^{\frac{1}{4}})$. Where $M$ is the upper bound of $L$ and $R$, and in this problem, $M \leq 10^{18}$.

Similar problems:

- [2967. Minimum Cost to Make Array Equalindromic](https://github.com/doocs/leetcode/blob/main/solution/2900-2999/2967.Minimum%20Cost%20to%20Make%20Array%20Equalindromic/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
ps = []
for i in range(1, 10**5 + 1):
    s = str(i)
    t1 = s[::-1]
    t2 = s[:-1][::-1]
    ps.append(int(s + t1))
    ps.append(int(s + t2))

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(x: int) -> bool:
            y, t = 0, x
            while t:
                y = y * 10 + t % 10
                t //= 10
            return x == y

        l, r = int(left), int(right)
        return sum(l <= x <= r and is_palindrome(x) for x in map(lambda x: x * x, ps))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
