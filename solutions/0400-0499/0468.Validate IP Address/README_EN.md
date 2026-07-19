---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0468.Validate%20IP%20Address/README_EN.md
tags:
    - String
---

<!-- problem:start -->

# [468. Validate IP Address](https://leetcode.com/problems/validate-ip-address)

## Description

<!-- description:start -->

<p>Given a string <code>queryIP</code>, return <code>&quot;IPv4&quot;</code> if IP is a valid IPv4 address, <code>&quot;IPv6&quot;</code> if IP is a valid IPv6 address or <code>&quot;Neither&quot;</code> if IP is not a correct IP of any type.</p>

<p><strong>A valid IPv4</strong> address is an IP in the form <code>&quot;x<sub>1</sub>.x<sub>2</sub>.x<sub>3</sub>.x<sub>4</sub>&quot;</code> where <code>0 &lt;= x<sub>i</sub> &lt;= 255</code> and <code>x<sub>i</sub></code> <strong>cannot contain</strong> leading zeros. For example, <code>&quot;192.168.1.1&quot;</code> and <code>&quot;192.168.1.0&quot;</code> are valid IPv4 addresses while <code>&quot;192.168.01.1&quot;</code>, <code>&quot;192.168.1.00&quot;</code>, and <code>&quot;192.168@1.1&quot;</code> are invalid IPv4 addresses.</p>

<p><strong>A valid IPv6</strong> address is an IP in the form <code>&quot;x<sub>1</sub>:x<sub>2</sub>:x<sub>3</sub>:x<sub>4</sub>:x<sub>5</sub>:x<sub>6</sub>:x<sub>7</sub>:x<sub>8</sub>&quot;</code> where:</p>

<ul>
	<li><code>1 &lt;= x<sub>i</sub>.length &lt;= 4</code></li>
	<li><code>x<sub>i</sub></code> is a <strong>hexadecimal string</strong> which may contain digits, lowercase English letter (<code>&#39;a&#39;</code> to <code>&#39;f&#39;</code>) and upper-case English letters (<code>&#39;A&#39;</code> to <code>&#39;F&#39;</code>).</li>
	<li>Leading zeros are allowed in <code>x<sub>i</sub></code>.</li>
</ul>

<p>For example, &quot;<code>2001:0db8:85a3:0000:0000:8a2e:0370:7334&quot;</code> and &quot;<code>2001:db8:85a3:0:0:8A2E:0370:7334&quot;</code> are valid IPv6 addresses, while &quot;<code>2001:0db8:85a3::8A2E:037j:7334&quot;</code> and &quot;<code>02001:0db8:85a3:0000:0000:8a2e:0370:7334&quot;</code> are invalid IPv6 addresses.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> queryIP = &quot;172.16.254.1&quot;
<strong>Output:</strong> &quot;IPv4&quot;
<strong>Explanation:</strong> This is a valid IPv4 address, return &quot;IPv4&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> queryIP = &quot;2001:0db8:85a3:0:0:8A2E:0370:7334&quot;
<strong>Output:</strong> &quot;IPv6&quot;
<strong>Explanation:</strong> This is a valid IPv6 address, return &quot;IPv6&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> queryIP = &quot;256.256.256.256&quot;
<strong>Output:</strong> &quot;Neither&quot;
<strong>Explanation:</strong> This is neither a IPv4 address nor a IPv6 address.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>queryIP</code> consists only of English letters, digits and the characters <code>&#39;.&#39;</code> and <code>&#39;:&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We can define two functions `isIPv4` and `isIPv6` to determine whether a string is a valid IPv4 address and IPv6 address.

The implementation of the function `isIPv4` is as follows:

1. We first check if the string `s` ends with `.`. If so, `s` is not a valid IPv4 address, and we directly return `false`.
1. Then we split the string `s` by `.` into a string array `ss`. If the length of `ss` is not `4`, `s` is not a valid IPv4 address, and we directly return `false`.
1. For each string `t` in the array `ss`, we check:
    - If the length of `t` is greater than `1` and the first character of `t` is `0`, `t` is not a valid IPv4 address, and we directly return `false`.
    - If `t` is not a number or `t` is not in the range of `0` to `255`, `t` is not a valid IPv4 address, and we directly return `false`.
1. If none of the above conditions are met, `s` is a valid IPv4 address, and we return `true`.

The implementation of the function `isIPv6` is as follows:

1. We first check if the string `s` ends with `:`. If so, `s` is not a valid IPv6 address, and we directly return `false`.
1. Then we split the string `s` by `:` into a string array `ss`. If the length of `ss` is not `8`, `s` is not a valid IPv6 address, and we directly return `false`.
1. For each string `t` in the array `ss`, we check:
    - If the length of `t` is less than `1` or greater than `4`, `t` is not a valid IPv6 address, and we directly return `false`.
    - If the characters in `t` are not all between `0` and `9` and `a` and `f` (case insensitive), `t` is not a valid IPv6 address, and we directly return `false`.
1. If none of the above conditions are met, `s` is a valid IPv6 address, and we return `true`.

Finally, we call the `isIPv4` and `isIPv6` functions to determine if `queryIP` is a valid IPv4 address or IPv6 address. If it is neither, we return `Neither`.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the string `queryIP`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(s: str) -> bool:
            ss = s.split(".")
            if len(ss) != 4:
                return False
            for t in ss:
                if len(t) > 1 and t[0] == "0":
                    return False
                if not t.isdigit() or not 0 <= int(t) <= 255:
                    return False
            return True

        def is_ipv6(s: str) -> bool:
            ss = s.split(":")
            if len(ss) != 8:
                return False
            for t in ss:
                if not 1 <= len(t) <= 4:
                    return False
                if not all(c in "0123456789abcdefABCDEF" for c in t):
                    return False
            return True

        if is_ipv4(queryIP):
            return "IPv4"
        if is_ipv6(queryIP):
            return "IPv6"
        return "Neither"
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
