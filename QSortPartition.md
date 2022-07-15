# QSort Partition

This year number of students in MSAI program is enormous: 0 ≤ N ≤ 100000. Quadratic sorting algorithm you used in previous problem now is too slow. MSAI teachers ask you for help again. Now you don't need to sort tables. You are asked just to implement fast sorting algorithm.
You can try to submit quadratic sorting algorithm here to make sure it's too slow.
You are asked to implement QSort algorithm. To simplify your task, teachers prepared code sample for you (link to github repo shortened for convenience): https://bit.ly/3lVudRS
It already has input and output parts. Also it has qsort main function implemented. You need to implement partition function which divides an array into 3 parts (p<, p=, p>). This function should give you correct QSort algorithm.
Please, find partition function signature and description to follow in the sample file.
Solution will be tested as sorting algorithm.

### Input format

First line contains single integer number: 0 ≤ N ≤ 100000. Next line contains N integer numbers divided by space character: 0 ≤ xi ≤ 109.

### Output format

On single line you should print N integer numbers, divided by space character: xi in sorted (non-decreasing) order.
