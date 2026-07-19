---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1010.Pairs%20of%20Songs%20With%20Total%20Durations%20Divisible%20by%2060/README_EN.md
rating: 1377
source: Weekly Contest 128 Q2
tags:
    - Array
    - Hash Table
    - Counting
---

<!-- problem:start -->

# [1010. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60)

## Description

<!-- description:start -->

<p>You are given a list of songs where the <code>i<sup>th</sup></code> song has a duration of <code>time[i]</code> seconds.</p>

<p>Return <em>the number of pairs of songs for which their total duration in seconds is divisible by</em> <code>60</code>. Formally, we want the number of indices <code>i</code>, <code>j</code> such that <code>i &lt; j</code> with <code>(time[i] + time[j]) % 60 == 0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> time = [30,20,150,100,40]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> time = [60,60,60]
<strong>Output:</strong> 3
<strong>Explanation:</strong> All three pairs have a total duration of 120, which is divisible by 60.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= time.length &lt;= 6 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= time[i] &lt;= 500</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Math + Counting

If the sum of a pair $(a, b)$ is divisible by $60$, i.e., $(a + b) \bmod 60 = 0$, then $(a \bmod 60 + b \bmod 60) \bmod 60 = 0$. Let $x = a \bmod 60$ and $y = b \bmod 60$, then $(x + y) \bmod 60 = 0$, which means $y = (60 - x) \bmod 60$.

Therefore, we can iterate over the song list and use an array $cnt$ of length $60$ to record the number of occurrences of each remainder $x$. For the current $x$, if there exists a remainder $y = (60 - x) \bmod 60$ in array $cnt$, we add $cnt[y]$ to the answer. Then we increment the count of $x$ in array $cnt$ by $1$. We continue iterating until the entire song list has been traversed.

After the iteration, we get the number of song pairs that satisfy the condition.

The time complexity is $O(n)$ and the space complexity is $O(C)$, where $n$ is the length of the song list and $C$ is the number of possible remainders, here $C = 60$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for x in time:
            x %= 60
            y = (60 - x) % 60
            ans += cnt[y]
            cnt[x] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
