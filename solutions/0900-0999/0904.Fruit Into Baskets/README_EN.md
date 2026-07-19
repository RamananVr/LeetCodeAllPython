---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0904.Fruit%20Into%20Baskets/README_EN.md
tags:
    - Array
    - Hash Table
    - Sliding Window
---

<!-- problem:start -->

# [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets)

## Description

<!-- description:start -->

<p>You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array <code>fruits</code> where <code>fruits[i]</code> is the <strong>type</strong> of fruit the <code>i<sup>th</sup></code> tree produces.</p>

<p>You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:</p>

<ul>
	<li>You only have <strong>two</strong> baskets, and each basket can only hold a <strong>single type</strong> of fruit. There is no limit on the amount of fruit each basket can hold.</li>
	<li>Starting from any tree of your choice, you must pick <strong>exactly one fruit</strong> from <strong>every</strong> tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.</li>
	<li>Once you reach a tree with fruit that cannot fit in your baskets, you must stop.</li>
</ul>

<p>Given the integer array <code>fruits</code>, return <em>the <strong>maximum</strong> number of fruits you can pick</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> fruits = [<u>1,2,1</u>]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can pick from all 3 trees.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> fruits = [0,<u>1,2,2</u>]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> fruits = [1,<u>2,3,2,2</u>]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= fruits.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= fruits[i] &lt; fruits.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Sliding Window

We use a hash table $cnt$ to maintain the types and corresponding quantities of fruits in the current window, and use two pointers $j$ and $i$ to maintain the left and right boundaries of the window.

We traverse the $\textit{fruits}$ array, add the current fruit $x$ to the window, i.e., $cnt[x]++$, then judge whether the types of fruits in the current window exceed $2$. If it exceeds $2$, we need to move the left boundary $j$ of the window to the right until the types of fruits in the window do not exceed $2$. Then we update the answer, i.e., $ans = \max(ans, i - j + 1)$.

After the traversal ends, we can get the final answer.

```
1 2 3 2 2 1 4
^   ^
j   i

1 2 3 2 2 1 4
  ^ ^
  j i

1 2 3 2 2 1 4
  ^     ^
  j     i
```

The time complexity is $O(n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the $\textit{fruits}$ array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter()
        ans = j = 0
        for i, x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt) > 2:
                y = fruits[j]
                cnt[y] -= 1
                if cnt[y] == 0:
                    cnt.pop(y)
                j += 1
            ans = max(ans, i - j + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Monotonic Variable-Length Sliding Window

In Solution 1, we find that the window size sometimes increases and sometimes decreases, which requires us to update the answer each time.

But what this problem actually asks for is the maximum number of fruits, that is, the "largest" window. We don't need to shrink the window, we just need to let the window monotonically increase. So the code omits the operation of updating the answer each time, and only needs to return the size of the window as the answer after the traversal ends.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the $\textit{fruits}$ array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter()
        j = 0
        for x in fruits:
            cnt[x] += 1
            if len(cnt) > 2:
                y = fruits[j]
                cnt[y] -= 1
                if cnt[y] == 0:
                    cnt.pop(y)
                j += 1
        return len(fruits) - j
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
