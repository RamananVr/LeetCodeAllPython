---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3896.Minimum%20Operations%20to%20Transform%20Array%20into%20Alternating%20Prime/README_EN.md
rating: 1435
source: Biweekly Contest 180 Q3
tags:
    - Array
    - Math
    - Two Pointers
    - Binary Search
    - Number Theory
    - Sorting
---

<!-- problem:start -->

# [3896. Minimum Operations to Transform Array into Alternating Prime](https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>An array is considered <strong>alternating prime</strong> if:</p>

<ul>
	<li>Elements at <strong>even</strong> indices (0-based) are <strong>prime</strong> numbers.</li>
	<li>Elements at <strong>odd</strong> indices are <strong>non-prime</strong> numbers.</li>
</ul>

<p>In one operation, you may <strong>increment</strong> any element by 1.</p>

<p>Return the <strong>minimum</strong> number of operations required to transform <code>nums</code> into an <strong>alternating prime</strong> array.</p>

<p>A <strong>prime</strong> number is a natural number greater than 1 with only two factors, 1 and itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The element at index 0 must be prime. Increment <code>nums[0] = 1</code> to 2, using 1 operation.</li>
	<li>The element at index 1 must be non-prime. Increment <code>nums[1] = 2</code> to 4, using 2 operations.</li>
	<li>The element at index 2 is already prime.</li>
	<li>The element at index 3 is already non-prime.</li>
</ul>

<p>Total operations = <code>1 + 2 = 3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,6,7,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The elements at indices 0 and 2 are already prime.</li>
	<li>The elements at indices 1 and 3 are already non-prime.</li>
</ul>

<p>No operations are needed.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The element at index 0 must be prime. Increment <code>nums[0] = 4</code> to 5, using 1 operation.</li>
	<li>The element at index 1 is already non-prime.</li>
</ul>

<p>Total operations = 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Binary Search

We can first preprocess a sufficiently large list of prime numbers, denoted as $\textit{primes}$, and a boolean array $\textit{isPrime}$, where $\textit{isPrime}[i]$ indicates whether $i$ is a prime number.

Then we traverse each element in the array:

- If the index of the current element is even, we need to increase it to the next prime number. We can use binary search on $\textit{primes}$ to find the first prime number greater than or equal to the current element, and add the difference between them to the answer.
- If the index of the current element is odd and the current element is prime, we need to increase it to the next non-prime number. For the prime number 2, we need 2 increments to reach the next non-prime number 4; for other prime numbers, we only need 1 increment to reach the next non-prime number.

Finally, return the answer.

The time complexity is $O(n \times \log P)$, and the space complexity is $O(P)$. Here, $n$ and $P$ are the length of the array and the length of the preprocessed prime list, respectively.

<!-- tabs:start -->

#### Python3

```python
MX = 200000
is_prime = [True] * (MX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MX**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MX + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, MX + 1) if is_prime[i]]

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if i % 2 == 0:
                j = bisect_left(primes, x)
                ans += primes[j] - x
            else:
                if is_prime[x]:
                    ans += 2 if x == 2 else 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
