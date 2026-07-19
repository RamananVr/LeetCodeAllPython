---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3597.Partition%20String/README_EN.md
rating: 1347
source: Weekly Contest 456 Q1
tags:
    - Trie
    - Hash Table
    - String
    - Simulation
---

<!-- problem:start -->

# [3597. Partition String](https://leetcode.com/problems/partition-string)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, partition it into <strong>unique segments</strong> according to the following procedure:</p>

<ul>
	<li>Start building a segment beginning at index 0.</li>
	<li>Continue extending the current segment character by character until the current segment has not been seen before.</li>
	<li>Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.</li>
	<li>Repeat until you reach the end of <code>s</code>.</li>
</ul>

<p>Return an array of strings <code>segments</code>, where <code>segments[i]</code> is the <code>i<sup>th</sup></code> segment created.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abbccccd&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;a&quot;,&quot;b&quot;,&quot;bc&quot;,&quot;c&quot;,&quot;cc&quot;,&quot;d&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Index</th>
			<th style="border: 1px solid black;">Segment After Adding</th>
			<th style="border: 1px solid black;">Seen Segments</th>
			<th style="border: 1px solid black;">Current Segment Seen Before?</th>
			<th style="border: 1px solid black;">New Segment</th>
			<th style="border: 1px solid black;">Updated Seen Segments</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">&quot;a&quot;</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">&quot;&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">&quot;b&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">&quot;&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">&quot;b&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">&quot;b&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">&quot;bc&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">&quot;&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">&quot;c&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">&quot;&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;, &quot;c&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">&quot;c&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;, &quot;c&quot;]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">&quot;c&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;, &quot;c&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">&quot;cc&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;, &quot;c&quot;]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">&quot;&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;, &quot;c&quot;, &quot;cc&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">&quot;d&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;, &quot;c&quot;, &quot;cc&quot;]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">&quot;&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;, &quot;c&quot;, &quot;cc&quot;, &quot;d&quot;]</td>
		</tr>
	</tbody>
</table>

<p>Hence, the final output is <code>[&quot;a&quot;, &quot;b&quot;, &quot;bc&quot;, &quot;c&quot;, &quot;cc&quot;, &quot;d&quot;]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aaaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;a&quot;,&quot;aa&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Index</th>
			<th style="border: 1px solid black;">Segment After Adding</th>
			<th style="border: 1px solid black;">Seen Segments</th>
			<th style="border: 1px solid black;">Current Segment Seen Before?</th>
			<th style="border: 1px solid black;">New Segment</th>
			<th style="border: 1px solid black;">Updated Seen Segments</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">&quot;a&quot;</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">&quot;&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">&quot;a&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">&quot;a&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">&quot;aa&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">&quot;&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;aa&quot;]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">&quot;a&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;aa&quot;]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">&quot;a&quot;</td>
			<td style="border: 1px solid black;">[&quot;a&quot;, &quot;aa&quot;]</td>
		</tr>
	</tbody>
</table>

<p>Hence, the final output is <code>[&quot;a&quot;, &quot;aa&quot;]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> contains only lowercase English letters. </li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Simulation

We can use a hash table $\textit{vis}$ to record the segments that have already appeared. Then, we traverse the string $s$, building the current segment $t$ character by character until this segment has not appeared before. Each time we construct a new segment, we add it to the result list and mark it as seen.

After the traversal, we simply return the result list.

The time complexity is $O(n \times \sqrt{n})$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def partitionString(self, s: str) -> List[str]:
        vis = set()
        ans = []
        t = ""
        for c in s:
            t += c
            if t not in vis:
                vis.add(t)
                ans.append(t)
                t = ""
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: String Hashing + Hash Table + Simulation

We can use string hashing to speed up the lookup of segments. Specifically, we can compute a hash value for each segment and store it in a hash table. In this way, we can determine in constant time whether a segment has already appeared.

In detail, we first create a string hashing class $\textit{Hashing}$ based on the string $s$, which supports computing the hash value of any substring. Then, we traverse the string $s$ using two pointers $l$ and $r$ to represent the start and end positions of the current segment (indices starting from $1$). Each time we extend $r$, we compute the hash value $x$ of the current segment. If this hash value is not in the hash table, we add the segment to the result list and mark its hash value as seen. Otherwise, we continue to extend $r$ until we find a new segment.

After the traversal, we return the result list.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Hashing:
    __slots__ = ["mod", "h", "p"]

    def __init__(
        self, s: Union[str, List[str]], base: int = 13331, mod: int = 998244353
    ):
        self.mod = mod
        self.h = [0] * (len(s) + 1)
        self.p = [1] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            self.h[i] = (self.h[i - 1] * base + ord(s[i - 1])) % mod
            self.p[i] = (self.p[i - 1] * base) % mod

    def query(self, l: int, r: int) -> int:
        return (self.h[r] - self.h[l - 1] * self.p[r - l + 1]) % self.mod

class Solution:
    def partitionString(self, s: str) -> List[str]:
        hashing = Hashing(s)
        vis = set()
        l = 1
        ans = []
        for r, c in enumerate(s, 1):
            x = hashing.query(l, r)
            if x not in vis:
                vis.add(x)
                ans.append(s[l - 1 : r])
                l = r + 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
