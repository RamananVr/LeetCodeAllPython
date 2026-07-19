---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3556.Sum%20of%20Largest%20Prime%20Substrings/README_EN.md
rating: 1439
source: Biweekly Contest 157 Q1
tags:
    - Hash Table
    - Math
    - String
    - Number Theory
    - Sorting
---

<!-- problem:start -->

# [3556. Sum of Largest Prime Substrings](https://leetcode.com/problems/sum-of-largest-prime-substrings)

## Description

<!-- description:start -->

<p data-end="157" data-start="30">Given a string <code>s</code>, find the sum of the <strong>3 largest unique <span data-keyword="prime-number">prime numbers</span></strong> that can be formed using any of its<strong> <span data-keyword="substring">substrings</span></strong>.</p>

<p data-end="269" data-start="166">Return the <strong>sum</strong> of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of <strong>all</strong> available primes. If no prime numbers can be formed, return 0.</p>

<p data-end="370" data-is-last-node="" data-is-only-node="" data-start="271"><strong data-end="280" data-start="271">Note:</strong> Each prime number should be counted only <strong>once</strong>, even if it appears in <strong>multiple</strong> substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;12234&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1469</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="136" data-start="16">The unique prime numbers formed from the substrings of <code>&quot;12234&quot;</code> are 2, 3, 23, 223, and 1223.</li>
	<li data-end="226" data-start="137">The 3 largest primes are 1223, 223, and 23. Their sum is 1469.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;111&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="339" data-start="244">The unique prime number formed from the substrings of <code>&quot;111&quot;</code> is 11.</li>
	<li data-end="412" data-is-last-node="" data-start="340">Since there is only one prime number, the sum is 11.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="39" data-start="18"><code>1 &lt;= s.length &lt;= 10</code></li>
	<li data-end="68" data-is-last-node="" data-start="40"><code>s</code> consists of only digits.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration + Hash Table

We can enumerate all substrings and check whether they are prime numbers. Since the problem requires us to return the sum of the largest 3 distinct primes, we can use a hash table to store all the primes.

After traversing all substrings, we sort the primes in the hash table in ascending order, and then take the largest 3 primes to calculate the sum.

If there are fewer than 3 primes in the hash table, return the sum of all primes.

The time complexity is $O(n^2 \times \sqrt{M})$, and the space complexity is $O(n^2)$, where $n$ is the length of the string and $M$ is the value of the largest substring.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            return all(x % i for i in range(2, int(sqrt(x)) + 1))

        st = set()
        n = len(s)
        for i in range(n):
            x = 0
            for j in range(i, n):
                x = x * 10 + int(s[j])
                if is_prime(x):
                    st.add(x)
        return sum(sorted(st)[-3:])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
