---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1865.Finding%20Pairs%20With%20a%20Certain%20Sum/README_EN.md
rating: 1680
source: Weekly Contest 241 Q3
tags:
    - Design
    - Array
    - Hash Table
---

<!-- problem:start -->

# [1865. Finding Pairs With a Certain Sum](https://leetcode.com/problems/finding-pairs-with-a-certain-sum)

## Description

<!-- description:start -->

<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>. You are tasked to implement a data structure that supports queries of two types:</p>

<ol>
	<li><strong>Add</strong> a positive integer to an element of a given index in the array <code>nums2</code>.</li>
	<li><strong>Count</strong> the number of pairs <code>(i, j)</code> such that <code>nums1[i] + nums2[j]</code> equals a given value (<code>0 &lt;= i &lt; nums1.length</code> and <code>0 &lt;= j &lt; nums2.length</code>).</li>
</ol>

<p>Implement the <code>FindSumPairs</code> class:</p>

<ul>
	<li><code>FindSumPairs(int[] nums1, int[] nums2)</code> Initializes the <code>FindSumPairs</code> object with two integer arrays <code>nums1</code> and <code>nums2</code>.</li>
	<li><code>void add(int index, int val)</code> Adds <code>val</code> to <code>nums2[index]</code>, i.e., apply <code>nums2[index] += val</code>.</li>
	<li><code>int count(int tot)</code> Returns the number of pairs <code>(i, j)</code> such that <code>nums1[i] + nums2[j] == tot</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;FindSumPairs&quot;, &quot;count&quot;, &quot;add&quot;, &quot;count&quot;, &quot;count&quot;, &quot;add&quot;, &quot;add&quot;, &quot;count&quot;]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
<strong>Output</strong>
[null, 8, null, 2, 1, null, null, 11]

<strong>Explanation</strong>
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,<strong><u>4</u></strong><code>,5,4</code>]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [<strong><u><code>2</code></u></strong>,4,5,4<code>,5,4</code>]
findSumPairs.add(1, 1); // now nums2 = [<code>2</code>,<strong><u>5</u></strong>,5,4<code>,5,4</code>]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums2[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= index &lt; nums2.length</code></li>
	<li><code>1 &lt;= val &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= tot &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>1000</code> calls are made to <code>add</code> and <code>count</code> <strong>each</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We note that the length of the array $\textit{nums1}$ does not exceed ${10}^3$, while the length of the array $\textit{nums2}$ reaches ${10}^5$. Therefore, if we directly enumerate all index pairs $(i, j)$ and check whether $\textit{nums1}[i] + \textit{nums2}[j]$ equals the specified value $\textit{tot}$, it will exceed the time limit.

Can we only enumerate the shorter array $\textit{nums1}$? The answer is yes. We use a hash table $\textit{cnt}$ to count the occurrences of each element in the array $\textit{nums2}$, then enumerate each element $x$ in the array $\textit{nums1}$ and calculate the sum of $\textit{cnt}[\textit{tot} - x]$.

When calling the $\text{add}$ method, we need to first decrement the value corresponding to $\textit{nums2}[index]$ in $\textit{cnt}$ by $1$, then add $\textit{val}$ to the value of $\textit{nums2}[index]$, and finally increment the value corresponding to $\textit{nums2}[index]$ in $\textit{cnt}$ by $1$.

When calling the $\text{count}$ method, we only need to traverse the array $\textit{nums1}$ and calculate the sum of $\textit{cnt}[\textit{tot} - x]$ for each element $x$.

The time complexity is $O(n \times q)$, and the space complexity is $O(m)$. Here, $n$ and $m$ are the lengths of the arrays $\textit{nums1}$ and $\textit{nums2}$, respectively, and $q$ is the number of times the $\text{count}$ method is called.

<!-- tabs:start -->

#### Python3

```python
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt = Counter(nums2)
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.cnt[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.cnt[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.cnt[tot - x] for x in self.nums1)

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
