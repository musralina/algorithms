After graduating from MIPT you've decided to apply your knowledge in AI to Physics. You've become a world-wide famous physicist due to your deep knowledge of AI which you get on MSAI program. And now you are working on an innovational quantum process research: sigma-trimpazation*. Your research is definitely going to change the world!
Your experiment is in progress. Quantum sensors are installed and send you data permanently. You've found a regularity in this data. And now you are going to analyse it using python. What you need – is to get this data in sorted order.
Your process is initialized with three parameters: 0 ≤ N ≤ 107, 0 < M ≤ 104, 0 < q0 < 231. The process is the following: your data sequence x is generated from quantum data sequence q. You are given q0 value and next items are generated using the following rule** (this process is already implemented for you):

The data you need to analyze is calculated from quantum data: xi = (qi  mod  M) - M//2
Let's denote sorted data sequence as xs = sorted(x). You need to calculate the following value:

You've tried to use built-it python sorting algorithm but it takes too much time (your code is here: https://bit.ly/3vSlLpZ). You need to implement something faster. Try to optimize it somehow. No time to obtain TL verdict! Research must go on!

## Input format

The only line in input file contains 3 integer numbers divided by space character and followed by line break: 0 ≤ N ≤ 107, 0 < M ≤ 104, 0 < q0 < 231 — parameters of your process.

## Output format

Print the only integer number — y value for your process.
