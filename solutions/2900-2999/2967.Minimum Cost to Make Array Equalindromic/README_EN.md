---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2967.Minimum%20Cost%20to%20Make%20Array%20Equalindromic/README_EN.md
rating: 2116
source: Weekly Contest 376 Q3
tags:
    - Greedy
    - Array
    - Math
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [2967. Minimum Cost to Make Array Equalindromic](https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> having length <code>n</code>.</p>

<p>You are allowed to perform a special move <strong>any</strong> number of times (<strong>including zero</strong>) on <code>nums</code>. In one <strong>special</strong> <strong>move</strong> you perform the following steps <strong>in order</strong>:</p>

<ul>
	<li>Choose an index <code>i</code> in the range <code>[0, n - 1]</code>, and a <strong>positive</strong> integer <code>x</code>.</li>
	<li>Add <code>|nums[i] - x|</code> to the total cost.</li>
	<li>Change the value of <code>nums[i]</code> to <code>x</code>.</li>
</ul>

<p>A <strong>palindromic number</strong> is a positive integer that remains the same when its digits are reversed. For example, <code>121</code>, <code>2552</code> and <code>65756</code> are palindromic numbers whereas <code>24</code>, <code>46</code>, <code>235</code> are not palindromic numbers.</p>

<p>An array is considered <strong>equalindromic</strong> if all the elements in the array are equal to an integer <code>y</code>, where <code>y</code> is a <strong>palindromic number</strong> less than <code>10<sup>9</sup></code>.</p>

<p>Return <em>an integer denoting the <strong>minimum</strong> possible total cost to make </em><code>nums</code><em> <strong>equalindromic</strong> by performing any number of special moves.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> We can make the array equalindromic by changing all elements to 3 which is a palindromic number. The cost of changing the array to [3,3,3,3,3] using 4 special moves is given by |1 - 3| + |2 - 3| + |4 - 3| + |5 - 3| = 6.
It can be shown that changing all elements to any palindromic number other than 3 cannot be achieved at a lower cost.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,12,13,14,15]
<strong>Output:</strong> 11
<strong>Explanation:</strong> We can make the array equalindromic by changing all elements to 11 which is a palindromic number. The cost of changing the array to [11,11,11,11,11] using 5 special moves is given by |10 - 11| + |12 - 11| + |13 - 11| + |14 - 11| + |15 - 11| = 11.
It can be shown that changing all elements to any palindromic number other than 11 cannot be achieved at a lower cost.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [22,33,22,33,22]
<strong>Output:</strong> 22
<strong>Explanation:</strong> We can make the array equalindromic by changing all elements to 22 which is a palindromic number. The cost of changing the array to [22,22,22,22,22] using 2 special moves is given by |33 - 22| + |33 - 22| = 22.
It can be shown that changing all elements to any palindromic number other than 22 cannot be achieved at a lower cost.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Sorting + Binary Search

The range of palindrome numbers in the problem is $[1, 10^9]$. Due to the symmetry of palindrome numbers, we can enumerate in the range of $[1, 10^5]$, then reverse and concatenate them to get all palindrome numbers. Note that if it is an odd-length palindrome number, we need to remove the last digit before reversing. The array of palindrome numbers obtained by preprocessing is denoted as $ps$. We sort the array $ps$.

Next, we sort the array $nums$ and take the median $x$ of $nums$. We only need to find a number in the palindrome array $ps$ that is closest to $x$ through binary search, and then calculate the cost of $nums$ becoming this number to get the answer.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(M)$. Here, $n$ is the length of the array $nums$, and $M$ is the length of the palindrome array $ps$.

Similar problems:

- [906. Super Palindromes](https://github.com/doocs/leetcode/blob/main/solution/0900-0999/0906.Super%20Palindromes/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
ps = []
for i in range(1, 10**5 + 1):
    s = str(i)
    t1 = s[::-1]
    t2 = s[:-1][::-1]
    ps.append(int(s + t1))
    ps.append(int(s + t2))
ps.sort()

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def f(x: int) -> int:
            return sum(abs(v - x) for v in nums)

        nums.sort()
        i = bisect_left(ps, nums[len(nums) // 2])
        return min(f(ps[j]) for j in range(i - 1, i + 2) if 0 <= j < len(ps))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
