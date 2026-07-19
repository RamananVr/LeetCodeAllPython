---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2578.Split%20With%20Minimum%20Sum/README_EN.md
rating: 1350
source: Biweekly Contest 99 Q1
tags:
    - Greedy
    - Math
    - Sorting
---

<!-- problem:start -->

# [2578. Split With Minimum Sum](https://leetcode.com/problems/split-with-minimum-sum)

## Description

<!-- description:start -->

<p>Given a positive integer <code>num</code>, split it into two non-negative integers <code>num1</code> and <code>num2</code> such that:</p>

<ul>
	<li>The concatenation of <code>num1</code> and <code>num2</code> is a permutation of <code>num</code>.

    <ul>
    	<li>In other words, the sum of the number of occurrences of each digit in <code>num1</code> and <code>num2</code> is equal to the number of occurrences of that digit in <code>num</code>.</li>
    </ul>
    </li>
    <li><code>num1</code> and <code>num2</code> can contain leading zeros.</li>

</ul>

<p>Return <em>the <strong>minimum</strong> possible sum of</em> <code>num1</code> <em>and</em> <code>num2</code>.</p>

<p><strong>Notes:</strong></p>

<ul>
	<li>It is guaranteed that <code>num</code> does not contain any leading zeros.</li>
	<li>The order of occurrence of the digits in <code>num1</code> and <code>num2</code> may differ from the order of occurrence of <code>num</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 4325
<strong>Output:</strong> 59
<strong>Explanation:</strong> We can split 4325 so that <code>num1</code> is 24 and <code>num2</code> is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 687
<strong>Output:</strong> 75
<strong>Explanation:</strong> We can split 687 so that <code>num1</code> is 68 and <code>num2</code> is 7, which would give an optimal sum of 75.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>10 &lt;= num &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting + Greedy

First, we use a hash table or array $cnt$ to count the occurrences of each digit in $num$, and use a variable $n$ to record the number of digits in $num$.

Next, we enumerate all the digits $i$ in $nums$, and alternately allocate the digits in $cnt$ to $num1$ and $num2$ in ascending order, recording them in an array $ans$ of length $2$. Finally, we return the sum of the two numbers in $ans$.

The time complexity is $O(n)$, and the space complexity is $O(C)$. Where $n$ is the number of digits in $num$; and $C$ is the number of different digits in $num$, in this problem, $C \leq 10$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def splitNum(self, num: int) -> int:
        cnt = Counter()
        n = 0
        while num:
            cnt[num % 10] += 1
            num //= 10
            n += 1
        ans = [0] * 2
        j = 0
        for i in range(n):
            while cnt[j] == 0:
                j += 1
            cnt[j] -= 1
            ans[i & 1] = ans[i & 1] * 10 + j
        return sum(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Sorting + Greedy

We can convert $num$ to a string or character array, then sort it, and then alternately allocate the digits in the sorted array to $num1$ and $num2$ in ascending order. Finally, we return the sum of $num1$ and $num2$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Where $n$ is the number of digits in $num$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def splitNum(self, num: int) -> int:
        s = sorted(str(num))
        return int(''.join(s[::2])) + int(''.join(s[1::2]))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
