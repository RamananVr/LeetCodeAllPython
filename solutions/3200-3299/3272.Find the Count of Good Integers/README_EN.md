---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3272.Find%20the%20Count%20of%20Good%20Integers/README_EN.md
rating: 2382
source: Biweekly Contest 138 Q3
tags:
    - Hash Table
    - Math
    - Combinatorics
    - Enumeration
---

<!-- problem:start -->

# [3272. Find the Count of Good Integers](https://leetcode.com/problems/find-the-count-of-good-integers)

## Description

<!-- description:start -->

<p>You are given two <strong>positive</strong> integers <code>n</code> and <code>k</code>.</p>

<p>An integer <code>x</code> is called <strong>k-palindromic</strong> if:</p>

<ul>
	<li><code>x</code> is a <span data-keyword="palindrome-integer">palindrome</span>.</li>
	<li><code>x</code> is divisible by <code>k</code>.</li>
</ul>

<p>An integer is called <strong>good</strong> if its digits can be <em>rearranged</em> to form a <strong>k-palindromic</strong> integer. For example, for <code>k = 2</code>, 2020 can be rearranged to form the <em>k-palindromic</em> integer 2002, whereas 1010 cannot be rearranged to form a <em>k-palindromic</em> integer.</p>

<p>Return the count of <strong>good</strong> integers containing <code>n</code> digits.</p>

<p><strong>Note</strong> that <em>any</em> integer must <strong>not</strong> have leading zeros, <strong>neither</strong> before <strong>nor</strong> after rearrangement. For example, 1010 <em>cannot</em> be rearranged to form 101.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">27</span></p>

<p><strong>Explanation:</strong></p>

<p><em>Some</em> of the good integers are:</p>

<ul>
	<li>551 because it can be rearranged to form 515.</li>
	<li>525 because it is already k-palindromic.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1, k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The two good integers are 4 and 8.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">2468</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 9</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration + Combinatorics

We can consider enumerating all palindromic numbers of length $n$ and checking whether they are $k$-palindromic numbers. Due to the properties of palindromic numbers, we only need to enumerate the first half of the digits and then reverse and append them to form the full number.

The length of the first half of the digits is $\lfloor \frac{n - 1}{2} \rfloor$, so the range of the first half is $[10^{\lfloor \frac{n - 1}{2} \rfloor}, 10^{\lfloor \frac{n - 1}{2} \rfloor + 1})$. We can reverse the first half and append it to form a palindromic number of length $n$. Note that if $n$ is odd, the middle digit needs special handling.

Next, we check whether the palindromic number is $k$-palindromic. If it is, we count all unique permutations of the number. To avoid duplicates, we can use a set $\textit{vis}$ to store the smallest permutation of each palindromic number that has already been processed. If the smallest permutation of the current palindromic number is already in the set, we skip it. Otherwise, we calculate the number of unique permutations of the palindromic number and add it to the result.

We can use an array $\textit{cnt}$ to count the occurrences of each digit and use combinatorics to calculate the number of permutations. Specifically, if digit $0$ appears $x_0$ times, digit $1$ appears $x_1$ times, ..., and digit $9$ appears $x_9$ times, the number of permutations of the palindromic number is:

$$
\frac{(n - x_0) \cdot (n - 1)!}{x_0! \cdot x_1! \cdots x_9!}
$$

Here, $(n - x_0)$ represents the number of choices for the highest digit (excluding $0$), $(n - 1)!$ represents the permutations of the remaining digits, and we divide by the factorial of the occurrences of each digit to avoid duplicates.

Finally, we sum up all the permutation counts to get the final result.

Time complexity is $O(10^m \times n \times \log n)$, and space complexity is $O(10^m \times n)$, where $m = \lfloor \frac{n - 1}{2} \rfloor$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        vis = set()
        base = 10 ** ((n - 1) // 2)
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][n % 2 :]
            if int(s) % k:
                continue
            t = "".join(sorted(s))
            if t in vis:
                continue
            vis.add(t)
            cnt = Counter(t)
            res = (n - cnt["0"]) * fac[n - 1]
            for x in cnt.values():
                res //= fac[x]
            ans += res
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
