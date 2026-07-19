---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1324.Print%20Words%20Vertically/README_EN.md
rating: 1328
source: Weekly Contest 172 Q2
tags:
    - Array
    - String
    - Simulation
---

<!-- problem:start -->

# [1324. Print Words Vertically](https://leetcode.com/problems/print-words-vertically)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>.&nbsp;Return&nbsp;all the words vertically in the same order in which they appear in <code>s</code>.<br />

Words are returned as a list of strings, complete with&nbsp;spaces when is necessary. (Trailing spaces are not allowed).<br />

Each word would be put on only one column and that in one column there will be only one word.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>

<strong>Input:</strong> s = &quot;HOW ARE YOU&quot;

<strong>Output:</strong> [&quot;HAY&quot;,&quot;ORO&quot;,&quot;WEU&quot;]

<strong>Explanation: </strong>Each word is printed vertically. 

 &quot;HAY&quot;

&nbsp;&quot;ORO&quot;

&nbsp;&quot;WEU&quot;

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>

<strong>Input:</strong> s = &quot;TO BE OR NOT TO BE&quot;

<strong>Output:</strong> [&quot;TBONTB&quot;,&quot;OEROOE&quot;,&quot;   T&quot;]

<strong>Explanation: </strong>Trailing spaces is not allowed. 

&quot;TBONTB&quot;

&quot;OEROOE&quot;

&quot;   T&quot;

</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>

<strong>Input:</strong> s = &quot;CONTEST IS COMING&quot;

<strong>Output:</strong> [&quot;CIC&quot;,&quot;OSO&quot;,&quot;N M&quot;,&quot;T I&quot;,&quot;E N&quot;,&quot;S G&quot;,&quot;T&quot;]

</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>1 &lt;= s.length &lt;= 200</code></li>

    <li><code>s</code>&nbsp;contains only upper case English letters.</li>

    <li>It&#39;s guaranteed that there is only one&nbsp;space between 2 words.</li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max(len(w) for w in words)
        ans = []
        for j in range(n):
            t = [w[j] if j < len(w) else ' ' for w in words]
            while t[-1] == ' ':
                t.pop()
            ans.append(''.join(t))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
