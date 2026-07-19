---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0567.Permutation%20in%20String/README_EN.md
tags:
    - Hash Table
    - Two Pointers
    - String
    - Sliding Window
---

<!-- problem:start -->

# [567. Permutation in String](https://leetcode.com/problems/permutation-in-string)

## Description

<!-- description:start -->

<p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code> if <code>s2</code> contains a <span data-keyword="permutation-string">permutation</span> of <code>s1</code>, or <code>false</code> otherwise.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>&#39;s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidbaooo&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidboaoo&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sliding Window

We use an array $\textit{cnt}$ to record the characters and their counts that need to be matched, and a variable $\textit{need}$ to record the number of different characters that still need to be matched. Initially, $\textit{cnt}$ contains the character counts from the string $\textit{s1}$, and $\textit{need}$ is the number of different characters in $\textit{s1}$.

Then we traverse the string $\textit{s2}$. For each character, we decrement its corresponding value in $\textit{cnt}$. If the decremented value equals $0$, it means the current character's count in $\textit{s1}$ is satisfied, and we decrement $\textit{need}$. If the current index $i$ is greater than or equal to the length of $\textit{s1}$, we need to increment the corresponding value in $\textit{cnt}$ for $\textit{s2}[i-\textit{s1}]$. If the incremented value equals $1$, it means the current character's count in $\textit{s1}$ is no longer satisfied, and we increment $\textit{need}$. During the traversal, if the value of $\textit{need}$ equals $0$, it means all character counts are satisfied, and we have found a valid substring, so we return $\text{true}$.

Otherwise, if the traversal ends without finding a valid substring, we return $\text{false}$.

The time complexity is $O(m + n)$, where $m$ and $n$ are the lengths of strings $\textit{s1}$ and $\textit{s2}$, respectively. The space complexity is $O(|\Sigma|)$, where $\Sigma$ is the character set. In this problem, the character set is lowercase letters, so the space complexity is constant.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        need = len(cnt)
        m = len(s1)
        for i, c in enumerate(s2):
            cnt[c] -= 1
            if cnt[c] == 0:
                need -= 1
            if i >= m:
                cnt[s2[i - m]] += 1
                if cnt[s2[i - m]] == 1:
                    need += 1
            if need == 0:
                return True
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
