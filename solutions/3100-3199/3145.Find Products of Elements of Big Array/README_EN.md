---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3145.Find%20Products%20of%20Elements%20of%20Big%20Array/README_EN.md
rating: 2859
source: Biweekly Contest 130 Q4
tags:
    - Bit Manipulation
    - Array
    - Binary Search
---

<!-- problem:start -->

# [3145. Find Products of Elements of Big Array](https://leetcode.com/problems/find-products-of-elements-of-big-array)

## Description

<!-- description:start -->

<p>The <strong>powerful array</strong> of a non-negative integer <code>x</code> is defined as the shortest sorted array of powers of two that sum up to <code>x</code>. The table below illustrates examples of how the <strong>powerful array</strong> is determined. It can be proven that the powerful array of <code>x</code> is unique.</p>

<table border="1">
	<tbody>
		<tr>
			<th>num</th>
			<th>Binary Representation</th>
			<th>powerful array</th>
		</tr>
		<tr>
			<td>1</td>
			<td>0000<u>1</u></td>
			<td>[1]</td>
		</tr>
		<tr>
			<td>8</td>
			<td>0<u>1</u>000</td>
			<td>[8]</td>
		</tr>
		<tr>
			<td>10</td>
			<td>0<u>1</u>0<u>1</u>0</td>
			<td>[2, 8]</td>
		</tr>
		<tr>
			<td>13</td>
			<td>0<u>11</u>0<u>1</u></td>
			<td>[1, 4, 8]</td>
		</tr>
		<tr>
			<td>23</td>
			<td><u>1</u>0<u>111</u></td>
			<td>[1, 2, 4, 16]</td>
		</tr>
	</tbody>
</table>

<p>The array <code>big_nums</code> is created by concatenating the <strong>powerful arrays</strong> for every positive integer <code>i</code> in ascending order: 1, 2, 3, and so on. Thus, <code>big_nums</code> begins as <code>[<u>1</u>, <u>2</u>, <u>1, 2</u>, <u>4</u>, <u>1, 4</u>, <u>2, 4</u>, <u>1, 2, 4</u>, <u>8</u>, ...]</code>.</p>

<p>You are given a 2D integer matrix <code>queries</code>, where for <code>queries[i] = [from<sub>i</sub>, to<sub>i</sub>, mod<sub>i</sub>]</code> you should calculate <code>(big_nums[from<sub>i</sub>] * big_nums[from<sub>i</sub> + 1] * ... * big_nums[to<sub>i</sub>]) % mod<sub>i</sub></code><!-- notionvc: a71131cc-7b52-4786-9a4b-660d6d864f89 -->.</p>

<p>Return an integer array <code>answer</code> such that <code>answer[i]</code> is the answer to the <code>i<sup>th</sup></code> query.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">queries = [[1,3,7]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4]</span></p>

<p><strong>Explanation:</strong></p>

<p>There is one query.</p>

<p><code>big_nums[1..3] = [2,1,2]</code>. The product of them is 4. The result is <code>4 % 7 = 4.</code></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">queries = [[2,5,3],[7,7,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>There are two queries.</p>

<p>First query: <code>big_nums[2..5] = [1,2,4,1]</code>. The product of them is 8. The result is <code>8 % 3 = 2</code>.</p>

<p>Second query: <code>big_nums[7] = 2</code>. The result is <code>2 % 4 = 2</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= 500</code></li>
	<li><code>queries[i].length == 3</code></li>
	<li><code>0 &lt;= queries[i][0] &lt;= queries[i][1] &lt;= 10<sup>15</sup></code></li>
	<li><code>1 &lt;= queries[i][2] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search + Bit Manipulation

The continuous positive integer numbers correspond to the strong integer array, forming the array $\textit{bignums}$. The problem requires us to find the result of the product of the subarray $\textit{bignums}[\textit{left}..\textit{right}]$ modulo $\textit{mod}$ for each query $[\textit{left}, \textit{right}, \textit{mod}]$. Since each element of the subarray is a power of 2, this is equivalent to finding the sum of the powers $\textit{power}$ of the subarray, and then calculating $2^{\textit{power}} \bmod \textit{mod}$. For example, for the subarray $[1, 4, 8]$, i.e., $[2^0, 2^2, 2^3]$, the sum of the powers is $0 + 2 + 3 = 5$, so $2^5 \bmod \textit{mod}$ is the result we need.

Therefore, we can convert $\textit{bignums}$ into an array of powers. For example, for the subarray $[1, 4, 8]$, we convert it to $[0, 2, 3]$. Thus, the problem is transformed into finding the sum of the subarray of powers, i.e., $\textit{power} = \textit{f}(\textit{right} + 1) - \textit{f}(\textit{left})$, where $\textit{f}(i)$ represents the sum of the powers of $\textit{bignums}[0..i)$, which is the prefix sum.

Next, we calculate the value of $\textit{f}(i)$ based on the index $i$. We can use binary search to find the largest number whose strong array length is less than $i$, and then calculate the sum of the powers of the remaining numbers.

According to the problem description, we list the strong integers for numbers $0..14$:

| $\textit{nums}$ | 8($2^3$)                              | 4($2^2$)                              | 2($2^1$)                              | ($2^0$)                               |
| --------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| 0               | 0                                     | 0                                     | 0                                     | 0                                     |
| 1               | <span style="color: red;">0</span>    | <span style="color: red;">0</span>    | <span style="color: red;">0</span>    | <span style="color: red;">1</span>    |
| 2               | <span style="color: blue;">0</span>   | <span style="color: blue;">0</span>   | <span style="color: blue;">1</span>   | <span style="color: blue;">0</span>   |
| 3               | <span style="color: blue;">0</span>   | <span style="color: blue;">0</span>   | <span style="color: blue;">1</span>   | <span style="color: blue;">1</span>   |
| 4               | <span style="color: green;">0</span>  | <span style="color: green;">1</span>  | <span style="color: green;">0</span>  | <span style="color: green;">0</span>  |
| 5               | <span style="color: green;">0</span>  | <span style="color: green;">1</span>  | <span style="color: green;">0</span>  | <span style="color: green;">1</span>  |
| 6               | <span style="color: green;">0</span>  | <span style="color: green;">1</span>  | <span style="color: green;">1</span>  | <span style="color: green;">0</span>  |
| 7               | <span style="color: green;">0</span>  | <span style="color: green;">1</span>  | <span style="color: green;">1</span>  | <span style="color: green;">1</span>  |
| 8               | <span style="color: yellow;">1</span> | <span style="color: yellow;">0</span> | <span style="color: yellow;">0</span> | <span style="color: yellow;">0</span> |
| 9               | <span style="color: yellow;">1</span> | <span style="color: yellow;">0</span> | <span style="color: yellow;">0</span> | <span style="color: yellow;">1</span> |
| 10              | <span style="color: yellow;">1</span> | <span style="color: yellow;">0</span> | <span style="color: yellow;">1</span> | <span style="color: yellow;">0</span> |
| 11              | <span style="color: yellow;">1</span> | <span style="color: yellow;">0</span> | <span style="color: yellow;">1</span> | <span style="color: yellow;">1</span> |
| 12              | <span style="color: yellow;">1</span> | <span style="color: yellow;">1</span> | <span style="color: yellow;">0</span> | <span style="color: yellow;">0</span> |
| 13              | <span style="color: yellow;">1</span> | <span style="color: yellow;">1</span> | <span style="color: yellow;">0</span> | <span style="color: yellow;">1</span> |
| 14              | <span style="color: yellow;">1</span> | <span style="color: yellow;">1</span> | <span style="color: yellow;">1</span> | <span style="color: yellow;">0</span> |

By dividing the numbers into different colors according to the interval $[2^i, 2^{i+1}-1]$, we can see that the numbers in the interval $[2^i, 2^{i+1}-1]$ are equivalent to adding $2^i$ to each number in the interval $[0, 2^i-1]$. Based on this pattern, we can calculate the total number of strong arrays $\textit{cnt}[i]$ and the sum of powers $\textit{s}[i]$ for the first $i$ groups of numbers in $\textit{bignums}$.

Next, for any number, we consider how to calculate the number of strong arrays and the sum of powers. We can use the binary method, calculating from the highest bit. For example, for the number $13 = 2^3 + 2^2 + 2^0$, the result of the first $2^3$ numbers can be obtained from $\textit{cnt}[3]$ and $\textit{s}[3]$, and the result of the remaining $[2^3, 13]$ is equivalent to adding $3$ to all numbers in $[0, 13-2^3]$, i.e., $[0, 5]$. The problem is transformed into calculating the number of strong arrays and the sum of powers for $[0, 5]$. In this way, we can calculate the number of strong arrays and the sum of powers for any number.

Finally, based on the value of $\textit{power}$, we use the fast exponentiation method to calculate the result of $2^{\textit{power}} \bmod \textit{mod}$.

The time complexity is $O(q \times \log M)$, and the space complexity is $O(\log M)$. Here, $q$ is the number of queries, and $M$ is the upper bound of the number, with $M \le 10^{15}$ in this problem.

<!-- tabs:start -->

#### Python3

```python
m = 50
cnt = [0] * (m + 1)
s = [0] * (m + 1)
p = 1
for i in range(1, m + 1):
    cnt[i] = cnt[i - 1] * 2 + p
    s[i] = s[i - 1] * 2 + p * (i - 1)
    p *= 2

def num_idx_and_sum(x: int) -> tuple:
    idx = 0
    total_sum = 0
    while x:
        i = x.bit_length() - 1
        idx += cnt[i]
        total_sum += s[i]
        x -= 1 << i
        total_sum += (x + 1) * i
        idx += x + 1
    return (idx, total_sum)

def f(i: int) -> int:
    l, r = 0, 1 << m
    while l < r:
        mid = (l + r + 1) >> 1
        idx, _ = num_idx_and_sum(mid)
        if idx < i:
            l = mid
        else:
            r = mid - 1

    total_sum = 0
    idx, total_sum = num_idx_and_sum(l)
    i -= idx
    x = l + 1
    for _ in range(i):
        y = x & -x
        total_sum += y.bit_length() - 1
        x -= y
    return total_sum

class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        return [pow(2, f(right + 1) - f(left), mod) for left, right, mod in queries]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
