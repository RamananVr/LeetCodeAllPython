---
comments: true
difficulty: Medium
tags:
    - String
    - Backtracking
---

<!-- problem:start -->

# [306. Additive Number](https://leetcode.com/problems/additive-number)

## Description

<!-- description:start -->

<p>An <strong>additive number</strong> is a string whose digits can form an <strong>additive sequence</strong>.</p>

<p>A valid <strong>additive sequence</strong> should contain <strong>at least</strong> three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</p>

<p>Given a string containing only digits, return <code>true</code> if it is an <strong>additive number</strong> or <code>false</code> otherwise.</p>

<p><strong>Note:</strong> Numbers in the additive sequence <strong>cannot</strong> have leading zeros, so sequence <code>1, 2, 03</code> or <code>1, 02, 3</code> is invalid.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;112358&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;199100199&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> 
The additive sequence is: 1, 99, 100, 199.&nbsp;
1 + 99 = 100, 99 + 100 = 199
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 35</code></li>
	<li><code>num</code> consists only of digits.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> How would you handle overflow for very large input integers?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> An additive number concatenates at least three numbers, each after the second being the sum of the previous two. Once the first two addends are fixed, the rest of the string is determined.
>
> Enumerate the split points of the first two numbers, skip leading zeros, and recursively check that each remaining prefix equals their sum. On a match, roll the pair forward; success means the string is consumed. The length bound keeps the enumeration feasible.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(a, b, num):
            if not num:
                return True
            if a + b > 0 and num[0] == '0':
                return False
            for i in range(1, len(num) + 1):
                if a + b == int(num[:i]):
                    if dfs(b, a + b, num[i:]):
                        return True
            return False

        n = len(num)
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if i > 1 and num[0] == '0':
                    break
                if j - i > 1 and num[i] == '0':
                    continue
                if dfs(int(num[:i]), int(num[i:j]), num[j:]):
                    return True
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
