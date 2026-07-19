---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3900-3999/3913.Sort%20Vowels%20by%20Frequency/README_EN.md
rating: 1524
source: Weekly Contest 499 Q2
---

<!-- problem:start -->

# [3913. Sort Vowels by Frequency](https://leetcode.com/problems/sort-vowels-by-frequency)

## Description

<!-- description:start -->

<p data-end="271" data-start="95">You are given a string <code>s</code> consisting of lowercase English characters.</p>

<p>Rearrange only the <strong>vowels</strong> in the string so that they appear in <strong>non-increasing</strong> order of their frequency.</p>

<p>If multiple vowels have the same <strong>frequency</strong>, order them by the position of their <strong>first occurrence</strong> in <code>s</code>.</p>

<p>Return the modified string.</p>

<p>Vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>.</p>

<p>The <strong>frequency</strong> of a letter is the number of times it occurs in the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leetcode&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;leetcedo&quot;</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>Vowels in the string are <code>[&#39;e&#39;, &#39;e&#39;, &#39;o&#39;, &#39;e&#39;]</code> with frequencies: <code>e = 3</code>, <code>o = 1</code>.</li>
	<li>Sorting in non-increasing order of frequency and placing them back into the vowel positions results in <code>&quot;leetcedo&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aeiaaioooa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;aaaaoooiie&quot;</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>Vowels in the string are <code>[&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;a&#39;, &#39;a&#39;, &#39;i&#39;, &#39;o&#39;, &#39;o&#39;, &#39;o&#39;, &#39;a&#39;]</code> with frequencies: <code>a = 4</code>, <code>o = 3</code>, <code>i = 2</code>, <code>e = 1</code>.</li>
	<li>Sorting them in non-increasing order of frequency and placing them back into the vowel positions results in <code>&quot;aaaaoooiie&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;baeiou&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;baeiou&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Each vowel appears exactly once, so all have the same frequency.</li>
	<li>Thus, they retain their relative order based on first occurrence, and the string remains unchanged.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting + Custom Sorting

We can use a hash table $\textit{cnt}$ to record the frequency of each vowel. We also need a list $\textit{vowels}$ to store the vowels that appear in the string, ordered by their first occurrence.

We then sort the $\textit{vowels}$ list with a custom comparator: vowels are sorted in non-increasing order of their frequency.

Finally, we traverse the string, replacing each vowel with the corresponding letter from the $\textit{vowels}$ list, and update the frequency in the hash table. When the frequency of a vowel becomes 0, we move the pointer in the $\textit{vowels}$ list forward by one.

The time complexity is $O(n + |\Sigma| \log |\Sigma|)$ and the space complexity is $O(n + |\Sigma|)$, where $n$ is the length of the string and $\Sigma$ is the set of vowels that appear in the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sortVowels(self, s: str) -> str:
        st = set("aeiou")
        vowels = []
        cnt = Counter()
        for c in s:
            if c not in st:
                continue
            if c not in cnt:
                vowels.append(c)
            cnt[c] += 1
        vowels.sort(key=lambda c: -cnt[c])
        ans = list(s)
        i = 0
        for k, c in enumerate(s):
            if c not in st:
                continue
            ans[k] = c = vowels[i]
            cnt[c] -= 1
            if cnt[c] == 0:
                i += 1
        return "".join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
