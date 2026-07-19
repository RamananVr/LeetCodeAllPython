---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3430.Maximum%20and%20Minimum%20Sums%20of%20at%20Most%20Size%20K%20Subarrays/README_EN.md
rating: 2644
source: Weekly Contest 433 Q4
tags:
    - Stack
    - Array
    - Math
    - Monotonic Stack
---

<!-- problem:start -->

# [3430. Maximum and Minimum Sums of at Most Size K Subarrays](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and a <strong>positive</strong> integer <code>k</code>. Return the sum of the <strong>maximum</strong> and <strong>minimum</strong> elements of all <span data-keyword="subarray-nonempty">subarrays</span> with <strong>at most</strong> <code>k</code> elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">20</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarrays of <code>nums</code> with at most 2 elements are:</p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;"><b>Subarray</b></th>
			<th style="border: 1px solid black;">Minimum</th>
			<th style="border: 1px solid black;">Maximum</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[1]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[2]</code></td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[3]</code></td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[1, 2]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[2, 3]</code></td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><strong>Final Total</strong></td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">20</td>
		</tr>
	</tbody>
</table>

<p>The output would be 20.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,-3,1], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-6</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarrays of <code>nums</code> with at most 2 elements are:</p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;"><b>Subarray</b></th>
			<th style="border: 1px solid black;">Minimum</th>
			<th style="border: 1px solid black;">Maximum</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[1]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[-3]</code></td>
			<td style="border: 1px solid black;">-3</td>
			<td style="border: 1px solid black;">-3</td>
			<td style="border: 1px solid black;">-6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[1]</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[1, -3]</code></td>
			<td style="border: 1px solid black;">-3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">-2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>[-3, 1]</code></td>
			<td style="border: 1px solid black;">-3</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">-2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><strong>Final Total</strong></td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">-6</td>
		</tr>
	</tbody>
</table>

<p>The output would be -6.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 80000</code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Deques for Maximums and Minimums

The goal is to calculate total sum $S = \sum_i (\text{MaxSum}_i + \text{MinSum}_i)$, where:

1.  $\text{MaxSum}_i$: sum of maximum values of all valid subarrays ending at index $i$.
2.  $\text{MinSum}_i$: sum of minimum values of all valid subarrays ending at index $i$.

We maintain two **Deques**, used as monotonic stacks with boundary control: `max_stack` and `min_stack`.

These track maximum and minimum values for all subarrays ending at index $i$ with a length not exceeding $k$.

Each element in deques is a triplet: `[index, value, count]`,
where `count` represents how many times this `value` acts as the max/min within current window.

#### Step 1: Boundary Control

For each element $nums[i]$, check if window boundary $\max(0, i - k + 1)$ has advanced.

- If $i - k \ge 0$, it means the subarray $nums[i-k \dots i]$ would exceed length $k$ due to inclusion of $nums[i]$.
- Contribution of the subarray starting at $i-k$ must be removed. This contribution is located at the **front** of our deques.
- We decrement the `count` of deques' front. If the front element's index falls out of window range, we `popleft()` to maintain efficiency.

#### Step 2: Monotonicity

Taking `max_stack` as an example:

- While `max_stack` is not empty and `max_stack` top value $\leq nums[i]$ (1):
    - Current $nums[i]$ will replace this top element as the new maximum for all subarrays this top element previously "served."
    - We take over the `prev_shares` (which is the count) from this popped element.
    - Net increase to `subarrays_max_sum` is calculated as $(nums[i] - prev\_num) \times prev\_shares$.
- After while-loop, we add $nums[i]$'s own contribution, as a single-element subarray, to `subarrays_max_sum`,
  and push $nums[i]$ onto `max_stack` with its cumulative `count` and index.

Logic for `min_stack` processing is similar, but inequality (1) must change into `min_stack` top value $\geq nums[i]$.

#### Step 3: Accumulation

At the end of each iteration $i$, we add current `subarrays_max_sum` and `subarrays_min_sum` to global total `subarrays_max_min_sum`.

### Complexity Analysis

- **Time Complexity:** $O(n)$, where $n$ is length of $nums$. Each element is pushed and popped at most 4 times in total among two deques.
- **Space Complexity:** $O(n)$ to store deques and state variables.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minMaxSubarraySum(self, nums: list[int], k: int) -> int:
        subarrays_max_min_sum = 0

        max_stack: deque[list[int]] = deque([])  # Format: [idx, num, shares].
        subarrays_max_sum = 0

        min_stack: deque[list[int]] = deque([])  # Format: [idx, num, shares].
        subarrays_min_sum = 0

        for end_idx, num in enumerate(nums):
            start_idx = max(0, end_idx - k + 1)

            # Window start idx slides by 1: must update stacks' info.
            if start_idx > 0:
                max_stack[0][2] -= 1  # Decrement stack's front num shares.
                subarrays_max_sum -= max_stack[0][1]

                if max_stack[0][0] < start_idx:  # Front num out of window.
                    max_stack.popleft()

                min_stack[0][2] -= 1  # Decrement stack's front num shares.
                subarrays_min_sum -= min_stack[0][1]

                if min_stack[0][0] < start_idx:  # Front num out of window.
                    min_stack.popleft()

            max_shares = 1  # Base case.
            subarrays_max_sum += num

            while max_stack and max_stack[-1][1] <= num:
                _, prev_num, prev_shares = max_stack.pop()

                max_shares += prev_shares  # Max shares transition.

                # Reflect transition in max sum.
                subarrays_max_sum += (num - prev_num) * prev_shares

            max_stack.append([end_idx, num, max_shares])

            min_shares = 1  # Base case.
            subarrays_min_sum += num

            while min_stack and min_stack[-1][1] >= num:
                _, prev_num, prev_shares = min_stack.pop()

                min_shares += prev_shares  # Min shares transition.

                # Reflect transition in min sum.
                subarrays_min_sum += (num - prev_num) * prev_shares

            min_stack.append([end_idx, num, min_shares])

            subarrays_max_min_sum += subarrays_max_sum + subarrays_min_sum

        return subarrays_max_min_sum
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
