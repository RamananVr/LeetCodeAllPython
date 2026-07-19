---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2953.Count%20Complete%20Substrings/README_EN.md
rating: 2449
source: Weekly Contest 374 Q3
tags:
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [2953. Count Complete Substrings](https://leetcode.com/problems/count-complete-substrings)

## Description

<!-- description:start -->

<p>You are given a string <code>word</code> and an integer <code>k</code>.</p>

<p>A substring <code>s</code> of <code>word</code> is <strong>complete</strong> if:</p>

<ul>
	<li>Each character in <code>s</code> occurs <strong>exactly</strong> <code>k</code> times.</li>
	<li>The difference between two adjacent characters is <strong>at most</strong> <code>2</code>. That is, for any two adjacent characters <code>c1</code> and <code>c2</code> in <code>s</code>, the absolute difference in their positions in the alphabet is <strong>at most</strong> <code>2</code>.</li>
</ul>

<p>Return <em>the number of <strong>complete </strong>substrings of</em> <code>word</code>.</p>

<p>A <strong>substring</strong> is a <strong>non-empty</strong> contiguous sequence of characters in a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;igigee&quot;, k = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The complete substrings where each character appears exactly twice and the difference between adjacent characters is at most 2 are: <u><strong>igig</strong></u>ee, igig<u><strong>ee</strong></u>, <u><strong>igigee</strong></u>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;aaabbbccc&quot;, k = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> The complete substrings where each character appears exactly three times and the difference between adjacent characters is at most 2 are: <strong><u>aaa</u></strong>bbbccc, aaa<u><strong>bbb</strong></u>ccc, aaabbb<u><strong>ccc</strong></u>, <strong><u>aaabbb</u></strong>ccc, aaa<u><strong>bbbccc</strong></u>, <u><strong>aaabbbccc</strong></u>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= word.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumerate Character Types + Sliding Window

According to condition 2 in the problem description, we can find that in a complete string, the difference between two adjacent characters does not exceed 2. Therefore, we traverse the string $word$, and we can use two pointers to split $word$ into several substrings. The number of character types in these substrings does not exceed 26, and the difference between adjacent characters does not exceed 2. Next, we only need to count the number of substrings in each substring where each character appears $k$ times.

We define a function $f(s)$, which is used to count the number of substrings in the string $s$ where each character appears $k$ times. Since the number of character types in $s$ does not exceed 26, we can enumerate each character type $i$, where $1 \le i \le 26$, then the length of the substring with character type $i$ is $l = i \times k$.

We can use an array or hash table $cnt$ to maintain the number of times each character appears in a sliding window of length $l$, and use another hash table $freq$ to maintain the number of times each frequency appears. If $freq[k] = i$, that is, there are $i$ characters that appear $k$ times, then we have found a substring that meets the conditions. We can use two pointers to maintain this sliding window. Each time we move the right pointer, we increase the number of times the character pointed to by the right pointer appears and update the $freq$ array; each time we move the left pointer, we decrease the number of times the character pointed to by the left pointer appears and update the $freq$ array. After each pointer movement, we judge whether $freq[k]$ is equal to $i$. If it is equal, it means that we have found a substring that meets the conditions.

The time complexity is $O(n \times |\Sigma|)$, and the space complexity is $O(|\Sigma|)$, where $n$ is the length of the string $word$; and $\Sigma$ is the size of the character set. In this problem, the character set is lowercase English letters, so $|\Sigma| = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def f(s: str) -> int:
            m = len(s)
            ans = 0
            for i in range(1, 27):
                l = i * k
                if l > m:
                    break
                cnt = Counter(s[:l])
                freq = Counter(cnt.values())
                ans += freq[k] == i
                for j in range(l, m):
                    freq[cnt[s[j]]] -= 1
                    cnt[s[j]] += 1
                    freq[cnt[s[j]]] += 1

                    freq[cnt[s[j - l]]] -= 1
                    cnt[s[j - l]] -= 1
                    freq[cnt[s[j - l]]] += 1

                    ans += freq[k] == i
            return ans

        n = len(word)
        ans = i = 0
        while i < n:
            j = i + 1
            while j < n and abs(ord(word[j]) - ord(word[j - 1])) <= 2:
                j += 1
            ans += f(word[i:j])
            i = j
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
