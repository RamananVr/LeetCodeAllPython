---
comments: true
difficulty: Hard
tags:
    - Breadth-First Search
    - String
    - Backtracking
---

<!-- problem:start -->

# [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.</p>

<p>Return <em>a list of <strong>unique strings</strong> that are valid with the minimum number of removals</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()())()&quot;
<strong>Output:</strong> [&quot;(())()&quot;,&quot;()()()&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(a)())()&quot;
<strong>Output:</strong> [&quot;(a())()&quot;,&quot;(a)()()&quot;]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)(&quot;
<strong>Output:</strong> [&quot;&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 25</code></li>
	<li><code>s</code> consists of lowercase English letters and parentheses <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>.</li>
	<li>There will be at most <code>20</code> parentheses in <code>s</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> We must delete as few parentheses as possible and list every optimal string. Choosing delete-or-keep at each parenthesis branches too widely, and most paths are not minimal.
>
> A scan first yields lower bounds $l$ and $r$ on deletions. The search tracks remaining quotas and the current left/right counts; prune when leftover characters cannot finish the deletions or a prefix has more right parentheses than left. Try deleting (if quota remains) then keeping, and deduplicate with a set. Only paths that delete exactly the minimum survive.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(i, l, r, lcnt, rcnt, t):
            if i == n:
                if l == 0 and r == 0:
                    ans.add(t)
                return
            if n - i < l + r or lcnt < rcnt:
                return
            if s[i] == '(' and l:
                dfs(i + 1, l - 1, r, lcnt, rcnt, t)
            elif s[i] == ')' and r:
                dfs(i + 1, l, r - 1, lcnt, rcnt, t)
            dfs(i + 1, l, r, lcnt + (s[i] == '('), rcnt + (s[i] == ')'), t + s[i])

        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1
        ans = set()
        n = len(s)
        dfs(0, l, r, 0, 0, '')
        return list(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
