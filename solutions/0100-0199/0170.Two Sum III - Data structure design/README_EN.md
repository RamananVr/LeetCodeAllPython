---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0170.Two%20Sum%20III%20-%20Data%20structure%20design/README_EN.md
tags:
    - Design
    - Array
    - Hash Table
    - Two Pointers
    - Data Stream
---

<!-- problem:start -->

# [170. Two Sum III - Data structure design 🔒](https://leetcode.com/problems/two-sum-iii-data-structure-design)

## Description

<!-- description:start -->

<p>Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.</p>

<p>Implement the <code>TwoSum</code> class:</p>

<ul>
	<li><code>TwoSum()</code> Initializes the <code>TwoSum</code> object, with an empty array initially.</li>
	<li><code>void add(int number)</code> Adds <code>number</code> to the data structure.</li>
	<li><code>boolean find(int value)</code> Returns <code>true</code> if there exists any pair of numbers whose sum is equal to <code>value</code>, otherwise, it returns <code>false</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;TwoSum&quot;, &quot;add&quot;, &quot;add&quot;, &quot;add&quot;, &quot;find&quot;, &quot;find&quot;]
[[], [1], [3], [5], [4], [7]]
<strong>Output</strong>
[null, null, null, null, true, false]

<strong>Explanation</strong>
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --&gt; [1]
twoSum.add(3);   // [1] --&gt; [1,3]
twoSum.add(5);   // [1,3] --&gt; [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>5</sup> &lt;= number &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= value &lt;= 2<sup>31</sup> - 1</code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code> and <code>find</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We use a hash table `cnt` to store the count of each number.

When the `add` method is called, we increment the count of the number `number`.

When the `find` method is called, we iterate over the hash table `cnt`. For each key `x`, we check if `value - x` is also a key in the hash table `cnt`. If it is, we check if `x` is equal to `value - x`. If they are not equal, it means we have found a pair of numbers whose sum is `value`, and we return `true`. If they are equal, we check if the count of `x` is greater than `1`. If it is, it means we have found a pair of numbers whose sum is `value`, and we return `true`. If it is less than or equal to `1`, it means we have not found a pair of numbers whose sum is `value`, and we continue to iterate over the hash table `cnt`. If we have not found a pair after the iteration, we return `false`.

Time complexity:

- The time complexity of the `add` method is $O(1)$.
- The time complexity of the `find` method is $O(n)$.

Space complexity is $O(n)$, where $n$ is the size of the hash table `cnt`.

<!-- tabs:start -->

#### Python3

```python
class TwoSum:

    def __init__(self):
        self.cnt = defaultdict(int)

    def add(self, number: int) -> None:
        self.cnt[number] += 1

    def find(self, value: int) -> bool:
        for x, v in self.cnt.items():
            y = value - x
            if y in self.cnt and (x != y or v > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
