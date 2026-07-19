---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2300-2399/2380.Time%20Needed%20to%20Rearrange%20a%20Binary%20String/README_EN.md
rating: 1481
source: Biweekly Contest 85 Q2
tags:
    - String
    - Dynamic Programming
    - Simulation
---

<!-- problem:start -->

# [2380. Time Needed to Rearrange a Binary String](https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string)

## Description

<!-- description:start -->

<p>You are given a binary string <code>s</code>. In one second, <strong>all</strong> occurrences of <code>&quot;01&quot;</code> are <strong>simultaneously</strong> replaced with <code>&quot;10&quot;</code>. This process <strong>repeats</strong> until no occurrences of <code>&quot;01&quot;</code> exist.</p>

<p>Return<em> the number of seconds needed to complete this process.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0110101&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
After one second, s becomes &quot;1011010&quot;.
After another second, s becomes &quot;1101100&quot;.
After the third second, s becomes &quot;1110100&quot;.
After the fourth second, s becomes &quot;1111000&quot;.
No occurrence of &quot;01&quot; exists any longer, and the process needed 4 seconds to complete,
so we return 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;11100&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong>
No occurrence of &quot;01&quot; exists in s, and the processes needed 0 seconds to complete,
so we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<p>Can you solve this problem in O(n) time complexity?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        while s.count('01'):
            s = s.replace('01', '10')
            ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = cnt = 0
        for c in s:
            if c == '0':
                cnt += 1
            elif cnt:
                ans = max(ans + 1, cnt)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
