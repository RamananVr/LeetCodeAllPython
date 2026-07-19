---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2595.Number%20of%20Even%20and%20Odd%20Bits/README_EN.md
rating: 1206
source: Weekly Contest 337 Q1
tags:
    - Bit Manipulation
---

<!-- problem:start -->

# [2595. Number of Even and Odd Bits](https://leetcode.com/problems/number-of-even-and-odd-bits)

## Description

<!-- description:start -->

<p>You are given a <strong>positive</strong> integer <code>n</code>.</p>

<p>Let <code>even</code> denote the number of even indices in the binary representation of <code>n</code> with value 1.</p>

<p>Let <code>odd</code> denote the number of odd indices in the binary representation of <code>n</code> with value 1.</p>

<p>Note that bits are indexed from <strong>right to left</strong> in the binary representation of a number.</p>

<p>Return the array <code>[even, odd]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 50</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 50 is <code>110010</code>.</p>

<p>It contains 1 on indices 1, 4, and 5.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 2 is <code>10</code>.</p>

<p>It contains 1 only on index 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumerate

According to the problem description, enumerate the binary representation of $n$ from the low bit to the high bit. If the bit is $1$, add $1$ to the corresponding counter according to whether the index of the bit is odd or even.

The time complexity is $O(\log n)$ and the space complexity is $O(1)$. Where $n$ is the given integer.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        i = 0
        while n:
            ans[i] += n & 1
            i ^= 1
            n >>= 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Bit Manipulation

We can define a mask $\textit{mask} = \text{0x5555}$, which is represented in binary as $\text{0101 0101 0101 0101}_2$. Then, performing a bitwise AND operation between $n$ and $\textit{mask}$ will give us the bits at even indices in the binary representation of $n$. Performing a bitwise AND operation between $n$ and the complement of $\textit{mask}$ will give us the bits at odd indices in the binary representation of $n$. We can count the number of 1s in these two results.

The time complexity is $O(1)$, and the space complexity is $O(1)$. Here, $n$ is the given integer.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        mask = 0x5555
        even = (n & mask).bit_count()
        odd = (n & ~mask).bit_count()
        return [even, odd]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
