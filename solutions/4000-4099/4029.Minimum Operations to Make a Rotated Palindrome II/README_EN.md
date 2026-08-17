---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/4000-4099/4029.Minimum%20Operations%20to%20Make%20a%20Rotated%20Palindrome%20II/README_EN.md
---

<!-- problem:start -->

# [4029. Minimum Operations to Make a Rotated Palindrome II 🔒](https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-ii)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>You can perform the following operations any number of times (including zero) and in any order:</p>

<ul>
	<li><strong>Increment</strong>: Choose any index <code>i</code> and replace <code>s[i]</code> with the next lowercase English letter. The letter after <code>&#39;z&#39;</code> is <code>&#39;a&#39;</code>.</li>
	<li><strong>Left rotate</strong>: Move the first character of the string to the end.</li>
</ul>

<p>Return the <strong>minimum</strong> number of operations required to make <code>s</code> a <span data-keyword="palindrome-string">palindrome</span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>
One optimal solution:

<ul>
	<li>Left rotate the string: <code>&quot;abc&quot; -&gt; &quot;bca&quot;</code>.</li>
	<li>Increment <code>&#39;a&#39;</code> to <code>&#39;b&#39;</code>: <code>&quot;bca&quot; -&gt; &quot;bcb&quot;</code>.</li>
	<li><code>&quot;bcb&quot;</code> is a palindrome. Thus, the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;yb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Increment the first character three times: <code>&quot;yb&quot; -&gt; &quot;zb&quot; -&gt; &quot;ab&quot; -&gt; &quot;bb&quot;</code>.</li>
	<li><code>&quot;bb&quot;</code> is a palindrome. Thus, the answer is 3.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s​​​​​​​​​​​​​​</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: FFT

This problem is the same as "Minimum Operations to Make a Rotated Palindrome I", but $n$ can be as large as $5 \times 10^4$, so enumerating rotations and pairing characters naively is too slow.

After $k$ left rotations, index $i$ in the new string corresponds to index $(i+k) \bmod n$ in the original string. The sum of original indices of a palindrome pair $(i, n-1-i)$ is $2k+n-1$, which is constant for all pairs. Thus, after $k$ rotations, every pair has original-index sum congruent to $c = (2k+n-1) \bmod n$.

The increment cost of two letters is the shorter arc $\min(d, 26-d)$ on the letter ring. Viewing the cost as a function on $\mathbb{Z}/26\mathbb{Z}$ and expanding it by the discrete Fourier transform, we map each character $x$ to the phase $e^{2\pi i t x / 26}$ for each frequency $t$, then compute a circular convolution of the sequence. This yields the total pairing cost for every index-sum $c$ at once. Since the cost function is even, we only need frequencies $t = 0, \ldots, 13$ (the rest follow by conjugate symmetry). Each pair is counted twice, and we also divide by $26$ from the DFT, so dividing the convolution by $52$ and rounding gives the increment cost.

For each $k$, the candidate answer is $k$ plus the increment cost of the corresponding $c$. We take the minimum.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
import numpy as np

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        size = 1
        while size < 2 * n:
            size <<= 1

        nums = np.array([ord(c) - ord('a') for c in s], dtype=np.int64)

        cost = np.zeros(26)

        for t in range(26):
            for z in range(26):
                cost[t] += min(z, 26 - z) * math.cos(2 * math.pi * t * z / 26)

        dp = np.zeros(n)

        for t in range(14):
            theta = 2 * math.pi * t / 26

            a = np.exp(1j * theta * nums)
            a = np.pad(a, (0, size - n))

            b = np.conj(a)

            fa = np.fft.fft(a)
            fb = np.fft.fft(b)

            conv = np.fft.ifft(fa * fb).real

            mult = 1 if t == 0 or t == 13 else 2

            dp += mult * cost[t] * (conv[:n] + conv[n : 2 * n])

        ans = inf

        for k in range(n):
            c = (2 * k + n - 1) % n
            d = round(dp[c] / 52)

            ans = min(ans, k + d)

        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
