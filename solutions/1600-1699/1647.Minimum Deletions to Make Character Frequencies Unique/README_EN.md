---
comments: true
difficulty: Medium
rating: 1509
source: Weekly Contest 214 Q2
tags:
    - Greedy
    - Hash Table
    - String
    - Sorting
---

<!-- problem:start -->

# [1647. Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique)

## Description

<!-- description:start -->

<p>A string <code>s</code> is called <strong>good</strong> if there are no two different characters in <code>s</code> that have the same <strong>frequency</strong>.</p>

<p>Given a string <code>s</code>, return<em> the <strong>minimum</strong> number of characters you need to delete to make </em><code>s</code><em> <strong>good</strong>.</em></p>

<p>The <strong>frequency</strong> of a character in a string is the number of times it appears in the string. For example, in the string <code>&quot;aab&quot;</code>, the <strong>frequency</strong> of <code>&#39;a&#39;</code> is <code>2</code>, while the <strong>frequency</strong> of <code>&#39;b&#39;</code> is <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aab&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> <code>s</code> is already good.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabbbcc&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can delete two &#39;b&#39;s resulting in the good string &quot;aaabcc&quot;.
Another way it to delete one &#39;b&#39; and one &#39;c&#39; resulting in the good string &quot;aaabbc&quot;.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ceabaacb&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can delete both &#39;c&#39;s resulting in the good string &quot;eabaab&quot;.
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;contains only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Array + Sorting

<!-- thinking:start -->

> **Thinking**
>
> Frequencies must become unique and we may only delete characters. With $26$ letters, sort frequencies decreasingly so each value occupies at most one integer slot.
>
> Keep the next free upper bound $\textit{pre}$. If $v \ge \textit{pre}$, delete down to $\textit{pre}-1$ (or delete all once $\textit{pre}$ is $0$).
>
> Otherwise keep $v$ and set $\textit{pre}=v$.

<!-- thinking:end -->

First, we use an array $\textit{cnt}$ of length $26$ to count the occurrences of each letter in the string $s$.

Then, we sort the array $\textit{cnt}$ in descending order. We define a variable $\textit{pre}$ to record the current number of occurrences of the letter.

Next, we traverse each element $v$ in the array $\textit{cnt}$. If the current $\textit{pre}$ is $0$, we directly add $v$ to the answer. Otherwise, if $v \geq \textit{pre}$, we add $v - \textit{pre} + 1$ to the answer and decrement $\textit{pre}$ by $1$. Otherwise, we directly update $\textit{pre}$ to $v$. Then, we continue to the next element.

After traversing, we return the answer.

The time complexity is $O(n + |\Sigma| \times \log |\Sigma|)$, and the space complexity is $O(|\Sigma|)$. Here, $n$ is the length of the string $s$, and $|\Sigma|$ is the size of the alphabet. In this problem, $|\Sigma| = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        ans, pre = 0, inf
        for v in sorted(cnt.values(), reverse=True):
            if pre == 0:
                ans += v
            elif v >= pre:
                ans += v - pre + 1
                pre -= 1
            else:
                pre = v
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Greedy (Adjacent Decrement)

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 enforces a global upper bound. Equivalently, after sorting, force adjacent frequencies to decrease: while the next is not smaller, decrement it and count deletions.
>
> The implementation matches “neighbors differ” and has the same complexity.

<!-- thinking:end -->

Count frequencies and sort them in descending order. Walking adjacent frequencies, decrement the current one until it is strictly smaller than the previous.

The time complexity is $O(n + |\Sigma| \times \log |\Sigma| + n)$, and the space complexity is $O(|\Sigma|)$, where $n$ is the length of $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        vals = sorted(cnt.values(), reverse=True)
        ans = 0
        for i in range(1, len(vals)):
            while vals[i] >= vals[i - 1] and vals[i] > 0:
                vals[i] -= 1
                ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
