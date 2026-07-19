---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3266.Final%20Array%20State%20After%20K%20Multiplication%20Operations%20II/README_EN.md
rating: 2508
source: Weekly Contest 412 Q3
tags:
    - Array
    - Simulation
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3266. Final Array State After K Multiplication Operations II](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>, an integer <code>k</code>, and an integer <code>multiplier</code>.</p>

<p>You need to perform <code>k</code> operations on <code>nums</code>. In each operation:</p>

<ul>
	<li>Find the <strong>minimum</strong> value <code>x</code> in <code>nums</code>. If there are multiple occurrences of the minimum value, select the one that appears <strong>first</strong>.</li>
	<li>Replace the selected minimum value <code>x</code> with <code>x * multiplier</code>.</li>
</ul>

<p>After the <code>k</code> operations, apply <strong>modulo</strong> <code>10<sup>9</sup> + 7</code> to every value in <code>nums</code>.</p>

<p>Return an integer array denoting the <em>final state</em> of <code>nums</code> after performing all <code>k</code> operations and then applying the modulo.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,3,5,6], k = 5, multiplier = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[8,4,6,5,6]</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Result</th>
		</tr>
		<tr>
			<td>After operation 1</td>
			<td>[2, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 2</td>
			<td>[4, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 3</td>
			<td>[4, 4, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 4</td>
			<td>[4, 4, 6, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 5</td>
			<td>[8, 4, 6, 5, 6]</td>
		</tr>
		<tr>
			<td>After applying modulo</td>
			<td>[8, 4, 6, 5, 6]</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [100000,2000], k = 2, multiplier = 1000000</span></p>

<p><strong>Output:</strong> <span class="example-io">[999999307,999999993]</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Result</th>
		</tr>
		<tr>
			<td>After operation 1</td>
			<td>[100000, 2000000000]</td>
		</tr>
		<tr>
			<td>After operation 2</td>
			<td>[100000000000, 2000000000]</td>
		</tr>
		<tr>
			<td>After applying modulo</td>
			<td>[999999307, 999999993]</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= multiplier &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue (Min-Heap) + Simulation

Let the length of the array $\textit{nums}$ be $n$, and the maximum value be $m$.

We first use a priority queue (min-heap) to simulate the operations until we complete $k$ operations or all elements in the heap are greater than or equal to $m$.

At this point, all elements in the array are less than $m \times \textit{multiplier}$. Since $1 \leq m \leq 10^9$ and $1 \leq \textit{multiplier} \leq 10^6$, $m \times \textit{multiplier} \leq 10^{15}$, which is within the range of a 64-bit integer.

Next, each operation will turn the smallest element in the array into the largest element. Therefore, after every $n$ consecutive operations, each element in the array will have undergone exactly one multiplication operation.

Thus, after the simulation, for the remaining $k$ operations, the smallest $k \bmod n$ elements in the array will undergo $\lfloor k / n \rfloor + 1$ multiplication operations, while the other elements will undergo $\lfloor k / n \rfloor$ multiplication operations.

Finally, we multiply each element in the array by the corresponding number of multiplication operations and take the result modulo $10^9 + 7$. This can be calculated using fast exponentiation.

The time complexity is $O(n \times \log n \times \log M + n \times \log k)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$, and $M$ is the maximum value in the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        pq = [(x, i) for i, x in enumerate(nums)]
        heapify(pq)
        m = max(nums)
        while k and pq[0][0] < m:
            x, i = heappop(pq)
            heappush(pq, (x * multiplier, i))
            k -= 1
        n = len(nums)
        mod = 10**9 + 7
        pq.sort()
        for i, (x, j) in enumerate(pq):
            nums[j] = x * pow(multiplier, k // n + int(i < k % n), mod) % mod
        return nums
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
