---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1500-1599/1577.Number%20of%20Ways%20Where%20Square%20of%20Number%20Is%20Equal%20to%20Product%20of%20Two%20Numbers/README_EN.md
rating: 1593
source: Weekly Contest 205 Q2
tags:
    - Array
    - Hash Table
    - Math
    - Two Pointers
---

<!-- problem:start -->

# [1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers)

## Description

<!-- description:start -->

<p>Given two arrays of integers <code>nums1</code> and <code>nums2</code>, return the number of triplets formed (type 1 and type 2) under the following rules:</p>

<ul>
	<li>Type 1: Triplet (i, j, k) if <code>nums1[i]<sup>2</sup> == nums2[j] * nums2[k]</code> where <code>0 &lt;= i &lt; nums1.length</code> and <code>0 &lt;= j &lt; k &lt; nums2.length</code>.</li>
	<li>Type 2: Triplet (i, j, k) if <code>nums2[i]<sup>2</sup> == nums1[j] * nums1[k]</code> where <code>0 &lt;= i &lt; nums2.length</code> and <code>0 &lt;= j &lt; k &lt; nums1.length</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [7,4], nums2 = [5,2,8,9]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Type 1: (1, 1, 2), nums1[1]<sup>2</sup> = nums2[1] * nums2[2]. (4<sup>2</sup> = 2 * 8). 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,1], nums2 = [1,1,1]
<strong>Output:</strong> 9
<strong>Explanation:</strong> All Triplets are valid, because 1<sup>2</sup> = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]<sup>2</sup> = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]<sup>2</sup> = nums1[j] * nums1[k].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [7,7,8,3], nums2 = [1,2,9,7]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]<sup>2</sup> = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]<sup>2</sup> = nums1[0] * nums1[1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Enumeration

We use a hash table $\textit{cnt1}$ to count the occurrences of each pair $(\textit{nums}[j], \textit{nums}[k])$ in $\textit{nums1}$, where $0 \leq j < k < m$, and $m$ is the length of the array $\textit{nums1}$. Similarly, we use a hash table $\textit{cnt2}$ to count the occurrences of each pair $(\textit{nums}[j], \textit{nums}[k])$ in $\textit{nums2}$, where $0 \leq j < k < n$, and $n$ is the length of the array $\textit{nums2}$.

Next, we enumerate each number $x$ in the array $\textit{nums1}$ and calculate the value of $\textit{cnt2}[x^2]$, which is the number of pairs $(\textit{nums}[j], \textit{nums}[k])$ in $\textit{nums2}$ that satisfy $\textit{nums}[j] \times \textit{nums}[k] = x^2$. Similarly, we enumerate each number $x$ in the array $\textit{nums2}$ and calculate the value of $\textit{cnt1}[x^2]$, which is the number of pairs $(\textit{nums}[j], \textit{nums}[k])$ in $\textit{nums1}$ that satisfy $\textit{nums}[j] \times \textit{nums}[k] = x^2$. Finally, we return the sum of the two results.

The time complexity is $O(m^2 + n^2 + m + n)$, and the space complexity is $O(m^2 + n^2)$. Here, $m$ and $n$ are the lengths of the arrays $\textit{nums1}$ and $\textit{nums2}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(nums: List[int]) -> Counter:
            cnt = Counter()
            for j in range(len(nums)):
                for k in range(j + 1, len(nums)):
                    cnt[nums[j] * nums[k]] += 1
            return cnt

        def cal(nums: List[int], cnt: Counter) -> int:
            return sum(cnt[x * x] for x in nums)

        cnt1 = count(nums1)
        cnt2 = count(nums2)
        return cal(nums1, cnt2) + cal(nums2, cnt1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Hash Table + Enumeration Optimization

We use a hash table $\textit{cnt1}$ to count the occurrences of each number in $\textit{nums1}$, and a hash table $\textit{cnt2}$ to count the occurrences of each number in $\textit{nums2}$.

Next, we enumerate each number $x$ in the array $\textit{nums1}$, and then enumerate each pair $(y, v1)$ in $\textit{cnt2}$, where $y$ is the key of $\textit{cnt2}$ and $v1$ is the value of $\textit{cnt2}$. We calculate $z = x^2 / y$. If $y \times z = x^2$, and if $y = z$, it means $y$ and $z$ are the same number, then the number of ways to choose two numbers from $v1$ is $v1 \times (v1 - 1) = v1 \times (v2 - 1)$. If $y \neq z$, then the number of ways to choose two numbers from $v1$ is $v1 \times v2$. Finally, we sum all the ways and divide by $2$. The division by $2$ is because we count the number of ways for the pair $(j, k)$, but $(j, k)$ and $(k, j)$ are the same way.

The time complexity is $O(m \times n)$, and the space complexity is $O(m + n)$. Here, $m$ and $n$ are the lengths of the arrays $\textit{nums1}$ and $\textit{nums2}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def cal(nums: List[int], cnt: Counter) -> int:
            ans = 0
            for x in nums:
                for y, v1 in cnt.items():
                    z = x * x // y
                    if y * z == x * x:
                        v2 = cnt[z]
                        ans += v1 * (v2 - int(y == z))
            return ans // 2

        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        return cal(nums1, cnt2) + cal(nums2, cnt1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
