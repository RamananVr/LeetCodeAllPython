---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0466.Count%20The%20Repetitions/README_EN.md
tags:
    - Two Pointers
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [466. Count The Repetitions](https://leetcode.com/problems/count-the-repetitions)

## Description

<!-- description:start -->

<p>We define <code>str = [s, n]</code> as the string <code>str</code> which consists of the string <code>s</code> concatenated <code>n</code> times.</p>

<ul>
	<li>For example, <code>str == [&quot;abc&quot;, 3] ==&quot;abcabcabc&quot;</code>.</li>
</ul>

<p>We define that string <code>s1</code> can be obtained from string <code>s2</code> if we can remove some characters from <code>s2</code> such that it becomes <code>s1</code>.</p>

<ul>
	<li>For example, <code>s1 = &quot;abc&quot;</code> can be obtained from <code>s2 = &quot;ab<strong><u>dbe</u></strong>c&quot;</code> based on our definition by removing the bolded underlined characters.</li>
</ul>

<p>You are given two strings <code>s1</code> and <code>s2</code> and two integers <code>n1</code> and <code>n2</code>. You have the two strings <code>str1 = [s1, n1]</code> and <code>str2 = [s2, n2]</code>.</p>

<p>Return <em>the maximum integer </em><code>m</code><em> such that </em><code>str = [str2, m]</code><em> can be obtained from </em><code>str1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
<strong>Output:</strong> 1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
	<li><code>1 &lt;= n1, n2 &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Iteration

We preprocess the string $s_2$ such that for each starting position $i$, we calculate the next position $j$ and the count of $s_2$ after matching a complete $s_1$, i.e., $d[i] = (cnt, j)$, where $cnt$ represents the count of $s_2$, and $j$ represents the next position in the string $s_2$.

Next, we initialize $j=0$, and then loop $n1$ times. Each time, we add $d[j][0]$ to the answer, and then update $j=d[j][1]$.

The final answer is the count of $s_2$ that can be matched by $n1$ $s_1$, divided by $n2$.

The time complexity is $O(m \times n + n_1)$, and the space complexity is $O(n)$. Where $m$ and $n$ are the lengths of $s_1$ and $s_2$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        n = len(s2)
        d = {}
        for i in range(n):
            cnt = 0
            j = i
            for c in s1:
                if c == s2[j]:
                    j += 1
                if j == n:
                    cnt += 1
                    j = 0
            d[i] = (cnt, j)

        ans = 0
        j = 0
        for _ in range(n1):
            cnt, j = d[j]
            ans += cnt
        return ans // n2
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
