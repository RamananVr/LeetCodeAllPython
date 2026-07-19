---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3704.Count%20No-Zero%20Pairs%20That%20Sum%20to%20N/README_EN.md
rating: 2419
source: Weekly Contest 470 Q4
tags:
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [3704. Count No-Zero Pairs That Sum to N](https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n)

## Description

<!-- description:start -->

<p>A <strong>no-zero</strong> integer is a <strong>positive</strong> integer that <strong>does not contain the digit</strong> 0 in its decimal representation.</p>

<p>Given an integer <code>n</code>, count the number of pairs <code>(a, b)</code> where:</p>

<ul>
	<li><code>a</code> and <code>b</code> are <strong>no-zero</strong> integers.</li>
	<li><code>a + b = n</code></li>
</ul>

<p>Return an integer denoting the number of such pairs.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only pair is <code>(1, 1)</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The pairs are <code>(1, 2)</code> and <code>(2, 1)</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 11</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The pairs are <code>(2, 9)</code>, <code>(3, 8)</code>, <code>(4, 7)</code>, <code>(5, 6)</code>, <code>(6, 5)</code>, <code>(7, 4)</code>, <code>(8, 3)</code>, and <code>(9, 2)</code>. Note that <code>(1, 10)</code> and <code>(10, 1)</code> do not satisfy the conditions because 10 contains 0 in its decimal representation.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>15</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Digit DP

We do a digit DP over the decimal representation of $n$ from the least-significant digit to the most-significant digit.

State: `dp[pos][carry][aliveA][aliveB]` = number of ways for the processed suffix.

- `carry` is the carry into the current digit (0 or 1).
- `aliveA/aliveB` indicates whether the number still has digits in higher positions. If `aliveX = 0`, all remaining higher digits must be leading zeros (digit 0), which are not part of the decimal representation.

Transition: choose digits `da` and `db`:

- If `aliveX = 1`, digit is in `[1..9]` (no-zero).
- Otherwise digit is `0`.

They must satisfy `(da + db + carry) % 10 == digit_n[pos]`. After that, `aliveA`/`aliveB` can stay `1` or become `0` (ending the number at this digit).

We append one extra leading digit `0` to $n$ so the last carry is fully handled. The answer is `dp[last][0][0][0]`.

Time complexity is $O(L \cdot 9^2)$ and space complexity is $O(1)$, where $L$ is the number of digits of $n$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
	def countNoZeroPairs(self, n: int) -> int:
		digits = list(map(int, str(n)))[::-1]
		digits.append(0)  # absorb final carry
		L = len(digits)

		# dp[carry][aliveA][aliveB]
		dp = [[[0] * 2 for _ in range(2)] for _ in range(2)]
		dp[0][1][1] = 1

		for pos in range(L):
			ndp = [[[0] * 2 for _ in range(2)] for _ in range(2)]
			target = digits[pos]
			for carry in range(2):
				for aliveA in range(2):
					for aliveB in range(2):
						ways = dp[carry][aliveA][aliveB]
						if ways == 0:
							continue

						if aliveA:
							A = [(d, 1) for d in range(1, 10)]
							if pos > 0:
								A.append((0, 0))  # end number here
						else:
							A = [(0, 0)]

						if aliveB:
							B = [(d, 1) for d in range(1, 10)]
							if pos > 0:
								B.append((0, 0))
						else:
							B = [(0, 0)]

						for da, na in A:
							for db, nb in B:
								s = da + db + carry
								if s % 10 != target:
									continue
								ndp[s // 10][na][nb] += ways
			dp = ndp

		return dp[0][0][0]

```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
