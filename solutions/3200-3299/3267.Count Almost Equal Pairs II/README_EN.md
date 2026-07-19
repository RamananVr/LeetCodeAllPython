---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3267.Count%20Almost%20Equal%20Pairs%20II/README_EN.md
rating: 2545
source: Weekly Contest 412 Q4
tags:
    - Array
    - Hash Table
    - Counting
    - Enumeration
    - Sorting
---

<!-- problem:start -->

# [3267. Count Almost Equal Pairs II](https://leetcode.com/problems/count-almost-equal-pairs-ii)

## Description

<!-- description:start -->

<p><strong>Attention</strong>: In this version, the number of operations that can be performed, has been increased to <strong>twice</strong>.<!-- notionvc: 278e7cb2-3b05-42fa-8ae9-65f5fd6f7585 --></p>

<p>You are given an array <code>nums</code> consisting of positive integers.</p>

<p>We call two integers <code>x</code> and <code>y</code> <strong>almost equal</strong> if both integers can become equal after performing the following operation <strong>at most <u>twice</u></strong>:</p>

<ul>
	<li>Choose <strong>either</strong> <code>x</code> or <code>y</code> and swap any two digits within the chosen number.</li>
</ul>

<p>Return the number of indices <code>i</code> and <code>j</code> in <code>nums</code> where <code>i &lt; j</code> such that <code>nums[i]</code> and <code>nums[j]</code> are <strong>almost equal</strong>.</p>

<p><strong>Note</strong> that it is allowed for an integer to have leading zeros after performing an operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1023,2310,2130,213]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The almost equal pairs of elements are:</p>

<ul>
	<li>1023 and 2310. By swapping the digits 1 and 2, and then the digits 0 and 3 in 1023, you get 2310.</li>
	<li>1023 and 213. By swapping the digits 1 and 0, and then the digits 1 and 2 in 1023, you get 0213, which is 213.</li>
	<li>2310 and 213. By swapping the digits 2 and 0, and then the digits 3 and 2 in 2310, you get 0213, which is 213.</li>
	<li>2310 and 2130. By swapping the digits 3 and 1 in 2310, you get 2130.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,10,100]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The almost equal pairs of elements are:</p>

<ul>
	<li>1 and 10. By swapping the digits 1 and 0 in 10, you get 01 which is 1.</li>
	<li>1 and 100. By swapping the second 0 with the digit 1 in 100, you get 001, which is 1.</li>
	<li>10 and 100. By swapping the first 0 with the digit 1 in 100, you get 010, which is 10.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>1 &lt;= nums[i] &lt; 10<sup>7</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Enumeration

We can enumerate each number, and for each number, we can enumerate each pair of different digits, then swap these two digits to get a new number. Record this new number in a hash table $\textit{vis}$, representing all possible numbers after at most one swap. Then continue to enumerate each pair of different digits, swap these two digits to get a new number, and record it in the hash table $\textit{vis}$, representing all possible numbers after at most two swaps.

This enumeration may miss some pairs of numbers, such as $[100, 1]$, because the number obtained after swapping $100$ is $1$, and the previously enumerated numbers do not include $1$, so some pairs of numbers will be missed. We only need to sort the array before enumeration to solve this problem.

The time complexity is $O(n \times (\log n + \log^5 M))$, and the space complexity is $O(n + \log^4 M)$. Here, $n$ is the length of the array $\textit{nums}$, and $M$ is the maximum value in the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        cnt = defaultdict(int)
        for x in nums:
            vis = {x}
            s = list(str(x))
            m = len(s)
            for j in range(m):
                for i in range(j):
                    s[i], s[j] = s[j], s[i]
                    vis.add(int("".join(s)))
                    for q in range(i + 1, m):
                        for p in range(i + 1, q):
                            s[p], s[q] = s[q], s[p]
                            vis.add(int("".join(s)))
                            s[p], s[q] = s[q], s[p]
                    s[i], s[j] = s[j], s[i]
            ans += sum(cnt[x] for x in vis)
            cnt[x] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
