---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1106.Parsing%20A%20Boolean%20Expression/README_EN.md
rating: 1880
source: Weekly Contest 143 Q4
tags:
    - Stack
    - Recursion
    - String
---

<!-- problem:start -->

# [1106. Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression)

## Description

<!-- description:start -->

<p>A <strong>boolean expression</strong> is an expression that evaluates to either <code>true</code> or <code>false</code>. It can be in one of the following shapes:</p>

<ul>
	<li><code>&#39;t&#39;</code> that evaluates to <code>true</code>.</li>
	<li><code>&#39;f&#39;</code> that evaluates to <code>false</code>.</li>
	<li><code>&#39;!(subExpr)&#39;</code> that evaluates to <strong>the logical NOT</strong> of the inner expression <code>subExpr</code>.</li>
	<li><code>&#39;&amp;(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)&#39;</code> that evaluates to <strong>the logical AND</strong> of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where <code>n &gt;= 1</code>.</li>
	<li><code>&#39;|(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)&#39;</code> that evaluates to <strong>the logical OR</strong> of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where <code>n &gt;= 1</code>.</li>
</ul>

<p>Given a string <code>expression</code> that represents a <strong>boolean expression</strong>, return <em>the evaluation of that expression</em>.</p>

<p>It is <strong>guaranteed</strong> that the given expression is valid and follows the given rules.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;&amp;(|(f))&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> 
First, evaluate |(f) --&gt; f. The expression is now &quot;&amp;(f)&quot;.
Then, evaluate &amp;(f) --&gt; f. The expression is now &quot;f&quot;.
Finally, return false.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;|(f,f,f,t)&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The evaluation of (false OR false OR false OR true) is true.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;!(&amp;(f,t))&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> 
First, evaluate &amp;(f,t) --&gt; (false AND true) --&gt; false --&gt; f. The expression is now &quot;!(f)&quot;.
Then, evaluate !(f) --&gt; NOT false --&gt; true. We return true.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li>expression[i] is one following characters: <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;&amp;&#39;</code>, <code>&#39;|&#39;</code>, <code>&#39;!&#39;</code>, <code>&#39;t&#39;</code>, <code>&#39;f&#39;</code>, and <code>&#39;,&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack

For this type of expression parsing problem, we can use a stack to assist.

We traverse the expression `expression` from left to right. For each character $c$ we encounter:

- If $c$ is one of `"tf!&|"`, we push it directly onto the stack;
- If $c$ is a right parenthesis `')'`, we pop elements from the stack until we encounter an operator `'!'`, `'&'`, or `'|'`. During this process, we use variables $t$ and $f$ to record the number of `'t'` and `'f'` characters popped from the stack. Finally, based on the number of characters popped and the operator, we calculate a new character `'t'` or `'f'` and push it onto the stack.

After traversing the expression `expression`, there is only one character left in the stack. If it is `'t'`, return `true`, otherwise return `false`.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the expression `expression`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in 'tf!&|':
                stk.append(c)
            elif c == ')':
                t = f = 0
                while stk[-1] in 'tf':
                    t += stk[-1] == 't'
                    f += stk[-1] == 'f'
                    stk.pop()
                match stk.pop():
                    case '!':
                        c = 't' if f else 'f'
                    case '&':
                        c = 'f' if f else 't'
                    case '|':
                        c = 't' if t else 'f'
                stk.append(c)
        return stk[0] == 't'
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
