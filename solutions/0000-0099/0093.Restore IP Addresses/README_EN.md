---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0093.Restore%20IP%20Addresses/README_EN.md
tags:
    - String
    - Backtracking
---

<!-- problem:start -->

# [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses)

## Description

<!-- description:start -->

<p>A <strong>valid IP address</strong> consists of exactly four integers separated by single dots. Each integer is between <code>0</code> and <code>255</code> (<strong>inclusive</strong>) and cannot have leading zeros.</p>

<ul>
	<li>For example, <code>&quot;0.1.2.201&quot;</code> and <code>&quot;192.168.1.1&quot;</code> are <strong>valid</strong> IP addresses, but <code>&quot;0.011.255.245&quot;</code>, <code>&quot;192.168.1.312&quot;</code> and <code>&quot;192.168@1.1&quot;</code> are <strong>invalid</strong> IP addresses.</li>
</ul>

<p>Given a string <code>s</code> containing only digits, return <em>all possible valid IP addresses that can be formed by inserting dots into </em><code>s</code>. You are <strong>not</strong> allowed to reorder or remove any digits in <code>s</code>. You may return the valid IP addresses in <strong>any</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;25525511135&quot;
<strong>Output:</strong> [&quot;255.255.11.135&quot;,&quot;255.255.111.35&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0000&quot;
<strong>Output:</strong> [&quot;0.0.0.0&quot;]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;101023&quot;
<strong>Output:</strong> [&quot;1.0.10.23&quot;,&quot;1.0.102.3&quot;,&quot;10.1.0.23&quot;,&quot;10.10.2.3&quot;,&quot;101.0.2.3&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> consists of digits only.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

We define a function $dfs(i)$, which represents the list of IP addresses that can be formed starting from the $i$th position of string $s$.

The execution steps of function $dfs(i)$ are as follows:

If $i$ is greater than or equal to the length of string $s$, it means that we have completed the splicing of four segments of the IP address. At this point, we need to check whether it meets the requirements of the four segments of the IP address. If it does, add the current $IP$ to the answer.

If $i$ is less than the length of string $s$, it means that we still need to splice a segment of the IP address. At this point, we need to determine the value of this segment of the IP address. If the value is greater than $255$, or the current position $i$ is $0$ and the value of several positions after $i$ is greater than $0$, it means that it does not meet the requirements, so we return directly. Otherwise, add it to the IP address list, and continue to search for the next segment of the IP address.

The time complexity is $O(n \times 3^4)$, and the space complexity is $O(n)$. Here, $n$ is the length of string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(i: int, j: int) -> int:
            if s[i] == "0" and i != j:
                return False
            return 0 <= int(s[i : j + 1]) <= 255

        def dfs(i: int):
            if i >= n and len(t) == 4:
                ans.append(".".join(t))
                return
            if i >= n or len(t) >= 4:
                return
            for j in range(i, min(i + 3, n)):
                if check(i, j):
                    t.append(s[i : j + 1])
                    dfs(j + 1)
                    t.pop()

        n = len(s)
        ans = []
        t = []
        dfs(0)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
