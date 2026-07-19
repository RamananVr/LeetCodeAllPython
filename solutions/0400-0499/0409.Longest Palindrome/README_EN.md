---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0409.Longest%20Palindrome/README_EN.md
tags:
    - Greedy
    - Hash Table
    - String
---

<!-- problem:start -->

# [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> which consists of lowercase or uppercase letters, return the length of the <strong>longest <span data-keyword="palindrome-string">palindrome</span></strong>&nbsp;that can be built with those letters.</p>

<p>Letters are <strong>case sensitive</strong>, for example, <code>&quot;Aa&quot;</code> is not considered a palindrome.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abccccdd&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> One longest palindrome that can be built is &quot;dccaccd&quot;, whose length is 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest palindrome that can be built is &quot;a&quot;, whose length is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase <strong>and/or</strong> uppercase English&nbsp;letters only.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

A valid palindrome string can have at most one character that appears an odd number of times, and the rest of the characters appear an even number of times.

Therefore, we can first traverse the string $s$, count the number of occurrences of each character, and record it in an array or hash table $cnt$.

Then, we traverse $cnt$, for each count $v$, we divide $v$ by 2, take the integer part, multiply by 2, and add it to the answer $ans$.

Finally, if the answer is less than the length of the string $s$, we increment the answer by one and return $ans$.

The time complexity is $O(n + |\Sigma|)$, and the space complexity is $O(|\Sigma|)$. Where $n$ is the length of the string $s$, and $|\Sigma|$ is the size of the character set. In this problem, $|\Sigma| = 128$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = sum(v // 2 * 2 for v in cnt.values())
        ans += int(ans < len(s))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Bit Manipulation + Counting

We can use an array or hash table $odd$ to record whether each character in string $s$ appears an odd number of times, and an integer variable $cnt$ to record the number of characters that appear an odd number of times.

We iterate through the string $s$. For each character $c$, we flip $odd[c]$, i.e., $0 \rightarrow 1$, $1 \rightarrow 0$. If $odd[c]$ changes from $0$ to $1$, then we increment $cnt$ by one; if $odd[c]$ changes from $1$ to $0$, then we decrement $cnt$ by one.

Finally, if $cnt$ is greater than $0$, the answer is $n - cnt + 1$, otherwise, the answer is $n$.

The time complexity is $O(n)$, and the space complexity is $O(|\Sigma|)$. Where $n$ is the length of the string $s$, and $|\Sigma|$ is the size of the character set. In this problem, $|\Sigma| = 128$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = defaultdict(int)
        cnt = 0
        for c in s:
            odd[c] ^= 1
            cnt += 1 if odd[c] else -1
        return len(s) - cnt + 1 if cnt else len(s)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
