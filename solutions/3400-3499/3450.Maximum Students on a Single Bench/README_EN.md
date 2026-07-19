---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3450.Maximum%20Students%20on%20a%20Single%20Bench/README_EN.md
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [3450. Maximum Students on a Single Bench 🔒](https://leetcode.com/problems/maximum-students-on-a-single-bench)

## Description

<!-- description:start -->

<p data-pm-slice="1 1 []">You are given a 2D integer array of student data <code>students</code>, where <code>students[i] = [student_id, bench_id]</code> represents that student <code>student_id</code> is sitting on the bench <code>bench_id</code>.</p>

<p>Return the <strong>maximum</strong> number of <em>unique</em> students sitting on any single bench. If no students are present, return 0.</p>

<p><strong>Note</strong>: A student can appear multiple times on the same bench in the input, but they should be counted only once per bench.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">students = [[1,2],[2,2],[3,3],[1,3],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Bench 2 has two unique students: <code>[1, 2]</code>.</li>
	<li>Bench 3 has three unique students: <code>[1, 2, 3]</code>.</li>
	<li>The maximum number of unique students on a single bench is 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">students = [[1,1],[2,1],[3,1],[4,2],[5,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Bench 1 has three unique students: <code>[1, 2, 3]</code>.</li>
	<li>Bench 2 has two unique students: <code>[4, 5]</code>.</li>
	<li>The maximum number of unique students on a single bench is 3.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">students = [[1,1],[1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The maximum number of unique students on a single bench is 1.</li>
</ul>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">students = []</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Since no students are present, the output is 0.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= students.length &lt;= 100</code></li>
	<li><code>students[i] = [student_id, bench_id]</code></li>
	<li><code>1 &lt;= student_id &lt;= 100</code></li>
	<li><code>1 &lt;= bench_id &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We use a hash table $d$ to store the students on each bench, where the key is the bench number and the value is a set containing the student IDs on that bench.

Traverse the student array $\textit{students}$ and store the student IDs and bench numbers in the hash table $d$.

Finally, we traverse the values of the hash table $d$ and take the maximum size of the sets, which is the maximum number of different students on a single bench.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the student array $\textit{students}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        if not students:
            return 0
        d = defaultdict(set)
        for student_id, bench_id in students:
            d[bench_id].add(student_id)
        return max(map(len, d.values()))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
