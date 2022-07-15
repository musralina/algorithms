Implement deque data structure. Deque is also called double-ended queue (Double-Ended QUEue). This is a data structure interface, and it should support the following operations:
push_back;
push_front;
len;
pop_back;
pop_front.
You are given list of 1 ≤ N ≤ 100000 requests to deque data structure. You need to process these requests, and check for possible errors (pop from empty dequeue). If the request cannot be processed, it should not make any changes in deque.
Request types are encoded by integer numbers:
0 — push_back;
1 — push_front;
2 — len;
3 — pop_back;
4 — pop_front;
-1 — End of list.

## Input format

Each line contains a request description, which consists of 1 or 2 integer numbers.
First number is a request type. For request types 0, 1, line also contains space character followed by one more integer number: value to be pushed to deque: 0 ≤ v ≤ 109.
Last line of input file contains one integer number: -1, which denotes end of list of requests.
Total number of requests do not exceed 100000.

## Output format

For each request of types 2-4, write a result on a separate line (requested length, or value to be removed by pop). If request cannot be performed, you should write Error! on separate line.
