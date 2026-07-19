---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3234.Count%20the%20Number%20of%20Substrings%20With%20Dominant%20Ones/README_EN.md
rating: 2556
source: Weekly Contest 408 Q3
tags:
    - String
    - Enumeration
---

<!-- problem:start -->

# [3234. Count the Number of Substrings With Dominant Ones](https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones)

## Description

<!-- description:start -->

<p>You are given a binary string <code>s</code>.</p>

<p>Return the number of <span data-keyword="substring-nonempty">substrings</span> with <strong>dominant</strong> ones.</p>

<p>A string has <strong>dominant</strong> ones if the number of ones in the string is <strong>greater than or equal to</strong> the <strong>square</strong> of the number of zeros in the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;00011&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The substrings with dominant ones are shown in the table below.</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>Number of Zeros</th>
			<th>Number of Ones</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>3</td>
			<td>3</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td>01</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>4</td>
			<td>11</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>4</td>
			<td>011</td>
			<td>1</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;101101&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>The substrings with <strong>non-dominant</strong> ones are shown in the table below.</p>

<p>Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>Number of Zeros</th>
			<th>Number of Ones</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td>0110</td>
			<td>2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>0</td>
			<td>4</td>
			<td>10110</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>1</td>
			<td>5</td>
			<td>01101</td>
			<td>2</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists only of characters <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Enumeration

According to the problem description, a dominant string satisfies $\textit{cnt}_1 \geq \textit{cnt}_0^2$, which means the maximum value of $\textit{cnt}_0$ does not exceed $\sqrt{n}$, where $n$ is the length of the string. Therefore, we can enumerate the value of $\textit{cnt}_0$ and then calculate the number of substrings that satisfy the condition.

We first preprocess the position of the first $0$ starting from each position in the string, storing it in the array $\textit{nxt}$, where $\textit{nxt}[i]$ represents the position of the first $0$ starting from position $i$, or $n$ if it doesn't exist.

Next, we iterate through each position $i$ in the string as the starting position of the substring, initializing $\textit{cnt}_0$ to $0$ or $1$ (depending on whether the current position is $0$). Then we use a pointer $j$ starting from position $i$, jumping step by step to the position of the next $0$, while updating the value of $\textit{cnt}_0$.

For a substring starting at position $i$ and containing $\textit{cnt}_0$ zeros, it can contain at most $\textit{nxt}[j + 1] - i - \textit{cnt}_0$ ones. If this quantity is greater than or equal to $\textit{cnt}_0^2$, it means there exists a substring that satisfies the condition. At this point, we need to determine how many positions the right endpoint $\textit{nxt}[j + 1] - 1$ can move left while still satisfying the condition. Specifically, the right endpoint has a total of $\min(\textit{nxt}[j + 1] - j, \textit{cnt}_1 - \textit{cnt}_0^2 + 1)$ possible choices. We accumulate these counts to the answer. Then we move pointer $j$ to the position of the next $0$ and continue enumerating the next value of $\textit{cnt}_0$ until $\textit{cnt}_0^2$ exceeds the string length.

The time complexity is $O(n \times \sqrt{n})$, and the space complexity is $O(n)$, where $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        nxt = [n] * (n + 1)
        for i in range(n - 1, -1, -1):
            nxt[i] = nxt[i + 1]
            if s[i] == "0":
                nxt[i] = i
        ans = 0
        for i in range(n):
            cnt0 = int(s[i] == "0")
            j = i
            while j < n and cnt0 * cnt0 <= n:
                cnt1 = (nxt[j + 1] - i) - cnt0
                if cnt1 >= cnt0 * cnt0:
                    ans += min(nxt[j + 1] - j, cnt1 - cnt0 * cnt0 + 1)
                j = nxt[j + 1]
                cnt0 += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
