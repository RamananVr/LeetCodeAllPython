---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3890.Integers%20With%20Multiple%20Sum%20of%20Two%20Cubes/README_EN.md
rating: 1534
source: Weekly Contest 496 Q2
tags:
    - Hash Table
    - Counting
    - Enumeration
    - Sorting
---

<!-- problem:start -->

# [3890. Integers With Multiple Sum of Two Cubes](https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes)

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code>.</p>

<p>An integer <code>x</code> is considered <strong>good</strong> if there exist <strong>at least</strong> two <strong>distinct</strong> pairs <code>(a, b)</code> such that:</p>

<ul>
	<li><code>a</code> and <code>b</code> are positive integers.</li>
	<li><code>a &lt;= b</code></li>
	<li><code>x = a<sup>3</sup> + b<sup>3</sup></code></li>
</ul>

<p>Return an array containing all good integers <strong>less than or equal to</strong> <code>n</code>, sorted in ascending order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4104</span></p>

<p><strong>Output:</strong> <span class="example-io">[1729,4104]</span></p>

<p><strong>Explanation:</strong></p>

<p>Among integers less than or equal to 4104, the good integers are:</p>

<ul>
	<li>1729: <code>1<sup>3</sup> + 12<sup>3</sup> = 1729</code> and <code>9<sup>3</sup> + 10<sup>3</sup> = 1729</code>.</li>
	<li>4104: <code>2<sup>3</sup> + 16<sup>3</sup> = 4104</code> and <code>9<sup>3</sup> + 15<sup>3</sup> = 4104</code>.</li>
</ul>

<p>Thus, the answer is <code>[1729, 4104]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 578</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no good integers less than or equal to 578, so the answer is an empty array.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Binary Search

We observe that when $a$ or $b$ is greater than $1000$, the expression $a^3 + b^3 > 10^9$. Therefore, we only need to enumerate $1 \leq a \leq b \leq 1000$ and count the occurrences of each integer $x = a^3 + b^3$. Finally, we filter out the integers that appear more than once and sort them in ascending order to obtain all good integers.

We preprocess all good integers and store them in an array $\textit{GOOD}$. For each query, we use binary search to find the index $idx$ of the first integer in $\textit{GOOD}$ that is greater than $n$, then return the first $idx$ integers in $\textit{GOOD}$.

The time complexity is $O(m^2 + k \log k)$, where $m = 1000$ is the enumeration range and $k$ is the number of good integers. The space complexity is $O(k)$.

<!-- tabs:start -->

#### Python3

```python
LIMIT = 10**9

cnt = defaultdict(int)
cubes = [i**3 for i in range(1001)]

for a in range(1, 1001):
    for b in range(a, 1001):
        x = cubes[a] + cubes[b]
        if x > LIMIT:
            break
        cnt[x] += 1

GOOD = sorted(x for x, v in cnt.items() if v > 1)

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        idx = bisect_right(GOOD, n)
        return GOOD[:idx]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
