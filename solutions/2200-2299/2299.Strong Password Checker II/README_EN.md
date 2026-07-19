---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2200-2299/2299.Strong%20Password%20Checker%20II/README_EN.md
rating: 1241
source: Biweekly Contest 80 Q1
tags:
    - String
---

<!-- problem:start -->

# [2299. Strong Password Checker II](https://leetcode.com/problems/strong-password-checker-ii)

## Description

<!-- description:start -->

<p>A password is said to be <strong>strong</strong> if it satisfies all the following criteria:</p>

<ul>
	<li>It has at least <code>8</code> characters.</li>
	<li>It contains at least <strong>one lowercase</strong> letter.</li>
	<li>It contains at least <strong>one uppercase</strong> letter.</li>
	<li>It contains at least <strong>one digit</strong>.</li>
	<li>It contains at least <strong>one special character</strong>. The special characters are the characters in the following string: <code>&quot;!@#$%^&amp;*()-+&quot;</code>.</li>
	<li>It does <strong>not</strong> contain <code>2</code> of the same character in adjacent positions (i.e., <code>&quot;aab&quot;</code> violates this condition, but <code>&quot;aba&quot;</code> does not).</li>
</ul>

<p>Given a string <code>password</code>, return <code>true</code><em> if it is a <strong>strong</strong> password</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> password = &quot;IloveLe3tcode!&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The password meets all the requirements. Therefore, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> password = &quot;Me+You--IsMyDream&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> password = &quot;1aB!&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The password does not meet the length requirement. Therefore, we return false.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= password.length &lt;= 100</code></li>
	<li><code>password</code> consists of letters, digits, and special characters: <code>&quot;!@#$%^&amp;*()-+&quot;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation + Bit Manipulation

According to the problem description, we can simulate the process of checking whether the password meets the requirements.

First, we check if the length of the password is less than $8$. If it is, we return $\textit{false}$.

Next, we use a mask $\textit{mask}$ to record whether the password contains lowercase letters, uppercase letters, digits, and special characters. We traverse the password, and for each character, we first check if it is the same as the previous character. If it is, we return $\textit{false}$. Then, we update the mask $\textit{mask}$ based on the character type. Finally, we check if the mask $\textit{mask}$ is $15$. If it is, we return $\textit{true}$; otherwise, we return $\textit{false}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the password.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        mask = 0
        for i, c in enumerate(password):
            if i and c == password[i - 1]:
                return False
            if c.islower():
                mask |= 1
            elif c.isupper():
                mask |= 2
            elif c.isdigit():
                mask |= 4
            else:
                mask |= 8
        return mask == 15
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
