---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2300-2399/2315.Count%20Asterisks/README_EN.md
rating: 1250
source: Biweekly Contest 81 Q1
tags:
    - String
---

<!-- problem:start -->

# [2315. Count Asterisks](https://leetcode.com/problems/count-asterisks)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code>, where every <strong>two</strong> consecutive vertical bars <code>&#39;|&#39;</code> are grouped into a <strong>pair</strong>. In other words, the 1<sup>st</sup> and 2<sup>nd</sup> <code>&#39;|&#39;</code> make a pair, the 3<sup>rd</sup> and 4<sup>th</sup> <code>&#39;|&#39;</code> make a pair, and so forth.</p>

<p>Return <em>the number of </em><code>&#39;*&#39;</code><em> in </em><code>s</code><em>, <strong>excluding</strong> the </em><code>&#39;*&#39;</code><em> between each pair of </em><code>&#39;|&#39;</code>.</p>

<p><strong>Note</strong> that each <code>&#39;|&#39;</code> will belong to <strong>exactly</strong> one pair.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;l|*e*et|c**o|*de|&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The considered characters are underlined: &quot;<u>l</u>|*e*et|<u>c**o</u>|*de|&quot;.
The characters between the first and second &#39;|&#39; are excluded from the answer.
Also, the characters between the third and fourth &#39;|&#39; are excluded from the answer.
There are 2 asterisks considered. Therefore, we return 2.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;iamprogrammer&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this example, there are no asterisks in s. Therefore, we return 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;yo|uar|e**|b|e***au|tifu|l&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The considered characters are underlined: &quot;<u>yo</u>|uar|<u>e**</u>|b|<u>e***au</u>|tifu|<u>l</u>&quot;. There are 5 asterisks considered. Therefore, we return 5.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters, vertical bars <code>&#39;|&#39;</code>, and asterisks <code>&#39;*&#39;</code>.</li>
	<li><code>s</code> contains an <strong>even</strong> number of vertical bars <code>&#39;|&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We define an integer variable $\textit{ok}$ to indicate whether we can count when encountering `*`. Initially, $\textit{ok}=1$, meaning we can count.

Traverse the string $s$. If we encounter `*`, we decide whether to count based on the value of $\textit{ok}$. If we encounter `|`, we toggle the value of $\textit{ok}$.

Finally, return the count result.

The time complexity is $O(n)$, where $n$ is the length of the string $s$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countAsterisks(self, s: str) -> int:
        ans, ok = 0, 1
        for c in s:
            if c == "*":
                ans += ok
            elif c == "|":
                ok ^= 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
