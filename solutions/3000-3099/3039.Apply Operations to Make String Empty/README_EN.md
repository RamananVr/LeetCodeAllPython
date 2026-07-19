---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3000-3099/3039.Apply%20Operations%20to%20Make%20String%20Empty/README_EN.md
rating: 1423
source: Biweekly Contest 124 Q2
tags:
    - Array
    - Hash Table
    - Counting
    - Sorting
---

<!-- problem:start -->

# [3039. Apply Operations to Make String Empty](https://leetcode.com/problems/apply-operations-to-make-string-empty)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code>.</p>

<p>Consider performing the following operation until <code>s</code> becomes <strong>empty</strong>:</p>

<ul>
	<li>For <strong>every</strong> alphabet character from <code>&#39;a&#39;</code> to <code>&#39;z&#39;</code>, remove the <strong>first</strong> occurrence of that character in <code>s</code> (if it exists).</li>
</ul>

<p>For example, let initially <code>s = &quot;aabcbbca&quot;</code>. We do the following operations:</p>

<ul>
	<li>Remove the underlined characters <code>s = &quot;<u><strong>a</strong></u>a<strong><u>bc</u></strong>bbca&quot;</code>. The resulting string is <code>s = &quot;abbca&quot;</code>.</li>
	<li>Remove the underlined characters <code>s = &quot;<u><strong>ab</strong></u>b<u><strong>c</strong></u>a&quot;</code>. The resulting string is <code>s = &quot;ba&quot;</code>.</li>
	<li>Remove the underlined characters <code>s = &quot;<u><strong>ba</strong></u>&quot;</code>. The resulting string is <code>s = &quot;&quot;</code>.</li>
</ul>

<p>Return <em>the value of the string </em><code>s</code><em> right <strong>before</strong> applying the <strong>last</strong> operation</em>. In the example above, answer is <code>&quot;ba&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabcbbca&quot;
<strong>Output:</strong> &quot;ba&quot;
<strong>Explanation:</strong> Explained in the statement.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;
<strong>Output:</strong> &quot;abcd&quot;
<strong>Explanation:</strong> We do the following operation:
- Remove the underlined characters s = &quot;<u><strong>abcd</strong></u>&quot;. The resulting string is s = &quot;&quot;.
The string just before the last operation is &quot;abcd&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table or Array

We use a hash table or array $cnt$ to record the occurrence times of each character in string $s$, and use another hash table or array $last$ to record the last occurrence position of each character in string $s$. The maximum occurrence times of characters in string $s$ is denoted as $mx$.

Then we traverse the string $s$. If the occurrence times of the current character equals $mx$ and the position of the current character equals the last occurrence position of this character, then we add the current character to the answer.

After the traversal, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(|\Sigma|)$, where $n$ is the length of string $s$, and $\Sigma$ is the character set. In this problem, $\Sigma$ is the set of lowercase English letters.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        mx = cnt.most_common(1)[0][1]
        last = {c: i for i, c in enumerate(s)}
        return "".join(c for i, c in enumerate(s) if cnt[c] == mx and last[c] == i)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
