---
comments: true
difficulty: Hard
rating: 3101
source: Biweekly Contest 143 Q4
tags:
    - Greedy
    - Math
    - String
    - Backtracking
    - Number Theory
---

<!-- problem:start -->

# [3348. Smallest Divisible Digit Product II](https://leetcode.com/problems/smallest-divisible-digit-product-ii)

## Description

<!-- description:start -->

<p>You are given a string <code>num</code> which represents a <strong>positive</strong> integer, and an integer <code>t</code>.</p>

<p>A number is called <strong>zero-free</strong> if <em>none</em> of its digits are 0.</p>

<p>Return a string representing the <strong>smallest</strong> <strong>zero-free</strong> number greater than or equal to <code>num</code> such that the <strong>product of its digits</strong> is divisible by <code>t</code>. If no such number exists, return <code>&quot;-1&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = &quot;1234&quot;, t = 256</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;1488&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = &quot;12355&quot;, t = 50</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;12355&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = &quot;11111&quot;, t = 26</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;-1&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>No number greater than 11111 has the product of its digits divisible by 26.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= num.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>num</code> consists only of digits in the range <code>[&#39;0&#39;, &#39;9&#39;]</code>.</li>
	<li><code>num</code> does not contain leading zeros.</li>
	<li><code>1 &lt;= t &lt;= 10<sup>14</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> We need the smallest zero-free integer that is at least $\textit{num}$ and whose digit product is divisible by $t$. With $|\textit{num}| \le 2 \times 10^5$ we cannot increment from $n$.
>
> If $t$ has a prime factor other than $2,3,5,7$, there is no answer. Otherwise we pack the remaining primes into digits $8,9,6,4$ so the length is minimized.
>
> From the right we try to raise one digit and fill the suffix with ones plus those packed digits; if the current length is too short we prepend ones. That yields the lexicographically smallest valid number.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        digit_primes = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [3, 0, 0, 0],
            [0, 2, 0, 0],
        ]

        def factorize(target: int):
            counts = [0, 0, 0, 0]
            for i, p in enumerate((2, 3, 5, 7)):
                while target % p == 0:
                    target //= p
                    counts[i] += 1
            return counts, target == 1

        def subtract(a, b):
            return [max(0, x - y) for x, y in zip(a, b)]

        def to_digits(primes):
            count8 = primes[0] // 3
            remaining2 = primes[0] % 3
            count9 = primes[1] // 2
            count3 = primes[1] % 2
            count4 = remaining2 // 2
            count2 = remaining2 % 2
            count6 = 0
            if count2 == 1 and count3 == 1:
                count2 = count3 = 0
                count6 = 1
            if count3 == 1 and count4 == 1:
                count2 = 1
                count6 = 1
                count3 = count4 = 0
            return [
                0,
                0,
                count2,
                count3,
                count4,
                primes[2],
                count6,
                primes[3],
                count8,
                count9,
            ]

        def construct(digits) -> str:
            return "".join(str(d) * digits[d] for d in range(2, 10))

        required, ok = factorize(t)
        if not ok:
            return "-1"
        need = to_digits(required)
        if sum(need) > len(num):
            return construct(need)

        prefix = [0, 0, 0, 0]
        for ch in num:
            d = ord(ch) - 48
            for i in range(4):
                prefix[i] += digit_primes[d][i]
        first_zero = num.find("0")
        if first_zero == -1:
            first_zero = len(num)
            if all(r <= p for r, p in zip(required, prefix)):
                return num

        n = len(num)
        for i in range(n - 1, -1, -1):
            d = ord(num[i]) - 48
            prefix = subtract(prefix, digit_primes[d])
            space = n - 1 - i
            if i > first_zero:
                continue
            for bigger in range(d + 1, 10):
                suffix = to_digits(
                    subtract(subtract(required, prefix), digit_primes[bigger])
                )
                if sum(suffix) <= space:
                    return (
                        num[:i]
                        + str(bigger)
                        + "1" * (space - sum(suffix))
                        + construct(suffix)
                    )
        ext = to_digits(required)
        return "1" * (n + 1 - sum(ext)) + construct(ext)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
