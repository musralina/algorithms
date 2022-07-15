class Node:
    def __init__(self, id, nxt=None):
        self.id = id
        self.nxt = nxt


class MyQueue:
    def __init__(self):
        self.dummy = Node(None)
        self.back = self.dummy
        self.cnt = 0

    def put(self, node):
        self.back.nxt = node
        self.back = node
        self.cnt += 1

    def pop(self):
        res = self.dummy.nxt.id
        self.dummy.nxt = self.dummy.nxt.nxt

        if self.dummy.nxt is None:
            self.back = self.dummy

        self.cnt -= 1

        return res

    def pushFront(self, node):
        if self.cnt == 0:
            self.put(node)
        else:
            node.nxt = self.dummy.nxt
            self.dummy.nxt = node
            self.cnt += 1

    def print(self):
        ptr = self.dummy
        while ptr.nxt is not None:
            ptr = ptr.nxt
            if ptr == self.back:
                print(f"back!{ptr.id} ", end="")
            else:
                print(f"{ptr.id} ", end="")

        print()


class QueueWithPrivileges:
    def __init__(self):
        self.q1 = MyQueue()
        self.q2 = MyQueue()

    def put(self, node):
        if self.q1.cnt + self.q2.cnt == 0:
            self.q1.put(node)
            return

        if self.q1.cnt == self.q2.cnt:
            id1 = self.q2.pop()
            self.q1.put(Node(id1))
        self.q2.put(node)

    def put_privileged(self, node):
        if self.q1.cnt + self.q2.cnt == 0:
            self.q1.put(node)
            return

        if self.q1.cnt == self.q2.cnt:
            self.q1.put(node)
            return

        self.q2.pushFront(node)

    def pop(self):
        if self.q1.cnt == self.q2.cnt:
            id1 = self.q2.pop()
            self.q1.put(Node(id1))

        return self.q1.pop()

    def len(self):
        return self.q1.cnt + self.q2.cnt

    def print(self):
        print(f"q1({self.q1.cnt}): ", end="")
        self.q1.print()
        print(f"q2({self.q2.cnt}): ", end="")
        self.q2.print()


def testPushFront():
    q = MyQueue()
    for i in range(5):
        q.pushFront(Node(i))
        q.print()

    for i in range(100, 140, 10):
        q.put(Node(i))
        q.print()


def testPutPrivileged(n):
    q = QueueWithPrivileges()

    for i in range(n):
        q.put(Node(i))
        q.print()

    q.put_privileged(Node(n))
    q.print()


def test():
    for i in range(4):
        print(i)
        testPutPrivileged(i)


if False:
    test()
    # testPushFront()
else:
    n = int(input())

    shops = [QueueWithPrivileges() for i in range(n)]

    s = list(input().split())
    while s[0] != '#':
        q = int(s[1])
        if s[0] == '+':
            client = int(s[2])
            shops[q].put(Node(client))
        elif s[0] == '!':
            client = int(s[2])
            shops[q].put_privileged(Node(client))
        elif s[0] == '?':
            print(f"\t{shops[q].len()}")
        elif s[0] == '-':
            res = shops[q].pop()
            print(res)

        s = list(input().split())

