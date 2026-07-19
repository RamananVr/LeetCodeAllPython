---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0925.Long%20Pressed%20Name/README_EN.md
tags:
    - Two Pointers
    - String
---

<!-- problem:start -->

# [925. Long Pressed Name](https://leetcode.com/problems/long-pressed-name)

## Description

<!-- description:start -->

<p>Your friend is typing his <code>name</code> into a keyboard. Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>

<p>You examine the <code>typed</code> characters of the keyboard. Return <code>True</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> name = &quot;alex&quot;, typed = &quot;aaleex&quot;
<strong>Output:</strong> true
<strong>Explanation: </strong>&#39;a&#39; and &#39;e&#39; in &#39;alex&#39; were long pressed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> name = &quot;saeed&quot;, typed = &quot;ssaaedd&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>&#39;e&#39; must have been pressed twice, but it was not in the typed output.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= name.length, typed.length &lt;= 1000</code></li>
	<li><code>name</code> and <code>typed</code> consist of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use two pointers $i$ and $j$ to point to the first character of the strings `typed` and `name` respectively, and then start traversing. If `typed[j]` is not equal to `name[i]`, it means the two strings do not match, and we directly return `False`. Otherwise, we find the next position of the continuous identical characters, denoted as $x$ and $y$ respectively. If $x - i > y - j$, it means the number of characters in `typed` is less than the number of characters in `name`, and we directly return `False`. Otherwise, we update $i$ and $j$ to $x$ and $y$ respectively, continue traversing, until $i$ and $j$ have traversed `name` and `typed` respectively, and return `True`.

The time complexity is $O(m + n)$, where $m$ and $n$ are the lengths of the strings `name` and `typed` respectively. The space complexity is $O(1)`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        i = j = 0
        while i < m and j < n:
            if name[i] != typed[j]:
                return False
            x = i + 1
            while x < m and name[x] == name[i]:
                x += 1
            y = j + 1
            while y < n and typed[y] == typed[j]:
                y += 1
            if x - i > y - j:
                return False
            i, j = x, y
        return i == m and j == n
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
