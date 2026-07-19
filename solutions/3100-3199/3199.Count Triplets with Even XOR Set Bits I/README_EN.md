---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3199.Count%20Triplets%20with%20Even%20XOR%20Set%20Bits%20I/README_EN.md
tags:
    - Bit Manipulation
    - Array
---

<!-- problem:start -->

# [3199. Count Triplets with Even XOR Set Bits I 🔒](https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i)

## Description

<!-- description:start -->

Given three integer arrays <code>a</code>, <code>b</code>, and <code>c</code>, return the number of triplets <code>(a[i], b[j], c[k])</code>, such that the bitwise <code>XOR</code> of the elements of each triplet has an <strong>even</strong> number of <span data-keyword="set-bit">set bits</span>.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">a = [1], b = [2], c = [3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only triplet is <code>(a[0], b[0], c[0])</code> and their <code>XOR</code> is: <code>1 XOR 2 XOR 3 = 00<sub>2</sub></code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">a = [1,1], b = [2,3], c = [1,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Consider these four triplets:</p>

<ul>
	<li><code>(a[0], b[1], c[0])</code>: <code>1 XOR 3 XOR 1 = 011<sub>2</sub></code></li>
	<li><code>(a[1], b[1], c[0])</code>: <code>1 XOR 3 XOR 1 = 011<sub>2</sub></code></li>
	<li><code>(a[0], b[0], c[1])</code>: <code>1 XOR 2 XOR 5 = 110<sub>2</sub></code></li>
	<li><code>(a[1], b[0], c[1])</code>: <code>1 XOR 2 XOR 5 = 110<sub>2</sub></code></li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length, c.length &lt;= 100</code></li>
	<li><code>0 &lt;= a[i], b[i], c[i] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bit Manipulation

For two integers, the parity of the number of $1$s in the XOR result depends on the parity of the number of $1$s in the binary representations of the two integers.

We can use three arrays `cnt1`, `cnt2`, `cnt3` to record the parity of the number of $1$s in the binary representations of each number in arrays `a`, `b`, `c`, respectively.

Then, we enumerate the parity of the number of $1$s in the binary representations of each number in the three arrays within the range $[0, 1]$. If the sum of the parity of the number of $1$s in the binary representations of three numbers is even, then the number of $1$s in the XOR result of these three numbers is also even. At this time, we multiply the combination of these three numbers and accumulate it into the answer.

Finally, return the answer.

The time complexity is $O(n)$, where $n$ is the length of arrays `a`, `b`, `c`. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        cnt1 = Counter(x.bit_count() & 1 for x in a)
        cnt2 = Counter(x.bit_count() & 1 for x in b)
        cnt3 = Counter(x.bit_count() & 1 for x in c)
        ans = 0
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if (i + j + k) & 1 ^ 1:
                        ans += cnt1[i] * cnt2[j] * cnt3[k]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
