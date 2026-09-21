---
comments: true
difficulty: Medium
rating: 2113
source: Weekly Contest 519 Q2
---

<!-- problem:start -->

# [4053. Minimum Operations to Make Every Element Palindromic](https://leetcode.com/problems/minimum-operations-to-make-every-element-palindromic)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>In one <strong>operation</strong>, you may choose an index <code>i</code> and either increment or decrement <code>nums[i]</code> by 2.</p>

<p>Return the <strong>minimum</strong> number of operations required to make every element in <code>nums</code> a <strong>positive</strong> <span data-keyword="palindrome-integer">palindrome</span>. Different elements may be changed into different palindromic integers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [10,12,14,16]</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal sequence of operations is:</p>

<ul>
	<li>Decrement <code>nums[0]</code> by 2 once to change it from 10 to 8.</li>
	<li>Decrement <code>nums[1]</code> by 2 twice to change it from 12 to 8.</li>
	<li>Decrement <code>nums[2]</code> by 2 three times to change it from 14 to 8.</li>
	<li>Increment <code>nums[3]</code> by 2 three times to change it from 16 to 22.</li>
</ul>

<p>After <code>1 + 2 + 3 + 3 = 9</code> operations, <code>nums = [8, 8, 8, 22]</code>, and every element is a positive palindromic integer.</p>

<p>It can be shown that fewer than 9 operations cannot achieve this.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [9,10,11,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Decrement <code>nums[1]</code> and <code>nums[3]</code> by 2 once each.</p>

<p>After 2 operations, <code>nums = [9, 8, 11, 8]</code>, and every element is a positive palindromic integer.</p>

<p>At least one operation is needed for each of these two elements, so the minimum number of operations is 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [125]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Decrement <code>nums[0]</code> by 2 twice to change it from 125 to 121, which is a positive palindromic integer.</p>

<p>A single operation would change it to 123 or 127, neither of which is palindromic. Thus, the minimum number of operations is 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Precompute Palindromes + Binary Search

<!-- thinking:start -->

> **Thinking**
>
> Each operation adds or subtracts $2$, so parity never changes: $\textit{nums}[i]$ can only become a positive palindrome of the same parity. The elements are independent, and the answer is the sum of each value's distance to the nearest same-parity palindrome, divided by $2$.
>
> With $n = 10^5$ and values up to $10^9$, walking from $x$ by steps of $2$ until a palindrome appears is too slow.
>
> Every palindrome is a mirrored prefix. Enumerating prefixes $1 \ldots 10^5$ and forming both even-length and odd-length palindromes covers everything around $10^9$. Split them by parity, sort each list, and binary-search the nearest neighbor for every $x$.

<!-- thinking:end -->

An operation increments or decrements an element by $2$, so its parity is invariant and the target palindrome must have the same parity. The elements are independent: for each $x$, find the nearest same-parity positive palindrome $p$ and add $\lvert x - p \rvert / 2$.

During preprocessing, enumerate prefixes $i = 1, 2, \ldots, 10^5$ and let $s$ be the decimal representation of $i$:

- Even-length palindrome: $s + \mathrm{reverse}(s)$
- Odd-length palindrome: $s + \mathrm{reverse}(s[:-1])$

Store them in two lists by parity and sort each list. This range covers all palindromes with up to about $12$ digits, which is enough for values up to $10^9$.

For each $x$, binary-search the first palindrome that is at least $x$ in the same-parity list, compare it with the previous one, and take the smaller distance divided by $2$.

Let $M$ be the number of palindromes (about $2 \times 10^5$). Preprocessing takes $O(M \log M)$ and each query takes $O(\log M)$. The overall time complexity is $O(M \log M + n \log M)$, and the space complexity is $O(M)$.

<!-- tabs:start -->

#### Python3

```python
ps = [[], []]
for i in range(1, 10**5 + 1):
    s = str(i)
    t1 = s[::-1]
    t2 = s[:-1][::-1]
    x = int(s + t1)
    ps[x & 1].append(x)
    y = int(s + t2)
    ps[y & 1].append(y)
for p in ps:
    p.sort()

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for x in nums:
            p = ps[x & 1]
            i = bisect_left(p, x)
            t = inf
            if i < len(p):
                t = p[i] - x
            if i:
                t = min(t, x - p[i - 1])
            ans += t // 2
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
