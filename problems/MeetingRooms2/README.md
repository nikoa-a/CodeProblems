## Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

---

#### Example 1:

> **Input:** intervals = [(0,40),(5,10),(15,20)]<br>
> **Output:** 2<br>
> **Explanation:**<br>
> day1: (0,40)<br>
> day2: (5,10),(15,20)

#### Example 2:

> **Input:** intervals = [(4,9)]<br>
> **Output**: 1<br>
> **Note:** (0,8),(8,10) is not considered a conflict at 8
