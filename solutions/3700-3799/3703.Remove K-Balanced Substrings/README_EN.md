---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3703.Remove%20K-Balanced%20Substrings/README_EN.md
rating: 1802
source: Weekly Contest 470 Q3
tags:
    - Stack
    - String
    - Simulation
---

<!-- problem:start -->

# [3703. Remove K-Balanced Substrings](https://leetcode.com/problems/remove-k-balanced-substrings)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> consisting of <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, and an integer <code>k</code>.</p>

<p>A <strong>string</strong> is <strong>k-balanced</strong> if it is <strong>exactly</strong> <code>k</code> <strong>consecutive</strong> <code>&#39;(&#39;</code> followed by <code>k</code> <strong>consecutive</strong> <code>&#39;)&#39;</code>, i.e., <code>&#39;(&#39; * k + &#39;)&#39; * k</code>.</p>

<p>For example, if <code>k = 3</code>, k-balanced is <code>&quot;((()))&quot;</code>.</p>

<p>You must <strong>repeatedly</strong> remove all <strong>non-overlapping k-balanced <span data-keyword="substring-nonempty">substrings</span></strong> from <code>s</code>, and then join the remaining parts. Continue this process until no k-balanced <strong>substring</strong> exists.</p>

<p>Return the final string after all possible removals.</p>

<p>&nbsp;</p>
<p>​​​​​​​<strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;(())&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>k-balanced substring is <code>&quot;()&quot;</code></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Step</th>
			<th style="border: 1px solid black;">Current <code>s</code></th>
			<th style="border: 1px solid black;"><code>k-balanced</code></th>
			<th style="border: 1px solid black;">Result <code>s</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>(())</code></td>
			<td style="border: 1px solid black;"><code>(<s><strong>()</strong></s>)</code></td>
			<td style="border: 1px solid black;"><code>()</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>()</code></td>
			<td style="border: 1px solid black;"><s><strong><code>()</code></strong></s></td>
			<td style="border: 1px solid black;">Empty</td>
		</tr>
	</tbody>
</table>

<p>Thus, the final string is <code>&quot;&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;(()(&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;((&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>k-balanced substring is <code>&quot;()&quot;</code></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Step</th>
			<th style="border: 1px solid black;">Current <code>s</code></th>
			<th style="border: 1px solid black;"><code>k-balanced</code></th>
			<th style="border: 1px solid black;">Result <code>s</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>(()(</code></td>
			<td style="border: 1px solid black;"><code>(<s><strong>()</strong></s>(</code></td>
			<td style="border: 1px solid black;"><code>((</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>((</code></td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;"><code>((</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the final string is <code>&quot;((&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;((()))()()()&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;()()()&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>k-balanced substring is <code>&quot;((()))&quot;</code></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Step</th>
			<th style="border: 1px solid black;">Current <code>s</code></th>
			<th style="border: 1px solid black;"><code>k-balanced</code></th>
			<th style="border: 1px solid black;">Result <code>s</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>((()))()()()</code></td>
			<td style="border: 1px solid black;"><code><s><strong>((()))</strong></s>()()()</code></td>
			<td style="border: 1px solid black;"><code>()()()</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>()()()</code></td>
			<td style="border: 1px solid black;">-</td>
			<td style="border: 1px solid black;"><code>()()()</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the final string is <code>&quot;()()()&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>.</li>
	<li><code>1 &lt;= k &lt;= s.length / 2</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack

We use a stack to maintain the current state of the string. Each element in the stack is a pair representing a character and its consecutive count.

Traverse each character in the string:

- If the stack is not empty and the character of the top element matches the current character, increment the count of the top element.
- Otherwise, push the current character with count 1 as a new element onto the stack.
- If the current character is `')'`, and there are at least two elements in the stack, and the count of the top element equals $k$, and the count of the previous element is greater than or equal to $k$, then pop the top element and subtract $k$ from the count of the previous element. If the count of the previous element becomes 0, pop it as well.

After traversal, the remaining elements in the stack represent the final state of the string. We concatenate these elements in order to get the result string.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
            if c == ")" and len(stk) > 1 and stk[-1][1] == k and stk[-2][1] >= k:
                stk.pop()
                stk[-1][1] -= k
                if stk[-1][1] == 0:
                    stk.pop()
        return "".join(c * v for c, v in stk)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
