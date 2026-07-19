---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0677.Map%20Sum%20Pairs/README_EN.md
tags:
    - Design
    - Trie
    - Hash Table
    - String
---

<!-- problem:start -->

# [677. Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs)

## Description

<!-- description:start -->

<p>Design a map that allows you to do the following:</p>

<ul>
	<li>Maps a string key to a given value.</li>
	<li>Returns the sum of the values that have a key with a prefix equal to a given string.</li>
</ul>

<p>Implement the <code>MapSum</code> class:</p>

<ul>
	<li><code>MapSum()</code> Initializes the <code>MapSum</code> object.</li>
	<li><code>void insert(String key, int val)</code> Inserts the <code>key-val</code> pair into the map. If the <code>key</code> already existed, the original <code>key-value</code> pair will be overridden to the new one.</li>
	<li><code>int sum(string prefix)</code> Returns the sum of all the pairs&#39; value whose <code>key</code> starts with the <code>prefix</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MapSum&quot;, &quot;insert&quot;, &quot;sum&quot;, &quot;insert&quot;, &quot;sum&quot;]
[[], [&quot;apple&quot;, 3], [&quot;ap&quot;], [&quot;app&quot;, 2], [&quot;ap&quot;]]
<strong>Output</strong>
[null, null, 3, null, 5]

<strong>Explanation</strong>
MapSum mapSum = new MapSum();
mapSum.insert(&quot;apple&quot;, 3);  
mapSum.sum(&quot;ap&quot;);           // return 3 (<u>ap</u>ple = 3)
mapSum.insert(&quot;app&quot;, 2);    
mapSum.sum(&quot;ap&quot;);           // return 5 (<u>ap</u>ple + <u>ap</u>p = 3 + 2 = 5)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= key.length, prefix.length &lt;= 50</code></li>
	<li><code>key</code> and <code>prefix</code> consist of only lowercase English letters.</li>
	<li><code>1 &lt;= val &lt;= 1000</code></li>
	<li>At most <code>50</code> calls will be made to <code>insert</code> and <code>sum</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Trie

We use a hash table $d$ to store key-value pairs and a trie $t$ to store the prefix sums of the key-value pairs. Each node in the trie contains two pieces of information:

- `val`: the total sum of the values of the key-value pairs with this node as the prefix
- `children`: an array of length $26$ that stores the child nodes of this node

When inserting a key-value pair $(key, val)$, we first check if the key exists in the hash table. If it does, the `val` of each node in the trie needs to subtract the original value of the key and then add the new value. If it does not exist, the `val` of each node in the trie needs to add the new value.

When querying the prefix sum, we start from the root node of the trie and traverse the prefix string. If the current node's child nodes do not contain the character, it means the prefix does not exist in the trie, and we return $0$. Otherwise, we continue to traverse the next character until we finish traversing the prefix string and return the `val` of the current node.

In terms of time complexity, the time complexity of inserting a key-value pair is $O(n)$, where $n$ is the length of the key. The time complexity of querying the prefix sum is $O(m)$, where $m$ is the length of the prefix.

The space complexity is $O(n \times m \times C)$, where $n$ and $m$ are the number of keys and the maximum length of the keys, respectively; and $C$ is the size of the character set, which is $26$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Trie:
    def __init__(self):
        self.children: List[Trie | None] = [None] * 26
        self.val: int = 0

    def insert(self, w: str, x: int):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.val += x

    def search(self, w: str) -> int:
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return 0
            node = node.children[idx]
        return node.val

class MapSum:
    def __init__(self):
        self.d = defaultdict(int)
        self.tree = Trie()

    def insert(self, key: str, val: int) -> None:
        x = val - self.d[key]
        self.d[key] = val
        self.tree.insert(key, x)

    def sum(self, prefix: str) -> int:
        return self.tree.search(prefix)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
