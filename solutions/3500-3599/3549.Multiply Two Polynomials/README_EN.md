---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3549.Multiply%20Two%20Polynomials/README_EN.md
tags:
    - Array
    - Math
---

<!-- problem:start -->

# [3549. Multiply Two Polynomials 🔒](https://leetcode.com/problems/multiply-two-polynomials)

## Description

<!-- description:start -->

<p data-end="315" data-start="119">You are given two integer arrays <code>poly1</code> and <code>poly2</code>, where the element at index <code>i</code> in each array represents the coefficient of <code>x<sup>i</sup></code> in a polynomial.</p>

<p>Let <code>A(x)</code> and <code>B(x)</code> be the polynomials represented by <code>poly1</code> and <code>poly2</code>, respectively.</p>

<p>Return an integer array <code>result</code> of length <code>(poly1.length + poly2.length - 1)</code> representing the coefficients of the product polynomial <code>R(x) = A(x) * B(x)</code>, where <code>result[i]</code> denotes the coefficient of <code>x<sup>i</sup></code> in <code>R(x)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">poly1 = [3,2,5], poly2 = [1,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,14,13,20]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>A(x) = 3 + 2x + 5x<sup>2</sup></code> and <code>B(x) = 1 + 4x</code></li>
	<li><code>R(x) = (3 + 2x + 5x<sup>2</sup>) * (1 + 4x)</code></li>
	<li><code>R(x) = 3 * 1 + (3 * 4 + 2 * 1)x + (2 * 4 + 5 * 1)x<sup>2</sup> + (5 * 4)x<sup>3</sup></code></li>
	<li><code>R(x) = 3 + 14x + 13x<sup>2</sup> + 20x<sup>3</sup></code></li>
	<li>Thus, result = <code>[3, 14, 13, 20]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">poly1 = [1,0,-2], poly2 = [-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,0,2]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>A(x) = 1 + 0x - 2x<sup>2</sup></code> and <code>B(x) = -1</code></li>
	<li><code>R(x) = (1 + 0x - 2x<sup>2</sup>) * (-1)</code></li>
	<li><code>R(x) = -1 + 0x + 2x<sup>2</sup></code></li>
	<li>Thus, result = <code>[-1, 0, 2]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">poly1 = [1,5,-3], poly2 = [-4,2,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-4,-18,22,-6,0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>A(x) = 1 + 5x - 3x<sup>2</sup></code> and <code>B(x) = -4 + 2x + 0x<sup>2</sup></code></li>
	<li><code>R(x) = (1 + 5x - 3x<sup>2</sup>) * (-4 + 2x + 0x<sup>2</sup>)</code></li>
	<li><code>R(x) = 1 * -4 + (1 * 2 + 5 * -4)x + (5 * 2 + -3 * -4)x<sup>2</sup> + (-3 * 2)x<sup>3</sup> + 0x<sup>4</sup></code></li>
	<li><code>R(x) = -4 -18x + 22x<sup>2</sup> -6x<sup>3</sup> + 0x<sup>4</sup></code></li>
	<li>Thus, result = <code>[-4, -18, 22, -6, 0]</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= poly1.length, poly2.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>3</sup> &lt;= poly1[i], poly2[i] &lt;= 10<sup>3</sup></code></li>
	<li><code>poly1</code> and <code>poly2</code> contain at least one non-zero coefficient.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: FFT

We can use the Fast Fourier Transform (FFT) to efficiently compute the product of two polynomials. FFT is an efficient algorithm that can compute the product of polynomials in $O(n \log n)$ time complexity.

The specific steps are as follows:

1. **Padding the length** Let the result length be $m = |A|+|B|-1$, and round it up to the nearest power of 2, $n$, to facilitate divide-and-conquer FFT.
2. **FFT transformation** Perform the forward FFT (with `invert=False`) on both coefficient sequences.
3. **Pointwise multiplication** Multiply the corresponding elements in the frequency domain.
4. **Inverse FFT** Perform the inverse FFT (with `invert=True`) on the product sequence, and round the real parts to the nearest integer to obtain the final coefficients.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the polynomials.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def multiply(self, poly1: List[int], poly2: List[int]) -> List[int]:
        if not poly1 or not poly2:
            return []

        m = len(poly1) + len(poly2) - 1
        n = 1
        while n < m:
            n <<= 1

        fa = list(map(complex, poly1)) + [0j] * (n - len(poly1))
        fb = list(map(complex, poly2)) + [0j] * (n - len(poly2))

        self._fft(fa, invert=False)
        self._fft(fb, invert=False)

        for i in range(n):
            fa[i] *= fb[i]

        self._fft(fa, invert=True)
        return [int(round(fa[i].real)) for i in range(m)]

    def _fft(self, a: List[complex], invert: bool) -> None:
        n = len(a)

        j = 0
        for i in range(1, n):
            bit = n >> 1
            while j & bit:
                j ^= bit
                bit >>= 1
            j ^= bit
            if i < j:
                a[i], a[j] = a[j], a[i]

        len_ = 2
        while len_ <= n:
            ang = 2 * math.pi / len_ * (-1 if invert else 1)
            wlen = complex(math.cos(ang), math.sin(ang))
            for i in range(0, n, len_):
                w = 1 + 0j
                half = i + len_ // 2
                for j in range(i, half):
                    u = a[j]
                    v = a[j + len_ // 2] * w
                    a[j] = u + v
                    a[j + len_ // 2] = u - v
                    w *= wlen
            len_ <<= 1

        if invert:
            for i in range(n):
                a[i] /= n
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
