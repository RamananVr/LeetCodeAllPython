---
comments: true
difficulty: Medium
rating: 1544
source: Weekly Contest 159 Q2
tags:
    - Depth-First Search
    - Trie
    - Array
    - String
---

<!-- problem:start -->

# [1233. Remove Sub-Folders from the Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem)

## Description

<!-- description:start -->

<p>Given a list of folders <code>folder</code>, return <em>the folders after removing all <strong>sub-folders</strong> in those folders</em>. You may return the answer in <strong>any order</strong>.</p>

<p>If a <code>folder[i]</code> is located within another <code>folder[j]</code>, it is called a <strong>sub-folder</strong> of it. A sub-folder of <code>folder[j]</code> must start with <code>folder[j]</code>, followed by a <code>&quot;/&quot;</code>. For example, <code>&quot;/a/b&quot;</code> is a sub-folder of <code>&quot;/a&quot;</code>, but <code>&quot;/b&quot;</code> is not a sub-folder of <code>&quot;/a/b/c&quot;</code>.</p>

<p>The format of a path is one or more concatenated strings of the form: <code>&#39;/&#39;</code> followed by one or more lowercase English letters.</p>

<ul>
	<li>For example, <code>&quot;/leetcode&quot;</code> and <code>&quot;/leetcode/problems&quot;</code> are valid paths while an empty string and <code>&quot;/&quot;</code> are not.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> folder = [&quot;/a&quot;,&quot;/a/b&quot;,&quot;/c/d&quot;,&quot;/c/d/e&quot;,&quot;/c/f&quot;]
<strong>Output:</strong> [&quot;/a&quot;,&quot;/c/d&quot;,&quot;/c/f&quot;]
<strong>Explanation:</strong> Folders &quot;/a/b&quot; is a subfolder of &quot;/a&quot; and &quot;/c/d/e&quot; is inside of folder &quot;/c/d&quot; in our filesystem.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> folder = [&quot;/a&quot;,&quot;/a/b/c&quot;,&quot;/a/b/d&quot;]
<strong>Output:</strong> [&quot;/a&quot;]
<strong>Explanation:</strong> Folders &quot;/a/b/c&quot; and &quot;/a/b/d&quot; will be removed because they are subfolders of &quot;/a&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> folder = [&quot;/a/b/c&quot;,&quot;/a/b/ca&quot;,&quot;/a/b/d&quot;]
<strong>Output:</strong> [&quot;/a/b/c&quot;,&quot;/a/b/ca&quot;,&quot;/a/b/d&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= folder.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= folder[i].length &lt;= 100</code></li>
	<li><code>folder[i]</code> contains only lowercase letters and <code>&#39;/&#39;</code>.</li>
	<li><code>folder[i]</code> always starts with the character <code>&#39;/&#39;</code>.</li>
	<li>Each folder name is <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting

<!-- thinking:start -->

> **Thinking**
>
> A subfolder is lexicographically after its parent and starts with the parent path plus $/$. $n$ reaches $4\times 10^4$, so pairwise prefix tests are too slow.
>
> After sorting we only compare with the last kept folder: a descendant is dropped, otherwise the path is a new root. Sorting turns parent-child into an adjacent-prefix relation, so one scan suffices.

<!-- thinking:end -->

First, we sort the array `folder` in lexicographical order, then traverse the array. For the current folder $f$ we are traversing, if its length is greater than or equal to the length of the last folder in the answer array, and its prefix includes the last folder in the answer array plus a `/`, then $f$ is a subfolder of the last folder in the answer array, and we don't need to add it to the answer array. Otherwise, we add $f$ to the answer array.

After the traversal ends, the folders in the answer array are the answer required by the problem.

The time complexity is $O(n \times \log n \times m)$, and the space complexity is $O(m)$. Where $n$ and $m$ are the length of the array `folder` and the maximum length of the strings in the array `folder`, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for f in folder[1:]:
            m, n = len(ans[-1]), len(f)
            if m >= n or not (ans[-1] == f[:m] and f[m] == '/'):
                ans.append(f)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Trie

<!-- thinking:start -->

> **Thinking**
>
> Sorting relies on global lexicographic order and pays string-prefix comparisons. A trie inserts path segments and marks folder ends; a search that hits an end can skip the whole subtree as nested folders. Time follows total path length and avoids sorting.

<!-- thinking:end -->

We can use a trie to store all the folders in the array `folder`. Each node of the trie contains a `children` field, used to store the child nodes of the current node, and a `fid` field, used to store the index of the folder corresponding to the current node in the array `folder`.

For each folder $f$ in the array `folder`, we first split $f$ into several substrings according to `/`, then start from the root node and add the substrings to the trie in turn. Next, we start from the root node to search the trie. If the `fid` field of the current node is not `-1`, it means that the folder corresponding to the current node is a folder in the answer array. We add it to the answer array and return. Otherwise, we recursively search all child nodes of the current node and finally return the answer array.

The time complexity is $O(n \times m)$, and the space complexity is $O(n \times m)$. Where $n$ and $m$ are the length of the array `folder` and the maximum length of the strings in the array `folder`, respectively.

<!-- tabs:start -->

#### Python3

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.fid = -1

    def insert(self, i, f):
        node = self
        ps = f.split('/')
        for p in ps[1:]:
            if p not in node.children:
                node.children[p] = Trie()
            node = node.children[p]
        node.fid = i

    def search(self):
        def dfs(root):
            if root.fid != -1:
                ans.append(root.fid)
                return
            for child in root.children.values():
                dfs(child)

        ans = []
        dfs(self)
        return ans

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for i, f in enumerate(folder):
            trie.insert(i, f)
        return [folder[i] for i in trie.search()]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
