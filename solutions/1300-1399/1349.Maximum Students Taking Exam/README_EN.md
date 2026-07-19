---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1349.Maximum%20Students%20Taking%20Exam/README_EN.md
rating: 2385
source: Weekly Contest 175 Q4
tags:
    - Bit Manipulation
    - Array
    - Dynamic Programming
    - Bitmask
    - Matrix
---

<!-- problem:start -->

# [1349. Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam)

## Description

<!-- description:start -->

<p>Given a <code>m&nbsp;* n</code>&nbsp;matrix <code>seats</code>&nbsp;&nbsp;that represent seats distributions&nbsp;in a classroom.&nbsp;If a seat&nbsp;is&nbsp;broken, it is denoted by <code>&#39;#&#39;</code> character otherwise it is denoted by a <code>&#39;.&#39;</code> character.</p>

<p>Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting&nbsp;directly in front or behind him. Return the <strong>maximum </strong>number of students that can take the exam together&nbsp;without any cheating being possible.</p>

<p>Students must be placed in seats in good condition.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img height="200" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1349.Maximum%20Students%20Taking%20Exam/images/image.png" width="339" />
<pre>
<strong>Input:</strong> seats = [[&quot;#&quot;,&quot;.&quot;,&quot;#&quot;,&quot;#&quot;,&quot;.&quot;,&quot;#&quot;],
&nbsp;               [&quot;.&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;.&quot;],
&nbsp;               [&quot;#&quot;,&quot;.&quot;,&quot;#&quot;,&quot;#&quot;,&quot;.&quot;,&quot;#&quot;]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Teacher can place 4 students in available seats so they don&#39;t cheat on the exam. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> seats = [[&quot;.&quot;,&quot;#&quot;],
&nbsp;               [&quot;#&quot;,&quot;#&quot;],
&nbsp;               [&quot;#&quot;,&quot;.&quot;],
&nbsp;               [&quot;#&quot;,&quot;#&quot;],
&nbsp;               [&quot;.&quot;,&quot;#&quot;]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Place all students in available seats. 

</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> seats = [[&quot;#&quot;,&quot;.&quot;,&quot;<strong>.</strong>&quot;,&quot;.&quot;,&quot;#&quot;],
&nbsp;               [&quot;<strong>.</strong>&quot;,&quot;#&quot;,&quot;<strong>.</strong>&quot;,&quot;#&quot;,&quot;<strong>.</strong>&quot;],
&nbsp;               [&quot;<strong>.</strong>&quot;,&quot;.&quot;,&quot;#&quot;,&quot;.&quot;,&quot;<strong>.</strong>&quot;],
&nbsp;               [&quot;<strong>.</strong>&quot;,&quot;#&quot;,&quot;<strong>.</strong>&quot;,&quot;#&quot;,&quot;<strong>.</strong>&quot;],
&nbsp;               [&quot;#&quot;,&quot;.&quot;,&quot;<strong>.</strong>&quot;,&quot;.&quot;,&quot;#&quot;]]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Place students in available seats in column 1, 3 and 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>seats</code>&nbsp;contains only characters&nbsp;<code>&#39;.&#39;<font face="sans-serif, Arial, Verdana, Trebuchet MS">&nbsp;and</font></code><code>&#39;#&#39;.</code></li>
	<li><code>m ==&nbsp;seats.length</code></li>
	<li><code>n ==&nbsp;seats[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 8</code></li>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: State Compression + Memoization Search

We notice that each seat has two states: selectable and non-selectable. Therefore, we can use a binary number to represent the seat state of each row, where $1$ represents selectable, and $0$ represents non-selectable. For example, for the first row in Example 1, we can represent it as $010010$. Therefore, we convert the initial seats into a one-dimensional array $ss$, where $ss[i]$ represents the seat state of the $i$th row.

Next, we design a function $dfs(seat, i)$, which represents the maximum number of students that can be accommodated starting from the $i$th row, and the seat state of the current row is $seat$.

We can enumerate all the seat selection states $mask$ of the $i$th row, and judge whether $mask$ meets the following conditions:

- The state $mask$ cannot select seats outside of $seat$;
- The state $mask$ cannot select adjacent seats.

If the conditions are met, we calculate the number of seats selected in the current row $cnt$. If it is the last row, update the return value of the function, that is, $ans = \max(ans, cnt)$. Otherwise, we continue to recursively solve the maximum number of the next row. The seat state of the next row is $nxt = ss[i + 1]$, and we need to exclude the left and right sides of the selected seats in the current row. Then we recursively solve the maximum number of the next row, that is, $ans = \max(ans, cnt + dfs(nxt, i + 1))$.

Finally, we return $ans$ as the return value of the function.

To avoid repeated calculations, we can use memoization search to save the return value of the function $dfs(seat, i)$ in a two-dimensional array $f$, where $f[seat][i]$ represents the maximum number of students that can be accommodated starting from the $i$th row, and the seat state of the current row is $seat$.

The time complexity is $O(4^n \times n \times m)$, and the space complexity is $O(2^n \times m)$. Where $m$ and $n$ are the number of rows and columns of the seats, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        def f(seat: List[str]) -> int:
            mask = 0
            for i, c in enumerate(seat):
                if c == '.':
                    mask |= 1 << i
            return mask

        @cache
        def dfs(seat: int, i: int) -> int:
            ans = 0
            for mask in range(1 << n):
                if (seat | mask) != seat or (mask & (mask << 1)):
                    continue
                cnt = mask.bit_count()
                if i == len(ss) - 1:
                    ans = max(ans, cnt)
                else:
                    nxt = ss[i + 1]
                    nxt &= ~(mask << 1)
                    nxt &= ~(mask >> 1)
                    ans = max(ans, cnt + dfs(nxt, i + 1))
            return ans

        n = len(seats[0])
        ss = [f(s) for s in seats]
        return dfs(ss[0], 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
