---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2810.Faulty%20Keyboard/README_EN.md
rating: 1192
source: Weekly Contest 357 Q1
tags:
    - String
    - Simulation
---

<!-- problem:start -->

# [2810. Faulty Keyboard](https://leetcode.com/problems/faulty-keyboard)

## Description

<!-- description:start -->

<p>Your laptop keyboard is faulty, and whenever you type a character <code>&#39;i&#39;</code> on it, it reverses the string that you have written. Typing other characters works as expected.</p>

<p>You are given a <strong>0-indexed</strong> string <code>s</code>, and you type each character of <code>s</code> using your faulty keyboard.</p>

<p>Return <em>the final string that will be present on your laptop screen.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;string&quot;
<strong>Output:</strong> &quot;rtsng&quot;
<strong>Explanation:</strong> 
After typing first character, the text on the screen is &quot;s&quot;.
After the second character, the text is &quot;st&quot;. 
After the third character, the text is &quot;str&quot;.
Since the fourth character is an &#39;i&#39;, the text gets reversed and becomes &quot;rts&quot;.
After the fifth character, the text is &quot;rtsn&quot;. 
After the sixth character, the text is &quot;rtsng&quot;. 
Therefore, we return &quot;rtsng&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;poiinter&quot;
<strong>Output:</strong> &quot;ponter&quot;
<strong>Explanation:</strong> 
After the first character, the text on the screen is &quot;p&quot;.
After the second character, the text is &quot;po&quot;. 
Since the third character you type is an &#39;i&#39;, the text gets reversed and becomes &quot;op&quot;. 
Since the fourth character you type is an &#39;i&#39;, the text gets reversed and becomes &quot;po&quot;.
After the fifth character, the text is &quot;pon&quot;.
After the sixth character, the text is &quot;pont&quot;. 
After the seventh character, the text is &quot;ponte&quot;. 
After the eighth character, the text is &quot;ponter&quot;. 
Therefore, we return &quot;ponter&quot;.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>s[0] != &#39;i&#39;</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We directly simulate the keyboard input process, using a character array $t$ to record the text on the screen, initially $t$ is empty.

For each character $c$ in string $s$, if $c$ is not the character $'i'$, then we add $c$ to the end of $t$; otherwise, we reverse all characters in $t$.

The final answer is the string composed of characters in $t$.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the length of string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def finalString(self, s: str) -> str:
        t = []
        for c in s:
            if c == "i":
                t = t[::-1]
            else:
                t.append(c)
        return "".join(t)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
