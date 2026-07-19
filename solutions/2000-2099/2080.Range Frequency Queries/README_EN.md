---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2080.Range%20Frequency%20Queries/README_EN.md
rating: 1702
source: Weekly Contest 268 Q3
tags:
    - Design
    - Segment Tree
    - Array
    - Hash Table
    - Binary Search
---

<!-- problem:start -->

# [2080. Range Frequency Queries](https://leetcode.com/problems/range-frequency-queries)

## Description

<!-- description:start -->

<p>Design a data structure to find the <strong>frequency</strong> of a given value in a given subarray.</p>

<p>The <strong>frequency</strong> of a value in a subarray is the number of occurrences of that value in the subarray.</p>

<p>Implement the <code>RangeFreqQuery</code> class:</p>

<ul>
	<li><code>RangeFreqQuery(int[] arr)</code> Constructs an instance of the class with the given <strong>0-indexed</strong> integer array <code>arr</code>.</li>
	<li><code>int query(int left, int right, int value)</code> Returns the <strong>frequency</strong> of <code>value</code> in the subarray <code>arr[left...right]</code>.</li>
</ul>

<p>A <strong>subarray</strong> is a contiguous sequence of elements within an array. <code>arr[left...right]</code> denotes the subarray that contains the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> (<strong>inclusive</strong>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;RangeFreqQuery&quot;, &quot;query&quot;, &quot;query&quot;]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
<strong>Output</strong>
[null, 1, 2]

<strong>Explanation</strong>
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i], value &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= left &lt;= right &lt; arr.length</code></li>
	<li>At most <code>10<sup>5</sup></code> calls will be made to <code>query</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Binary Search

We use a hash table $g$ to store the array of indices corresponding to each value. In the constructor, we traverse the array $\textit{arr}$, adding the index corresponding to each value to the hash table.

In the query function, we first check whether the given value exists in the hash table. If it does not exist, it means that the value does not exist in the array, so we directly return $0$. Otherwise, we get the index array $\textit{idx}$ corresponding to the value. Then we use binary search to find the first index $l$ that is greater than or equal to $\textit{left}$, and the first index $r$ that is greater than $\textit{right}$. Finally, we return $r - l$.

In terms of time complexity, the time complexity of the constructor is $O(n)$, and the time complexity of the query function is $O(\log n)$. The space complexity is $O(n)$. Where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.g = defaultdict(list)
        for i, x in enumerate(arr):
            self.g[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        idx = self.g[value]
        l = bisect_left(idx, left)
        r = bisect_left(idx, right + 1)
        return r - l

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
