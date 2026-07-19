---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3740.Minimum%20Distance%20Between%20Three%20Equal%20Elements%20I/README_EN.md
rating: 1287
source: Weekly Contest 475 Q1
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [3740. Minimum Distance Between Three Equal Elements I](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>A tuple <code>(i, j, k)</code> of 3 <strong>distinct</strong> indices is <strong>good</strong> if <code>nums[i] == nums[j] == nums[k]</code>.</p>

<p>The <strong>distance</strong> of a <strong>good</strong> tuple is <code>abs(i - j) + abs(j - k) + abs(k - i)</code>, where <code>abs(x)</code> denotes the <strong>absolute value</strong> of <code>x</code>.</p>

<p>Return an integer denoting the <strong>minimum</strong> possible <strong>distance</strong> of a <strong>good</strong> tuple. If no <strong>good</strong> tuples exist, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The minimum distance is achieved by the good tuple <code>(0, 2, 3)</code>.</p>

<p><code>(0, 2, 3)</code> is a good tuple because <code>nums[0] == nums[2] == nums[3] == 1</code>. Its distance is <code>abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,3,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The minimum distance is achieved by the good tuple <code>(2, 4, 6)</code>.</p>

<p><code>(2, 4, 6)</code> is a good tuple because <code>nums[2] == nums[4] == nums[6] == 2</code>. Its distance is <code>abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no good tuples. Therefore, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We can use a hash table $\textit{g}$ to store the list of indices for each number in the array. While traversing the array, we add each number's index to its corresponding list in the hash table. Define a variable $\textit{ans}$ to store the answer, with an initial value of infinity $\infty$.

Next, we iterate through each index list in the hash table. If the length of an index list for a particular number is greater than or equal to $3$, it means there exists a valid triplet. To minimize the distance, we can choose three consecutive indices $i$, $j$, and $k$ from that number's index list, where $i < j < k$. The distance of this triplet is $j - i + k - j + k - i = 2 \times (k - i)$. We traverse all combinations of three consecutive indices in the list, calculate the distance, and update the answer.

Finally, if the answer is still the initial value $\infty$, it means no valid triplet exists, so we return $-1$; otherwise, we return the calculated minimum distance.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        g = defaultdict(list)
        for i, x in enumerate(nums):
            g[x].append(i)
        ans = inf
        for ls in g.values():
            for h in range(len(ls) - 2):
                i, k = ls[h], ls[h + 2]
                ans = min(ans, (k - i) * 2)
        return -1 if ans == inf else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
