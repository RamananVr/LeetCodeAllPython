---
comments: true
difficulty: Easy
tags:
    - String
---

<!-- problem:start -->

# [434. Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <em>the number of segments in the string</em>.</p>

<p>A <strong>segment</strong> is defined to be a contiguous sequence of <strong>non-space characters</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;Hello, my name is John&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The five segments are [&quot;Hello,&quot;, &quot;my&quot;, &quot;name&quot;, &quot;is&quot;, &quot;John&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;Hello&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 300</code></li>
	<li><code>s</code> consists of lowercase and uppercase English letters, digits, or one of the following characters <code>&quot;!@#$%^&amp;*()_+-=&#39;,.:&quot;</code>.</li>
	<li>The only space character in <code>s</code> is <code>&#39; &#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: String Splitting

<!-- thinking:start -->

> **Thinking**
>
> Segments are blank-separated. A hand-written scan must handle leading, trailing, and repeated spaces. $\texttt{split}$ already drops empty pieces, so its length is the answer.
>
> The library walk is a fine first solution.

<!-- thinking:end -->

We split the string $\textit{s}$ by spaces and then count the number of non-empty words.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $\textit{s}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Simulation

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 allocates the list of words. Counting only, a new segment starts at a non-space whose previous character is a space (or the first index). Extra memory becomes $O(1)$.

<!-- thinking:end -->

We can also directly traverse each character $\text{s[i]}$ in the string. If $\text{s[i]}$ is not a space and $\text{s[i-1]}$ is a space or $i = 0$, then $\text{s[i]}$ marks the beginning of a new word, and we increment the answer by one.

After the traversal, we return the answer.

The time complexity is $O(n)$, where $n$ is the length of the string $\textit{s}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            if c != ' ' and (i == 0 or s[i - 1] == ' '):
                ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
