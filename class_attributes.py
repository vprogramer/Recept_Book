class Test:
    val1 = 1
    val2 = 2

    def __init__(self, data1, data2):
        print(self.val1, self.val2)
        val1 = data1
        val2 = data2
        print(val1, val2)
        print(self.val1, self.val2)
        self.val1 = data1
        self.val2 = data2
        print(self.val1, self.val2)


t1 = Test(5, 6)