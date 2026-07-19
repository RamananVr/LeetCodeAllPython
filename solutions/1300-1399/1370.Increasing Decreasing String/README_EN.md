---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1370.Increasing%20Decreasing%20String/README_EN.md
rating: 1369
source: Biweekly Contest 21 Q1
tags:
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [1370. Increasing Decreasing String](https://leetcode.com/problems/increasing-decreasing-string)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code>. Reorder the string using the following algorithm:</p>

<ol>
	<li>Remove the <strong>smallest</strong> character from <code>s</code> and <strong>append</strong> it to the result.</li>
	<li>Remove the <strong>smallest</strong> character from <code>s</code> that is greater than the last appended character, and <strong>append</strong> it to the result.</li>
	<li>Repeat step 2 until no more characters can be removed.</li>
	<li>Remove the <strong>largest</strong> character from <code>s</code> and <strong>append</strong> it to the result.</li>
	<li>Remove the <strong>largest</strong> character from <code>s</code> that is smaller than the last appended character, and <strong>append</strong> it to the result.</li>
	<li>Repeat step 5 until no more characters can be removed.</li>
	<li>Repeat steps 1 through 6 until all characters from <code>s</code> have been removed.</li>
</ol>

<p>If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.</p>

<p>Return the resulting string after reordering <code>s</code> using this algorithm.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaaabbbbcccc&quot;
<strong>Output:</strong> &quot;abccbaabccba&quot;
<strong>Explanation:</strong> After steps 1, 2 and 3 of the first iteration, result = &quot;abc&quot;
After steps 4, 5 and 6 of the first iteration, result = &quot;abccba&quot;
First iteration is done. Now s = &quot;aabbcc&quot; and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = &quot;abccbaabc&quot;
After steps 4, 5 and 6 of the second iteration, result = &quot;abccbaabccba&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;rat&quot;
<strong>Output:</strong> &quot;art&quot;
<strong>Explanation:</strong> The word &quot;rat&quot; becomes &quot;art&quot; after re-ordering it with the mentioned algorithm.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting + Simulation

First, we use a hash table or an array $cnt$ of length $26$ to count the number of occurrences of each character in the string $s$.

Then, we enumerate the letters $[a,...,z]$. For the current enumerated letter $c$, if $cnt[c] > 0$, we append the letter $c$ to the end of the answer string and decrease $cnt[c]$ by one. We repeat this step until $cnt[c] = 0$. Then we enumerate the letters $[z,...,a]$ in reverse order and perform similar operations. If the length of the answer string equals the length of $s$, then we have completed all the concatenation operations.

The time complexity is $O(n \times |\Sigma|)$, and the space complexity is $O(|\Sigma|)$. Where $n$ is the length of the string $s$, and $\Sigma$ is the character set. In this problem, the character set is all lowercase letters, so $|\Sigma| = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sortString(self, s: str) -> str:
        cnt = Counter(s)
        cs = ascii_lowercase + ascii_lowercase[::-1]
        ans = []
        while len(ans) < len(s):
            for c in cs:
                if cnt[c]:
                    ans.append(c)
                    cnt[c] -= 1
        return "".join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
