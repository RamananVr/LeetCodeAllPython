---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0364.Nested%20List%20Weight%20Sum%20II/README_EN.md
tags:
    - Stack
    - Depth-First Search
    - Breadth-First Search
---

<!-- problem:start -->

# [364. Nested List Weight Sum II 🔒](https://leetcode.com/problems/nested-list-weight-sum-ii)

## Description

<!-- description:start -->

<p>You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists.</p>

<p>The <strong>depth</strong> of an integer is the number of lists that it is inside of. For example, the nested list <code>[1,[2,2],[[3],2],1]</code> has each integer&#39;s value set to its <strong>depth</strong>. Let <code>maxDepth</code> be the <strong>maximum depth</strong> of any integer.</p>

<p>The <strong>weight</strong> of an integer is <code>maxDepth - (the depth of the integer) + 1</code>.</p>

<p>Return <em>the sum of each integer in </em><code>nestedList</code><em> multiplied by its <strong>weight</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0364.Nested%20List%20Weight%20Sum%20II/images/nestedlistweightsumiiex1.png" style="width: 426px; height: 181px;" />
<pre>
<strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> Four 1&#39;s with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0364.Nested%20List%20Weight%20Sum%20II/images/nestedlistweightsumiiex2.png" style="width: 349px; height: 192px;" />
<pre>
<strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> 17
<strong>Explanation:</strong> One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 50</code></li>
	<li>The values of the integers in the nested list is in the range <code>[-100, 100]</code>.</li>
	<li>The maximum <strong>depth</strong> of any integer is less than or equal to <code>50</code>.</li>
	<li>There are no empty lists.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

Let's assume the integers are $a_1, a_2, \cdots, a_n$, their depths are $d_1, d_2, \cdots, d_n$, the maximum depth is $\textit{maxDepth}$, then the answer is:

$$
a_1 \times \textit{maxDepth} - a_1 \times d_1 + a_1 + a_2 \times \textit{maxDepth} - a_2 \times d_2 + a_2 + \cdots + a_n \times \textit{maxDepth} - a_n \times d_n + a_n
$$

which is:

$$
(\textit{maxDepth} + 1) \times (a_1 + a_2 + \cdots + a_n) - (a_1 \times d_1 + a_2 \times d_2 + \cdots + a_n \times d_n)
$$

If we denote the sum of all integers as $s$, and the sum of each integer multiplied by its depth as $ws$, then the answer is:

$$
(\textit{maxDepth} + 1) \times s - ws
$$

Therefore, we design a function $dfs(x, d)$, which starts searching from $x$ with depth $d$. The execution process of $dfs(x, d)$ is as follows:

- We first update $\textit{maxDepth} = \max(\textit{maxDepth}, d)$;
- If $x$ is an integer, then we update $s = s + x$, $ws = ws + x \times d$;
- Otherwise, we recursively traverse each element $y$ of $x$, and call $dfs(y, d + 1)$.

We traverse the entire list, for each element $x$, we call $dfs(x, 1)$, and finally return $(\textit{maxDepth} + 1) \times s - ws$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the number of integers.

<!-- tabs:start -->

#### Python3

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def dfs(x, d):
            nonlocal maxDepth, s, ws
            maxDepth = max(maxDepth, d)
            if x.isInteger():
                s += x.getInteger()
                ws += x.getInteger() * d
            else:
                for y in x.getList():
                    dfs(y, d + 1)

        maxDepth = s = ws = 0
        for x in nestedList:
            dfs(x, 1)
        return (maxDepth + 1) * s - ws
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
