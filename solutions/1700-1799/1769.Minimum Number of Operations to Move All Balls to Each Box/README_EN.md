---
comments: true
difficulty: Medium
rating: 1294
source: Weekly Contest 229 Q2
tags:
    - Array
    - String
    - Prefix Sum
---

<!-- problem:start -->

# [1769. Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box)

## Description

<!-- description:start -->

<p>You have <code>n</code> boxes. You are given a binary string <code>boxes</code> of length <code>n</code>, where <code>boxes[i]</code> is <code>&#39;0&#39;</code> if the <code>i<sup>th</sup></code> box is <strong>empty</strong>, and <code>&#39;1&#39;</code> if it contains <strong>one</strong> ball.</p>

<p>In one operation, you can move <strong>one</strong> ball from a box to an adjacent box. Box <code>i</code> is adjacent to box <code>j</code> if <code>abs(i - j) == 1</code>. Note that after doing so, there may be more than one ball in some boxes.</p>

<p>Return an array <code>answer</code> of size <code>n</code>, where <code>answer[i]</code> is the <strong>minimum</strong> number of operations needed to move all the balls to the <code>i<sup>th</sup></code> box.</p>

<p>Each <code>answer[i]</code> is calculated considering the <strong>initial</strong> state of the boxes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;110&quot;
<strong>Output:</strong> [1,1,3]
<strong>Explanation:</strong> The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;001011&quot;
<strong>Output:</strong> [11,8,5,4,3,4]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == boxes.length</code></li>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>boxes[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sums

<!-- thinking:start -->

> **Thinking**
>
> The cost of gathering every ball at box $i$ is the sum of index distances. $n\le 2000$ allows a double loop, but a linear recurrence exists.
>
> The left (right) cost follows from the neighbour: one more ball on that side increases the cost by the ball count. Precompute $left[i]$ and $right[i]$ and add them.

<!-- thinking:end -->

Precompute $\textit{left}[i]$ as the cost of moving all balls on the left of $i$ to position $i$, and $\textit{right}[i]$ as the cost of moving all balls on the right of $i$ to position $i$. The answer at $i$ is $\textit{left}[i] + \textit{right}[i]$.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of $\textit{boxes}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left = [0] * n
        right = [0] * n
        cnt = 0
        for i in range(1, n):
            if boxes[i - 1] == '1':
                cnt += 1
            left[i] = left[i - 1] + cnt
        cnt = 0
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                cnt += 1
            right[i] = right[i + 1] + cnt
        return [a + b for a, b in zip(left, right)]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Prefix Sums (Space Optimization)

<!-- thinking:start -->

> **Thinking**
>
> The two arrays in Solution 1 depend only on the previous cell. Accumulate the same recurrences into $ans$ left-to-right and right-to-left, using constant extra space.

<!-- thinking:end -->

$\textit{left}[i]$ and $\textit{right}[i]$ in Solution 1 depend only on the previous position, so we can drop those arrays and accumulate into $\textit{ans}$ with one left-to-right pass and one right-to-left pass.

The time complexity is $O(n)$. Ignoring the answer array, the extra space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        cnt = 0
        for i in range(1, n):
            if boxes[i - 1] == '1':
                cnt += 1
            ans[i] = ans[i - 1] + cnt
        cnt = s = 0
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                cnt += 1
            s += cnt
            ans[i] += s
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Enumeration

<!-- thinking:start -->

> **Thinking**
>
> A direct implementation stores every ball index and, for each box, sums $|i-j|$. It passes for this $n$, at a worse constant than the prefix recurrences.

<!-- thinking:end -->

Collect every ball position, then for each box $i$ add $|i - j|$ for every ball $j$.

The time complexity is $O(n \times m)$ and the space complexity is $O(m)$, where $n$ is the length of $\textit{boxes}$ and $m$ is the number of balls.

<!-- solution:end -->

<!-- problem:end -->
