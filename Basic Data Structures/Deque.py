class MyDeque:

    def __init__(self, N):
        self.N = N
        self.data = [None] * (self.N + 1)
        self.beg = self.end = 0

    # instance method
    def push_back(self, value):
        # we won't need it in this program, but still
        # it's a good idea to make a check
        if self.len() == self.N:
            return

        self.data[self.end] = value
        self.end = (self.end + 1) % (self.N + 1)

    def push_front(self, value):
        # we won't need it in this program, but still
        # it's a good idea to make a check
        if self.len() == self.N:
            return

        self.beg = (self.beg - 1 + self.N + 1) % (self.N + 1)
        self.data[self.beg] = value

    def len(self):
        return (self.end - self.beg + self.N + 1) % (self.N + 1)

    def pop_back(self):
        if self.len() == 0:
            return False

        self.end = (self.end - 1 + self.N + 1) % (self.N + 1)
        return self.data[self.end]

    def pop_front(self):
        if self.len() == 0:
            return False

        val = self.data[self.beg]
        self.beg = (self.beg + 1) % (self.N + 1)
        return val


d = MyDeque(100000)

s = list(map(int, input().split()))
while s[0] != -1:
    if s[0] == 0:
        d.push_back(s[1])
    elif s[0] == 1:
        d.push_front(s[1])
    elif s[0] == 2:
        print(d.len())
    elif s[0] == 3:
        res = d.pop_back()
        if not res:
            print("Error!")
        else:
            print(res)
    elif s[0] == 4:
        res = d.pop_front()
        if not res:
            print("Error!")
        else:
            print(res)

    s = list(map(int, input().split()))

