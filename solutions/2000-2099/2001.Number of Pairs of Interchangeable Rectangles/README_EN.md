---
comments: true
difficulty: Medium
rating: 1435
source: Weekly Contest 258 Q2
tags:
    - Array
    - Hash Table
    - Math
    - Counting
    - Number Theory
---

<!-- problem:start -->

# [2001. Number of Pairs of Interchangeable Rectangles](https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles)

## Description

<!-- description:start -->

<p>You are given <code>n</code> rectangles represented by a <strong>0-indexed</strong> 2D integer array <code>rectangles</code>, where <code>rectangles[i] = [width<sub>i</sub>, height<sub>i</sub>]</code> denotes the width and height of the <code>i<sup>th</sup></code> rectangle.</p>

<p>Two rectangles <code>i</code> and <code>j</code> (<code>i &lt; j</code>) are considered <strong>interchangeable</strong> if they have the <strong>same</strong> width-to-height ratio. More formally, two rectangles are <strong>interchangeable</strong> if <code>width<sub>i</sub>/height<sub>i</sub> == width<sub>j</sub>/height<sub>j</sub></code> (using decimal division, not integer division).</p>

<p>Return <em>the <strong>number</strong> of pairs of <strong>interchangeable</strong> rectangles in </em><code>rectangles</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> rectangles = [[4,8],[3,6],[10,20],[15,30]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> rectangles = [[4,5],[7,8]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no interchangeable pairs of rectangles.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == rectangles.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>rectangles[i].length == 2</code></li>
	<li><code>1 &lt;= width<sub>i</sub>, height<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Mathematics + Hash Table

<!-- thinking:start -->

> **Thinking**
>
> Two rectangles are interchangeable iff they share a width-to-height ratio. With $n \le 10^5$, pairwise comparison is quadratic.
>
> Floating-point $w/h$ is unsafe as a key. Dividing $(w,h)$ by $\gcd(w,h)$ maps each ratio to a unique integer pair.
>
> A hash table therefore counts each reduced pair; for every rectangle we add the current count, then increment, so combinations accumulate in one pass.

<!-- thinking:end -->

In order to uniquely represent a rectangle, we need to simplify the width-to-height ratio of the rectangle to a simplest fraction. Therefore, we can find the greatest common divisor of the width-to-height ratio of each rectangle, and then simplify the width-to-height ratio to the simplest fraction. Next, we use a hash table to count the number of rectangles for each simplest fraction, and then calculate the combination of the number of rectangles for each simplest fraction to get the answer.

The time complexity is $O(n \times \log M)$, and the space complexity is $O(n)$. Here, $n$ and $M$ are the number of rectangles and the maximum side length of the rectangles, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        cnt = Counter()
        for w, h in rectangles:
            g = gcd(w, h)
            w, h = w // g, h // g
            ans += cnt[(w, h)]
            cnt[(w, h)] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
